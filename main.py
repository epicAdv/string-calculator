from string_calculator import Add

### NOTE:
# The following testing doesn't use a framework, but I haven't had much experience
# with testing frameworks to date.
###
def main():
	count = 0

	# Question 1 - simple calculator
	test = Add("")
	if test == 0: 
		print "pass"
		count+=1

	test = Add("1,2,5")
	if test == 8: 
		print "pass"
		count+=1

	# Question 2 - strip newline
	test = Add("1\n,2,\n5")
	if test == 8: 
		print "pass"
		count+=1
	#test = Add(",1,500") #TO DO: strip comma, strip \n in 0 position
	#if test == 501: print "pass"

	#Question 3 - custom delimiter
	test = Add("//;\n1;3;4")
	if test == 8:
		print "pass"
		count+=1

	test = Add("//@\n3\n@5@10")
	if test == 18: 
		print "pass"
		count+=1

	test = Add("//$\n100$\n\n100$5")
	if test == 205: 
		print "pass"
		count+=1

	try: test = Add("//!\n1@2@3")
	except: 
		print "pass"
		count+=1

	try: test = Add("//$\n5$8,10")
	except: 
		print "pass"
		count+=1

	#Question 4 - negatives not allowed
	try: test = Add("1,-3,4")
	except ValueError: 
		print "pass"
		count+=1

	#Question 5 - ignore numbers larger than 1000
	test = Add("1000,2,1")
	if test == 1003: 
		print "pass"
		count+=1

	test = Add("1001,2,1")
	if test == 3: 
		print "pass"
		count+=1
		
	test = Add("//!\n10000!7!3")
	if test == 10: 
		print "pass"
		count+=1

	print("Passes: " + str(count) + " of 12")

if __name__ == "__main__":
 	main()