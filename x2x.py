# _*_ coding: utf-8 _*_

import math

def quadratic(a,b,c):
	if a == 0:
		print ('error a!=0!!!')
	elif (b*b - 4*a*c) < 0 :
		print ('no answer')
	elif (b*b - 4*a*c) == 0:
		x = -(b/2*a)
		print ('x = %',x)
	else:
		x1 = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
		x2 = (-b - math.sqrt(b*b - 4*a*c))/(2*a)
		return x1,x2

print(quadratic(0, 3, 1)) # => (-0.5, -1.0)
print(quadratic(1, 3, -4)) # => (1.0, -4.0)