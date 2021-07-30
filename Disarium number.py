from math import *
def digit_count(n):
	return int(log10(n))+1
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