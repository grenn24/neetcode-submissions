class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        sumW = a
        carried = b
        while True:
            tmp = sumW
            sumW = (sumW ^ carried) & MASK
            carried = ((tmp & carried) << 1) & MASK
            if carried == 0:
                break

        if sumW > 0x7FFFFFFF:
            sumW = sumW - (1 << 32)

        return sumW