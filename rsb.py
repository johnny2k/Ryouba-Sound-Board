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
        audiomenu = wx.Menu()
        helpmenu = wx.Menu()


        ##### FILE MENU ####
        menuOpen= filemenu.Append(wx.ID_OPEN, "&Open", "Open a soundboard")
        menuSaveAs = filemenu.Append(wx.ID_SAVEAS, "Save &As...", "Save this shit")
        menuExit = filemenu.Append(wx.ID_EXIT,"&Exit","Run away!")
        
        #### AUDIO MENU ####
        menuAdd = audiomenu.Append(wx.ID_ADD,"&Add Audio Clip","Select a clip.")
        menuImport = audiomenu.Append(-1,"&Import Soundboard","Select a clip.")

        #### HELP MENU ####
        menuAbout = helpmenu.Append(wx.ID_ABOUT, "&About","Push buttons to make Ryouba talk!")
        

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File")
        menuBar.Append(audiomenu,"&Audio")
        menuBar.Append(helpmenu,"&Help")


        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnAdd, menuAdd)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnSaveAs, menuSaveAs)
        self.Bind(wx.EVT_MENU, self.OnImport, menuImport)

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
        dlg = wx.MessageDialog(self, "Add clips and then push the buttons to hear the sounds.", "About Ryouba Sound Board", wx.OK)
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
      if self.buttons is not None:
          self.RemoveButtons()

      self.OnImport(e)

    def RemoveButtons(self):
      for button in self.buttons:
          button.Destroy()
      
      self.buttons = []


    def OnImport(self, e):
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
              self.AddClip(line.rsplit("/", 1)[0], line.rsplit("/")[-1])
              line = file.readline()[:-1]

          file.close()

#      dlg.destroy()

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
          self.buttons[-1].Bind(wx.EVT_BUTTON, self.OnClick)
          self.buttons[-1].myname = os.path.join(path, name)
          self.buttons[-1].SetToolTipString(string.capitalize(name[:-4]))
          self.sizer.Add(self.buttons[-1], 0, wx.ALIGN_CENTER|wx.ALL, 5)
          
          # Buttons won't align right with this next line. Why? 
          #self.buttons[-1].SetMaxSize(wx.Size(100, 50))
          self.Fit()

    def OnClick(self, event):
          #filename = event.GetEventObject().myname.rsplit("/")[-1][:-1]
          filename = str(event.GetEventObject().myname)
          self.PushStatusText(string.capitalize(filename.rsplit("/", 1)[-1][:-4]))
          audio.sayit(event.GetEventObject().myname)
          self.PushStatusText("")

app = wx.App(False)
frame = RyoubaBoard(None, "Ryouba Sound Board")
app.MainLoop()



