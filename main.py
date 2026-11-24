continueLoop = True

while continueLoop == True:           
    userInput = int(input("Enter a BPM: "))
    def beepGeneration():
            import time
            1 / (userInput / 60)
            time.sleep(1 / (userInput / 60))
            import winsound
            winsound.Beep(550, 200)
            beepGeneration()
            
    if userInput < 0 or userInput > 250:
     print("Please enter a BPM value between 0 and 250.")
    else:
        print(f"{userInput} BPM started")
        beepGeneration()
