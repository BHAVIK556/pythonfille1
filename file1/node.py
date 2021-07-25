cat=input("enter a sentence")
print(cat)
cc=0
wordcount=1
for i in cat:
    cc=cc+1 
    wordcount=wordcount+1
if(i == ''):
    wordcount=wordcount+1
print("word in sentence")
print(wordcount)
print("carth in sentence")
print(cc)