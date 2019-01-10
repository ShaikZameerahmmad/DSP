import random
m=input('rows=')
n=input('col=')
r=input('rows=')
s=input('col=')
a=[[random.random()for col in range(n)]for row in range(m)]
for i in range(m):
	for j in range(n):
		a[i][j]=input()
b=[[random.random()for col in range(s)]for row in range(r)]
for i in range(r):
	for j in range(s):
		b[i][j]=input()
c=[[random.random()for col in range(s)]for row in range(m)]
if(n==r):
	for i in range(m):
		for j in range(s):
			c[i][j]=0
			for k in range(n):
				c[i][j]+=a[i][k]*b[k][j]
			print c[i][j],
		print
else:
	print 'multiplication cannot be done'
		
