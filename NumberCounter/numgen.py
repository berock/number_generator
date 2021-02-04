# number generator. generates a lists of numbers from user input


start = int(input("What number do you want to start with? "))
end = int(input("What number do you want me to count to? "))
end1 = end + 1
evenOrOdd = input("Do you want even, odd or all? E/O/A ")



def NumGen(start, end):
    inc = int(input("What increments do you want to count by? "))
    print("Starting number is ", start)
    print("Ending number is ", end)
    print("Incriments of ", inc)
    for i in range(start, end1, inc):
        print(i)

def NumGenEven(start, end):
    print("Starting number is ", start)
    print("Ending number is ", end)
    for i in range(start, end1):
        if i % 2 == 0:
            print(i)

def NumGenOdd(start, end):
    print("Starting number is ", start)
    print("Ending number is ", end)
    for i in range(start, end1):
        if i % 2 != 0:
            print(i)

if evenOrOdd == "a" or evenOrOdd == "A" or evenOrOdd == "all" or evenOrOdd == "ALL" or evenOrOdd == "All":
    NumGen(start, end)
elif evenOrOdd == "e" or evenOrOdd == "E" or evenOrOdd == "even" or evenOrOdd == "Even":
    NumGenEven(start, end)
elif evenOrOdd == "o" or evenOrOdd == "O" or evenOrOdd == "odd" or evenOrOdd == "Odd":
    NumGenOdd(start, end)
input("press enter to close program..... ")




