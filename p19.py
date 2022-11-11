xlist=["blue","yellow","green","purple"]
ylist=["white","yellow","pink"]
zlist=[]
for i in xlist:
	if i not in ylist:
		zlist.append(i)
print("The colors not in color list 2 is ",zlist)
