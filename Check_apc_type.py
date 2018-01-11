def checking_pw_model(pdu_ipv4):
	import pexpect
	import AP8941_auto
	import AP7941_auto

	#pdu_ipv4 = '100.119.12.118'
	prompt_username = 'User Name : '
	default_username = 'apc\r'
	default_username2 = 'apc\r'
	default_cec_username = 'hmussa\r'
	prompt_password = 'Password  : '
	default_password = 'apc\r'
	default_password2 = 'cat\r'
	default_password3 = 'apc\r'
	prompt_system = 'System'
	prompt_7941 = '> '
	prompt_8941 = 'apc>'
	prompt_locked = 'Access to the Control Console will be denied for 2 minutes'

	def debugPrint(text, mode = 1):
		if mode is 1:
			if isinstance(text, str):
				print (text)
			elif isinstance (text, bytes):
				print (str(text, 'utf-8'))
	return

	# Login stuff
	child = pexpect.spawn('telnet ' + pdu_ipv4)

	child.expect(prompt_username)
	debugPrint(child.before)
	child.send(default_username)
	debugPrint("**** We sent: " + default_username )

	child.expect(prompt_password)
	debugPrint(child.before)
	child.send(default_password)
	debugPrint("**** We sent: " + default_password )


	#Set Name
	got_prompt = child.expect([prompt_7941, prompt_8941, prompt_username])
	#child.expect(prompt)
	debugPrint(child.before)


	if(got_prompt is 0): # This is the scenario in which we have tried the first password, succeeded and it turns out to be a 7941
		print ("This is a 7941!")
		#AP7941_auto.main(pdu_ipv4, default_username, default_password)
		AP7941_auto.main(child)
	elif(got_prompt is 1): # This is the scenario in which we have tried the first password, succeeded and it turns out to be a 8941
		print ("This is a 8941!")
		AP8941_auto.main(child)
	elif(got_prompt is 2): 
		print ("This is wrong password! Trying the second password!")
		debugPrint(child.before)
		child.send(default_username)
		debugPrint("**** We sent: " + default_username )

		child.expect(prompt_password)
		debugPrint(child.before)
		child.send(default_password2)
		debugPrint("**** We sent: " + default_password2 )

		got_prompt2 = child.expect([prompt_7941, prompt_8941, prompt_username])
		debugPrint(child.before)

		if(got_prompt2 is 0):
			print ("This is a 7941!")
			AP7941_auto.main(child)
		elif(got_prompt2 is 1):
			print ("This is a 8941!")
			AP8941_auto.main(child)
		elif(got_prompt2 is 2):
			print ("Oh no! We screw up again! Trying the third password")
			debugPrint(child.before)
			child.send(default_username)
			debugPrint("**** We sent: " + default_username )

			child.expect(prompt_password)
			debugPrint(child.before)
			child.send(default_password3)
			debugPrint("**** We sent: " + default_password3 )
			got_prompt3 = child.expect([prompt_7941, prompt_8941, prompt_username, prompt_locked])
			debugPrint(child.before)

			if(got_prompt3 is 0):
				print ("This is a 7941!")
				AP7941_auto.main(child)
			elif(got_prompt3 is 1):
				print ("This is a 8941!")
				AP8941_auto.main(child)
			elif(got_prompt3 is 2):
				print ("Umm. This is awkward. For some reason I am still getting the username prompt.... That shouldn't happen!")
				# If I wanted to enter a fourth password I could do it here but I would have to wait for 2 minutes to make that happen.... I don't really want to do that.
			elif(got_prompt3 is 3):
				print ("Crap! I am locked out.")
			else:
				print ("Oh crap. Something weird is happening - Episode 3!")
		else:
			print ("Oh crap. The return of Something weird is happening")

	else:
		print ("Oh crap. Something weird is happening")

	print ("Done!")

