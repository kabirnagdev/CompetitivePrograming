class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        s_counts = Counter(s)
        
        # Check if we can match prefix target[0...i-1]
        def can_build_prefix(prefix_len):
            needed = Counter(target[:prefix_len])
            for char, count in needed.items():
                if s_counts[char] < count:
                    return False
            return True

        # Try to diverge at position i (from longest prefix to shortest)
        for i in range(n - 1, -1, -1):
            if not can_build_prefix(i):
                continue
            
            # Calculate remaining available characters after forming target[0...i-1]
            rem_counts = s_counts.copy()
            for ch in target[:i]:
                rem_counts[ch] -= 1
            
            # Find smallest character > target[i]
            target_char = target[i]
            for c_code in range(ord(target_char) + 1, ord('z') + 1):
                c = chr(c_code)
                if rem_counts[c] > 0:
                    # Place c at index i
                    rem_counts[c] -= 1
                    
                    # Build suffix with remaining characters sorted
                    suffix = []
                    for code in range(ord('a'), ord('z') + 1):
                        char = chr(code)
                        suffix.append(char * rem_counts[char])
                    
                    return target[:i] + c + "".join(suffix)
                    
        return ""