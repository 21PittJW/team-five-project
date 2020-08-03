from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Med Software V0.0")

print("v 0.0")

#sets up the window to put buttons, text etc. in
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#code for creating a button
ttk.Button(root, text="start").grid()

root.mainloop()


#to add:
# allergies - head/face
# pink eye - head/face
# cold - head/face
# flu - head/face
# headache - head/face
# sinus infection - head/face
# mononucleosis - head/face
# ear infection - head/face
# stomach ache - body
# acute bronchitis - body/chest
# coronavirus - body/lungs
# tuberculosis - body/lungs
# fever - temperature
# hypothermia - temperature
# hyperpyrexia - temperature

#def getTemp():
    #arduino temp module

#user inputs here

#if loop tree here

#output here
