def insertion_sort (lyst):

    i = 1

    while i < len(lyst):

        target = lyst[i]
        j = i - 1

        while j >= 0:
            if target < lyst[j]:

                lyst[ j + 1] = lyst [j]
                j -=1

            else : 
                break

        lyst[j + 1] = target
        i += 1

    return lyst

def get_valid_input():

    while True:

        try:
            # Receive input from the user, split by spaces, and convert to a list of integers
            user_input = input ("Enter numbers separated by spaces ( All numbers must be non-negative): ")
            lyst = list(map(int, user_input.split()))

            # Check if any number is negative
            if any (num < 0 for num in lyst):
                print ("All numbers must be non-negative. Please try again.")

            else:
                return lyst

        except ValueError:
            print("Invalid input.Plese enter valid intgers")

# get valid input from the user
lyst = get_valid_input()

# Call the insertion_sort function
result = insertion_sort(lyst)

# Print result
print ("The sorting list is:", result)




