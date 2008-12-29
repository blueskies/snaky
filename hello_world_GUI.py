#!/usr/bin/python

from Tkinter import *
from time    import gmtime, strftime

class Application(Frame):

       """
       Callbacks ... no arguments allowed
       """

       def say_hi(self):
           print "Hello cruel world ...."

       def show_date(self):
           print strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

       """
       Define the interface ...
       """

       def createWidgets(self):

           self.QUIT = Button(self)
           self.QUIT["text"] = "QUIT"
           self.QUIT["fg"]   = "red"
           self.QUIT["command"] =  self.quit
           self.QUIT.pack({"side": "left"})

           self.DATE = Button(self)
           self.DATE["text"] = "DATE"
           self.DATE["fg"]   = "red"
           self.DATE["command"] =  self.show_date
           self.DATE.pack({"side": "left"})

           self.hi_there = Button(self)
           self.hi_there["text"] = "Hello",
           self.hi_there["command"] = self.say_hi
           self.hi_there.pack({"side": "left"})

       """
       Initialization code ...
       """

       def __init__(self, master=None):

           Frame.__init__(self, master)
           self.pack()
           self.createWidgets()

       """
       Application starts ...
       """

root = Tk()
app = Application( master=root )
app.master.title("First python GUI application")
app.master.maxsize(1000, 400)

app.mainloop()
root.destroy()

