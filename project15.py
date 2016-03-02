#First implementation involved iteration outward from a 1x1 grid,
# this took way too long to run

#initialize a 2d array
arr=[[1 for x in range(21)] for x in range(21)]
for row in range(1,21):
    for col in range(1,21):
#for any given lattice, the number of possible paths can be thought
# of as the sum of: (that array -1 row) and (that array -1 col)
# for singular edges, such as the top and bottom, there are only
# one path, hince the initilization at 1
        arr[row][col]=arr[row-1][col]+arr[row][col-1]
print arr[-1][-1]
