class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for string in strs:
            result += str(len(string))
            result += "#"
            result += string

        return result

    def decode(self, s: str) -> List[str]:
        pointer = 0
        result = []
        firstIntPos = 0
        print(s)
        while pointer < len(s):
            hash_pos = pointer
            while s[hash_pos] != "#":
                hash_pos += 1

            length = int(s[pointer:hash_pos])
            start = hash_pos + 1
            end = start + length

            result.append(s[start:end])
            pointer = end


        return result


