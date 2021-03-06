# Copyright (C) 2016 dRonin, http://dronin.org
# Licensed under the GNU LGPL version 2.1 or any later version (see COPYING.LESSER)

from struct import Struct

try:
    import lxml.etree as etree
except:
    import xml.etree.ElementTree as etree

class LogFSImport(dict):
    # vastly varying arena_size -- 0x1000 to 0x20000 ... though 0x20000 (aq32) is
    # probably illegit   all slot sizes 0x100 for settings

    known_magics = {
            'aq32/quanton'                   : 0x3b1b14cf,
            'brain'                          : 0x3bb141cf,
            'cc3d'                           : 0x99abcdef,
            'discoveryf4'                    : 0x99abcfef,
            'sparky2 int/revo/sim'           : 0x99abcedf,
            'sparky2'                        : 0x77abcedf,
            'simulation'                     : 0x89abceef,
            'colibri'                        : 0x3bb141ed,
            'flyingf3/lux/naze/pipx/sparky'  : 0x9ae1ee11
            }

    # magic, state .. 8 byte offset in
    arena_header = Struct('II')

    arena_states = { 'ERASED' : 0xffffffff,
            'RESERVED'  : 0xe6e6ffff,
            'ACTIVE'    : 0xe6e66666,
            'OBSOLETE'  : 0x00000000 }

    # state, obj_id, obj_inst_id, obj_size
    slot_header = Struct('IIHH')

    slot_states = { 'EMPTY' : 0xffffffff,
            'RESERVED'      : 0xfafaffff,
            'ACTIVE'        : 0xfafaaaaa,
            'OBSOLETE'      : 0x00000000 }

    slot_size = 256

    def __init__(self, githash, contents):
        from dronin import uavo_collection

        our_magic = None

        pos = 0

        prev_state_good = False
        in_good_arena = False

        obj_offsets = {}

        while pos + self.slot_size < len(contents):
            # check if we're in a sane state

            # assumption: arena sizes are power of 2, at least 2048 bytes
            if (pos & 0x7ff) == 0:
                magic,arena_state = self.arena_header.unpack_from(contents, pos)

                if our_magic is None:
                    for k in self.known_magics:
                        if self.known_magics[k] == magic:
                            #print "Selected magic number for targ " + k
                            our_magic = magic

                if magic == our_magic:
                    # let's assume this is good.  the slot is in the right place to
                    # actually be an arena header, and it has the right magic.

                    # print "Found probable arena at %x, state=%08x" % (pos, arena_state)

                    if arena_state == self.arena_states['ACTIVE']:
                        in_good_arena = True
                    else:
                        in_good_arena = False

                    pos += self.slot_size
                    prev_state_good = True

                    continue

            state, obj_id, inst_id, size = self.slot_header.unpack_from(contents, pos)

            prev_state_good = False

            if state == self.slot_states['ACTIVE']:
                if in_good_arena:
                    obj_offsets[(obj_id, inst_id)] = pos + self.slot_header.size

                prev_state_good = True

            pos += self.slot_size

        # We do this in two passes; A) so we can try and guess a good version from the
        # set of IDs if it is not known in the future, B) to unpack all at once

        uavo_defs = uavo_collection.UAVOCollection()

        self.githash = uavo_defs.from_git_hash(githash)

        for id_tup,offset in obj_offsets.items():
            obj_id, inst_id = id_tup

            uavo_key = '{0:08x}'.format(obj_id)

            obj = uavo_defs.get(uavo_key)

            if obj is not None:
                # print(slot state=%08x, objid=%08x, instid=%04x, size=%d"%(state, obj_id, inst_id, size))

                objInstance = obj.from_bytes(contents, 0, offset=offset)

                self[obj._name] = objInstance

