# @author dono/ozkan0
# tr, basit sayaç
# en, basic timer
import time

def countdown(t):
    while t:
        mins, secs = divmod(t,60)
        timer='{:02d}:{:02d}'.format(mins,secs)
        print(timer,end="\r")
        time.sleep(1)
        t -= 1
    print("Sayaç bitti")

t = input("Sayaç süresini girin: ")
countdown(int(t))