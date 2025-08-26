import math
# exercise - 3: 
# Q1: Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.




print(3) #Int
print(4.5) #Float
print(2+2j) #Complex
print('Example') #String
print(False) #Boolean
print([1,"Test",3.14, False, (2,'4t')]) #List
print({"id":"1","name":"Jon Snow"}) #Dictionary
print({2,3,4,5}) #Set
print((2,'xyz',1.5)) #Tuple

# Q2: Find an Euclidian distance between (2, 3) and (10, 8)
pair1 = (2-3)**2
pair2 = (10-8)**2
dist = math.sqrt(pair1+pair2)
print(dist)
