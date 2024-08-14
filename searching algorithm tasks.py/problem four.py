# Rotated Sorted Array
# Given a sorted array of n integers that has been rotated an unknown number of times, write a function that
# returns how many times the array has been rotated. You may assume that the array was originally sorted in
# increasing order. Bonus: Solve the problem in O(log n) time.
def rotated_sorted_array(numbers: list[int],target) -> int:
          start = 0
          end = len(numbers) - 1
          while start <= end:
                mid = (start + end) // 2
                if numbers[mid] == target:
                     return mid
                elif target < numbers[mid]:
                     end = mid - 1
                else:
                     start = mid + 1
          print(lst.index(target))
lst=list(eval(input("enter:")))
rotated_sorted_array(lst,min(lst)) 
