from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_char = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno',
        '7':'pqrs','8':'tuv','9':'wxyz'}
        ans = []
        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                ans.append(combination)
            else:
                for letter in num_to_char[next_digits[0]]:
                    backtrack(combination+letter, next_digits[1:])

        if digits:
            backtrack("", digits) # start with an empty string
        return ans

if __name__ == "__main__":
    digits = "23"
    print(Solution().letterCombinations(digits))
