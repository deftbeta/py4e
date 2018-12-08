fname = input("Enter file:")
fh = open(fname)
emails = list()
emailcounts = dict()
for line in fh:
    if not line.startswith("From:") : continue
    line = line.rstrip()
    line = line.split()
    email = line[1]
    emails.append(email)
    #for email in emails:
    emailcounts[email] = emailcounts.get(email,0) + 1
        #print(emailcounts)
print ('list of emails: ',emails)
print('dictionary of emails: ',emailcounts)
bigcount = None
bigemail = None
for email,count in emailcounts.items():
    if bigcount is None or count > bigcount:
        bigemail = email
        bigcount = count
print(bigemail, bigcount)

#if len(name) < 1 : name = "mbox-short.txt"
#handle = open(name)
