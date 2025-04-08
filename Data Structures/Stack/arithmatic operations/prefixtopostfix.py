def pretopost(s):
    n = len(s)
    i = n
    st = []

    while i >= n:
        if (s[i] >= "A" and s[i] <= "Z") or (s[i] >= "a" and s[i] <= "z") or (s[i] >= "0" and s[i] <= "9"):
            st.append(s[i])
        
        else:
            t1 = st[-1]
            st.pop()
            t2 = st[-1]
            st.pop()

            st.append(t1 + t2 + s[i])
        i+=1

    return st        