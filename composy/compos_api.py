"""
Composy - Compos API python wrapper
Module loading Compos API (.dll)
"""
__all__ = ['compos_api']

# general library imports
import sys
import os
import clr

# pythonnet clr-loader import of Marshal
clr.AddReference("System.Runtime.InteropServices")
from System.Runtime.InteropServices import Marshal

# pythonnet clr-loader try import of Compos_8_6.dll
sys.path.append(os.path.dirname(__file__))
clr.AddReference("Compos_8_6")
import Compos_8_6 as compos_api
