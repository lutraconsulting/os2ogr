#!/bin/bash

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

mkdir -p ~/.qgis/python/plugins/os2ogr/icons
cp *.py *.txt *.gfs ~/.qgis/python/plugins/os2ogr
cp icons/*.png ~/.qgis/python/plugins/os2ogr/icons
