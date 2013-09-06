#!/usr/bin/env python

import wx
import os
import audio
import string

class RyoubaBoard(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(600,400))
        self.CreateStatusBar() # at bottom of window

        filemenu = wx.Menu()
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About","Push buttons to make Ryouba talk!")
        menuOpen = filemenu.Append(wx.ID_OPEN,"&Open","Select a clip.")
        menuSaveAs = filemenu.Append(wx.ID_SAVEAS, "Save &As...", "Save this shit")
        menuExit = filemenu.Append(wx.ID_EXIT,"&Exit","Run away!")

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File")

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnSaveAs, menuSaveAs)

        self.buttons = []
        self.files = []
        self.directory = "clips"

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Lay em out
        self.SetSizerAndFit(self.sizer)
        #self.AutoLayout =(1)
        #self.sizer.Fit(self)
        self.Show()

  # variables needed a long the way. this probably bad

#    def AddButton(self, filename):
# RyoubaBoard.sizer2.Add(RyoubaBoard.buttons.append(wx.Button(self, -1, "Button &"+str(filename)))) 
    
    def OnAbout(self, e):
        dlg = wx.MessageDialog(self, "Push buttons to make Ryouba talk!", "About Ryouba Sound Board", wx.OK)
        dlg.ShowModal() # Shows it.
        dlg.Destroy() # Close it.

    def OnExit(self,e):
        self.Close(True) # Close teh frame

    def OnSaveAs(self, e):
       self.dirname = "."

       dlg = wx.FileDialog(self, "Choose a save location", self.dirname, "New Soundboard", "*.sb", wx.OPEN)
      
       if dlg.ShowModal() == wx.ID_OK:
           self.filename = dlg.GetFilename()
           self.dirname = dlg.GetDirectory()
           self.directory = self.dirname
           file = open(os.path.join(self.dirname, self.filename), 'w+')

           for files in self.buttons:
               file.write(files.myname + "\n")


           file.close()
       dlg.Destroy() 

    def OnOpen(self,e):
      global buttoncount
      """Open a clip"""
      self.dirname = "clips" if self.directory is None else self.directory

      dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
      
      if dlg.ShowModal() == wx.ID_OK:
          self.filename = dlg.GetFilename()
          self.dirname = dlg.GetDirectory()
          self.directory = self.dirname
          file = open(os.path.join(self.dirname, self.filename), 'r')
          
          # The button creation and binding should be a separate function. 
          self.buttons.append(wx.Button(self, label=string.capitalize(self.filename[:-4])))
          #i = len(self.buttons) - 1
          #self.Bind(wx.EVT_BUTTON, self.OnClick(file), self.buttons[i])
          self.buttons[-1].Bind(wx.EVT_BUTTON, self.OnClick)
          self.buttons[-1].myname = os.path.join(self.dirname, self.filename)
          self.sizer.Add(self.buttons[-1], 0, wx.ALIGN_CENTER|wx.ALL, 5)
          self.Fit()

          file.close()
      dlg.Destroy()

    def OnClick(self, event):
          audio.sayit(event.GetEventObject().myname)

app = wx.App(False)
frame = RyoubaBoard(None, "Ryouba Sound Board")
app.MainLoop()



