# -*- coding: utf-8 -*-

## OS2OGR - Converts OS GML to OGR using OsmmLoader
## Copyright (C) 2011 Faunalia UK

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

def name():
	return "Ordnance Survey Translator"

def description():
	return "Converts GML (compressed) to various OGR formats"

def version():
	return "Version 0.6"

def qgisMinimumVersion():
	return "1.5.0"
  
def icon():
	return ":/icons/osTrans.png"

def classFactory(iface):
	from OS2OGR import OS2OGR
	return OS2OGR(iface)
