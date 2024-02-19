# class Solution:
#     def two_sum(self, nums, target):
#         dict = {}
#         for i, num in enumerate(nums):
#             complement = target - num
#             if complement in dict:
#                 return [dict[complement], i]
#             else:
#                 dict[num] = i
#         return []
    
# s = Solution()
# # print(s.two_sum([2, 7, 8, 4], 9))

# def group_anagrams(strs):
#     anagram_dict = {}
#     for word in strs:
#         sorted_word = ''.join(sorted(word))
#         if sorted_word in anagram_dict:
#             anagram_dict[sorted_word].append(word)
#         else:
#             anagram_dict[sorted_word] = [word]
#     return list(anagram_dict.values())

# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# # print(group_anagrams(strs))

# from collections import defaultdict

# def group_anagrams(strs):
#     anagrams = defaultdict(set)
#     for word in strs:
#         sorted_word = ''.join(sorted(word))
#         anagrams[sorted_word].add(word)
#     return list(anagrams.values())

# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# # print(group_anagrams(strs))


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def sum_number(l1, l2):
#     dummy_head = ListNode()
#     current = dummy_head
#     carry = 0

#     while l1 or l2 or carry:
#         val1 = l1.val if l1 else 0
#         val2 = l2.val if l2 else 0

#         total = val1 + val2 + carry
#         carry = total//10
#         digit = total%10

#         current.next = ListNode(digit)
#         current = current.next

#         if l1:
#             l1 = l1.next 
#         if l2:
#             l2 = l2.next

#     return dummy_head.next


# l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)

# l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)

# result = sum_number(l1, l2)
# # while result:
# #     print(result.val, end=" > ")
# #     result = result.next


# def longest_common_prefix(strs):
#     min_len = len(strs[0])
#     for word in strs[1:]:
#         min_len = min(min_len, len(word))

#     for i in range((min_len)):
#         char = strs[0][i]
#         if not all(char==word[i] for word in strs):
#             return strs[0][:i]
        
#     return strs[0][:min_len]

# strs = ["flower", "flow", "flight"]
# # print(longest_common_prefix(strs))


# class Solution:
#     def longest_common_prefix(self, strs):
#         if not strs:
#             return ""
        
#         min_len = len(strs[0])
#         for word in strs[1:]:
#             min_len = min(min_len, len(word))


#         for i in range(min_len):
#             char = strs[0][i]
#             if not all(word[i] == char for word in strs):
#                 return strs[0][:i]
        
#         return strs[0][:min_len]

# strs = ['flower', 'flight', 'flow']   
# s = Solution()
# # print(s.longest_common_prefix(strs))

# def sum_two(nums, target):
#     dict = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in dict:
#             return [dict[complement], i]
#         else:
#             dict[num] = i
#     return []

# # print(sum_two([2, 7, 1, 3], 9)) 


# def group_anagrams(strs):
#     anagram_dict = {}
#     for word in strs:
#         sorted_word = "".join(sorted(word))
#         if sorted_word in anagram_dict:
#             anagram_dict[sorted_word].append(word)
#         else:
#             anagram_dict[sorted_word] = [word]
#     return list(anagram_dict.values())
# # print(group_anagrams( ["eat", "tea", "tan", "ate", "nat", "bat"]))


# def target_sum_indices(nums, target):
#     indices_dict = {}
#     for i, num in enumerate(nums):
#         complement = target-num
#         if complement in indices_dict:
#             return [indices_dict[complement], i]
#         else:
#             indices_dict[num] = i
#     return []

# # print(target_sum_indices([2, 6, 3, 9], 9))


# def anagrams(strs):
#     anagram_dict = {}

#     for word in strs:
#         sorted_word = "".join(sorted(word))
#         if sorted_word in anagram_dict:
#             anagram_dict[sorted_word].append(word)
#         else:
#             anagram_dict[sorted_word] = [word]

#     return (anagram_dict.values())

# # print(anagrams( ["eat", "tea", "tan", "ate", "nat", "bat"]))


# def sum_no_to_target(nums, target):
#     indices_dict = {}
#     for i, num in enumerate(nums):
#         complement = target-num
#         if complement in indices_dict:
#             return [indices_dict[complement], i]
#         indices_dict[num] = i
#     return []

# # print(sum_no_to_target([2, 7 , 5, 9], 9))


# def anagrams(strs):
#     anagrams = {}
#     for word in strs:
#         sorted_word = ''.join(sorted(word))
#         if sorted_word in anagrams:
#             anagrams[sorted_word].append(word)
#         else:
#             anagrams[sorted_word] = [word]
#     return list(anagrams.values())
    

# # strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# # print(anagrams(strs))


# def palindrome(num):
#     if num < 0:
#         return False
    
#     original_num = num
#     reversed_num = 0

#     while num!=0:
#         digit = num%10
#         reversed_num = reversed_num*10 + digit
#         num = num//10

#     return original_num == reversed_num
# # print(palindrome(987121))


# def sum_two(nums, target):
#     dict = {}
#     for i, num in enumerate(nums):
#         complement = target-num
#         if complement in dict:
#             return [dict[complement], i]
#         else:
#             dict[num] = i
#     return []

# # print(sum_two([3,4,5,8], 13))

# def group_anagrams(strs):
#     anagrams_dict = {}
#     for word in strs:
#         sorted_word = "".join(sorted(word))
#         if sorted_word in anagrams_dict:
#             anagrams_dict[sorted_word].append(word)
#         else:
#             anagrams_dict[sorted_word] = [word]
#     return list(anagrams_dict.values())

# # strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# # print(group_anagrams(strs))


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def sum_two(l1, l2):
#     dummy_head = ListNode()
#     current = dummy_head
#     carry = 0

#     while l1 or l2 or carry:
#         val1 = l1.val if l1 else 0
#         val2 = l2.val if l2 else 0

#         total = val1 + val2 + carry
#         carry = total//10
#         digit = total%10

#         current.next = ListNode(digit)
#         current = current.next

#         if l1:
#             l1 = l1.next 
#         if l2:
#             l2 = l2.next


#     return dummy_head.next

# l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)

# l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)

# result = sum_two(l1, l2)
# while result:
#     # print(result.val, end=" -> ")
#     # result = result.next
        



# # nums1 = [1, 2, 4, 0, 0, 0]
# # m = 3
# # nums2 = [3, 5, 6]
# # n = 3

# # p1, p2, p3 = m - 1, n - 1, m + n - 1

# # while p1 >= 0 and p2 >= 0:
# #     if nums1[p1] > nums2[p2]:
# #         nums1[p3] = nums1[p1]
# #         p1 -= 1
# #     else:
# #         nums1[p3] = nums2[p2]
# #         p2 -= 1
# #     p3 -= 1

# # # Copy remaining elements from nums2 if any
# # while p2 >= 0:
# #     nums1[p3] = nums2[p2]
# #     p2 -= 1
# #     p3 -= 1

# # print(nums1)  # Output: [1, 2, 3, 4, 5, 6]


# # def merge(nums1, m, nums2, n):
# #     p1, p2, p3 = m-1, n-1, m+n-1

# #     while p1 >= 0 and p2 >= 0:
# #         if nums1[p1] > nums2[p2]:
# #             nums1[p3] = nums1[p1]
# #             p1 -= 1
# #         else:
# #             nums1[p3] = nums2[p2]
# #             p2 -= 1
# #         p3 -= 1

# # # Copy remaining elements from nums2 if any
# #     while p2 >= 0:
# #         nums1[p3] = nums2[p2]
# #         p2 -= 1
# #         p3 -= 1


# # num1 = [1, 2, 4, 0, 0, 0]
# # m = 3
# # num2 = [3, 5, 6]
# # n = 3
# # merge(num1, m, num2, n)

# # # print(num1)

# school = {"VNC":"Nagpur", "DPC":"Delhi", "YPS":"Yavatmal"}
# k = school.keys()
# print(k)
# v = school.values()
# print(v)
# i = school.items()
# print(i)
# g = school.get("VNCt", 123)
# print(g)
# s = school.setdefault("VNCt", 123)
# print(s, school)
# p = school.pop("VNCk", 1234)
# print(p)
# pi = school.popitem()
# print(pi)
# # c = school.clear()
# # print(school)
# copied = school.copy()
# (copied.update([(1,2), (5,6)]))
# print(copied, school)

# my_set = {1, 2, 3, 4,8, 5, 6}
# my_set.add(2)
# print(my_set)
# my_set.update((1,2,3),[1,2,3,4],{1,2,3,4})
# print(my_set)
# my_set.remove(2)
# print(my_set)
# print(my_set.pop())
# print(my_set)
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# union_result = set1.symmetric_difference(set2)
# print(union_result)  # Output: {1, 2, 3, 4, 5}



list = [1, 2, 3, 4, 5, 6, 7]
list.extend([1,2,3])
# print(list)
text = "apple,banana,grape,orange,kiwi"
fruits = text.split(",", 3)  # Split into a maximum of 2 parts
# print(fruits)
# Output: ['apple', 'banana', 'grape,orange,kiwi']


text = 36
# stripped_text = text.rstrip()  # Removes trailing spaces
# print(stripped_text)
# Output: "Hello, World!"
# print(bytes(text))
# print(bytearray(text))


import random
import time

names = ['Sunny', 'Bunny', 'Chinny', 'Vinny']
subjects = ['Python', 'Java', 'Blockchain']

def people_list(num_people):
    # results = []
    for i in range(num_people):
        person={
            'id':i,
            'name':random.choice(names),
            'subject':random.choice(subjects)
        }
    yield person
    #     results.append(person)
    # return results

t1 = time.time()
people = people_list(10000000)
# print(people)
t2 = time.time()
print("took:", t2-t1)