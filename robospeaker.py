import pyttsx3

if __name__== "__main__": #Making sure the code inside runs directly without referring to other py files
    print("------------------------Welcome------------------------".center(50))
    print("-------------------------------------------------------")
   
    while True: #loops keep going as long as we don't press 'q'
        x = input("Enter what do you want to pronounce ('q' to break): ")
        eng = pyttsx3.init() #Init is like an engine that converts energy from one source to another. So, init converts the text to speech
        eng.say(x) #pronounce the scripts
        eng.runAndWait() 
        #waits until the speech engine finishes speaking the input text before moving on to the next command

        if x == "q": #breaks the loop
            break
