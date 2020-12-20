circleX, circleY, radius = input('enter x,y,r: ').split(',')
x, y = input('enter point (x,y): ').split(',')

isPointInCircle = (int(x) - int(circleX)) ** 2 + (int(y) - int(circleY)) ** 2 < int(radius) ** 2

if isPointInCircle == True:
    print('yes')
else:
    print('no')
