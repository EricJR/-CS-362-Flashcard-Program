#Using cx_freeze to create and executable 
#usage: python3 setup.py build
#usage for mac: python3 setup.py bdist_mac
#Trying to use the example: https://vimeo.com/60208841

#I am getting the error: error: [Errno 2] No such file or directory: '/Library/Frameworks/Tcl.framework/Versions/8.5/Tcl'

application_title = "Flash_Card_Program"
main_python_file = "flashCards.py"

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

includes = ["atexit","re"]

setup(
      name = application_title,
      version = "1.0",
      description = "Sample cx_Freeze PyQt4 script",
      options = {
      "build_exe" : {
      "includes" : includes,
      "excludes": ['Tcl', 'ttk', 'tkinter', 'Tkinter'],
      }
      },
      executables = [
                     Executable(main_python_file, base = base)
                     ]
      )
