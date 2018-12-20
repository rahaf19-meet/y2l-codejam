n=10
c=1
pn=0.0
summ=0.0
def commun_factor(a,b):
	for i in range(1,min(a,b)-1):
		if a%i==b%i==0:
			return True
		else:
			return False
def dividable(a,b):
	if a%b==0:
		return True
	else:
		return False

while n>c:
	if commun_factor(1,10)==True and dividable(1,10)==True:
		print c
		pn+=1
	c+=1

print pn