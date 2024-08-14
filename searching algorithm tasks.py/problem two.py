#Find the Missing Number
#You are given a list of n-1 integers and these integers are in the range of 1 to n.There are no duplicates in the
#list. One of the integers is missing in the list. Write a function that finds the missing number.
def missing_number(numbers: list[int]) -> int:
    for i in range(numbers[0]+1,numbers[-1]):
       if i not in numbers:
           print(i)
numb=eval(input("enter list(no duplication):"))
set_numb=set(numb)
print(set_numb)
if numb!=set_numb:
     print("please enter list without any dublication numb.:(")
     exit()
missing_number(numb)




