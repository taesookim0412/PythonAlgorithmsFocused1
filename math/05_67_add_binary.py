class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == "0" and b == "0":
            return "0"
        nums = [0, 0]
        for i, c in zip(range(len(a)), reversed(a)):
            nums[0] += int(c) * (2 ** i)
        for i, c in zip(range(len(b)), reversed(b)):
            nums[1] += int(c) * (2 ** i)
        num_total = sum(nums)
        res = []
        while num_total > 0:
            res.append(str(num_total % 2))
            num_total //= 2
        return ''.join(res[::-1])

