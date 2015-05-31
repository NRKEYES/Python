## print from 1 to 100
## but multiples of three print fizz
## multiples of 5 print buzz
## multiples of both print fizzbuzz


for i in range(1,100):
	if i%3 == 0:
		if i%5 == 0:
			print "fizzbuzz"
			continue;
		print "fizz"
		continue;
	if i%5 == 0:
		print "buzz"
		continue;
	print i;

