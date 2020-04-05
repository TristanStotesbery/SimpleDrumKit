#BASIC DRUMPAD SCRIPT
#Tristan Stotesbery
#04/05/2020
#Disclaimer: This is my first python code, so forgive me for 
#			 Improper styling or syntax if there is any

# Load this code with .wav files, and wire to buttons to make your
# Raspberry Pi work as a drum machine, or soundboard


#import statements for the different libraries used
#gpiozero handles gpio input and output, pygame is used to handle loading
#and playing sounds
from gpiozero import Button
from gpiozero import LED
from time import sleep
import pygame

#initialize the LED to tell when the script is running
#ledx = LED(num) means assign gpio pin num to be an LED an place that in variable ledx
led1 = LED(20)

#pre_init sets the pygame settings for initialization. All of these
#values are the default exept for the last, which is lowered from the default
#to reduce the latency of button pushes to sound playing.
#read the pygame documentation for more info
pygame.mixer.pre_init(22050, -16, 2, 1024)

#initialize the pygame.mixer module which handles sound
pygame.mixer.init()

#set how many channels can be playing at once. Pygame is supposed to handle this 
#automatically, but i set each sound to it's own individual channel manually to make 
#hopefully run a little bit faster. 
pygame.mixer.set_num_channels(12)


#initialize the different sounds that you want to use with the drum pad.
#Replace the file path and file name with the path and name of the .wav
#files you are using


# soundx = pygame.mixer.Sound('filepath') means use the pygame library to 
# load a sound file, and store it in a variable named soundx

#channelx = pygame.mixer.Channel(num) means make a variable called channelx
# and store one of the pygame channels that you assigned to that  variable
sound1 = pygame.mixer.Sound('/home/pi/Documents/sounds/tom1.wav')
channel1 = pygame.mixer.Channel(0)

sound2 = pygame.mixer.Sound('/home/pi/Documents/sounds/kick1.wav')
channel2 = pygame.mixer.Channel(1)

channel3 = pygame.mixer.Channel(2)
sound3 = pygame.mixer.Sound('/home/pi/Documents/sounds/cl_hihat.wav')

channel4 = pygame.mixer.Channel(3)
sound4 = pygame.mixer.Sound('/home/pi/Documents/sounds/conga1.wav')

channel5 = pygame.mixer.Channel(4)
sound5 = pygame.mixer.Sound('/home/pi/Documents/sounds/cowbell.wav')

channel6 = pygame.mixer.Channel(5)
sound6 = pygame.mixer.Sound('/home/pi/Documents/sounds/crashcym.wav')

channel7 = pygame.mixer.Channel(6)
sound7 = pygame.mixer.Sound('/home/pi/Documents/sounds/handclap.wav')

channel8 = pygame.mixer.Channel(7)
sound8 = pygame.mixer.Sound('/home/pi/Documents/sounds/hi_conga.wav')

channel9 = pygame.mixer.Channel(8)
sound9 = pygame.mixer.Sound('/home/pi/Documents/sounds/hightom.wav')

channel10 = pygame.mixer.Channel(9)
sound10 = pygame.mixer.Sound('/home/pi/Documents/sounds/kick2.wav')

channel11 = pygame.mixer.Channel(10)
sound11 = pygame.mixer.Sound('/home/pi/Documents/sounds/open_hh.wav')

channel12 = pygame.mixer.Channel(11)
sound12 = pygame.mixer.Sound('/home/pi/Documents/sounds/snare.wav')

#define methods for each sound to be called when a button is pressed
def play1():
	channel1.play(sound1)
	
def play2():
	channel2.play(sound2)
	
def play3():
	channel3.play(sound3)
	
def play4():
	channel4.play(sound4)
	
def play5():
	channel5.play(sound5)
	
def play6():
	channel6.play(sound6)
	
def play7():
	channel7.play(sound7)
	
def play8():
	channel8.play(sound8)
	
def play9():
	channel9.play(sound9)
	
def play10():
	channel10.play(sound10)
	
def play11():
	channel11.play(sound11)
	
def play12():
	channel12.play(sound12)

#uses the gpiozero library to register the buttons
# buttonx = Button(num) means make a new Button named buttonx, 
# and assign the button to gpio pin num
#
# buttonx.when_pressed = playx means take the button named buttonx,
# and setting the playx method to be the method that runs when the button 
# is pressed 
button1 = Button(17)
button1.when_pressed = play1
button2 = Button(27)
button2.when_pressed = play2
button3 = Button(22)
button3.when_pressed = play3
button4 = Button(10)
button4.when_pressed = play4
button5 = Button(9)
button5.when_pressed = play5
button6 = Button(11)
button6.when_pressed = play6
button7 = Button(6)
button7.when_pressed = play7
button8 = Button(26)
button8.when_pressed = play8
button9 = Button(23)
button9.when_pressed = play9
button10 = Button(24)
button10.when_pressed = play10
button11= Button(25)
button11.when_pressed = play11
button12= Button(16)
button12.when_pressed = play12

#print to console to know the script is initialized and running successfully
print("running")

#Infinite Loop to keep script running, LED stays on so you can see the script is running without monitor
while True:
	led1.on()
	
		
	
