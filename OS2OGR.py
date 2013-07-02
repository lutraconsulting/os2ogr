# -*- coding: utf-8 -*-

## OS2OGR - Converts OS GML to OGR using OsmmLoader
## Copyright (c) 2011 Peter Wells for Lutra Consulting

## peter dot wells at lutraconsulting dot co dot uk
## Lutra Consulting
## 23 Chestnut Close
## Burgess Hill
## West Sussex
## RH15 8HN

## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

import doOs2Ogr

import resources_rc

class OS2OGR:

  def __init__(self, iface):
    # Save reference to the QGIS interface
    self.iface = iface
	
  def initGui(self):
    # Create action that will start plugin configuration
    self.action = QAction(QIcon(":/icons/osTrans.png"), "Convert OS GML to OGR", self.iface.mainWindow())
    QObject.connect(self.action, SIGNAL("triggered()"), self.run)

    # Add toolbar button and menu item
    self.iface.addToolBarIcon(self.action)
    self.iface.addPluginToMenu("&OS GML Tools", self.action)
		
	
  def unload(self):
    # Remove the plugin menu item and icon
    self.iface.removePluginMenu("&OS GML Tools",self.action)
    self.iface.removeToolBarIcon(self.action)
	
  def run(self):
    
    d = doOs2Ogr.Dialog(self.iface)
    d.exec_()
