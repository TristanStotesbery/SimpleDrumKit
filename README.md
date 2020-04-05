# SimpleDrumKit
Python Script and Instructions on how I built my drum machine/soundboard

Raspbian OS: https://www.raspberrypi.org/downloads/raspbian/

gpiozero documentation (gpiozero should come with raspbian installed): https://gpiozero.readthedocs.io/en/stable/

pygame.mixer documentation (used to handle loading and playing sound files, this should also come preinstalled with raspbian):
https://devdocs.io/pygame/ref/mixer#module-pygame.mixer

In order to make my python script run on startup, I followed the instructions here:
https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/
I used the first method, which works good, the only problem is I can't figure out how to make the script stop running. This means that any
time i want to update something in the script and test it out I have to restart the pi. Other than that it works great for me.



Parts Used:
  -12 normally open buttons (You can use any buttons you want, these are the ones that I used) :
  https://www.amazon.com/Twidec-Normal-Momentary-Pre-soldered-PBS-110-XBKR/dp/B07RTZVZ6L/ref=sr_1_3?dchild=1&keywords=electronic%2Bbuttons&qid=1586117721&sr=8-3&th=1

-Raspberry pi 1 Model B+

-1 Red LED (Again, you can use any LED you want, or even remove the LED completely)
-breadboard and wires
-thin wooden board to mount the buttons to/ make a box out of

Here is a basic tutorial on how I made my drum machine/soundboard for the Raspberry Pi. I used a RPi 1 B+ for this project, but you 
should be able to use any model of Pi. 

First, wire the buttons and LED to the Pi. Connect all of the negative(ground) ends of the buttons to the same ground. Then, connect the 
positive end of each button to it's own GPIO pin on the Raspberry Pi. You can see which pins I used for mine in the wiring diagram.
I also connected an LED, with the negative end connected to the same ground rail and the positive end connected to it's own GPIO pin.

Next, load the sounds you want to use as .wav files onto a flash drive and copy them onto your Pi (Or download them directly, my pi is 
just really slow on the internet so its faster to use another computer). I got my drum sounds as a free download from a website that 
provides free drumkits, they came in a .aiff file type which unfortunately is not supported by pygame, so I used an online converter
to convert them into .wav file type, which I then copied into a folder on my Raspbery Pi.

Now write the python script. Feel free to use the python script I uploaded, or to use mine as a reference to write your own. When I
wrote the code, I first wrote it for just one button, then once I had sound working for the one button, I added another and tweaked
the code until the button presses could play sounds asynchronously. I usually code in Java, C, or C# so I had never coded in python
before this project, so there might be some syntactical/styling errors in the code, or something I could have written much better.
Feel free to let me know if you find anything like this.

Finally, once you have finished testing your script to make it work as you like, set up the script so it will run at startup, that way
you can just plug in the Pi without any monitor, mouse, or keyboard, and once the script runs you can use it! Ifollowed directions from 
a google search to make this work, link above. I also used an LED for this purpose, so the LED will light up when the script is running 
so I know it booted successfully and is running. I currently just plug in headphones or an aux cable to the built-in jack on the Pi to 
hear the output

And you're done! There are a lot of things I want to add to/change about this project, and when I get the time to, I will update the 
code/README file to show any changes I've made. Some things I want to do in the future, that you could consider adding to your own: 
 Connect all of the Buttons to one ADC to make it so they only use one GPIO pin but still work playing sounds asynchronously, 
 upgrade the buttons to be actual drum pad buttons, 
 Add LEDs for each button so a button lights up when it is pressed, 
 have an additional button or 2 that records sound when held, so you can record loops and play more beats over your loops, 
 slide switch or selector that switches between sound presets so you can use different drum kits without changing the code, 
 Adding a sound card and playing sounds through that for higher sound quality
Have fun!
