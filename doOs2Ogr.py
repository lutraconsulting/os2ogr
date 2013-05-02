
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

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.core import *
from qgis.gui import *

from frmos2ogr import Ui_os2ogrDialog

class Dialog(QDialog, Ui_os2ogrDialog):

  #====================================================================
  #
  # __init__ 
  #
  #====================================================================
  def __init__(self, iface):
    
    import os
    import subprocess
    
    # Do init stuff
    QDialog.__init__(self)
    self.iface = iface
    self.setupUi(self)
    
    # Populate shape file types
    self.outputFormatComboBox.addItem('ESRI Shapefile')
    
    self.inputDir = None
    self.outputDir = None
    self.tempDir = None
    self.conversionScript = None
    
    defTempDir = ''
    defInputDir = ''
    defOutputDir = ''
    
    self.pluginRoot = ''
    self.userPrefFile = ''
    self.pathToPrepScript = ''
    self.gdal_dir = ''
    
    # Retrieve or set default file path variables
    self.pluginRoot = os.path.join( str(QgsApplication.qgisSettingsDirPath()), 'python/plugins/os2ogr' )
    self.userPrefFile = os.path.join( self.pluginRoot, 'userprefs.txt' )
    self.conversionScript = os.path.join( self.pluginRoot, 'osmmloader.py' )
    self.pathToPrepScript = os.path.join( self.pluginRoot, 'preposmm4ogr.py' )
    
    if os.name is 'posix':
      defInputDir = os.environ['HOME']
      defOutputDir = defInputDir
      defTempDir = '/tmp'
    elif os.name is 'nt':
      defInputDir = os.path.join( os.environ['HOMEDRIVE'], os.environ['HOMEPATH'] )
      defOutputDir = defInputDir
      defTempDir = os.environ['TEMP']
      ogr2ogrInPath = False
      for path in os.environ['PATH']:
        if os.path.isfile( os.path.join(path, 'ogr2ogr.exe') ):
          ogr2ogrInPath = True
          self.gdal_dir = path
      if not ogr2ogrInPath:
        if os.path.isfile( os.path.join( os.environ['OSGEO4W_ROOT'], 'apps', 'gdal-17', 'bin', 'ogr2ogr.exe' ) ):
          self.gdal_dir = os.path.join( os.environ['OSGEO4W_ROOT'], 'apps', 'gdal-17', 'bin' )
        elif os.path.isfile( os.path.join( os.environ['OSGEO4W_ROOT'], 'bin', 'ogr2ogr.exe' ) ):
          self.gdal_dir = os.path.join( os.environ['OSGEO4W_ROOT'], 'bin' )
        else:
          QMessageBox.critical(None, "ERROR", "Can't find ogr2ogr.exe, can't continue" )
          self.pushButton_2.setEnabled(False)
          return
          
    # Look for ogr2ogr.exe and check its version
    majorVersion = 0.0
    try:
      sErr = open(os.devnull, 'w')
      sIn = open(os.devnull, 'r')
      p = subprocess.Popen(['ogr2ogr', '--version'], stdout=subprocess.PIPE, stdin=sIn, stderr=sErr)
      sErr.close()
      sIn.close()
      out, err = p.communicate()
      majorVersion = float( out[5:8] )
    except:
      # not found
      QMessageBox.critical(None, "ERROR", "Can't find ogr2ogr[.exe], can't continue" )
      self.pushButton_2.setEnabled(False)
      return
        
    if majorVersion < 1.8:
      QMessageBox.warning(None, "WARNING", "OGR 1.8 or above is recommended to be able to extract all features from the input data" )
      
    if not 'GDAL_DATA' in os.environ:
      QMessageBox.critical(None, "ERROR", "Please ensure that the GDAL_DATA environment variable is set and try again" )
      self.pushButton_2.setEnabled(False)
      return
      
    try:
      f = open(self.userPrefFile, 'r')
      for line in f:
        if line.startswith('inputDir='):
          self.inputDir = line.split('inputDir=')[1].strip()
        elif line.startswith('outputDir='):
          self.outputDir = line.split('outputDir=')[1].strip()
        elif line.startswith('tempDir='):
          self.tempDir = line.split('tempDir=')[1].strip()
      f.close()
    except:
      pass
    
    if not self.inputDir:
      self.inputDir = defInputDir
    if not self.outputDir:
      self.outputDir = defOutputDir
    if not self.tempDir:
      self.tempDir = defTempDir
      
    # Populate the dialogs
    self.inputDirLineEdit.setText(self.inputDir)
    self.outputDirLineEdit.setText(self.outputDir)
    self.tempDirLineEdit.setText(self.tempDir)
    
  def browseInputFolder(self):
    startDir = str( self.inputDirLineEdit.text() )
    dir = QFileDialog.getExistingDirectory(self, 'Input Folder', startDir, QFileDialog.ShowDirsOnly)
    self.inputDir = dir
    self.inputDirLineEdit.setText(self.inputDir)
    
  def browseOutputFolder(self):
    startDir = str( self.outputDirLineEdit.text() )
    dir = QFileDialog.getExistingDirectory(self, 'Output Folder', startDir, QFileDialog.ShowDirsOnly)
    self.outputDir = dir
    self.outputDirLineEdit.setText(self.outputDir)
    
  def browseTempFolder(self):
    startDir = str( self.tempDirLineEdit.text() )
    dir = QFileDialog.getExistingDirectory(self, 'Temporary Folder', startDir, QFileDialog.ShowDirsOnly)
    self.tempDir = dir
    self.tempDirLineEdit.setText(self.tempDir)
      
  def accept(self):
    
    import subprocess
    import shlex
    import os
    from osmmloader import OsmmLoader
    
    self.pushButton_2.setEnabled(False)
    self.pushButton_2.setText('Working')
    
    # Store prefs
    f = open(self.userPrefFile, 'w')
    f.write('inputDir=' + str( self.inputDirLineEdit.text() ) + '\n')
    f.write('outputDir=' + str( self.outputDirLineEdit.text() ) + '\n')
    f.write('tempDir=' + str( self.tempDirLineEdit.text() ) + '\n')
    f.close()
    
    # create a config file in the temp folder
    # envoke the 3rd party script on this
    # looks for errors
    # (what about script depends)?
    # remove the config file
    
    config = {
      'src_dir' : str( self.inputDirLineEdit.text() ),
      'tmp_dir' : str( self.tempDirLineEdit.text() ),
      'out_dir' : str( self.outputDirLineEdit.text() ),
      'prep_cmd' : "python preposmm4ogr.py --output-to-shape $file_path",
      'ogr_cmd' : 'ogr2ogr -f "ESRI Shapefile" $out_path $file_path',
      'gfs_file' : "osmm_topo_shape.gfs",
      'standalone' : False }
      
    QMessageBox.information(None, "Please be patient", "The conversion process may take some time, during which, QGIS may become irresponsive" )
    
    self.pushButton_2.setText('Working...')
    self.pushButton_2.setEnabled(False)
    
    os.chdir( self.pluginRoot )
    loader = OsmmLoader(config)
    
    self.pushButton_2.setText('Convert')
    self.pushButton_2.setEnabled(True)
    
    ret, messages = loader.getStatus()
    
    if ret == 0:
      QMessageBox.information(None, "INFO", "Conversion complete" )
    else:
      QMessageBox.critical(None, "ERROR", "Conversion failed:\n\n" + messages )
    

  def about(self):
    from DlgAbout import DlgAbout
    dialog = DlgAbout(self)
    dialog.exec_()

