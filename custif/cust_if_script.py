#!/usr/bin/env python3

message = 'Calculating your projected retirement date... '
print("since we know you purchaed you coin at 20 cents")

try: 
	# wrap connection in a float() to accept decimals as numbers
	dogecoinprice = float(input("What is the current price of your Dogecoin?"))

	# if input value was higher or equal to 25
	if dogecoinprice <=.02:
	    message = message + 'You are pretty much even..keep the faith.'
	elif dogecoinprice <=.04:
	    message = message + 'its not 1 but still good.'
	elif dogecoinprice <= 1:
	    message = message + 'Looks like you can take a year off work!'
	elif dogecoinprice <= 5:
	    message = message + 'CONGRATULATIONS.. You won the lottery.'
	else:
	    message = message + 'Stempie..you fool..You have lost your einter inheriteance.'
	print(message)

except:
	print("You need to enter a number for the price of dogecoin!")
