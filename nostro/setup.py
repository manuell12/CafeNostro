__author__ = 'Manuel Lavin Esteban Huenuman Daniel Molina Tomas Vera' #Tu nombre o el del autor
# Let's start with some default (for me) imports...
import sys
from cx_Freeze import setup, Executable
#Para compilar el setup usar en cmd: python setup.py bdist_msi

build_exe_options = {
"include_msvcr": True   #skip error msvcr100.dll missing
}
# Process the includes, excludes and packages first

carpeta = 'CafeNostro'  #nombre de la carpeta donde se instalara el programa

if 'bdist_msi' in sys.argv:
    sys.argv += ['--initial-target-dir', 'C:\Program Files\\ ' + carpeta]

includes = ['atexit','sys', 'PySide.QtGui','PySide.QtCore','PySide.QtNetwork','PySide.QtWebKit', 'MySQLdb', 'random','os','datetime','time','reportlab.pdfgen.canvas','reportlab.lib.pagesizes','_winreg','subprocess'] #librerias que lleva tu proyecto separadas por comas entre comillas
excludes = []
packages = []
path = []
include_files = ['admin_empresa','admin_productos','admin_usuarios', 'estadisticas','images', 'login','main_window','ventas','style.qss'] #carpetas que lleva tu aplicacion separadas por comas entre comillas
include_msvcr = ['networkChanger.exe.manifest']

if sys.platform == 'win32':
    base = 'Win32GUI'
if sys.platform == 'linux' or sys.platform == 'linux2':
    base = None

cafeNostro = Executable(
    # what to build
    script = "CafeNostro.py",
    initScript = None,
    base = 'Win32GUI',
    #targetName = "installer.exe",
    compress = True,
    copyDependentFiles = True,
    appendScriptToExe = False,
    appendScriptToLibrary = False,
    #icon = "YOUR ICON FILE.ico"
    icon = "logo.ico" #ruta del icono del programa
    #shortcutName="DHCP",
    #shortcutDir="ProgramMenuFolder"
    )

setup(

    version = "1.0", # version
    description = "Punto de venta", #descripcion
    author = "Manuel Lavin Esteban Huenuman Daniel Molina Tomas Vera", #autor
    name = "CafeNostro", #nombre del programa

    options = {
            "build_exe": {
                "includes": includes,
                "excludes": excludes,
                "packages": packages,
                "path": path,
                "include_files": include_files,
                "include_msvcr": include_msvcr
            }
    },
    executables=[cafeNostro],
    requires=['PySide', 'cx_Freeze', 'simplejson']
    )
