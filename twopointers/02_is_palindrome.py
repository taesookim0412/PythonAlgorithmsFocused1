def is_palindrome(s: str) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE
    s_list = list(s)
    filtered_list = list(map(lambda x: x.lower(), filter(lambda c: c.isalpha(), s_list)))
    s = ''.join(filtered_list)
    l, r = 0, len(s) - 1
    while l <= r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

if __name__ == '__main__':
    s = input()
    res = is_palindrome(s)
    print('true' if res else 'false')
