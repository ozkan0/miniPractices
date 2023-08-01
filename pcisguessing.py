# @author dono
# tr, bilgisayar, tutulan sayıyı tahmin ediyor
# en, computer guessing the set number
import random
import time
#all variables below are modifiable
x = 500
thenumber=291
guess=0

def guessing(lowref=1,highornot=0,highref=x):
    #making the first guess
    guess = random.randint(1,x)
    while guess != thenumber:
        if guess < thenumber:
            #checking if the first higher number is guessed. If not, this will count the x as high number reference
            if highornot == 0:
                print(f'{guess} sayısını tahmin etmiştim fakat küçükmüş. Tekrar deniyorum...')
                lowref = guess
                guess = random.randint(lowref+1,x-1)
            else:
                #guessing part of lower number
                print(f'{guess} sayısını tahmin etmiştim fakat küçükmüş. Tekrar deniyorum...')
                lowref = guess
                guess = random.randint(lowref+1,highref-1)
        elif guess > thenumber:
            #guessing part of higher number. highornot counter is not important after the first increase
            print(f'{guess} sayısını tahmin etmiştim fakat büyükmüş. Tekrar deniyorum...')
            highref = guess
            highornot += 1
            guess = random.randint(lowref+1,highref-1)
    print(f'Cevap {guess}, bildim!')
guessing()