# https://leetcode.com/problems/median-of-two-sorted-arrays/


def pos(x: int | float, l: list[int]) -> int:
    """
    TODO: what if x in l
    l: sortyed array
    x: some number
    returns: index of x if inserted in l
    """
    if not l:
        return 0
    y = l[len(l) // 2]
    if len(l) == 1:
        return int(x > y)
    elif x > y:
        return len(l) // 2 + pos(x, l[len(l) // 2 :])
    elif x <= y:
        return pos(x, l[: len(l) // 2])


def pos2(n1, n2):
    original_n1 = n1.copy()
    original_n2 = n2.copy()
    acc_left = 0
    acc_left_n1 = 0
    acc_left_n2 = 0
    median_index = (len(n1) + len(n2)) // 2
    n = len(n1) + len(n2)
    while True:
        print(n1, n2)
        if not n1 and len(n2) == 1:
            break
        if len(n1) == len(n2) == 1 and n1[0] == n2[0]:
            break
        if not n1:
            n1, n2 = n2, n1
            acc_left_n1, acc_left_n2 = acc_left_n2, acc_left_n1
            original_n1, original_n2 = original_n2, original_n1
            continue
        n1_median_index = len(n1) // 2
        n2_pos = pos(n1[n1_median_index], n2)
        left = n2_pos + n1_median_index
        if acc_left + left > median_index:
            # we overshot
            n1 = n1[:n1_median_index]
            n2 = n2[:n2_pos]
        elif acc_left + left <= median_index:
            # we undershot
            acc_left += left
            acc_left_n1 += n1_median_index
            acc_left_n2 += n2_pos

            n1 = n1[n1_median_index:]
            n2 = n2[n2_pos:]

        n1, n2 = n2, n1
        acc_left_n1, acc_left_n2 = acc_left_n2, acc_left_n1
        original_n1, original_n2 = original_n2, original_n1

    if n % 2 == 0:
        print(acc_left_n2)
        others = []
        if 0 <= acc_left_n2 - 1 < len(original_n2):
            others.append(original_n2[acc_left_n2 - 1])
        if len(original_n1) > n // 2 - acc_left_n2 - 1 >= 0:
            others.append(original_n1[n // 2 - acc_left_n2 - 1])
        return (original_n2[acc_left_n2] + max(others)) / 2

    return original_n2[acc_left_n2]

n1 = [1, 2]
n2 = [1, 2]
n = sorted(n1 + n2)
print(pos2(n1, n2))
print(f"median is", n[len(n) // 2])
