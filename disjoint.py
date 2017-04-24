#!/usr/bin/python
"""
Program to manage disjointed intervals of integers
"""
Start = []
#Helper fucntion for add/remove
#return index beyond which all entries are greater than 'fromm'
def indexFirstElement(fromm):
	for item in Start:
		if fromm < item[0]:
			return (Start.index(item)-1)
	return (len(Start)-1)

#Helper fucntion for add/remove
#return index before which all entries are less than 'to'
def indexLastElement(to):
	for item in Start:
		if to < item[1]:
			return (Start.index(item))
	return (len(Start))

#helper function for add
#cleanup, merge overlapping entries.
#TBD: Instead of running over all items, probably could just touch impacted subset 
def merge():
	counter = len(Start) - 1
	while counter > 0:
		#merge and clean overlapping set
		if Start[counter-1][1] >= Start[counter][0]:
			#prepare the new set entry
			#[4,10][9,11]=>[4,11]
			#[1,5][1,3]=>[1,5]
			#[2,3][2,4]=>[2,4]
			fromm = Start[counter-1][0]
			to = Start[counter][1] if Start[counter][1] > Start[counter-1][1] else Start[counter-1][1]
			#remove overlapping sets
			del Start[counter]
			del Start[counter-1]
			#insert the new set entry
			Start.insert(counter-1, [fromm,to])
		counter = counter - 1

#add: add new disjoint set to an existing list of disjoint sets
#fromm/to: define range of disjoint set to be added
def add(fromm, to):
	#TBD: Add check for integer
	if to <= fromm:
		print [fromm,to], " is not a valid object!"
		return
	#empty list
	if not Start:
		Start.append([fromm,to])
		print "Add     ", [fromm, to], "=>", Start
		return

	#Remove disjoint set entries between 'fromm' and 'to'
	#delete items between indexLast and indexFirst from the list
	indexFirst = indexFirstElement(fromm)
	indexLast = indexLastElement(to)
	delIndex = indexLast - 1
	while delIndex > indexFirst:
		del Start[delIndex]
		delIndex = delIndex - 1
	#insert valid new entry into the list of disjoint sets
	Start.insert(indexFirst+1, [fromm, to])	
	#merge  any overlaps and cleanup due to new set insertion
	merge()
	print "Add     ", [fromm, to], "=>", Start


#remove: remove a disjoint set from an existing list of disjoint sets
#fromm/to: define range of disjoint set to be removed
def remove(fromm, to):
	#TBD: Add check for integer
	if (to <= fromm):
		print [fromm,to], " is not a valid object!"
		return

	if not Start:
		#nothing to remove
		print "Remove  ", [fromm, to], "=>", Start
		return
	indexFirst = indexFirstElement(fromm)
	indexLast  = indexLastElement(to)

	#indexFirst == indexlast => split a disjoint set
	if indexFirst == indexLast:
		Start.insert(indexFirst, [Start[indexFirst][0], fromm])
		Start[indexFirst+1][0] = to
		#remove entries like [1,1]
		if Start[indexFirst][0] == fromm:
			del Start[indexFirst]
		print "Remove  ", [fromm, to], "=>", Start
		return

	#Remove disjoint set entries between 'fromm' and 'to'
	#delete items between indexLast and indexFirst from the list
	delIndex = indexLast - 1
	while delIndex > indexFirst:
		del Start[delIndex]
		delIndex = delIndex - 1

	#corner case when list index is -1 in python
	if indexFirst == -1:
		if Start:
			if to > Start[0][0]:
				Start[0][0]=to

	else:
		if Start[indexFirst][1] > fromm:
			Start[indexFirst][1] = fromm
			if Start[indexFirst][0] == fromm:
				del Start[indexFirst]
		if indexFirst+1 < len(Start):
			if Start[indexFirst+1][0] < to:
				Start[indexFirst+1][0] = to
			
	#print Start, indexFirst, indexLast
	print "Remove  ", [fromm, to], "=>", Start
	return

#Test
print "Start =>", Start
add(1,5)
remove(2,3)
add(6,8)
remove(4,7)
add(2,7)

"""
add(1,5)
add(-10,-5)
add(-5,8)
add(-5,4)
remove(4,5)
add(3,5)
remove(8,9)
remove(7,9)
add(-20,3)
remove(1,2)
remove(3,5)
add(8,9)
remove(0,6)
"""
