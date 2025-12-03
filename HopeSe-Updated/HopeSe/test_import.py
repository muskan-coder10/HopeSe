
#@author: Ankit
#@title: versionKill
#@version: 1.0
#@date: 2025-12-03

import sys
import os
print(f"CWD: {os.getcwd()}")
print(f"Sys Path: {sys.path}")
try:
    import Frontend
    print("Import Frontend successful")
except ImportError as e:
    print(f"Import Frontend failed: {e}")

try:
    import Backend
    print("Import Backend successful")
except ImportError as e:
    print(f"Import Backend failed: {e}")
