def	main():
	dictionary = {}
	try:
		f = open("numbers.dict", "r")
	except IOError:
		print("Dict Error")
		return
	str = f.readline()
	while str != "":
		split_str = str.split(": ")
		dictionary[int(split_str[0])] = split_str[1].removesuffix("\n")
		str = f.readline()
	f.close()
	print(dictionary)

main()