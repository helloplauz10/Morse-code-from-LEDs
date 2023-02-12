import os
import time
import argparse
import json
morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----'
}
pars = argparse.ArgumentParser(prog="")
pars.add_argument("--dot-ledfolder",help="Used to identify that it is a dot and blinks after 0.5s (Optional but needs the --dash-ledfolder argument)")
pars.add_argument("--dash-ledfolder",help="Used to identify that is a dash and blinks after 2.4s (Optional but needs the --dot-ledfolder argument)")
pars.add_argument("--led-folder",help="If you din't placed a --dot-ledfolder or a --dash-ledfolder argument, use this argument. This argument is needed (unless --dot-ledfolder and --dash-ledfolder is placed)")
pars.add_argument("--text",help="Text that has a special character like !$&@ will be ignored instead of powering the leds. This argument is needed (When placing this argument that has spaces around its text, add a quote in it)")
pars.add_argument("--dot-delay",help="Delays from blinks (Example: this argument is set to 2.3 so it will power up the led, wait for 2.3s, power off the led and wait for 2.3s for the next morse code (Optional but needs the --dash-delay)")
pars.add_argument("--dash-delay",help="Delays from blinks (Example: this argument is set to 2.3 so it will power up the led, wait for 2.3s, power off the led and wait for 2.3s for the next morse code (Optional but needs the --dot-delay)")
args = pars.parse_args()
text = args.text
dotdelay = 0.5
dashdelay = 2
leds = [args.dot_ledfolder,args.dash_ledfolder]
def on(ledfolder):
	maxbright = os.popen(f"cat {ledfolder}/max_brightness").read().strip()
	os.system(f"echo {maxbright} > {ledfolder}/brightness")
def off(ledfolder):
	os.system(f"echo 0 > {ledfolder}/brightness")
if os.getuid() != 0:
	print("This python script will only work if you are root or you ran this in sudo. Fakeroot will make this script raise errors since it has no permissions to write or read")
else:
	pass
if not leds[0] and not leds[1] and args.led_folder:
	leds[0] = args.led_folder
	leds[1] = args.led_folder
elif not leds[0] and not leds[1] and not args.led_folder or not leds[0] and not args.led_folder or not leds[1] and not args_folder or args.dash_delay and not args.dot_delay or not args.dash_delay and args.dot_delay or not text:
	pars.print_help()
	exit()
elif args.dot_delay and args.dash_delay:
	dotdelay = float(args.dot_delay)
	dashdelay = float(args.dash_delay)
else:
	pass
for i in text:
	try:
		if i.upper() in morse:
			for e in morse[i.upper()]:
				print(f"Word: {i}    Morse: {e}",end="\r")
				if e == ".":
					on(leds[0])
					time.sleep(dotdelay)
					off(leds[0])
					time.sleep(dotdelay)
				elif e == "-":
					on(leds[1])
					time.sleep(dashdelay)
					off(leds[1])
					time.sleep(dashdelay)
		else:
			continue
	except KeyboardInterrupt:
		print("User reqested a exit. Turning off leds and exiting..")
		off(leds[0])
		off(leds[1])
		exit()
