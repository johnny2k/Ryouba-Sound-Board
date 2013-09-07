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
        menuAdd = filemenu.Append(wx.ID_ADD,"&Add Sound","Select a clip.")
        menuOpen= filemenu.Append(wx.ID_OPEN, "&Open", "Open a soundboard")
        menuSaveAs = filemenu.Append(wx.ID_SAVEAS, "Save &As...", "Save this shit")
        menuExit = filemenu.Append(wx.ID_EXIT,"&Exit","Run away!")

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File")

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnAdd, menuAdd)
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
    
    def OnAbout(self, e):
        dlg = wx.MessageDialog(self, "Push buttons to make Ryouba talk!", "About Ryouba Sound Board", wx.OK)
        dlg.ShowModal() # Shows it.
        dlg.Destroy() # Close it.

    def OnExit(self,e):
        self.Close(True) # Close teh frame

    def OnSaveAs(self, e):
       self.dirname = "."

       dlg = wx.FileDialog(self, "Choose a save location", self.dirname, "New Soundboard", "*.rsb", wx.OPEN)
      
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
      self.dirname = "clips" if self.directory is None else self.directory
      dlg = wx.FileDialog(self, "Choose a file", self.dirname, "Open a soundboard", "*.rsb", wx.OPEN)
      
      if dlg.ShowModal() == wx.ID_OK:
          self.filename = dlg.GetFilename()
          self.dirname = dlg.GetDirectory()
          self.directory = self.dirname
          file = open(os.path.join(self.dirname, self.filename), 'r')
          line = file.readline()[:-1]
          while line != "":
              print line
            # TODO: split path up to provide two parameters here.
              self.AddClip(line.rsplit("/", 1)[0], line.rsplit("/")[-1])
              line = file.readline()[:-1]

          file.close()
      dlg.Destroy()


    def OnAdd(self,e):
      global buttoncount
      """Add a clip"""
      self.dirname = "clips" if self.directory is None else self.directory

      dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
      
      if dlg.ShowModal() == wx.ID_OK:
          self.filename = dlg.GetFilename()
          self.dirname = dlg.GetDirectory()
          self.directory = self.dirname
          file = open(os.path.join(self.dirname, self.filename), 'r')
          self.AddClip(self.dirname, self.filename)
          file.close()
      dlg.Destroy()

    def AddClip(self, path, name):
          self.buttons.append(wx.Button(self, label=string.capitalize(name[:-4])))
          #i = len(self.buttons) - 1
          #self.Bind(wx.EVT_BUTTON, self.OnClick(file), self.buttons[i])
          self.buttons[-1].Bind(wx.EVT_BUTTON, self.OnClick)
          self.buttons[-1].myname = os.path.join(path, name)
          self.sizer.Add(self.buttons[-1], 0, wx.ALIGN_CENTER|wx.ALL, 5)
          self.Fit()

    def OnClick(self, event):
          audio.sayit(event.GetEventObject().myname)

app = wx.App(False)
frame = RyoubaBoard(None, "Ryouba Sound Board")
app.MainLoop()



