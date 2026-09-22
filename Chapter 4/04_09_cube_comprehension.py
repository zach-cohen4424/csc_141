#Just adding an append to the previous program. 

cubes = []
for i in range(1, 50,2):
    cubes.append(i)

print (cubes)
new_cubes = []

for cube in cubes:
    new_cubes.append( cube**3 )
    #print(cube)
print (new_cubes)