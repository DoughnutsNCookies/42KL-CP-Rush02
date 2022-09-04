# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    helper.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: schuah <schuah@student.42kl.edu.my>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/04 14:21:15 by schuah            #+#    #+#              #
#    Updated: 2022/09/04 14:21:16 by schuah           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def remove_suffix(input_string, suffix):
	if suffix and input_string.endswith(suffix):
		return input_string[:-len(suffix)]
	return input_string