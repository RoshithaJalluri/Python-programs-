#EMPTY SET
s={}
print(s)

#SET WITH ELEMENTS 
a={1,3,5,7}
print(a)

#SET WITH DUPLICATES
b={6,7,8,9,6,7}
print(b)

#ADDING ELEMENT IN SET(HERE BY USIND ADD WE CAN INSERT ONLY ONE ELEMENT )
b={1,2,3,4}
b.add(6)
print(b)

#ADDING MORE THAN ONE ELEMENT IN SET(UPDATE)
r={9,7,5,3}
s={2,4,6,8}
r.update(s)
print(r)

#REMOVE ELEMENT IN SET
r={5,6,8,9}
r.remove(6)
print(r)
#r.remove("r")(the difference between remove and discard is this i.e remove cant remove a element )


#DISCARD ELEMENT IN SET 
r={5,6,8,9}
r.discard(6)
print(r)
r.discard("r")
print (r)

