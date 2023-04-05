# in this chapter we are going to study about loops
#  two types of loops
# 1. while loops 2. for loops

# 1. loops means repeating of cycle 
# x=0
# while (x<5):
#     print(x)
#     x=x+1
 

#  2. for loops
for x in range (5,10):
    print(x)


   # using this an programme

#    array
days=("monday", "tuesday", "wednesday", "thursday", "friday")
#  for d in days:
#     if (d=="wednesday"):break #loop stops
#     print(d)

for d in days:
    if (d=="tuesday"):continue
    print(d)






