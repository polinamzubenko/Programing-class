print("Hello, this is a kinetic energy calculator!")
print("Enter the velocity of the body in meters per second:")
#request the user's body speed
v= float(input())
#body velocity entered by the user
print("Enter your body weight in kilograms:")
#regequest the user's body weight
m = float(input())
vv = v * v
#repare the numbers to fit into the formula by multiplaing the speed by the speed
mvv = vv * m
# multiply the just found number by the mass
mvv2 = mvv / 2 # at the end we simply divide the resulting number by 2
print( round( mvv/2, 2), "joules")
# display the number that we have after substituting in the formula and round the numbers after the decimal point to two