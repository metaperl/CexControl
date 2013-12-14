#-------------------------------------------------------------------------------
# Name:       CexControl
# Purpose:    Automatically add mined coins on Cex.IO to GHS pool   
#
# Author:     Eloque
#
# Created:    19-11-2013
# Copyright:  (c) Eloque 2013
# Licence:    Free to use, copy and distribute as long as I'm credited
#             Provided as is, use at your own risk and for your own benefit
# Donate BTC: 17w7oe38d8Rm3pHYLwNZLn8TFSBVEaogJA     
#-------------------------------------------------------------------------------

## Preparare Python 3
from __future__ import print_function

from Tkinter import *

## This file is meant only for logging purposes, to have a central place to change logging into print or or other statements



class Logger:
    
    ## Start the Logger object, consider it to be standard to StdOut
    def __init__(self):
        self.PrintToStdOut = True
        self.LogText = ""
        
    def Output( self, Message ):

        if self.PrintToStdOut == True:
            ## Just print it
            print ( Message )
        else:
            self.LogText.set( Message )
    
    def SetOutput(self, Value):
        
        self.PrintToStdOut = Value
        
