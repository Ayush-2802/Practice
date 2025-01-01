def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    
    if not strs:
        return ""
    
    # taking first string as refrence
    prefix = strs[0]
    
    # comparing the prefix with other strings
    for string in strs[1:]:
        while string.find(prefix) != 0:
            print(string.find(prefix))
            prefix = prefix[:-1]
            print(prefix)
            if not prefix:
                return ""
                
    return prefix

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))  # Output: "fl"

