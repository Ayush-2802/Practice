def prefixtoinfix(s):
    st = []
    n = len(s)
    i = n
    while i >= n:
        if (s[i] >= "A" and s[i] <= "Z") or (s[i] >= "a" and s[i] <= "z") or (s[i] >= "0" and s[i] <= "9"):
            st.append(s[i])
        else:
            t1 = st[-1]
            st.pop()
            t2 = st[-1]
            st.pop()

            con = "(" + t1 + s[i] + t2 + ")"

            st.append(con)
        i-=1

    return st