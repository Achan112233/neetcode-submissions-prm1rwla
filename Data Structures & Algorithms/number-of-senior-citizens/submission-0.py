class Solution:
    def countSeniors(self, details: List[str]) -> int:
        counter = 0
        for s in details:
            num = int(s[11] + s[12])
            print(num)
            if num > 60:
                counter += 1
        return counter