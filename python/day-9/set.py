setEg1 = set()
setEg1.add(1)
setEg1.add(5)
setEg1.add(5)
setEg1.add(6)
print(setEg1)
setEg2 = {1,7}
setEg3 = setEg2 | setEg1
print(setEg3)
setEg4 = setEg2 & setEg1
print(setEg4)
set5 = setEg1 - setEg2
print(set5)
set6 = setEg2 - setEg1
print(set6)