class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            new_mail = ""
            i = 0
            after_at = False
            while i < len(email):
                if email[i] == "." and after_at == False:
                    i += 1
                elif email[i] == "+":
                    while email[i] != "@":
                        i += 1
                        after_at = True
                else:
                    new_mail += email[i]
                    i += 1
            seen.add(new_mail)
        return len(seen)
        