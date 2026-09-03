import math
x1=float(input("Enter the x-coordinate of point 1:"))
y1=float(input("Enter the y-coordinate of point 1:"))
x2=float(input("Enter the x-coordinate of point 2:"))
y2=float(input("Enter the y-coordinate of point 2:"))

#Straigh-line distance between points
straighLine=math.sqrt((x2-x1)**2+(y2-y1)**2)

#Manhattan Distance(sum of absolute difference in x and y)
xDiff=abs(x2-x1)
yDiff=abs(y2-y1)
manhattan=xDiff+yDiff

#Midpoint Coordinates of Two Points
xCoor=(x1+x2)/2
yCoor=(y1+y2)/2
print(f"The Midpoint's coordinates are: ({xCoor},{yCoor})")