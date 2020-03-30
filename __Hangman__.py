import random
#First      CreaTE    the     list    of      words
animals=['elephant','monkey','donkey','horse','dog','cat','chimpanze','ape','rat','kiwi']
places=['america','india','japan','china','arab','srilanka','russia','germany']
games=['mario','pacman','pubg']
print('Select the Category you want to play :')
print('1.Animals')
print('2.Places')
print('3.Games')
choice1=int(input("Enter your choice :"))
if choice1==1 :
    words=animals.copy()
elif choice1==2 :
    words=places.copy()
elif choice1==3 :
    words=games.copy()

#   TO  ACCESS  A   WORD    FOR     EVERY   ATTEMPT
def getword() :
    word=random.choice(words)
    return word.upper()

#ACTUAL     GAME    CODE

def playgame(word) :
    word_completion='_'*len(word)
    #guessed variable used for telling if the game is finished or not
    guessed=False
    guess_letter=[]
    tries=6
    print('LETS START THE GAME!!')
    print(displayhangman(tries))
    print('The Word You will be Guessing  ::'+"_ "*len(word))
    print()
    print()
    print("START GUESSING THE WORDS ::\n")
    while not guessed and tries>0 :
        guess=input("Enter your guess word by word!!..").upper()
        if guess.isalpha() :   #JUST    TO  MAKE    SURE    IT  IS  ALPHABET
            if guess in guess_letter :    #IF   ALREADY GUESSED THE SAME    LETTER
                print('You have already guessed the letter',guess,'Try another word!!..')
            elif guess not in word:    #IF  THE GUESS    IS  INCORRECT
                print(guess," is an incorrect word..")
                tries-=1
                guess_letter.append(guess)
            else :    #IF   YOUR    GUESS   IS  CORRECT
                print(guess,'is a coreect guess keep trying...')
                guess_letter.append(guess)
                new=list(word_completion)
                ind=[i for i,l in enumerate(word) if guess==l]
                for i in ind :
                    new[i]=guess
                word_completion=''.join(new)
                print(word_completion)
                if '_' not in word_completion :  #ALL   THE LETTERS ARE FILLED
                    guessed=True
                    print("You have Finished the game!!!...")
        else :
            print("Sorry, Invalid guess !!..")
            tries-=1
        print(displayhangman(tries))

# MY HANGMAN GRAPHICS
def displayhangman(tries) :
    ans=['''           -------------@
            |            
            |           
            |      FATALITY     
            |        SEE
            |        YOU    
            |         IN   
            |         HELL
            |_____________''',
        '''               ---------------@
           |              |
           |              |
           |             ()
           |             /|/
           |              |
           |              /
           |_______________''',
           '''           -------------@
            |            |
            |            |
            |           ()
            |           /|/
            |            |
            |            
            |
            |_____________''',
            '''          -------------@
            |            |
            |            |
            |           ()
            |           /|
            |           
            |          
            |
            |_____________''',
            '''          -------------@
            |            |
            |            |
            |           ()
            |            |
            |            
            |            
            |
            |_____________''',
            '''          -------------@
            |            |
            |            |
            |           ()
            |           
            |            
            |            
            |
            |_____________''',
            '''           -------------@
            |            |
            |            |
            |           
            |        
            |            
            |            
            |        
            |_____________'''
            ]
    return ans[tries]


#TO     MAKE    THE CODE    RUNNING
x=getword()
playgame(x)
