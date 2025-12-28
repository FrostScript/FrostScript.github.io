---
title: 无重复字符的最长子串 - 算法解析与演示
date: 2025-12-27 10:00:00
tags: [算法, Python, 字符串, LeetCode]
categories: 技术教程
---

# 无重复字符的最长子串 - 算法解析与演示

## 问题描述

给定一个字符串，请找出其中不含有重复字符的最长子串的长度。

例如：
- 输入: "abcabcbb"，输出: 3，因为最长无重复字符子串是"abc"
- 输入: "bbbbb"，输出: 1，因为最长无重复字符子串是"b"
- 输入: "pwwkew"，输出: 3，因为最长无重复字符子串是"wke"

## 算法思路

这是一个经典的滑动窗口问题。我们可以使用一个字符串temp来维护当前无重复字符的子串，当遇到重复字符时，调整窗口的起始位置。

## 代码实现

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = ""      # 维护当前无重复字符的子串
        temp_ans = 0   # 当前子串长度
        ans = 0        # 记录最大长度
        
        for i in range(0, len(s)):
            if s[i] not in temp:
                # 如果当前字符不在temp中，将其加入temp
                temp += s[i]
                temp_ans += 1
            else:
                # 如果当前字符在temp中，找到重复字符的位置并截取
                temp = temp[temp.find(s[i]) + 1:]
                temp += s[i]
                temp_ans = len(temp)
            # 更新最大长度
            ans = max(ans, temp_ans)
        
        return ans
```

## 算法解析

1. 使用变量`temp`来存储当前无重复字符的子串
2. `temp_ans`记录当前子串的长度，`ans`记录遇到的最大长度
3. 遍历字符串中的每个字符：
   - 如果当前字符不在`temp`中，则将其加入`temp`，并增加长度计数
   - 如果当前字符已在`temp`中，则从重复字符的下一个位置开始截取`temp`，再加入当前字符
   - 每次迭代都更新最大长度

## 时间复杂度

- 时间复杂度：O(n²)，其中n是字符串的长度，因为temp.find()操作可能需要O(n)时间
- 空间复杂度：O(min(m,n))，其中m是字符串中不同字符的数量

## 优化方案

可以使用哈希表来优化查找重复字符的位置，将时间复杂度降低到O(n)：

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_map = {}  # 存储字符及其最新索引
        left = 0       # 滑动窗口左边界
        max_len = 0    # 最大长度
        
        for right in range(len(s)):
            if s[right] in char_map and char_map[s[right]] >= left:
                # 更新左边界
                left = char_map[s[right]] + 1
            
            char_map[s[right]] = right
            max_len = max(max_len, right - left + 1)
        
        return max_len
```

## 演示

[查看算法演示](/HTML/algorithm_demos/lengthOfLongestSubstring.html)
[index1](/HTML/index.html)
[index2](/HTML/algorithm_demos/index.html)
