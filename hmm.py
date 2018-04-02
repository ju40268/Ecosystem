# # scores = [1, 10, 5, 3, 5]
# # lower_bounds = [0, 11, 2, 5]
# # upper_bounds = [5, 20, 9, 5]
# # scores.sort()
# # print(scores)
# # def binarySearch(nums, target):
# #     # find insert position
# #     start, end = 0, len(nums)-1
# #     while (start + 1 < end):
# #         mid = (end - start) // 2 + start
# #         if (nums[mid] == target): return mid
# #         elif nums[mid] < target: start = mid
# #         else: end = mid
# #     # check final left, right pointer
# #     print(target, "start, end", start, end)
# #     if (target <= nums[start]): return start
# #     elif (target <= nums[end]): return end
# #     else: return end+1
# #
# # print(binarySearch(scores, 0))
# # print(binarySearch(scores, 5))
#
# def bruteforce(scores, lo, up):
#     count = 0
#     for s in scores:
#         if lo <= s <= up: count += 1
#     return count
#
# def binarysearch(score, target):
#     start, end = 0, len(scores)-1
#     while (start + 1 < end):
#         mid = (end-start)//2 + start
#         if (scores[mid] < target): start = mid
#         else: end = mid
#     # remove duplicated
#     while (start+1 < len(score) and score[start] == score[start + 1]): start += 1
#     while (end+1 < len(score) and score[end] == score[end + 1]): end += 1
#     if target < score[start]: return start
#     elif target < score[end]: return end
#     else: return (end+1)
#
#
#
# # [1, 10, 5, 3, 5]
# lower_bounds = [0, 11, 2, 5]
# upper_bounds = [5, 20, 9, 5]
# scores = [1, 3, 5, 5, 5, 5, 5, 10]
# if __name__ == "__main__":
#     res_brute_force, res_binary_search = [], []
#     for l, u in zip(lower_bounds, upper_bounds):
#         res_brute_force.append(bruteforce(scores, l, u))
#     print(res_brute_force)
#     # assert res_brute_force == [4, 0, 3, 2]
#     for l, u in zip(lower_bounds, upper_bounds):
#         res_binary_search.append(binarysearch(scores, u) - binarysearch(scores, l))
#     print(res_binary_search)

# sym = ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff']
# dec = [int(x, 16) for x in sym]
# color = "#09f166"
# output = ""
# min_val = [0] * len(sym)
# for i in range(3):
#     current = int(color[i * 2 + 1: i * 2 + 3], 16)
#     for d in range(len(dec)):
#         min_val[d] = abs(current - dec[d])
#     output += sym[min_val.index(min(min_val))]
#
# res = "#"
# for i in range(0, len(output), 2):
#     res += output[i]
# print(res)
# A = [0,4,4,5,9]
# B = [0,1,6,8,10]
# res = 0
# for i in range(len(A) - 1):
#     if A[i] == A[i+1]: continue
#     if B[i] == B[i+1]: continue
#     if A[i] > A[i+1]:
#         A[i+1], B[i+1] = B[i+1], A[i+1]
#         print(A, B)
#         res += 1
#     if B[i] > B[i+1]:
#         A[i+1], B[i+1] = B[i+1], A[i+1]
#         print(A, B)
#         res += 1
# print(res)
# print(A, B)

# cpdomains = ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
# cpdomains = ["9001 discuss.leetcode.com"]
# d = {}
# for cpdomain in cpdomains:
#     cnt, domain = cpdomain.split()
#     d[domain] = d.get(domain, 0) + int(cnt)
#     while domain.find('.') != -1:
#         i = domain.find('.')
#         d[domain[i + 1:]] = d.get(domain[i + 1:], 0) + int(cnt)
#         domain = domain[i + 1:]
#
# print([str(value) + " " + key for key, value in d.items()])


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Bring some raw data.
frequencies = [6, -16, 75, 160, 244, 260, 145, 73, 16, 4, 1]

# In my original code I create a series and run on that,
# so for consistency I create a series from the list.
freq_series = pd.Series.from_array(frequencies)

x_labels = [108300.0, 110540.0, 112780.0, 115020.0, 117260.0, 119500.0,
            121740.0, 123980.0, 126220.0, 128460.0, 130700.0]

# Plot the figure.
plt.figure(figsize=(12, 8))
ax = freq_series.plot(kind='bar')
ax.set_title('Amount Frequency')
ax.set_xlabel('Amount ($)')
ax.set_ylabel('Frequency')
ax.set_xticklabels(x_labels)

rects = ax.patches

# For each bar: Place a label
for rect in rects:
    # Get X and Y placement of label from rect.
    y_value = rect.get_height()
    x_value = rect.get_x() + rect.get_width() / 2

    # Number of points between bar and label. Change to your liking.
    space = 5
    # Vertical alignment for positive values
    va = 'bottom'

    # If value of bar is negative: Place label below bar
    if y_value < 0:
        # Invert space to place label below
        space *= -1
        # Vertically align label at top
        va = 'top'

    # Use Y value as label and format number with one decimal place
    # label = "{:.1f}".format(y_value)
    label = "{:}".format(y_value)

    # Create annotation
    plt.annotate(
        label,                      # Use `label` as label
        (x_value, y_value),         # Place label at end of the bar
        xytext=(0, space),          # Vertically shift label by `space`
        textcoords="offset points", # Interpret `xytext` as offset in points
        ha='center',                # Horizontally center label
        va=va)                      # Vertically align label differently for
                                    # positive and negative values.

plt.savefig("image.png")