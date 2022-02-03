#EXCEPTION1.PY
try:
	a=input("Enter First Value:")
	b=input("Enter Second Value:")
	x1=int(a)
	x2=int(b)
	x3=x1+x2

except ValueError:
	print("Do not enter invalid literals")

else:
	print("val of x1={}".format(x1))
	print("val of x2={}".format(x2))
	print("val of x3={}".format(x3))

finally:
	print("MY PROGRAM IS COMPLITED")
