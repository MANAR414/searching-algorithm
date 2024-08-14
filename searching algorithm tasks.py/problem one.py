#Given a list of integers, write a function that returns the second largest element in the list. If the list has less
#than 2 elements, return None.
def second_largest(numbers: list[int]) -> int:
    if len(numbers)<=2:
          return None
    else:
      print(numbers[-2])

numbers=eval(input("enter no.:"))
sorted_list=sorted(numbers)
second_largest(sorted_list)

