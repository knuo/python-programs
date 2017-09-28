#snake and ladder
#! /usr/bin/python3
import random
count=0
r=0
while count<=100:
	roll=input("press r to roll the dice:")
	if roll=="a":
		r=random.randint(1,6)
		count=count+r
	 	if count>=100:
	 		print("you won")
	 else:
		if count==8:
	 	count=37
	 	print("you have climbed the ladder to",count)
	elif count==13:
		count=34
		print("you have climbed the ladder to",count)
	elif count==40:
		count=68
		print("you have climbed the ladder to",count)
	elif count==52:
		count=81
		print("you have climbed the ladder to",count)
	elif count==76:
		count=97
		print("you have climbed the ladder to",count)
	elif count==38:
		count=count-r
		if r<6:
			 r=r+1
			 count=count+r
			 print(count)
			elif r==6:
				r=r-1
				count=count+r
				print(count)
	
	
