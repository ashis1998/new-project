#circle.py
#program for calculating the area and perimeter of circle
r=float(input("Enter the Radious of c:"))
ac=3.14*r*r
pc=2*3.14*r*r
print("----------------------------------------")
print("Radious={}".format(r))
print("Area of circle={}".format(ac))
print("Peri of circle={}".format(pc))
print("--------------------------------------")




#by using the normal function
def Area():
	ac=3.14*r*r
	return ac
	

def Peri():
	pc=2*3.14*r*r
	return pc

#main progra
r=float(input("Enter Radious:"))
Area()
print("Area of circle={}".format(ac))
Peri()
print("Prei of circle={}".format(pc))
print("----------------------------------")

#by using  lambda function
area=lambda ac:3.14*r*r
peri=lambda pc:2*3.14*r*r

#mainprogram
r=float(input("Enter Radious of circle:"))
print("Area of circle={}".format(ac))
print("Peri of circle={}".format(pc))
