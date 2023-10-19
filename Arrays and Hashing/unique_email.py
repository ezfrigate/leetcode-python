def numUniqueEmails(emails):
    ans = []
    for email in emails:
        lst = email.split('@')
        uniq = lst[0].split('+')[0].replace('.','') + '@' + lst[1]
        ans.append(uniq)
    return len(set(ans))
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(numUniqueEmails(emails))