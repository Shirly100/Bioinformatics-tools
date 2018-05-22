#Shirly Ohanona 314793910
#The program finds all most frequent k-mers in Text 
import string

file=open("seq.txt","r")#opens the file#example for a text.
data=file.read()#inserts the sequences into a string
data="\n".join(data.split("\n")[1:])#remove the first line


Kmer= input(" Choose a length of substring:  ")#gets the k-mer number from the user


Dictionary= {}
i=0
length=len(data)
while i<=length-Kmer:
    word=data[i:i+Kmer]#finds all the substrings
    if Dictionary.has_key(word):#if the substring already exists in the dictionary
        Dictionary[word] += 1
    else:
        Dictionary[word]=1
    i+=1


flag=0
most={}#dictionary for the most frequent k-mers
for k in Dictionary:
    if  Dictionary[k]>flag:#finds the most frequent k-mers
        flag=Dictionary[k]
        most.clear()
        most[k]=k
    elif Dictionary[k]==flag:
        most[k]=k#there are more than one  most frequent k-mers. inserts all of them into the dictionary
    

   
for k in most:
    print most[k],

print '\t'  
print Dictionary[k]# this isn't asked in the question. it just to know the number of occurrences of the k- mer   

        
#Example:        
#>>> 
# Choose a length of substring:  3
#tga


    





