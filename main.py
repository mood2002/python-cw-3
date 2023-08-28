# write your code here
favorite_animals=["dog","cat","monkey","rabbit"]
print(favorite_animals)
print( favorite_animals[1] )
favorite_animals.remove("monkey")
print(favorite_animals)
favorite_animals.append("parrot")
print(favorite_animals)
for favorite_animals in favorite_animals:
    print(f"I love {favorite_animals}")

numbers=[5,4,3,2,1]
numbers_sum=0
for numbers in numbers:
    numbers_sum += numbers
    print(numbers_sum)