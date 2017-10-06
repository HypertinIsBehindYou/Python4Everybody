"""
9.4 Write a program to read through the mbox-short.txt and figure out
who has the sent the greatest number of mail messages. The program looks
for 'From ' lines and takes the second word of those lines as the person
who sent the mail. The program creates a Python dictionary that maps the
sender's mail address to a count of the number of times they appear in the
file. After the dictionary is produced, the program reads through the
dictionary using a maximum loop to find the most prolific committer.
"""

fname = input("Open a file: ")
d = dict()
try:
    fh = open(fname)
except:
    print("No file name found")
    quit()

for line in fh:
    if not line.startswith("From "):
        continue
    else:
        line.rstrip()
        words = line.split()
        email = words[1]
        d[email] = d.get(email,0) + 1



maxCount = 0
maxEmail = 0
for email,count in d.items() :
	if maxCount < count :
		maxCount = count
		maxEmail = email

print (maxEmail, maxCount)
