#!/usr/bin/env python

import wx
import os
import audio
buttoncount = 1

class RyoubaBoard(wx.Frame):



    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(600,400))
        self.CreateStatusBar() # at bottom of window

        filemenu = wx.Menu()
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About","Push buttons to make Ryouba talk!")
        menuOpen = filemenu.Append(wx.ID_OPEN,"&Open","Select a clip.")
        menuExit = filemenu.Append(wx.ID_EXIT,"&Exit","Run away!")

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File")

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
	#self.Bind(wx.EVT_PLAY, self.
        self.Show(True)

        # Sizers.
        self.buttons = []
	#for i in range(0, 6):
	#    self.buttons.append(wx.Button(self, -1, "Button &"+str(i)))
	#    self.sizer2.Add(self.buttons[i], 1, wx.EXPAND)	    

	self.sizer = wx.BoxSizer(wx.VERTICAL)
	#self.sizer.Add(self.sizer2, 0, wx.EXPAND)
	
	# Lay em out
	self.SetSizer(self.sizer)
	self.AutoLayout =(1)
	self.sizer.Fit(self)
	self.Show()

	# variables needed a long the way. this probably bad

#    def AddButton(self, filename):
#	RyoubaBoard.sizer2.Add(RyoubaBoard.buttons.append(wx.Button(self, -1, "Button &"+str(filename)))) 
    
    def OnAbout(self, e):
        dlg = wx.MessageDialog(self, "Push buttons to make Ryouba talk!", "About Ryouba Sound Board", wx.OK)
        dlg.ShowModal() # Shows it.
        dlg.Destroy() # Close it.

    def OnExit(self,e):
	self.Close(True) # Close teh frame

    def OnOpen(self,e):
	global buttoncount
        """Open a clip"""
	self.dirname = ''
	dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
	
 	if dlg.ShowModal() == wx.ID_OK:
	    self.filename = dlg.GetFilename()
	    self.dirname = dlg.GetDirectory()
	    f = open(os.path.join(self.dirname, self.filename), 'r')
	    
	    # The button creation and binding should be a separate function. 
	    self.buttons.append(wx.Button(self, -1, f.name))
	    self.sizer.Add(self.buttons[buttoncount], 1, wx.EXPAND)
            self.Bind(wx.EVT_BUTTON, self.OnClick(f.name), self.button)
            buttoncount += 1 
	    print buttoncount

        f.close()
	dlg.Destroy()

    def OnClick(self, buttonid):
	print "It works!"
        print buttonid

app = wx.App(False)
frame = RyoubaBoard(None, "Ryouba Sound Board")
app.MainLoop()


