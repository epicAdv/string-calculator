def Add(numbers):

	# default return value and delimiter
	summed = 0
	# convert the input to a raw string
	numbers = numbers.encode('string-escape')

	# if the string is empty, return 0
	if (numbers is None or len(numbers) < 1):
		return summed

	##### Delimiters #####
	
	# Default delimiter is ',' and custom delimiters are wrapped in // and \n
	delim = "," 
	prefix = "//"
	suffix = r"\n" 

	# there is a custom delimiter when the string starts with //
	if numbers.startswith(prefix):

		# find the substring between the prefix and suffix
		delim = numbers[2 : numbers.find(suffix)]
		# remove the control code from the original input
		control_code = prefix + delim + suffix 
		numbers = numbers.replace(control_code, '')

	# remove newlines
	numbers = numbers.replace(r'\n','')
	# split the input string at the delimiter
	number_list = numbers.split(delim)

	# Loop through remaining input values, cast to ints, and add
	for i in range(len(number_list)):
		n = int(number_list[i])

		# check if the value is negative, and throw an exception
		if n < 0:
			raise ValueError("Negatives not allowed: " + str(n))

		# only add values that are less than 1000
		if n <= 1000:
			summed = summed + n

	return summed
