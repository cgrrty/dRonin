/**
 ******************************************************************************
 *
 * @file       emptyplugin.h
 * @author     The OpenPilot Team, http://www.openpilot.org Copyright (C) 2010.
 * @addtogroup GCSPlugins GCS Plugins
 * @{
 * @addtogroup EmptyGadgetPlugin Empty Gadget Plugin
 * @{
 * @brief A place holder gadget plugin
 *****************************************************************************/
/*
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
 * or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
 * for more details.
 *
 * You should have received a copy of the GNU General Public License along
 * with this program; if not, see <http://www.gnu.org/licenses/>
 */

#ifndef EMPTYPLUGIN_H_
#define EMPTYPLUGIN_H_

#include <extensionsystem/iplugin.h>

class EmptyGadgetFactory;

class EmptyPlugin : public ExtensionSystem::IPlugin
{
    Q_OBJECT
    Q_PLUGIN_METADATA(IID "org.dronin.plugins.EmptyGadget")

public:
    EmptyPlugin();
    ~EmptyPlugin();

    void extensionsInitialized();
    bool initialize(const QStringList &arguments, QString *errorString);
    void shutdown();

private:
    EmptyGadgetFactory *mf;
};
#endif /* EMPTYPLUGIN_H_ */
