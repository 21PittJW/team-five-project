#from tkinter import *
#from tkinter import ttk

#root = Tk()
#root.title("Med Software V0.0")

#def buttondel():
#    button1.remove()
#    return

#print("v 0.0")

#sets up the window to put buttons, text etc. in
#mainframe = ttk.Frame(root, padding="3 3 12 12")
#mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
#root.columnconfigure(0, weight=1)
#root.rowconfigure(0, weight=1)

#code for creating a button
#button1 = ttk.Button(root, text="click here to throw an error", command = buttondel).grid()

#label test
#label1 = ttk.Label(mainframe, text="Team 5 Medical Software").grid(column=2, row=2)

#root.mainloop()

# !! ditched tk gui code, not working properly. will fix if time allows.

temperature = 36.443
temperature = round(temperature, 1)
print(temperature)
#this can be changed as needed for debugging

if(temperature <= 35):
    print("hypothermia")
elif(temperature >= 36.5 and temperature <= 37.5):
    print("normal, no fever")
elif(temperature > 37.5 and temperature < 40):
    print("fever")
    ans1 = input("Do you experience pain/aches in your ears, muscles or joints? ")
    if ans1.lower() == "yes":
        ans2 = input("Do you occasionally feel nauseous? ")
        if ans2.lower() == "yes":
            ans3 = input("Do you expereince a sharp pain in your ear followed by a discharge of liquid? ")
            if ans3.lower() == "yes":
                print("You most likely have an Ear Infection")
            elif ans3.lower() == "no":
                print("Check your temperature again, you might have Heatstroke or Hypothermia")
        elif ans2.lower() == "no":
            ans4 = input("Do you have a sore throat?")
            if ans4.lower() == "yes":
                ans5 = input("Do you have rashes around your body?")
                if ans5.lower() == "yes":
                    print("You most likely have Mononucleosis")
                elif ans5.lower() == "no":
                    print("You most likely have the Flu")
            elif ans4.lower() == "no":
                print("You most likely have Rheumatoid Arthritis")
    elif ans1.lower() == "no":
        ans6 = input("Do you frequently sneeze?")
        if ans6.lower() == "yes":
            ans7 = input("Is your face more sensittive to touch?")
            if ans7.lower() == "yes":
                print("You most likely have a Sinus Infection")
        elif ans6.lower() == "no":
            ans8 = input("Do you get chills or shivers occasionally?")
            if ans8.lower() == "yes":
                print("You most likely have TB")
            elif ans8.lower() == "no":
                print("You most likely have Coronavirus")
            elif ans7.lower() == "no":
                print("You most likely have the Common Cold")
 
elif(temperature >= 40):
    print("hyperpyrexia")


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
# rheumatoid arthritis - joints temperature
# hypothermia - temperature
# hyperpyrexia - temperature

#def getTemp():
    #arduino temp module

#user inputs here

#if loop tree here

#output here
