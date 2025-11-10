"""Noesis Python Plugin

      File: tool_debug.py
    Author: Laurynas Zubavičius (Sparagas)
   Purpose: Opens the Noesis debug log window. It can also show Noesis modules docuemntation.
"""
import pydoc
from inc_noesis import *

def registerNoesisTypes():
    noesis.registerTool("Debug Log Window", debugTool, "Run debug window")
    handle = noesis.registerTool("`inc_noesis` text file", incNoesisTool, "Print to a log window")
    noesis.setToolSubMenuName(handle, "Documentation")
    handle = noesis.registerTool("`noesis` text file", noesisTool, "Print to a log window")
    noesis.setToolSubMenuName(handle, "Documentation")
    handle = noesis.registerTool("`rapi` text file", rapiTool, "Print to a log window")
    noesis.setToolSubMenuName(handle, "Documentation")
    handle = noesis.registerTool("write to html files", htmlTool, "Writes all docs in root folder as html")
    noesis.setToolSubMenuName(handle, "Documentation")
    return 0

def debugTool(toolIndex):
  noesis.logPopup()
  print("\ntype `clear` to clear debug log window...\n")
  return 0

def incNoesisTool(toolIndex):
  help('inc_noesis')
  return 0

def noesisTool(toolIndex):
  help(noesis)
  return 0

def rapiTool(toolIndex):
  help(rapi)
  return 0

def htmlTool(toolIndex):
  pydoc.writedoc('inc_noesis')
  pydoc.writedoc('noesis')
  pydoc.writedoc('rapi')
  return 0
