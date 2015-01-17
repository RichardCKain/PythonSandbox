# a way to play with strings
# by Richard Kain, Python NOOB v.1 Jan 17 2015
# what if I change text at github.com will it sync back?

import time
import random


name = raw_input('Enter a name for me to mess with: ')
allletters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#allletters good practice; initially entered without quotes.
scrabbleTuples = [ (1, "EAIONRTLSU"),   (5, "K"),
                   (2, "DG"),           (8, "JX"),
                   (3, "BCMP"),         (10, "QZ"),
                   (4, "FHVWY") ]


def namebox(name):
    print
    print "Box It Up!"
    print
    times = 1
    print
    print " "+name[::-1]

    for character in name:
        print character + " "*len(name)+ name[-times] # had done 'character[-1]'
        times += 1
        time.sleep(.25)
        
    print " "+name

def waterfall(name):
    print "Waterfall!"
    print
    print name
    for i in range(len(name)):
        name = name[1:]+name[0]
        print name
        time.sleep(3/(i+1))
    #now makes a river
    #width = len(name)*3 # if I want to constrain river
    startingPoint = 1
    for i in range(100):
        time.sleep(.25)
        print " " * startingPoint + name
        startingPoint += random.randint(-1,2)
        if startingPoint < 0:
            startingPoint = 0
        
    


    #so it speeds down; should I speed it up?  had gotten error with first writing ".i"
# then zeroDivision Error on 3/i and 3.0/i; prints in for loop just once. Demonstrated range starts with 0
# but just adding 10/i+1 doesn't work thanks to order of operations!
# could make this accelerating waterfall but should make it as nested function

def jumbler(name):
    print
    print "The Random Jumbler!"
    for i in range(len(name)):
        print
        for j in range(len(name)):
            print name[random.randrange(len(name))],
    print   

# def popper(name): just pop out letters
# def scrabbleScore(name):
    #How many points?  (adapated from http://infohost.nmt.edu/tcc/help/pubs/python/play/scrabble.py
# def letterRoulette(name):   
    
jumbler(name) 
namebox(name)  # Oct 18: made it a function so I could add more functions
waterfall(name)

