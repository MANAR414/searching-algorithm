def number_of_occurrences(numbers: list[int], target: int) -> int:
     for i in range(numbers[0],numbers[-1]):
           c=numbers.count(target)
           print(f"first index:{numbers.index(target)}")
           i=numbers.index(target)
           ind=[]
           for t in range(c-1):
                i+=1
                ind.append(i)
           print(f"last index:{ind[-1]}")
           print(f"occurances:{c}")

numbers=list(eval(input("enter your list:")))
target=int(input("enter your target:"))
number_of_occurrences(numbers,target)


