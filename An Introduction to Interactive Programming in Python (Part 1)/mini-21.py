# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# helper function to start and restart the game

range_limit = 100

def new_game():
    # initialize global variables used in your code here
    
    global secret_number
    global guess_limit
    if range_limit == 100:
        secret_number = random.randrange(0, 100)
        guess_limit = int(math.ceil(math.log(99, 2)))
    elif range_limit == 1000:
        secret_number = random.randrange(0, 1000)
        guess_limit = int(math.ceil(math.log(999, 2)))
    print secret_number
    # remove this when you add your code    
    


# define event handlers for control panel

def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number
    global guess_limit
    global range_limit
    range_limit = 100
    secret_number = random.randrange(0, 100)
    guess_limit = int(math.ceil(math.log(99, 2)))
    print 'Start of new game!'
    print secret_number
    #print guess_limit
        

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number
    global guess_limit
    global range_limit
    range_limit = 1000
    secret_number = random.randrange(0, 1000)
    guess_limit = int(math.ceil(math.log(999, 2)))
    print 'Start of new game!'
    print secret_number
    #print guess_limit
   
    
def input_guess(guess):
    # main game logic goes here	
    
    global guess_limit
    guess = int(guess)
    guess_limit = guess_limit - 1
    
    #print "User's guess was", guess
    
    if guess < secret_number:
        if guess_limit == 1:
            print "User's guess was", guess, '- Higher'
            print 'You lost! Start of new game'
            new_game()
            print
        elif guess_limit > 0:
            print "User's guess was", guess, '- Higher'
            print 'Remains', guess_limit, 'guesses'
            print
    elif guess > secret_number:
        if guess_limit == 1:
            print "User's guess was", guess, '- Lower'
            print 'You lost! Start of new game'
            new_game()
            print
        elif guess_limit > 0:
            print "User's guess was", guess, '- Lower'
            print 'Remains', guess_limit, 'guesses'
            print
    elif guess == secret_number:
        print "User's guess was", guess, '- Correct!'
        print 'You won!'
        new_game()    
    
        
        
  
    # remove this when you add your code
  
    
# create frame

frame = simplegui.create_frame('Guess the number', 200, 200)
inp = frame.add_input('Guess', input_guess, 100)
button1 = frame.add_button('0-100', range100)
button2 = frame.add_button('0-1000', range1000)
# register event handlers for control elements and start frame

frame.start()
# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
