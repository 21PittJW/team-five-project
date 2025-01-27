#from tkinter import *
#from tkinter import ttk
#A module that encapsulates the access to the serial port which allows us to use the arduino.
#import serial

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

# GET TEMP FROM ARDUINO

# temperature = serial.Serial('com6',9600)
# change COM port as needed

#start, pick which option the user wants. I for the diagnosis and k for a BMI calculator.
start = input("Do you want do the diagnosis?\n If so, press i.\n If you want to use the BMI calcualtor, press k.\n")
if start == "k":
  H = float(input("Enter your Height in M: "))
  W = float(input("Enter your Weight in KG: "))
  if (W/H**2)>18.5:
    print("you are underweight")
  elif (W/H**2)>18.5 and (W/H**2)<25:
    print("you are normal")
  elif (W/H**2)>25 and (W/H**2)<30:
    print("you are overweight")
  elif (W/H**2)<30:
    print("you are obese")
elif start == "i":
  #fake temp for testing
  temperature = 37
  temperature = round(temperature, 1)
  print(temperature)
#this can be changed as needed for debugging
  #if below 35 degrees
  if(temperature <= 35):
    print("hypothermia")
    #if above or equal to 36.5 and below or equal to 37.5 degrees
  elif(temperature >= 36.5 and temperature <= 37.5):
    print("normal, no fever")
    ans1 = input("Do you feel fatigued or nauseous? ")
    if ans1.lower() == "yes":
      ans2 = input("Do you have frequent abdominal pains? ")
      if ans2.lower() == "yes":
        print("You most likely have Food Poisoning. \n Common symptoms include abdominal pain, diarrhea, vomiting, nausea, headaches and weakness. \n Most food poisoning is mild and resolves without treatment. Ensure you are hydrated.")
      elif ans2.lower() == "no":
        print("You most likely have Bronchitis. \n Common symptoms include coughing, runny nose, fatigue, shortness of breath, slight chills and chest discomfort. \n Soothing remedies for coughs can help with treatment, though it will mostly go away by itself in a few weeks time.")
    elif ans1.lower() == "no":
      ans3 = input("Do you have hives or a swollen lip, tongue or face? ")
      if ans3.lower() == "yes":
        print("You most likely have food allergies. \n Common symptoms include, stomach aches, wheezing, tightness of chest, hives and a swollen body. \n Use antihistamine drugs against mild reactions, severe reactions require an epipen as well as hospital care as soon as possible.")
      elif ans3.lower() == "no":
        print("You most likely have Pink Eye/Conjunctivitis. Common symptoms include, a red/pink eye, increased tear production, itchy eyes and discharge or crusting of the eyes. \n Most of the time, it will go away on its own. If you wear contacts, stop for a small period of time as this will slow recovery.")
  #if temp is above 37.5 and below 40 degrees
  elif(temperature > 37.5 and temperature < 40):
    print("fever")
    ans1 = input("Do you experience pain/aches in your ears, muscles or joints? ")
    if ans1.lower() == "yes":
        ans2 = input("Do you occasionally feel nauseous? ")
        if ans2.lower() == "yes":
            ans3 = input("Do you expereince a sharp pain in your ear followed by a discharge of liquid? ")
            if ans3.lower() == "yes":
                print("You most likely have an Ear Infection.\n Common symptoms are ear pain and a fever, less commonly there may be drainage of fluid from the ear or hearing loss.\n Most Ear infections go away naturally, if not antibiotics may help.")
            elif ans3.lower() == "no":
                print("Check your temperature again, you might have Heatstroke or Hypothermia")
        elif ans2.lower() == "no":
            ans4 = input("Do you have a sore throat?")
            if ans4.lower() == "yes":
                ans5 = input("Do you have rashes around your body?")
                if ans5.lower() == "yes":
                    print("You most likely have Mononucleosis aka Glandular fever.\n Mononucleosis is transfered via saliva, common symptoms include fatigue, fever, sore throat, rash and swollen glands.\n Treatment includes rest, fluids and over-the-counter pain and fever-reducing medicines.")
                elif ans5.lower() == "no":
                    print("You most likely have the Flu.\n Common symptoms include fever, chills, muscle aches, cough, congestion, runny nose, headaches and fatigue.\n Primarily treated with rest and fluid, over-the-counter anti-inflammatory pain relievers may help with symptoms.")
            elif ans4.lower() == "no":
                print("You most likely have Rheumatoid Arthritis.\n Symptoms include warm, swollen and painful joints, pain and stiffness often worsen after rest. Commonly the wrist and hand are involved.\n Treatments include DMARDs, which are Disease-modifying antiheumatic drugs that can slow the progression of rheumatoid arthritis.")
    elif ans1.lower() == "no":
        ans6 = input("Do you frequently sneeze?")
        if ans6.lower() == "yes":
            ans7 = input("Is your face sensitive to touch?")
            if ans7.lower() == "yes":
                print("You most likely have a Sinus Infection.\n Common symptoms include headache, facial pain, runny nose, and nasal congestion.\n It is not very serious and therefore does not require much treatment other than symptomatic releif with pain medication, nasal decongestants and nasal saline rinses.")
            elif ans7.lower() == "no":
                print("You most likely have the Common Cold.\n Generally harmless, common symptoms include runny nose, sneezing and congestion.\n Most recover on their own within 2 weeks, if symptoms persist or there are signs of serious symptoms such as a high fever, go see a doctor, especially if they are a child.")
        elif ans6.lower() == "no":
            ans8 = input("Do you get chills or shivers occasionally?")
            if ans8.lower() == "yes":
                print("You most likely have TB.\n Can spread when an infected person coughs or sneezes.\n Symptoms do not occur immediately, symptoms include a cough (sometimes blood-tinged), weight loss, night sweats and fever.\n If you suspect you have TB, go see a doctor to aquire swift medical assistance.")
            elif ans8.lower() == "no":
                print("You most likely have Coronavirus.\n Most people with Covid will experience mild to moderate symptoms, these include fever, dry cough, tiredness.\n Most people who have Covid will recover without special treatment. However it is heavily advised that you get tested as soon as possible and follow the governments decision.")
#if temp is above or equal to 40 degrees 
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


