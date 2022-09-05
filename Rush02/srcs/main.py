# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: schuah <schuah@student.42kl.edu.my>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/04 14:21:18 by schuah            #+#    #+#              #
#    Updated: 2022/09/05 16:32:20 by schuah           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from helper import remove_suffix

def recurs(number, dictionary, count):
	previous = 0
	for key in dictionary:
		if previous < key and number >= key:
			previous = key
	if previous == 0:
		if count == 0:
			print(dictionary[previous], end=" ")
		return
	elif previous > 0 and previous <= 9:
		print(dictionary[previous], end=" ")
	else:
		n1, n2 = divmod(number, previous)
		if n1 > 1 or previous >= 100:
			recurs(n1, dictionary, count + 1)
		print(dictionary[previous], end=" ")
		recurs(n2, dictionary, count + 1)

def	main():
	dictionary = {}
	try:
		f = open(input("Dictionary: "), "r")
	except IOError:
		print("Dict Error")
		return
	str = f.readline()
	while str != "":
		split_str = str.split(": ")
		dictionary[int(split_str[0])] = remove_suffix(split_str[1], "\n")
		str = f.readline()
	f.close()
	inputNumber = input("Number: ")
	if (inputNumber == ""):
		print("Input Error")
		return
	recurs(int(inputNumber), dictionary, 0)
	print()

main()