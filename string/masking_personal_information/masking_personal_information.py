class Solution:
    def maskPII(self, s: str) -> str:
        
        def maskEmail(email):
            last = email.find('@') - 1
            email = list(email)
            email[1:last] = "*" * 5
            email = "".join(email)
            email = email.lower()
            return email

        def maskPhone(phone):
            fillers, data, result = ['+', '-', '(', ')', ' '], [], []
            tuplet = 0
            for num in phone:
                if num not in fillers: data.append(num)
            for num in reversed(data):
                if len(result) < 5: result.insert(0, num)
                else: result.insert(0, "*")
                if len(result) in (4, 8): result.insert(0, "-")

            if len(result) > 12: result.insert(-12, "-"); result.insert(0, "+")
            result = "".join(result)

            return result

        if '@' in s: return maskEmail(s)
        else: return maskPhone(s)
