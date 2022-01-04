msg = ["Enter an equation",
	"Do you even know what numbers are? Stay focused!",
	"Yes ... an interesting math operation. You've slept through all classes, haven't you?",
	"Yeah... division by zero. Smart move...",
	"Do you want to store the result? (y / n):",
	"Do you want to continue calculations? (y / n):",
	" ... lazy",
	" ... very lazy",
	" ... very, very lazy",
	"You are",
	"Are you sure? It is only one digit! (y / n)",
	"Don't be silly! It's just one number! Add to the memory? (y / n)",
	"Last chance! Do you really want to embarrass yourself? (y / n)"]
start = True
oper = ['+', '-', '*', '/']
result = 0
memory = 0
msg_index = 0
def is_one_digit(v):
	if v % 1 == 0 and -10 < v < 10:
		return True
	return False
def check(v1, v2, v3):
	mssg = ""
	if is_one_digit(v1) and is_one_digit(v2):
		msg_index = 6
		mssg += msg[msg_index]
	if (v1 == 1 or v2 == 1) and v3 == '*':
		msg_index = 7
		mssg += msg[msg_index]
	if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
		msg_index = 8
		mssg += msg[msg_index]
	if mssg != "":
		msg_index = 9
		mssg = msg[msg_index] + mssg
		print(mssg)
def itof(string):
	try:
		float(string)
		return True
	except:
		return False
def calculate(a, b, c):
	if c == '+':
		return a + b
	elif c == '-':
		return a - b
	elif c == '*':
		return a * b
	elif c == '/':
		return a / b
while start:
	msg_index = 0
	calc = input(f"{msg[msg_index]} \n").split()
	if len(calc) == 3:
		x, y = calc[0], calc[2]
		if calc[1] in oper:
			if x == 'M':
				x = memory
			if y == 'M':
				y = memory
			if itof(x) and itof(y):
				x = float(x)
				y = float(y)
				check(x, y, calc[1])
				if calc[1] == '/' and y == 0:
					msg_index = 3
					print(msg[msg_index])
				else:
					result = calculate(x, y, calc[1])
					print(str(result))
					end = True
					while end:
						msg_index = 4
						answer = input(f"{msg[msg_index]} \n")
						if answer == 'y' or answer == 'n':
							if answer == 'n':
								memory = 0
							else:
								if is_one_digit(result):
									msg_index = 9
									while msg_index < 12 and answer == 'y':
										msg_index += 1
										answer = input(f"{msg[msg_index]} \n")
									if msg_index >= 12:
										memory = result
								else:
									memory = result
							endl = True
							while endl:
								msg_index = 5
								answer = input(f"{msg[msg_index]} \n")
								if answer == 'y':
									endl = False
									end = False
								elif answer == 'n':
									start = False
									endl = False
									end = False
			else:
				msg_index = 1
				print(msg[msg_index])
		else:
			msg_index = 2
			print(msg[msg_index])
