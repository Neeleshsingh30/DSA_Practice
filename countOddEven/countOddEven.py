#Question: Write a python function that takes a list o integers as input and returns the count of odd and even numbers in the list?
#answer:

# define a function to count odd and even numbers in a list
def countOddEven(arr):
    odd_count=0
    even_count=0

    # iterate through the list and count odd and even numbers
    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return odd_count,even_count

# test the function with a sample list
if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,21,15,17]
    odd_count, even_count = countOddEven(arr)
    print("Number of odd numbers: ", odd_count)
    print("Number of even numbers: ", even_count)
