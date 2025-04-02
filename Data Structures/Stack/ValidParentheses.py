def valid(s):
    st = []

    for i in s:
        if i == "(" or i == "[" or i == "{":
            st.append(i)
        else:
            if len(st) == 0:
                return False

            ch = st[-1]
            st.pop()

            if s[i] == ")" and ch == "(" or s[i] == "]" and ch == "[" or s[i] == "}" and ch == "{":
                continue
            else:
                return False
            
    return len(st) == 0