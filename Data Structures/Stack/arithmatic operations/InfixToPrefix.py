def priority(op):
    if op == '(' or op == ')':
        return 0
    elif op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op == '^':
        return 3
    return 0

def InfixToPrefix(s):
    # Step 1: Reverse the infix expression
    s = s[::-1]
    
    # Step 2: Replace ( with ) and vice versa
    s = s.replace('(', 'temp').replace(')', '(').replace('temp', ')')
    
    # Step 3: Apply infix to postfix algorithm
    n = len(s)
    i = 0
    st = []
    ans = ""

    while i < n:
        if (s[i] >= "A" and s[i] <= "Z") or (s[i] >= "a" and s[i] <= "z") or (s[i] >= "0" and s[i] <= "9"):
            ans = ans + s[i]
        elif s[i] == "(":
            st.append(s[i])
        elif s[i] == ")":
            while len(st) > 0 and st[-1] != "(":
                ans += st.pop()
            if len(st) > 0 and st[-1] == "(":
                st.pop()
        else:  # For operators
            while len(st) > 0 and priority(s[i]) <= priority(st[-1]):
                ans += st.pop()
            st.append(s[i])
        i += 1
    
    # Pop remaining operators from stack
    while len(st) > 0:
        ans += st.pop()
    
    # Step 4: Reverse the result to get the prefix expression
    return ans[::-1]
