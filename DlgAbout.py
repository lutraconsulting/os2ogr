# -*- coding: utf-8 -*-

## OS2OGR - Converts OS GML to OGR using OsmmLoader
## Copyright (c) 2011 Faunalia

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

from DlgAbout_ui import Ui_DlgAbout
from os2ogr import name, description, version
import platform

try:
    import resources
except ImportError:
    import resources_rc

class DlgAbout(QDialog, Ui_DlgAbout):

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.logo.setPixmap( QPixmap( ":/lutra/logo" ) )
        self.title.setText( name() )
        self.description.setText( description() )

        text = self.txt.toHtml()
        text = text.replace( "$PLUGIN_NAME$", name() )

        subject = "Help: %s" % name()
        body = """\n\n
--------
Plugin name: %s
Plugin version: %s
Python version: %s
Platform: %s - %s
--------
""" % ( name(), version(), platform.python_version(), platform.system(), platform.version() )

        mail = QUrl( "mailto:abc@abc.com" )
        mail.addQueryItem( "subject", subject )
        mail.addQueryItem( "body", body )

        text = text.replace( "$MAIL_SUBJECT$", unicode(mail.encodedQueryItemValue( "subject" )) )
        text = text.replace( "$MAIL_BODY$", unicode(mail.encodedQueryItemValue( "body" )) )

        self.txt.setHtml(text)



