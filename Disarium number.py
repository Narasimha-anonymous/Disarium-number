def digit_count(n):
	c=0
	while n:
		c+=1
		n//=10
	return c
def disarium(n):
	a=n
	s=0
	for i in range(digit_count(n),0,-1):
		rem=n%10
		s+=rem**i
		n//=10
	return s==a

n=int(input())
print("Disarium Number") if disarium(n) else print("Not a disarium number")