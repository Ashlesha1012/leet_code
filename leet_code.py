####################################################################

class Solution:
    
    def two_sum(self, nums, target):
        num_indices = {}
        for i, num in enumerate(nums):
            complement = target-num
            if complement in num_indices:
                return [num_indices[complement], i]
            num_indices[num] = i

        return []
    
s = Solution()
result = s.two_sum([2, 7, 8, 4], 9)
# print(result)            

######################################################################

def group_anagrams(strs):
    anagrams = {}
    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]

    return list(anagrams.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# print(group_anagrams(strs))

######################################################################

from collections import defaultdict
def group_anagrams(strs):
    anagrams = defaultdict(list)

    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)

    return list(anagrams.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# print(group_anagrams(strs))

######################################################################

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dummy_head = ListNode()
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:
        # Get the values of the current nodes (or 0 if None)
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # Calculate the sum and carry
        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10

        # Create a new node with the sum digit
        current.next = ListNode(digit)
        current = current.next

        # Move to the next nodes in the input lists
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy_head.next

# Example usage:
# Suppose l1 = [2, 4, 3] and l2 = [5, 6, 4]
# Represented as linked lists: l1 = 2 -> 4 -> 3 and l2 = 5 -> 6 -> 4
# Expected output: 7 -> 0 -> 8, since 342 + 465 = 807

# Create linked lists l1 and l2
l1 = ListNode(2)
# print(l1)
l1.next = ListNode(4)
# print(l1.next)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# Call the addTwoNumbers function and print the result
# result = addTwoNumbers(l1, l2)
# while result:
#     print(result.val, end=" -> ")
#     result = result.next

######################################################################

class Solution:
    def __init__(self, x):
        self.x = 121

    def is_palindrome(self):
        if self.x < 0:
            return False
        
        reversed_num = 0
        original_num = self.x
        
        while self.x != 0:
            digit = self.x % 10
            reversed_num = reversed_num*10 + digit
            self.x = self.x // 10

        return reversed_num == original_num
s = Solution(121) 
# print(s.is_palindrome())


class Solution:
    
    def is_palindrome(self, x):
        if x < 0:
            return False
        
        reversed_num = 0
        original_num = x
        
        while x != 0:
            digit = x % 10
            reversed_num = reversed_num*10 + digit
            x = x // 10

        return reversed_num == original_num
s = Solution() 
# print(s.is_palindrome(121))

######################################################################

"""def longest_common_prefix(strs):
    if not strs:
        return ""
    
    # Find the minimum length string in the list
    min_len_str = min(strs, key=len)
    
    # Iterate through characters of the minimum length string
    for i, char in enumerate(min_len_str):
        # Check if the character at this position is the same in all strings
        if not all(word[i] == char for word in strs):
            # If not, return the prefix up to this point
            return min_len_str[:i]
    
    # If all characters match in the minimum length string, return it
    return min_len_str

# Example usage
strs = ["flower", "flow", "flight"]
print(longest_common_prefix(strs))  # Output: "fl"

"""
######################################################################

def longest_common_prefix(strs):
    if not strs:
        return ""
    
    # Find the length of the first string (assuming it's the shortest)
    min_len = len(strs[0])
    for word in strs[1:]:
        min_len = min(min_len, len(word))
    
    # Iterate through characters up to the length of the shortest string
    for i in range(min_len):
        # Compare characters at position i in all strings
        char = strs[0][i]
        if not all(word[i] == char for word in strs):
            return strs[0][:i]  # Return the prefix up to position i
    
    return strs[0][:min_len]  # Return the entire shortest string

# Example usage
strs = ["flower", "flow", "flight"]
# print(longest_common_prefix(strs))  # Output: "fl"

##################################################
def merge(nums1, m, nums2, n):
    p1, p2, p3 = m-1, n-1, m+n-1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p3] = nums1[p1]
            p1 -= 1
        else:
            nums1[p3] = nums2[p2]
            p2 -= 1
        p3 -= 1

# Copy remaining elements from nums2 if any
    while p2 >= 0:
        nums1[p3] = nums2[p2]
        p2 -= 1
        p3 -= 1


num1 = [1, 2, 4, 0, 0, 0]
m = 3
num2 = [3, 5, 6]
n = 3
merge(num1, m, num2, n)

print(num1)


##################################################


def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    a, b = 1, 2
    for _ in range(n - 2):  # We have already considered the first two steps, so iterate n - 2 times
        a, b = b, a + b
    
    return b

# Example usage:
n = 5
print(climbStairs(n))  # Output: 8
