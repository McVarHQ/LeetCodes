<div align="center">

# 🧩 LitCoder — LeetCode Submissions Vault

![Total Solutions](https://img.shields.io/badge/Total%20Solutions-89-6e40c9?style=for-the-badge) ![Made with my own good ol' human noggin](https://img.shields.io/badge/Made%20with-my%20good%20ol'%20human%20noggin-orange?style=for-the-badge)

![C++](https://img.shields.io/badge/C%2B%2B-29_solutions-00599C?style=flat-square&logo=cplusplus&logoColor=white) ![Java](https://img.shields.io/badge/Java-14_solutions-ED8B00?style=flat-square&logo=openjdk&logoColor=white) ![Python](https://img.shields.io/badge/Python-38_solutions-3776AB?style=flat-square&logo=python&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-8_solutions-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

</div>

---

## 📖 About This Repository

This repo is a running log of LeetCode problems solved across **C++, Java, Python, and JavaScript**. Each entry includes the problem statement, a link to the source file, and a sample input/output.

## 📑 Table of Contents

- [**C++**](#c) &nbsp;`29 solutions`
- [**Java**](#java) &nbsp;`14 solutions`
- [**Python**](#python) &nbsp;`38 solutions`
- [**JavaScript**](#javascript) &nbsp;`8 solutions`

---

<details open>
<summary>🔵 C++ &nbsp; <code>29 solutions</code></summary>

## 🔵 C++

#### 1. Balanced Brackets Checker

Given one or more strings of brackets (separated by commas), where each string contains only the characters '(', ')', '[', ']', '{', '}' (and possibly other characters which are ignored), determine for each string whether the brackets are balanced -- i.e., every opening bracket has a matching closing bracket of the same type in the correct order. Print "YES" if the string is balanced, otherwise print "NO".

**Source code:** [`balanced_brackets_checker.cpp`](./balanced_brackets_checker.cpp)

**Sample run**
```text
input: (a+b)*[c-d],{[)
output: YES
NO
```

#### 2. Balanced Brackets Checker Dup

Given one or more strings of brackets (separated by commas), where each string contains only the characters '(', ')', '[', ']', '{', '}' (and possibly other characters which are ignored), determine for each string whether the brackets are balanced -- i.e., every opening bracket has a matching closing bracket of the same type in the correct order. Print "YES" if the string is balanced, otherwise print "NO".

**Source code:** [`balanced_brackets_checker_dup.cpp`](./balanced_brackets_checker_dup.cpp)

**Sample run**
```text
input: (a+b)*[c-d],{[)
output: YES
NO
```

#### 3. Clumsy Factorial

The "clumsy factorial" of a positive integer N is computed by taking the integers from N down to 1, and grouping them in chunks of 4, applying the operations multiply, divide (integer division), add, subtract in that repeating order between consecutive numbers (e.g., N * (N-1) / (N-2) + (N-3) * (N-4) / (N-5) + (N-6) - ...). Given N, compute and return its clumsy factorial.

**Source code:** [`clumsy_factorial.cpp`](./clumsy_factorial.cpp)

**Sample run**
```text
input: 4
output: 7
```

#### 4. Communicating Servers

You are given an n x n binary matrix representing servers placed in a grid, where matrix[i][j] = 1 means there is a server at row i, column j (and 0 means no server). Two servers are said to communicate if they share the same row or the same column. Return the number of servers that can communicate with at least one other server.

**Source code:** [`communicating_servers.cpp`](./communicating_servers.cpp)

**Sample run**
```text
input: 3
1 0 0
0 1 1
0 1 1
output: 4
```

#### 5. Egyptian Fraction Decomposition

Given a fraction n/d (where n is the numerator and d is the denominator), express it as a sum of unit fractions (fractions with numerator 1) using the greedy Egyptian Fraction algorithm: repeatedly subtract the largest possible unit fraction from the remaining fraction until nothing remains. Print each unit fraction's denominator on its own line (i.e., print x meaning 1/x), in the order they are generated.

**Source code:** [`egyptian_fraction_decomposition.cpp`](./egyptian_fraction_decomposition.cpp)

**Sample run**
```text
input: 6
14
output: 3
11
231
```

#### 6. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

**Source code:** [`find_the_index_of_the_first_occurrence_in_a_string.cpp`](./find_the_index_of_the_first_occurrence_in_a_string.cpp)

**Sample run**
```text
input: haystack = "sadbutsad", needle = "sad"
output: 0
```

#### 7. Goat Latin

A sentence S is given (a string of space-separated words). Convert each word to "Goat Latin" using the following rules: if a word begins with a vowel (a, e, i, o, u, case-insensitive), append "ma" to the end of the word; if it begins with a consonant, remove the first letter and append it to the end, then append "ma"; for every word, an additional letter 'a' is added to the end for each word index in the sentence (1 'a' for the 1st word, 2 'a's for the 2nd word, etc.). Return the final sentence after transforming it using these rules.

**Source code:** [`goat_latin.cpp`](./goat_latin.cpp)

**Sample run**
```text
input: I speak Goat Latin
output: Imaa peaksmaaa oatGmaaaa atinLmaaaaa
```

#### 8. Greatest Common Divisor of Strings

For two strings s and t, "t divides s" if s is t concatenated with itself one or more times. Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

**Source code:** [`greatest_common_divisor_of_strings.cpp`](./greatest_common_divisor_of_strings.cpp)

**Sample run**
```text
input: str1 = "ABCABC", str2 = "ABC"
output: ABC
```

#### 9. Is Graph Bipartite

There are n nodes, and you are given an adjacency list graph representing an undirected graph where graph[u] is the list of nodes adjacent to node u. Return true if the graph is bipartite (i.e., the nodes can be colored using two colors such that no two adjacent nodes have the same color), otherwise return false.

**Source code:** [`is_graph_bipartite.cpp`](./is_graph_bipartite.cpp)

**Sample run**
```text
input: 4
1 3
0 2
1 3
0 2
output: true
```

#### 10. Job Sequencing Max Profit

You are given n jobs, each with a name (a single character), a deadline, and a profit. Each job takes exactly one unit of time to complete, and only one job can be scheduled at any given time unit, and a job is only counted if it is completed before or on its deadline. Find a sequence of jobs that maximizes the total profit (choosing, for ties, the job with the higher deadline first), and return the job names in the order they were processed.

**Source code:** [`job_sequencing_max_profit.cpp`](./job_sequencing_max_profit.cpp)

**Sample run**
```text
input: 4
a
b
c
d
4
2
4
1
20
15
10
5
output: a b c d
```

#### 11. Kth Smallest Trimmed Number

You are given an array of numeric strings nums (all the same length) and a list of queries, where each query is [k, trim] meaning: trim every number in nums to its rightmost `trim` digits, find the index of the k-th smallest such trimmed number (ties broken by the lower original index), then restore each number to its original length. Process all queries and return an array of the resulting indices, one per query.

**Source code:** [`kth_smallest_trimmed_number.cpp`](./kth_smallest_trimmed_number.cpp)

**Sample run**
```text
input: 102 473 251 814
4
1 1
2 3
4 2
1 2
output: 2 2 1 0
```

#### 12. Longest Substring Without Repeating

Given a string s, find the length of the longest substring without repeating characters.

**Source code:** [`longest_substring_without_repeating.cpp`](./longest_substring_without_repeating.cpp)

**Sample run**
```text
input: abcabcbb
output: 3
```

#### 13. Max Length Equal Zeros Ones

Given a binary array nums (containing only 0s and 1s), find the maximum length of a contiguous subarray with an equal number of 0s and 1s.

**Source code:** [`max_length_equal_zeros_ones.cpp`](./max_length_equal_zeros_ones.cpp)

**Sample run**
```text
input: 0 1 0 0 1 1
output: 6
```

#### 14. Max Subsequence After Insert

You are given a 0-indexed string text and a 0-indexed string pattern of length 2 (pattern[0] and pattern[1], which may be the same character). You may add either pattern[0] or pattern[1] anywhere in text exactly once. Return the maximum number of times pattern can occur as a subsequence of the modified text.

**Source code:** [`max_subsequence_after_insert.cpp`](./max_subsequence_after_insert.cpp)

**Sample run**
```text
input: abdcdbc
ac
output: 4
```

#### 15. Merge Strings Alternatively

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If one string is longer, append its remaining letters to the end of the merged string. Return the merged string.

**Source code:** [`merge_strings_alternatively.cpp`](./merge_strings_alternatively.cpp)

**Sample run**
```text
input: word1 = "abc", word2 = "pqr"
output: apbqcr
```

#### 16. Min Operations Make Multiple of Ten

You are given two integers, num and k. In one operation, you may add or subtract k from num. Find the minimum number of operations needed to make num equal to a multiple of 10 (i.e., make the last digit of num become 0). Return -1 if it is impossible.

**Source code:** [`min_operations_make_multiple_of_ten.cpp`](./min_operations_make_multiple_of_ten.cpp)

**Sample run**
```text
input: 58
9
output: 2
```

#### 17. Min Operations Max Sweetness

You are given an integer array candies representing the sweetness values of various candies, and an integer target. In one operation, you may remove the two candies with the smallest sweetness values and create a new candy whose sweetness equals (smaller value) + 2 * (second smaller value), then put it back. Repeat this operation until the smallest sweetness value among all candies is greater than or equal to target. Return the minimum number of operations required.

**Source code:** [`min_operations_max_sweetness.cpp`](./min_operations_max_sweetness.cpp)

**Sample run**
```text
input: 10
1 2 3 9 10
output: 3
```

#### 18. Min Operations Max Sweetness Dup

You are given an integer array candies representing the sweetness values of various candies, and an integer target. In one operation, you may remove the two candies with the smallest sweetness values and create a new candy whose sweetness equals (smaller value) + 2 * (second smaller value), then put it back. Repeat this operation until the smallest sweetness value among all candies is greater than or equal to target. Return the minimum number of operations required.

**Source code:** [`min_operations_max_sweetness_dup.cpp`](./min_operations_max_sweetness_dup.cpp)

**Sample run**
```text
input: 10
1 2 3 9 10
output: 3
```

#### 19. Number of 1 Bits

Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (the Hamming weight).

**Source code:** [`number_of_1_bits.cpp`](./number_of_1_bits.cpp)

**Sample run**
```text
input: n = 00000000000000000000000000001011
output: 3
```

#### 20. Queue Using Two Stacks

Implement a first-in-first-out (FIFO) queue using only two stacks. The queue is driven by a sequence of comma-separated operations: "1,x" -- enqueue element x to the back of the queue; "2" -- dequeue (remove) the element from the front of the queue; "3" -- return/print the element at the front of the queue. Process the operations and print the result of every front-query (operation 3).

**Source code:** [`queue_using_two_stacks.cpp`](./queue_using_two_stacks.cpp)

**Sample run**
```text
input: 1 1,1 2,1 3,3,2,3
output: 1
2
```

#### 21. Range Update Max Value

You are given an array of size `size` (1-indexed), initially all zeros, and a number of range-update queries. Each query gives a range [left, right] and a value, and adds that value to every element of the array within that inclusive range. After applying all queries, return the maximum value present anywhere in the array.

**Source code:** [`range_update_max_value.cpp`](./range_update_max_value.cpp)

**Sample run**
```text
input: 10 3
1 5 3
4 8 7
6 9 4
output: 11
```

#### 22. Reverse Bits

Reverse the bits of a given 32-bit unsigned integer.

**Source code:** [`reverse_bits.cpp`](./reverse_bits.cpp)

**Sample run**
```text
input: n = 00000010100101000001111010011100
output: 964176192
```

#### 23. Sliding Subarray Beauty

Given an integer array nums containing n integers, find the beauty of each subarray of size k. The beauty of a subarray is the x-th smallest integer in the subarray if it is negative, or 0 if there are fewer than x negative integers. Return an array of n - k + 1 integers, the beauty of each subarray of size k in order from the first index.

**Source code:** [`sliding_subarray_beauty.cpp`](./sliding_subarray_beauty.cpp)

**Sample run**
```text
input: 1 -1 -3 -2 3
3 2
output: -1 -2 -2
```

#### 24. String Character Composition

Given a string, analyze its composition and determine what percentage of its characters are uppercase letters, lowercase letters, digits, and special characters (anything that is not a letter or digit). Print each of the four percentages (formatted to 3 decimal places) on its own line, in the order: uppercase, lowercase, digit, special character.

**Source code:** [`string_character_composition.cpp`](./string_character_composition.cpp)

**Sample run**
```text
input: AbC123!@
output: 25.000%
12.500%
37.500%
25.000%
```

#### 25. Sudoku Solver

Write a program to solve a Sudoku puzzle by filling in the empty cells (represented by '.') of an n x n board, following the standard Sudoku rules -- each row, each column, and each of the 3x3 sub-boxes must contain each digit 1-9 exactly once. Print "YES" if a valid solution exists (and the board is solved), otherwise print "NO".

**Source code:** [`sudoku_solver.cpp`](./sudoku_solver.cpp)

**Sample run**
```text
input: 9
5 3 . . 7 . . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9
output: YES
```

#### 26. Text Editor with Undo

Design a text-editor-like system that supports a sequence of operations on a string of characters, given as a list of comma-separated commands. Each command is one of: "1 <string>" -- append the string to the end of the current text; "2 <k>" -- delete the last k characters from the text; "3 <k>" -- print the k-th character of the text (1-indexed); "4" -- undo the last insert or delete operation (undoing a get/print operation does nothing). Process the commands in order and print the results of every "3" (get character) operation.

**Source code:** [`text_editor_with_undo.cpp`](./text_editor_with_undo.cpp)

**Sample run**
```text
input: 1 abc,3 3,2 2,1 xyz,3 1,4,3 1
output: c
a
a
```

#### 27. Text Editor with Undo Dup

Design a text-editor-like system that supports a sequence of operations on a string of characters, given as a list of comma-separated commands. Each command is one of: "1 <string>" -- append the string to the end of the current text; "2 <k>" -- delete the last k characters from the text; "3 <k>" -- print the k-th character of the text (1-indexed); "4" -- undo the last insert or delete operation (undoing a get/print operation does nothing). Process the commands in order and print the results of every "3" (get character) operation.

**Source code:** [`text_editor_with_undo_dup.cpp`](./text_editor_with_undo_dup.cpp)

**Sample run**
```text
input: 1 abc,3 3,2 2,1 xyz,3 1,4,3 1
output: c
a
a
```

#### 28. Tiling Combinatorics Count

This problem deals with counting valid "towers" or "tilings": for n rows and up to m columns, there is a precomputed table T[i][j] representing the number of ways to tile a 1 x j strip using i types of tiles allowing tiles of length 1 to 4 (with combinations multiplying across i). Using this, the program computes B[j] (number of "bad"/breakable arrangements) and G[j] (number of "good" arrangements) for column counts from 1 to m via a recurrence, and prints G[m] modulo 1,000,000,007.

**Source code:** [`tiling_combinatorics_count.cpp`](./tiling_combinatorics_count.cpp)

**Sample run**
```text
input: 2 3
output: 9
```

#### 29. Trie Password Prefix Check

You are given a list of passwords (strings). A set of passwords is considered "GOOD" if no password is a prefix of another password in the list; otherwise, if any password is found to be a prefix of a previously inserted password (or vice versa), the set is "BAD". Using a Trie, process the passwords in order and print "GOOD PASSWORD" if none is a prefix of another, or "BAD PASSWORD" as soon as a prefix conflict is found.

**Source code:** [`trie_password_prefix_check.cpp`](./trie_password_prefix_check.cpp)

**Sample run**
```text
input: abc abd xyz
output: GOOD PASSWORD
```

</details>

---

<details open>
<summary>☕ Java &nbsp; <code>14 solutions</code></summary>

## ☕ Java

#### 1. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy and a different, later day to sell. Return the maximum profit you can achieve, or 0 if no profit is possible.

**Source code:** [`best_time_to_buy_and_sell_stock.java`](./best_time_to_buy_and_sell_stock.java)

**Sample run**
```text
input: prices = [7,1,5,3,6,4]
output: 5
```

#### 2. Container with Most Water

You are given an integer array height of length n, representing n vertical lines. Find two lines that, together with the x-axis, form a container holding the most water, and return the maximum amount of water it can store.

**Source code:** [`container_with_most_water.java`](./container_with_most_water.java)

**Sample run**
```text
input: height = [1,8,6,2,5,4,8,3,7]
output: 49
```

#### 3. Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

**Source code:** [`counting_bits.java`](./counting_bits.java)

**Sample run**
```text
input: n = 5
output: [0, 1, 1, 2, 1, 2]
```

#### 4. Find Maximum Average Subarray 1

You are given an integer array nums consisting of n elements, and an integer k. Find a contiguous subarray of length k that has the maximum average value, and return this value.

**Source code:** [`find_maximum_average_subarray_1.java`](./find_maximum_average_subarray_1.java)

**Sample run**
```text
input: nums = [1,12,-5,-6,50,3], k = 4
output: 12.75
```

#### 5. Find the Highest Altitude

A biker goes on a road trip with n + 1 points at different altitudes, starting at point 0 with altitude 0. Given an integer array gain of length n where gain[i] is the net altitude gain between points i and i+1, return the highest altitude reached.

**Source code:** [`find_the_highest_altitude.java`](./find_the_highest_altitude.java)

**Sample run**
```text
input: gain = [-5,1,5,0,-7]
output: 1
```

#### 6. Hamming Distance

The Hamming distance between two integers is the number of positions at which the corresponding bits differ. Given two integers x and y, return the Hamming distance between them.

**Source code:** [`hamming_distance.java`](./hamming_distance.java)

**Sample run**
```text
input: x = 1, y = 4
output: 2
```

#### 7. Increasing Triplet Subsequence

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exist, return false.

**Source code:** [`increasing_triplet_subsequence.java`](./increasing_triplet_subsequence.java)

**Sample run**
```text
input: nums = [1,2,3,4,5]
output: true
```

#### 8. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise. A subsequence is formed by deleting some (or no) characters from the original string without disturbing the relative order of the remaining characters.

**Source code:** [`is_subsequence.java`](./is_subsequence.java)

**Sample run**
```text
input: s = "abc", t = "ahbgdc"
output: true
```

#### 9. Max Number of K Sum Pairs

You are given an integer array nums and an integer k. In one operation, you can pick two numbers from the array whose sum equals k and remove them. Return the maximum number of such operations you can perform.

**Source code:** [`max_number_of_k-sum_pairs.java`](./max_number_of_k-sum_pairs.java)

**Sample run**
```text
input: nums = [1,2,3,4], k = 5
output: 2
```

#### 10. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements. This must be done in-place without making a copy of the array.

**Source code:** [`move_zeroes.java`](./move_zeroes.java)

**Sample run**
```text
input: nums = [0,1,0,3,12]
output: [1, 3, 12, 0, 0]
```

#### 11. Prooduct Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all elements of nums except nums[i]. Must run in O(n) time without using division.

**Source code:** [`prooduct_array_except_self.java`](./prooduct_array_except_self.java)

**Sample run**
```text
input: nums = [1,2,3,4]
output: [24, 12, 8, 6]
```

#### 12. Remove Duplicates From Sorted Array

Given an integer array nums sorted in non-decreasing order, remove duplicates in-place such that each unique element appears only once, keeping relative order. Return the number of unique elements.

**Source code:** [`remove_duplicates_from_sorted_array.java`](./remove_duplicates_from_sorted_array.java)

**Sample run**
```text
input: nums = [1,1,2]
output: k = 2, nums = [1, 2]
```

#### 13. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing causes the value to go outside the signed 32-bit integer range, return 0.

**Source code:** [`reverse_integer.java`](./reverse_integer.java)

**Sample run**
```text
input: x = 123
output: 321
```

#### 14. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found, or the index where it would be inserted in order. Must run in O(log n) time.

**Source code:** [`search_insert_position.java`](./search_insert_position.java)

**Sample run**
```text
input: nums = [1,3,5,6], target = 5
output: 2
```

</details>

---

<details open>
<summary>🐍 Python &nbsp; <code>38 solutions</code></summary>

## 🐍 Python

#### 1. Add Binary

Given two binary strings a and b, return their sum as a binary string.

**Source code:** [`add_binary.py`](./add_binary.py)

**Sample run**
```text
input: a = "11", b = "1"
output: 100
```

#### 2. Alid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Given a string s, return true if it is a palindrome, or false otherwise.

**Source code:** [`alid_palindrome.py`](./alid_palindrome.py)

**Sample run**
```text
input: s = "A man, a plan, a canal: Panama"
output: True
```

#### 3. Alindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.

**Source code:** [`alindrome_number.py`](./alindrome_number.py)

**Sample run**
```text
input: x = 121
output: True
```

#### 4. Appy Number

Write an algorithm to determine if a number n is happy. A happy number is defined by repeatedly replacing the number by the sum of the squares of its digits until the number equals 1 (happy) or it loops endlessly in a cycle that doesn't include 1 (not happy). Return true if n is a happy number, and false if not.

**Source code:** [`appy_number.py`](./appy_number.py)

**Sample run**
```text
input: n = 19
output: True
```

#### 5. Asteroid Collision

You are given an array asteroids of integers representing asteroids in a row. For each asteroid, the absolute value represents its size and the sign represents its direction (positive = right, negative = left). If two asteroids meet, the smaller one explodes; if both are the same size, both explode. Find the state of the asteroids after all collisions.

**Source code:** [`asteroid_collision.py`](./asteroid_collision.py)

**Sample run**
```text
input: asteroids = [5,10,-5]
output: [5, 10]
```

#### 6. Climbing Stairs

You are climbing a staircase that takes n steps to reach the top. Each time you can climb 1 or 2 steps. In how many distinct ways can you climb to the top?

**Source code:** [`climbing_stairs.py`](./climbing_stairs.py)

**Sample run**
```text
input: n = 2
output: 2
```

#### 7. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

**Source code:** [`contains_duplicate.py`](./contains_duplicate.py)

**Sample run**
```text
input: nums = [1,2,3,1]
output: True
```

#### 8. Difference Between Two Arrays

Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where answer[0] contains all distinct integers in nums1 not present in nums2, and answer[1] contains all distinct integers in nums2 not present in nums1.

**Source code:** [`difference_between_two_arrays.py`](./difference_between_two_arrays.py)

**Sample run**
```text
input: nums1 = [1,2,3], nums2 = [2,4,6]
output: [[1, 3], [4, 6]]
```

#### 9. Divisible and Non Divisible Sums Difference

You are given positive integers n and m. Define num1 as the sum of all integers in [1, n] not divisible by m, and num2 as the sum of all integers in [1, n] divisible by m. Return num1 - num2.

**Source code:** [`divisible_and_non-divisible_sums_difference.py`](./divisible_and_non-divisible_sums_difference.py)

**Sample run**
```text
input: n = 10, m = 3
output: 19
```

#### 10. Happy Number

Write an algorithm to determine if a number n is happy. A happy number is defined by repeatedly replacing the number by the sum of the squares of its digits until the number equals 1 (happy) or it loops endlessly in a cycle that doesn't include 1 (not happy). Return true if n is a happy number, and false if not.

**Source code:** [`happy_number.py`](./happy_number.py)

**Sample run**
```text
input: n = 19
output: True
```

#### 11. House Robber

You are a professional robber planning to rob houses along a street. Adjacent houses have connected security systems, so you cannot rob two adjacent houses on the same night. Given an integer array nums representing the money stashed in each house, return the maximum amount you can rob without alerting the police.

**Source code:** [`house_robber.py`](./house_robber.py)

**Sample run**
```text
input: nums = [1, 2, 3, 1]
output: Maximum amount you can rob: 4
```

#### 12. Isible and Non Divisible Sums Difference

You are given positive integers n and m. Define num1 as the sum of all integers in [1, n] not divisible by m, and num2 as the sum of all integers in [1, n] divisible by m. Return num1 - num2.

**Source code:** [`isible_and_non-divisible_sums_difference.py`](./isible_and_non-divisible_sums_difference.py)

**Sample run**
```text
input: n = 10, m = 3
output: 19
```

#### 13. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic. Two strings are isomorphic if the characters in s can be replaced to get t, where all occurrences of a character must map consistently to another character (no two characters may map to the same character).

**Source code:** [`isomorphic_strings.py`](./isomorphic_strings.py)

**Sample run**
```text
input: s = "egg", t = "add"
output: True
```

#### 14. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string. A word is a maximal substring of non-space characters.

**Source code:** [`length_of_last_word.py`](./length_of_last_word.py)

**Sample run**
```text
input: s = "Hello World"
output: 5
```

#### 15. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string.

**Source code:** [`longest_common_prefix.py`](./longest_common_prefix.py)

**Sample run**
```text
input: strs = ["flower","flow","flight"]
output: fl
```

#### 16. Merge Linked List

Given k sorted linked lists, merge them all into one sorted linked list and return it.

**Source code:** [`merge_linked_list.py`](./merge_linked_list.py)

**Sample run**
```text
input: 3 sorted lists: [1,3,5], [2,4,6], [0,7,8]
output: 0 1 2 3 4 5 6 7 8
```

#### 17. Number of Flowers in Full Bloom

You are given a 2D integer array flowers, where flowers[i] = [starti, endi] means the ith flower blooms from starti to endi (inclusive), and an integer array people, where people[i] is the time a person arrives to see the flowers. Return an array answer where answer[i] is the number of flowers in full bloom when the ith person arrives.

**Source code:** [`number_of_flowers_in_full_bloom.py`](./number_of_flowers_in_full_bloom.py)

**Sample run**
```text
input: flowers = [[1,6],[3,7],[9,12],[4,13]], people = [2,3,7,11]
output: [1, 2, 2, 2]
```

#### 18. Oman to Integer

Roman numerals are represented by the symbols I, V, X, L, C, D, and M. Given a roman numeral, convert it to an integer.

**Source code:** [`oman_to_integer.py`](./oman_to_integer.py)

**Sample run**
```text
input: s = "III"
output: 3
```

#### 19. Palindrome List

Given a singly linked list, determine whether it is a palindrome (reads the same forward and backward).

**Source code:** [`palindrome_list.py`](./palindrome_list.py)

**Sample run**
```text
input: linked list: 1 -> 2 -> 2 -> 1
output: true
```

#### 20. Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.

**Source code:** [`palindrome_number.py`](./palindrome_number.py)

**Sample run**
```text
input: x = 121
output: True
```

#### 21. Pascals Triangle

Given an integer numRows, return the first numRows of Pascal's triangle, where each number is the sum of the two numbers directly above it.

**Source code:** [`pascal's_triangle.py`](./pascal%27s_triangle.py)

**Sample run**
```text
input: numRows = 5
output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
```

#### 22. Power of Two

Given an integer n, return true if it is a power of two (there exists an integer x such that n == 2^x). Otherwise, return false.

**Source code:** [`power_of_two.py`](./power_of_two.py)

**Sample run**
```text
input: n = 1
output: True
```

#### 23. Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

**Source code:** [`rain_water.py`](./rain_water.py)

**Sample run**
```text
input: elevations = [0,1,0,2,1,0,1,3,2,1,2,1]
output: 6
```

#### 24. Ransom Note

Given two strings ransomNote and magazine, return true if ransomNote can be constructed using the letters from magazine (each letter in magazine can only be used once).

**Source code:** [`ransom_note.py`](./ransom_note.py)

**Sample run**
```text
input: ransomNote = "a", magazine = "b"
output: False
```

#### 25. Reduction Operations to Make the Array Elements Equal

Given an integer array nums, in one operation you find the largest value and change it to the next largest value (and increment an operation counter). Return the number of operations needed to make all array elements equal.

**Source code:** [`reduction_operations_to_make_the_array_elements_equal.py`](./reduction_operations_to_make_the_array_elements_equal.py)

**Sample run**
```text
input: nums = [5,1,3]
output: 3
```

#### 26. Remove Element

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place, and return the number of elements not equal to val. Order may change.

**Source code:** [`remove_element.py`](./remove_element.py)

**Sample run**
```text
input: nums = [3,2,2,3], val = 3
output: 2
```

#### 27. Remove Starts From a String

You are given a string s containing stars (*). In one operation, remove the closest non-star character to a star's left, along with the star itself. Return the string after all stars have been removed.

**Source code:** [`remove_starts_from_a_string.py`](./remove_starts_from_a_string.py)

**Sample run**
```text
input: s = "leet**cod*e"
output: lecoe
```

#### 28. Reverse Words in a String

Given an input string s, reverse the order of the words. Words are separated by at least one space; the returned string should have words separated by a single space with no leading/trailing spaces.

**Source code:** [`reverse_words_in_a_string.py`](./reverse_words_in_a_string.py)

**Sample run**
```text
input: s = "the sky is blue"
output: blue is sky the
```

#### 29. Roman to Integer

Roman numerals are represented by the symbols I, V, X, L, C, D, and M. Given a roman numeral, convert it to an integer.

**Source code:** [`roman_to_integer.py`](./roman_to_integer.py)

**Sample run**
```text
input: s = "III"
output: 3
```

#### 30. Rotate Array

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

**Source code:** [`rotate_array.py`](./rotate_array.py)

**Sample run**
```text
input: nums = [1,2,3,4,5,6,7], k = 3
output: [5, 6, 7, 1, 2, 3, 4]
```

#### 31. String Compression

Given an array of characters chars, compress it in-place: for each group of consecutive repeating characters, append the character to the result, followed by the group's length if greater than 1. Return the new length of the array.

**Source code:** [`string_compression.py`](./string_compression.py)

**Sample run**
```text
input: chars = ["a","a","b","b","c","c","c"]
output: 6 ['a', '2', 'b', '2', 'c', '3']
```

#### 32. Sum

Given an array of integers nums and an integer target, return the indices of the two numbers that add up to target. Each input has exactly one solution, and the same element cannot be used twice.

**Source code:** [`sum.py`](./sum.py)

**Sample run**
```text
input: nums = [2,7,11,15], target = 9
output: [0, 1]
```

#### 33. Two Sum

Given an array of integers nums and an integer target, return the indices of the two numbers that add up to target. Each input has exactly one solution, and the same element cannot be used twice.

**Source code:** [`two_sum.py`](./two_sum.py)

**Sample run**
```text
input: nums = [2,7,11,15], target = 9
output: [0, 1]
```

#### 34. Unique Number of Occurences

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.

**Source code:** [`unique_number_of_occurences.py`](./unique_number_of_occurences.py)

**Sample run**
```text
input: arr = [1,2,2,1,1,3]
output: True
```

#### 35. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise. An anagram is formed by rearranging the letters of a word using all the original letters exactly once.

**Source code:** [`valid_anagram.py`](./valid_anagram.py)

**Sample run**
```text
input: s = "anagram", t = "nagaram"
output: True
```

#### 36. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Given a string s, return true if it is a palindrome, or false otherwise.

**Source code:** [`valid_palindrome.py`](./valid_palindrome.py)

**Sample run**
```text
input: s = "A man, a plan, a canal: Panama"
output: True
```

#### 37. Valid Parenthesis

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid -- every open bracket must be closed by the same type of bracket, in the correct order.

**Source code:** [`valid_parenthesis.py`](./valid_parenthesis.py)

**Sample run**
```text
input: s = "()"
output: True
```

#### 38. Word Pattern

Given a pattern and a string s, find if s follows the same pattern, such that there is a bijection between each letter in pattern and each non-empty word in s.

**Source code:** [`word_pattern.py`](./word_pattern.py)

**Sample run**
```text
input: pattern = "abba", s = "dog cat cat dog"
output: True
```

</details>

---

<details open>
<summary>💛 JavaScript &nbsp; <code>8 solutions</code></summary>

## 💛 JavaScript

#### 1. Add Digits

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

**Source code:** [`add_digits.js`](./add_digits.js)

**Sample run**
```text
input: num = 38
output: 2
```

#### 2. Can Place Flowers

You have a long flowerbed where some plots are planted and some are not, and flowers cannot be planted in adjacent plots. Given an integer array flowerbed of 0s and 1s and an integer n, return true if n new flowers can be planted without violating the no-adjacent-flowers rule.

**Source code:** [`can_place_flowers.js`](./can_place_flowers.js)

**Sample run**
```text
input: flowerbed = [1,0,0,0,1], n = 1
output: true
```

#### 3. Find Pivot Index

Given an array of integers nums, find the leftmost pivot index, where the sum of all numbers strictly to the left of the index equals the sum of all numbers strictly to the right of it. If no such index exists, return -1.

**Source code:** [`find_pivot_index.js`](./find_pivot_index.js)

**Sample run**
```text
input: nums = [1,7,3,6,5,6]
output: 3
```

#### 4. Kids with the Greatest Number of Candies

There are n kids with candies, given as an integer array candies, and an integer extraCandies representing extra candies you have. Return a boolean array result where result[i] is true if giving the ith kid all the extraCandies would give them the greatest number of candies among all kids.

**Source code:** [`kids_with_the_greatest_number_of_candies.js`](./kids_with_the_greatest_number_of_candies.js)

**Sample run**
```text
input: candies = [2,3,5,1,3], extraCandies = 3
output: [true,true,true,false,true]
```

#### 5. Majority Element

Given an array nums of size n, return the majority element -- the element that appears more than floor(n / 2) times. You may assume the majority element always exists.

**Source code:** [`majority_element.js`](./majority_element.js)

**Sample run**
```text
input: nums = [3,2,3]
output: 3
```

#### 6. Plus One

You are given a large integer represented as an integer array digits, where each digits[i] is a digit, ordered from most significant to least significant. Increment the large integer by one and return the resulting array of digits.

**Source code:** [`plus_one.js`](./plus_one.js)

**Sample run**
```text
input: digits = [1,2,3]
output: [1, 2, 4]
```

#### 7. Reverse Vowels of String

Given a string s, reverse only the vowels in the string and return it. Vowels are 'a', 'e', 'i', 'o', 'u' and can appear in upper or lower case.

**Source code:** [`reverse_vowels_of_string.js`](./reverse_vowels_of_string.js)

**Sample run**
```text
input: s = "hello"
output: holle
```

#### 8. Single Number

Given a non-empty array of integers nums where every element appears twice except for one, find that single element. Must run in linear time using only constant extra space.

**Source code:** [`single_number.js`](./single_number.js)

**Sample run**
```text
input: nums = [2,2,1]
output: 1
```

</details>

---
