smallest = None
largest = None
sum = 0
total = 0
print("hello, please enter a number")
while True:
    theNumber = input("Number:")
    if theNumber == "done":
        break
    try:   
        num = float(theNumber)
    except:
        print("invalid input")
        continue
    for numero in [num]:
        sum = sum + numero
        total = total + 1

    for numero in [num]:
        if smallest is None:
            smallest = numero
        elif smallest > num:
            smallest =  num
    for numero in [num]:
        if largest is None:
            largest = numero
        elif largest < num:
            largest = num
   
print("Minimun:", smallest)
print("Maximun:", largest)
print("sum: ", sum)
print("Total: ", total)
print("Average: ", sum/total)