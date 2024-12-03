l1=[]
num=int(input("How many strings you want to enter? "))
found = True

for i in range(0,num):
   word=input("Enter a word: ")
   l1.append(word)
search=input("Enter a word you want to search: ")

for j in l1:
   if j == search:
      found = False

if found==False:
   print(search,"Found!!")
else:
   print("Not found!!")
