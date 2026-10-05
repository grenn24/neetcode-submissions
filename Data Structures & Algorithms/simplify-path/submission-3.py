class Solution:
    def simplifyPath(self, path: str) -> str:
        result = []

        parts = path.split("/")
        parts = list(filter(lambda x: x != "", parts))
        
        for part in parts:
            if part == "..":
                if result:
                    result.pop()
                continue

            if part == ".":
                continue

            result.append(part)
            
        return "/" + "/".join(result)