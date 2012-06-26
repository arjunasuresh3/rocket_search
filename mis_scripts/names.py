import random
alphabet = 'abcdefghijklmnopqrstuvwxyz'
min = 5
max = 15
total = 10000000
string=''
FILE = open("names.txt","w")
for count in xrange(1,total):
  for x in random.sample(alphabet,random.randint(min,max)):
      string+=x
  FILE.write(string+'\n')
  string=''
FILE.close() 
