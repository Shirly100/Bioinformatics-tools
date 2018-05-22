from string import *
import random
def count(string, substring):
    string_size = len(string)
    substring_size = len(substring)
    count = 0
    for i in xrange(0,string_size-substring_size+1):
        if string[i:i+substring_size] == substring:
            count+=1
    return count
def representation(word, dna_seq_file):
    a=word[0]
    b=word[1]
    file=open(dna_seq_file,"r")
    file.readline()
    Dictionary={}
    for line in file:
        i=0
        line=line.rstrip('\n')
        lenght=len(line)
        while i<lenght:
            word1=line[i]
            if Dictionary.has_key(word1):#if the substring already exists in the dictionary
                Dictionary[word1] += 1
            else:
                Dictionary[word1]=1
            
            i+=1


        
    file.close()
      
    Dictionary =  {k.lower(): v for k, v in Dictionary.items()}
    count1=Dictionary["a"]+Dictionary["t"]+Dictionary["g"]+Dictionary["c"]
    frequency={}
    frequency[a]=float(Dictionary[a])/count1
    frequency[b]=float(Dictionary[b])/count1
    
        
    
    
    
    
    file=open(dna_seq_file,"r")
    file.readline()

    Dictionary2={}
    what="actg"
    end=""
    

    for line in file:
        line=line.lower()
        line=line.rstrip('\n')
        end+=line
        line=end
       
        i=0
        while i!=4:
            j=0
            while j!=4:
                word2=""
                word2=what[i]
                word2+=(what[j])
                if Dictionary2.has_key(word2):#if the substring already exists in the dictionary
                    Dictionary2[word2]+=count(line, word2)
                    
                    
                else:
                    Dictionary2[word2]=count(line, word2)
                    
                j+=1
            i+=1
        lenght=len(line)
        end=line[lenght-1]
        
           
            
     

    sam=0
    for k in Dictionary2:
        sam+= Dictionary2[k]
        

    x=float(Dictionary2[word])/sam
    p= float(x)/(frequency[a]*frequency[b]) -0.022
    p= "{0:.3f}".format(p)
    return p
            
        
        
    
        

     
output=representation("gc", "sample_dna1.txt")
print "sample_dna1"
print "gc representation: ", output
print '\n'

output=representation("gc", "sample_dna2.txt")

print "sample_dna2"
print "gc representation: ", output
print '\n'


output=representation("gc", "Human adenovirus B2.txt")
print "Human adenovirus B2"
print "gc representation: ", output
print '\n'

output=representation("gc", "Escherichia coli.txt")
print "Escherichia coli"
print "gc representation: ", output
print '\n'


with open("DNA.txt","a+")as f:
    f.write("random DNA\n")
    for i in range(2000):
        line=random.choice("atgc")
        f.write(line)
    data=f.read()
f.close()

output=representation("gc", "DNA.txt")
print "random DNA"
print "gc representation: ", output
print '\n'




def deleteContent(fName):
    with open(fName, "w"):
        pass
    
deleteContent("DNA.txt")

     
output=representation("gc", "chromosome 22.txt")
print "chromosome 22"
print "gc representation: ", output
print '\n'




