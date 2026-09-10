class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)
            
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            # Read the length
            length = int(s[i:j])
            
            # Extract the actual string payload
            start = j + 1
            end = start + length
            res.append(s[start:end])
            
            # Move index past the current string payload
            i = end
        return res
        