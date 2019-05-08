'''
A - 100-90%
B - 89-80% 
C - 79-70% 
D - 69-60% 
F - 59-0% 
'''

def cal():
	pointsPossible = 100
	percent = ( score / pointsPossible ) * 100
	grade = ""

	if 100 >= percent >= 90:
		grade = "A"
	elif 89 >= percent >= 80:
		grade = "B"
	elif 79 >= percent >= 70:
		grade = "C"
	elif 69 >= percent >= 60:
		grade = "D"
	else:
		grade = "F"

	print ("{} score {} % and grade is {}".format(name, round(percent, 2), grade))
	
while True:
	try:
		name = input("What is your name? : ")	
		score = int(input("Score? : "))
		cal()
		break

	except Exception:
		print ("Please put valid score!")
