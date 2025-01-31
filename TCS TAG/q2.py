#backtracking
def highest_two_rods(rods):
    if not rods:
        return 0
    rods_sorted = sorted(rods, reverse=True)
    if len(rods_sorted) >= 2:
        a, b = rods_sorted[0], rods_sorted[1]
        if a == b:
            return a + b
    return rods_sorted[0]