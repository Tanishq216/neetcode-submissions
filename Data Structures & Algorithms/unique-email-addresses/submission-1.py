class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for e in emails:
            local,domain = e.split('@')
            local = local.split("+")[0]
            print(local)
            local = local.replace(".","")
            unique.add((local, domain))
            print(unique)
        return len(unique)


        