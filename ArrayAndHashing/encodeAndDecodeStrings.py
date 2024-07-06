'''
String Encode and Decode
Design an algorithm to encode a list of strings to a single string. The encoded
string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]'''

class Solution:

    def encode(self, strs: list[str]) -> str:
        if strs == []:
            return ""

        lenght_words = []

        encode_string = ""

        for string in strs:
            encode_string += string
            lenght_words.append(len(string))

        amounts = ";"

        for amount in lenght_words:
            amounts += str(amount) + ","

        encode_string += amounts

        return encode_string

    def decode(self, s: str) -> list[str]:
        if s == "":
            return []

        semi_colon_index = 0

        for i in range(len(s)):
            if s[i] == ";":
                semi_colon_index = i

        lengths_of_words = [0]
        lengths = ""

        for num in s[semi_colon_index + 1:]:

            if num == ",":
                lengths_of_words.append(int(lengths))
                lengths = ""
            else:
                lengths += num


        words = []
        start = 0


        for i in range(1, len(lengths_of_words)):
            end = start + lengths_of_words[i]
            word = s[start: end]

            words.append(word)
            start += lengths_of_words[i]


        return words


solution = Solution()

encoded_string = solution.encode(["neet","code","love","you"])

print(encoded_string)
print(solution.decode(encoded_string))
