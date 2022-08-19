inf = float('inf')
def solution():
    k = int(input())
    s = input()
    ct = 0
    word_lengths = []
    for ch in s:
        ct += 1
        if ch == ' ' or ch == '-':
            word_lengths.append(ct)
            ct = 0
    word_lengths.append(ct)
    
    # print(word_lengths)

    def test_ad(word_limit):
        line_size = 0
        lines_used = 0
        for l in word_lengths:
            if l > word_limit:
                # print(word_limit, "didn't work, used", lines_used, "lines")
                return False
            elif line_size + l > word_limit:
                lines_used += 1
                line_size = l
            else:
                line_size += l
            if lines_used > k:
                # print(word_limit, "didn't work, used", lines_used, "lines")
                return False
        if line_size != 0:
            lines_used += 1
        if lines_used > k:
            # print(word_limit, "didn't work, used", lines_used, "lines")
            return False
        # print(word_limit, "works, used", lines_used, "lines")
        return True

    left = 0
    right = len(s)

    while left < right:
        mid = left + (right - left) // 2
        if test_ad(mid):
            right = mid
        else:
            left = mid + 1
    print(left)


if __name__ == "__main__":
    solution()