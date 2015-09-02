import re
pattern = '^\+91-[0-9]{10}$'
a = str(input('Enter the country code'))
b = str(input('Enter 10 digit no.'))
c='+'+a+'-'+b
# print c
z = re.compile(pattern)
if z.match(c)==None:
	print "Not a Indian Number"
else:
	print 'Indian Number'
