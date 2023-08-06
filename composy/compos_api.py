# Comosy - Compos API python wrapper
# Compos Automation object interface
__all__ = ['compos']

# general library imports
import sys
import os
import clr
from pathlib import Path

# pythonnet clr-loader import of Marshal
clr.AddReference("System.Runtime.InteropServices")
from System.Runtime.InteropServices import Marshal

# pythonnet clr-loader try import of Compos_8_6.dll
sys.path.append(os.path.dirname(__file__))
clr.AddReference("Compos_8_6")
import Compos_8_6 as compos