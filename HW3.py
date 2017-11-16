##Crawford Kennedy, CS-1301, 17ckennedy@woodward.edu
##I worked on the homework assignment alone, using only this semester's course materials.

def mixtapeFire(timesPlayed, rating): ##Here I define the function
    if rating>10: ##Checks for an invalid input
        return "Invalid input. Try again" ##informs the user of the invalid input if it exists
    elif rating>5 and timesPlayed>9999: ##checks if the mix tape is fire
        return "Your mix tape is fire" ##returns that the mixtape is fire if it is
    else: ##catches all cases of valid input that aren't fire mix tapes
        return "You should quit the rap game." ##informs the user that their mix tape is no good and that they should quit the rap game.
    
def myFavSong(song, artist):
    guesses = 0 ##setting up my variables
    win = 0
    hints = 0
    hint = "hint"
    while (guesses < 5 and win == 0): ##while loop confirms you are still under the maximum guesses and haven't won yet
        guesses = guesses+1 ## increment guesses
        guess = input("Guess my favorite song:") ##takes user guess
        if song.lower() == guess.lower(): ##determines if the guess was correct
            win = 1
            print("Great Job! It took you", guesses, "tries and", hints, "hints to guess my favorite song.")
        elif guess.lower() == hint: ##determines if you were just asking for a hint
            guesses = guesses-1
            print("The artist of this song is", artist)
            hints = hints+1
        else: ##this is used for getting the answer wrong
            print("Try Again.")
            if guesses == 5: ##makes sure you are under the guess limit and informs you if you have hit the cap
                print("Thanks for playing. You have reached the maximum number of allowed guesses")

def illuminatiConfirmed(secretMsg):
    at = '@' ##setting up my variables
    count = 0 
    for character in secretMsg: ##for loop counts how many @ symbols are in the message
        if character == at:
            count = count+1
    if count>2: ##determines if the count is high enough to be an illuminati message
        print(secretMsg.replace("@", "a")) ##prints the illuminati message, but uses the replace function to take out all of the @ symbols and add a's instead
        return "illuminati Confirmed."
    else: ##is called if the message isn't from the illuminati
        print(secretMsg)
        return "Probably not the Illuminati"
    
def decNum(aString, aNum):
    occurences = aString.count(str(aNum)) ##confirms the number occurs in the string
    if occurences>0:
        return aString.replace(str(aNum), str(aNum-1)) ##returns the appropriate string
    else: ##askis you to try again if the number isn't found within the string
        return "Try a different number"

def numberTie(num):
    initial = num
    while (num>0):
        spaces = 0 ##declare variables
        count = 0
        string = ""
        while (count<(num*2)): ##creates a string that will be the next row of the tie
            string = string+str(num)
            count = count+1
        print('{:^20}'.format(string)) ##prints the created string as a formatted string so it stays centered
        num = num-1
    while (num<initial): ##does the same as the above while loop but symbols are reversed because we are creating a flipped version of the pyramid
        spaces = 0
        count = 0
        string = ""
        while (count<(num*2)): 
            string = string+str(num)
            count = count+1
        print('{:^20}'.format(string))
        num = num+1
    while (num>0): ##identical to the function of the first while loop
        spaces = 0
        count = 0
        string = ""
        while (count<(num*2)):
            string = string+str(num)
            count = count+1
        print('{:^20}'.format(string))
        num = num-1

def countDown(start, limit, decrement):
    string = "" ##declare variables
    initial = start
    while (start>=limit): ##runs until it hits the limit
        if start<initial: ##makes sure this isn't the first run through because we don't want a comma at the beggining
            string = string+"," ##adds a comma to the string
        string = string+str(start) ##adds the decremented number to the string
        start = start-decrement ##decrements the number
    print(string) ##prints the final string
