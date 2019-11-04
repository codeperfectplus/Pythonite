'''
Tkinter is Python Library for devloping  GUI( Graphincs User Interface).Tkinter is most common used GUI.
python with tkinter output the fastest and easiest way to create the GUI applications.
(1).import the module
(2).create the main window 
(3).Add any number ofwidgetss to the main wondow
(4).Apply the event trigger on the widgets.
'''
import tkinter as tk 

#to create a main window
m = tk.Tk()
m.title('Basic Tkinter')

#to add a button in your appliationw
w =tk.Button(m, text ='Exit', width =25, command=m.destroy)
w.pack()

m.mainloop()
