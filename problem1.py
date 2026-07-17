"""
BFS Approach:
1. Explore all possible strings by removing one parenthesis at a time (level by level).
2. For each level, check if any string is a valid expression.
3. If we find valid expressions at the current level, we stop generating further levels
   because any further removals would not be the minimum removals.
4. We use a set for each level to avoid processing duplicate strings.

TC: O(N * 2^N) in the worst case where we explore many combinations
SC: O(2^N) in the worst case to store strings in the level set
"""
from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
            if count < 0:
                return False
        return count == 0

    def removeInvalidParentheses(self, s: str) -> List[str]:
        # Initialize level with just the starting string
        level = {s}
        while True:
            # Check if there are any valid expressions in the current level
            valid_expressions = list(filter(self.isValid, level))
            if valid_expressions:
                return valid_expressions
            
            # Generate next level by removing exactly one parenthesis from each string
            next_level = set()
            for string in level:
                for i in range(len(string)):
                    if string[i] in '()':
                        # Slice out the parenthesis at index i
                        next_level.add(string[:i] + string[i+1:])
            
            # Move to the next level
            level = next_level