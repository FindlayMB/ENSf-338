# Exercise 5

# Question 1
def processdata(li):
    for i in range(len(li)):
        if li[i] > 5:
            for j in range(len(li)):
                li[i] *= 2

    # Complexity analysis

    # Best case - All elements of li are less than 5 or equal to 5
    # If all elements of li are less than 5 or equal to 5, then
    # the inner for loop doesn't run at all which will give the function
    # a linear complexity, O(n)

    # Worst case - All elements of li are greater than 5
    # If all elements of li are greater than 5, the inner for loop
    # will run with each execution of the outer for loop giving
    # a quadratic complexity, O(n^2)

    # Average case
    # If most of the elements in li are less than 5 then the
    # inner for loop will run only a few times this results
    # in a linear complexity, O(n)

    # However, if most of the elements in li are greater than 5 then
    # the inner for loop will run each time the outer for loop is executed
    # this will give the function a quadratic complexity, O(n^2)

    # As such the average case complexity is somewhere between
    # the best and worst cases.

# Question 2


def modifiedProccessData(li):
    for i in range(len(li)):
        li[i] = li[i] if li[i] <= 5 else li[i] * 2

    # Since the average, best, and worst case
    # complexity are not the same the function
    # was modified such that they are the same.
    # The modified code now has a linear, O(n)
    # best, average, and worst case complexity.
