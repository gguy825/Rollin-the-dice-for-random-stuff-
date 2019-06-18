### adventure game
### random choice

### user rolls dice 
### if dice lands on 1-6, random stuff happens
### if dice lands on 7, random deaths happen

### if he dies he dies and option to play again
### if he lives he dies and option to play again

import random
import time

something_happened = [
		"You find the sword of azeroth. ",
		"You encounter a man who gives you a mysterious amulet that gives you strength. ",
		"You find a gun. ",
		"You find a sack of beef jerky and eat it. Then a man runs at you yelling saying \n'THAT WAS MINE!!' and chases after you. ",
		"You want be the very best, like no one ever was, to catch them is your real test, \nto train them is your cause, you travel across the land, searching far and wide, \nteaching Pokémon to understand, the power that's insideeeeeeeeeee. ",
		"You encounter two men dressed in black suits pointing guns at you. \nYou're confused, saying 'what?' \nOne of the men scream out 'SAY WHAT AGAIN!' \nYou say 'what' again. The two start screaming and shooting. The bullets miss you and you flee. ",
		"You find a grenade. ",
		"You encounter two children throwing red and white balls back and forth at eachother. ",
		"You encounter a gorilla giving you signs. You cannot understand sign language, so instead you give it a banana. ",
		"You encounter Thanos. He gives you the infinity gauntlet. You are took weak to weild it. Thanos looks at you in dissapoint and says, \n'Fun isn't something one considers when balancing the universe. But this... does put a smile on my face.' ",
		"You encounter a stampede of angry villagers carrying a suspected witch to a lake. ",
		"You encounter the boys looking for beans .",
		"You encounter CJ and Big Smoke discussing their plans to crash a meeting between the Vagos and San Fierro Rifas. ",
		"You come upon a thing in the road saying something about a thing, idk. ",
		"You come to a random fork laying in the road, a fork in the road. You step over it and keep straight. ",
		"You find a random piano in the road called 'The Power'. You tap on the keyboard and are teleported to the moon. \nYou're on the moon now. Deal with it. ",
		"You encounter a man in iron armor and gold letters above his head saying 'Buying GF'. ",
		"You encounter a cat with bread on its head. ",
		"You encounter a dog barking at a tree. You look up and see a cat or something i dont know. "
]

deaths = {
		"7": [
		"As you're traveling, you stubmle and break your arms, \nand you cant feed yourself withour your arms, so....you starve to death. ",
		"As you're traveling, you stubmle and break your legs, \nand you cant walk without your legs, so....you just lay there and die. ",
		"You forgot to sleep, so you pass out, and die in your sleep, because that can happen. ",
		"You die of a, uhh, brain aneurysm, yep. ",
		"You get impaled by an angry amish man. Medieval driveby. WASTED. ",
		"You took an arrow to the knee and died. ",
		"You died of cholera while shooting from both ends. ",
		"You die of typhoids.  ",
		"You burn to death in a fire. ",
		"You have been burned at the stake for being considered a witch. ",
		"You die of something. I dont know. ",
		"A snake bit you and theres no anti venom cause like, they havent invented it yet. Dead. ",
		"You just die randomly. Oops, sowie. ",
		"You die from a fever so your body didnt do a good job of protecting you. ",
		"You drowned in that river over there.... ",
		"You drowned in that lake over there.... ",
		"You drowned in a random body of water. ",
		"You died of the measles. ",
		"You died of dysentery. ",
		"You got killed by a witch, cause she put a spell on you, and you died. ",
		"You died from eating a poisonus apple. Shout out to snow white. ",
		"You die from global warming. ",
		"You froze to death. ",
		"I'm running out of ideas so you just die. \nDont get mad at me, get mad at the programming language for choosing this death. ",
		"A fox kills you. What did it say? ",
		"You die from getting hit in the head due to celebratory catapult firing. Medieval rednecks. ",
		"You died cause you owed too much money to the mob. ",
		"You die from lightning strike. Those metal helmets have their downsides. ",
		"You die from a black hole. ",
		"Chuck norris kicks you out of nowhere killing you. ",
		"YOU DIED ",
		"Uhh, yea, you die. ",
		"Hey, you died again! ",
		"CONGRATS, YOU'RE THE 1000TH PERSON TO DIE!! CLICK HERE NOW! ",
		"zzzz.....zzzzz, OH, WHA, oh, yea yea, sorry i was asleep, uhh, yea, you died. ",
		"You're not very good at this game are you? ",
		"Thanos killed you. ",
		"You were ran over by a horse. ",
		"You were ran over by a carriage. ",
		"You died fighting a dragon. ",
		"You believed you could fly. You cant. ",
		"You chose the wrong potion. ",
		"You pressed the big red button. ",
		"A pokemon killed you. "
		"You were blown away by Team-Rocket, then died when you fell out of the sky. ",
		"You fell right out of the sky. ",
		"You fell into a spiked traped set by indigenous, people. ",
		"You got ran over by a car. "
		"You, uhh, lets see here, *flips through notebook* says here you died. ",
		"Stop dying, games not that hard I dont think. ",
		"What? Oh you died. ",
		"You're still playing? Im going home, its 5 o'clock. ",
		"Out to lunch. Come back at 1:00. ",
		"You were killed by darth vader. ",
		"Died you did, not a good player, you are. -Yoda ",
		"RIP fam ",
		"You were hit in the head with a stray arrow, and died. ",
		"You were killed by crippling credit card debt. ",
		"You got killed by an ALASKAN, BULL, WORM!!! ",
		"How did you die? You dont know? Well it says here you died. ",
		"You died, and that really rustled my jimmies",
		"You were killed by Harambe. ",
		"You got shot by John Wick. ",
		"You drink yourself to death off fine wine and beer. "
		]
	}

def intro():
	"""introducing the game thing"""
	print("""\
		  ~         ~~          __
		       _T      .,,.    ~--~ ^^
		 ^^   // \                    ~
		      ][O]    ^^      ,-~ ~
		   /''-I_I         _II____
		__/_  /   \ ______/ ''   /'\_,__
		  | II--'''' \,--:--..,_/,.-{ },
		; '/__\,.--';|   |[] .-.| O{ _ }
		:' |  | []  -|   ''--:.;[,.'\,/
		'  |[]|,.--'' '',   ''-,.    |
		  ..    ..-''    ;       ''. '  """)
	print("Welcome to this random adventure game! ")
	input("\nPress 'enter' to start your random adventure. ")

	print("\nHello weary traveler! ")
	time.sleep(1)
	print("\nLets take a step into a wonderful adventure! ")
	time.sleep(1)
	print("\nBut be careful! ")
	time.sleep(1)
	print("\nThe world is full of dangerous....")
	time.sleep(1)
	print("\nstuff ")
	time.sleep(1)
	print("....")
	time.sleep(1)
	print("Here, take this 7 sided dice and try not to die. ")
	time.sleep(1)
	print("\nThe dice will determine your fate, so yea.")
	time.sleep(0.8)
	print("\nGood luck traveler!")
	time.sleep(1)
	print("\nYa YEET!")

	adventure_or_leave = input("\nReady to adventure?! (yes or no) ")

	if adventure_or_leave == 'yes':
		print("\nExcellent! Come you ye!") # add ascii trail or something
		time.sleep(1)
	else:
		print("\nWelp, no adventure for you! ")
		time.sleep(1)
		print("Back to the tavern with ya! ")
		time.sleep(1)
		input("\nGo to the tavern to drink and pass out. (Press 'Enter') ")
		exit(0)

def start_of_adventure():
	"""the beggining of the end"""
	print("\nWonderful! Now that you're ready, ") 
	print("let me explain to you what your adventure entails. ")
	time.sleep(1)
	print("\nSo, bascally you get this dice, ") # add ascii dice
	print("it has 7 faces, ")
	print("you roll it, ")
	print("if it lands on 1-6, ")
	print("mans good, ")
	print("but if it lands on 7, ")
	print("mans dead. ")

	i_got_it = input("\nGot it? (yes or no) ")

	if i_got_it == 'yes':
		print("\nGood, heres your dice, gl fam! ")
		time.sleep(1)
	else:
		print("\nWelp, no adventure for you! ")
		time.sleep(1)
		print("Back to the tavern with ya! ")
		time.sleep(1)
		input("\nGo to the tavern to drink and pass out. (Press 'Enter') ")
		exit(0)

def main(has_respawned = False):
	"""dice rolls somones gonna die"""
	global deaths
	is_alive = True
	if not has_respawned:
		intro()
		start_of_adventure()
	while is_alive:
		rolled_number = random.randint(1,7)
		print(f"\nYou rolled a {rolled_number}!\n")
		if rolled_number < 7:
			print(random.choice(something_happened))
		if rolled_number == 7:
			print(random.choice(deaths['7']))
			print("( ✖ ╭╮ ✖ )")
			is_alive = False
			break

		roll_or_leave = input("\nRoll again? ")

		if roll_or_leave == 'yes':
			print("\nRolling! ")
		else:
			print("\nBack to the tavern with ya! ")
			input("\nGo to the tavern to drink and pass out. (Press 'Enter') ")
			exit(0)

	if not is_alive:
		input("\nPress 'enter' to respawn. ")
		main(has_respawned = True)

main()
