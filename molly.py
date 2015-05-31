
#  100 to 1
# for i in range(0,101:
# 	x = 100-i
# 	if x == 0:
# 		break;
# 	print x



## Fizz buzz

## Count from 1 to 100
## when the number is divisable by 3 print fizz
## when the number is div by 5 print buzz
## when div by both print fizzbuzz

for i in range(1,101):
	if i%3==0 and i%5==0:
		print "fizzbuzz"
		continue;
	if i%5==0:
		print "buzz"
		continue;
	if i%3==0:
		print "fizz"
		continue;
	print i


