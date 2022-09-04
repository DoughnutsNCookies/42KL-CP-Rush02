# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: schuah <schuah@student.42kl.edu.my>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/04 14:21:18 by schuah            #+#    #+#              #
#    Updated: 2022/09/04 15:31:20 by schuah           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from helper import remove_suffix

def recurs(number, dictionary, count):
	previous = 0
	for key in dictionary:
		if previous < key and number >= key:
			previous = key
	if (number == 0):
		if (count == 0):
			print(dictionary[previous], end=" ")
		return
	elif number >= 0 and number <= 9:
		print(dictionary[previous], end=" ")
	else:
		print(dictionary[previous], end=" ")
		recurs(number % previous, dictionary, count + 1)
	# for key in dictionary:
	# 	if number == key:
	# 		print(dictionary[key])
	# 		return
	# if key > number:
	# 	recurs(number % previous, dictionary, count + 1)
	# 	recurs(number / previous, dictionary, count + 1)

def	main():
	dictionary = {}
	try:
		f = open("dicts/numbers.dict", "r")
	except IOError:
		print("Dict Error")
		return
	str = f.readline()
	while str != "":
		split_str = str.split(": ")
		dictionary[int(split_str[0])] = remove_suffix(split_str[1], "\n")
		str = f.readline()
	f.close()
	# print(dictionary)
	recurs(int(input("Number: ")), dictionary, 0)

main()