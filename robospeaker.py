import pyttsx3
if __name__=="__main__":
    print("Welcome to Robo Speaker".center(50))
    while True:
        x = input("Enter what do you want to pronounce: ")
        eng = pyttsx3.init()
        eng.say(x)
        eng.runAndWait()

        if x == "q":
                break
