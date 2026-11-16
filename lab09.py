# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first):
    """
    use a nested loop to basically compare the number from the first loop to the number in the
    second loop. if it does add up to the target, then it returns both numbers
    """
    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #   to `target`. Assume there is exactly one answer.
    for i in range(len(nums)):
        for j in range(i):
            if ((nums[i]+nums[j])==target):
                return [i, j]
            else:
                pass


def max_profit(prices):
    # Outline:
    """
    look for smallest number in the list and then look for the largest number after that smallest number 
    and return the diffference between those two numbers
    
    """
    max=0
    min_price = 0
    max_price = 0
    for price in prices:
        if price == min(prices):
            min_price = price
    for i in range(prices.index(min_price) + 1, len(prices)-1):
        if prices[i]>max: 
            max_price = prices[i]
    difference = max_price - min_price
    if max_price > min_price:
        return difference
    else:
        return 0
    
    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0.
    


def max_subarray(nums):
    # Outline:
    #  grab the current sum within the range of the list and if it is greater
    # than that sum then set it to max sum
    # if not then set the current sum to 0 and continue until the end of the list
    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.
    current_sum = 0
    max_sum = nums[0]
    for num in nums:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return max_sum


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    print(max_profit([7, 1, 5, 3, 6, 4]))   # 5
    print(max_profit([7, 6, 4, 3, 1]))    # 0
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))   # returns 6   (4 + -1 + 2 + 1)
    print(max_subarray([5, 4, -1, 7, 8]))                  # returns 23  (the whole list)
    pass


if __name__ == "__main__":
    main()
