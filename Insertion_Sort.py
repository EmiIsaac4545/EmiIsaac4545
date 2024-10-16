
lyst = [4, 3, 5, 8, -2, 10, 67]

def insertion_Sort (lyst):

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

m



