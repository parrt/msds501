def intlog(n):
	n = int(n)
	log = 0
	while n>1:
		n /= 2
		log += 1
	return log

print "log(1)", intlog(1)
print "log(2)", intlog(2)
print "log(4)", intlog(4)
print "log(8)", intlog(8)
print "log(8.5)", intlog(8.5)
print "log(9)", intlog(9)
print "log(1024)", intlog(1024)
print "log(1025)", intlog(1025)
