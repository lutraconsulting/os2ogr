rem OS2OGR - Converts OS GML to OGR using OsmmLoader
rem Copyright (c) 2011 Peter Wells for Lutra Consulting

rem peter dot wells at lutraconsulting dot co dot uk
rem Lutra Consulting
rem 23 Chestnut Close
rem Burgess Hill
rem West Sussex
rem RH15 8HN

rem This program is free software: you can redistribute it and/or modify
rem it under the terms of the GNU General Public License as published by
rem the Free Software Foundation, either version 3 of the License, or
rem (at your option) any later version.

rem This program is distributed in the hope that it will be useful,
rem but WITHOUT ANY WARRANTY; without even the implied warranty of
rem MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
rem GNU General Public License for more details.

rem You should have received a copy of the GNU General Public License
rem along with this program.  If not, see <http://www.gnu.org/licenses/>.

SET PLUGINDIR=%HOMEDRIVE%%HOMEPATH%\.qgis2\python\plugins\os2ogr
mkdir %PLUGINDIR%\icons
copy /Y *.py %PLUGINDIR%
copy /Y *.txt %PLUGINDIR%
copy /Y *.gfs %PLUGINDIR%
copy /Y icons\*.png %PLUGINDIR%\icons
rem PAUSE
