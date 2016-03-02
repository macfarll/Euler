Pyramid=[]
class PyramidRow:
    def __init__(self,row,values):
       self.row=row
       self.values=values
       Pyramid.append(self)
row0=PyramidRow(0,[75])
row1=PyramidRow(1,[95,64])
row2=PyramidRow(2,[17,47,82])
row3=PyramidRow(3,[18,35,87,10])
row4=PyramidRow(4,[20,4,82,47,65])
row5=PyramidRow(5,[19,1,23,75,3,34])
row6=PyramidRow(6,[88,2,77,73,7,63,67])
row7=PyramidRow(7,[99,65,4,28,6,16,70,92])
row8=PyramidRow(8,[41,41,26,56,83,40,80,70,33])
row9=PyramidRow(9,[41,48,72,33,47,32,37,16,94,29])
row10=PyramidRow(10,[53,71,44,65,25,43,91,52,97,51,14])
row11=PyramidRow(11,[70,11,33,28,77,73,17,78,39,68,17,57])
row12=PyramidRow(12,[91,71,52,38,17,14,91,43,58,50,27,29,48])
row13=PyramidRow(13,[63,66,4,68,89,53,67,30,73,16,69,87,40,31])
row14=PyramidRow(14,[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23])

#iterate through pyramid from bottom to top
for unreversed_iter_row in range(1,len(Pyramid)):
    iter_row=14-unreversed_iter_row
#iterate through values in each row, in reverse order
    for iter_val in range(len(Pyramid[iter_row].values)):
        parent_1 = Pyramid[iter_row+1].values[iter_val]
        parent_2 = Pyramid[iter_row+1].values[iter_val+1]
#reassign current point as the sum of the best path beneath it and itself
        if parent_1 >= parent_2:
            Pyramid[iter_row].values[iter_val] += parent_1
        else:
            Pyramid[iter_row].values[iter_val] += parent_2
print row0.values
