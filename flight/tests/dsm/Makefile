###############################################################################
# @file       Makefile
# @author     Tau Labs, http://taulabs.org, Copyright (C) 2012-2013
# @addtogroup 
# @{
# @addtogroup 
# @{
# @brief Makefile for unit test
###############################################################################
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, see <http://www.gnu.org/licenses/>
#

WHEREAMI := $(dir $(lastword $(MAKEFILE_LIST)))
TOP      := $(realpath $(WHEREAMI)/../../../)
include $(TOP)/make/firmware-defs.mk

EXTRAINCDIRS += $(OPUAVOBJ)/inc
EXTRAINCDIRS += $(OPUAVSYNTHDIR)
EXTRAINCDIRS += $(PIOS)/posix/inc
EXTRAINCDIRS += $(PIOS)/inc
EXTRAINCDIRS += $(PIOS)

CFLAGS += -O0
CFLAGS += -Wall -Werror
CFLAGS += -g
CFLAGS += $(patsubst %,-I%,$(EXTRAINCDIRS)) -I.
CFLAGS += -D_GNU_SOURCE

CONLYFLAGS += -std=gnu99

SRC += $(PIOS)/posix/pios_heap.c
SRC += $(PIOS)/posix/pios_semaphore.c
SRC += $(PIOS)/posix/pios_delay.c
SRC += $(PIOS)/posix/pios_rtc.c
SRC += $(PIOS)/posix/pios_thread.c

include $(TOP)/make/unittest.mk
