import pyttsx3

if __name__== "__main__": #Making sure the code inside runs directly without referring to other py files
    print("________________________Welcome________________________".center(50))
    print("-------------------------------------------------------")
    while True: #loops keep going as long as we don't press q
        x = input("Enter what do you want to say ('q' to break): ")
        eng = pyttsx3.init() #use init to convert the text to speech
        eng.say(x) #pronounce the scripts
        eng.runAndWait() 
        #wait until the speech engine finishes speaking the input text before moving on next command

        if x == "q": #breaks the loop
            break
