def lengthofLongestSubstring(s: str) -> int:
    if not s:
        return 0
        
    left = 0
    char_count = {}
    max_len = 0
    
    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1

        while len(char_count) > 2:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

print(lengthofLongestSubstring('eceba'))
print(lengthofLongestSubstring('ccaabbb'))
