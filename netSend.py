import os

def Menu():
	os.system("clear")
	print "---NetSend---"
	print "[1] Send message to a single computer"
	print "[2] Send message to multiple computers"
	print "[3] Send spam to a single computer"
	print "[4] Send spam to multiple computers"
	print "[5] view computers on network"
	
	try:
		option = int(raw_input("Option: "))

		if option == 1:
			get_mach("single", "one", "single_msg_one_mach")

		elif option == 2:
			get_mach("single", "multi", "single_msg_multi_mach")

		elif option == 3:
			get_mach("spam", "one", "spam_msg_one_mach")

		elif option == 4:
			get_mach("spam", "multi", "spam_msg_multi_mach")

		elif option == 5:
			view_comps_on_network()

		else:
			print "error testing..."
			pause = raw_input()
			exit()
			errors("menu_option_err")

	except ValueError:
		print "error testing..."
		pause = raw_input()
		exit()
		errors("menu_option_err")

def get_mach(msg_type, mach_type, net_send_type):
	if mach_type == "one":
		computer_name = raw_input("computer name or ip: ")

		if len(computer_name) == 0:
			#call error
			print "error testing..."
			pause = raw_input()
			exit()

		else:
			get_msg(msg_type, mach_type, net_send_type, computer_name)

	elif mach_type == "multi":
		computer_names = []

		try:
			print "enter the name or ip of the computes with a space between each one"
			print "for example: computer1 computer2 computer3\n"
			computer_names_str = raw_input("computer names: ")

			if len(computer_names_str) < 1:
				#calls errors
				print "error testing..."
				pause = raw_input()
				exit()

			else:
				computer_names = computer_names_str.split()
				get_msg(msg_type, mach_type, net_send_type, computer_names)

		except ValueError:
			#call errors
			print "error testing..."
			pause = raw_input()
			exit()

def get_msg(msg_type, mach_type, net_send_type, computerNames):
	message = raw_input("message: ")

	if len(message) == 0:
		#calls errors
		print "error testing..."
		pause = raw_input()
		exit()

	else:
		if msg_type == "single":
			net_send(net_send_type, computerNames, message, "NA")

		else:
			try:
				spam_count = int(raw_input("number of times to spam: "))

				if spam_count == 0:
					#calls errors
					print "error testing..."
					pause = raw_input()
					exit()

				else:
					net_send(net_send_type, computerNames, message, spam_count)

			except ValueError:
				#calls errors
				print "error testing..."
				pause = raw_input()
				exit()


def net_send(net_send_type, computerNames, message, spamCount):
	if net_send_type == "single_msg_one_mach":
		#send message to single machine
		#os.system("net send %s %s" % (computerNames, message))
		#os.system("PAUSE")
		#Menu()
		print "net send %s %s" % (computerNames, message)
		print "message sent to %s" % computerNames
		pause = raw_input("Press any key to continue...")
		Menu()

	elif net_send_type == "single_msg_multi_mach":
		numb_of_computers = len(computerNames)
		i = 0

		while i < numb_of_computers:
			#os.system("net send %s %s" % (computerNames[i], message))
			print "net send %s %s" % (computerNames[i], message)
			print "message sent to %s" % computerNames[i]
			i += 1

		pause = raw_input("Press any key to continue...")
		Menu()

	elif net_send_type == "spam_msg_one_mach":
		print net_send_type
		print computerNames
		print message 
		print spamCount

	elif net_send_type == "spam_msg_multi_mach":
		print net_send_type
		print computerNames
		print message 
		print spamCount

	else:
		pass

def view_comps_on_network():
	#os.system("net view")
	#os.system("PAUSE")
	print "will use the 'net view' command to list computers on network"
	pause = raw_input()
	Menu()

def errors(error_type):
	print "test1"
	print "error testing..."

Menu()