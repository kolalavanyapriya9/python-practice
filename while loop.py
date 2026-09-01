even_count=0
odd_count=0
number=int(input("Enter a number or type 0to stop: "))
while number !=0:
    if number %2==1:
        odd_count+=1
    else:
        even_count+=1
    number=int(input("Enter a number or type 0 to stop: "))

print("Odd numbers count: ", odd_count)
print("even numbers count: ", even_count)