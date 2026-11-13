class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        multiplier = 0
        saved_string = ""

        for character in s:
            if character.isdigit():
                multiplier = multiplier * 10 + int(character)
            elif character == "[":
                stack.append((saved_string, multiplier))
                multiplier = 0
                saved_string = ""
            elif character == "]":
                prev_str, prev_num = stack.pop()
                saved_string = prev_str + saved_string * prev_num
            else:
                saved_string += character
        return saved_string