import string
import random
def bases_freq(dna_seq_file):
    file=open(dna_seq_file,"r")#opens the file#example for a text.
    file.readline()
    frequency={}
    Dictionary= {}
    for line in file:
        
        i=0
        lenght=len(line)
        while i<lenght:
            word=line[i]
            
            if Dictionary.has_key(word):#if the substring already exists in the dictionary
                Dictionary[word] += 1
            else:
                Dictionary[word]=1
            i+=1
        
    file.close()
        
   
             
    Dictionary =  {k.lower(): v for k, v in Dictionary.items()}
    count=0

    count=Dictionary["a"]+Dictionary["t"]+Dictionary["g"]+Dictionary["c"]
      
    for k in Dictionary:
        frequency[k]=float(Dictionary[k]*100)/count
    frequency['gc']=float((Dictionary['g']+Dictionary['c'])*100)/count
    for k in frequency:
       frequency[k]= "{0:.1f}".format(frequency[k])
    return frequency
    
       
    
     
    
#examples:

output= bases_freq("sample_dna1.txt")
print "sample_dna1",'\n'
print "a",  "    ", "t","     ","c","     ","g","     ","gc"
print output["a"]," ",output["t"]," ", output["c"]," ",output["g"]," ",output["gc"]
print '\n'
print '\n'

output= bases_freq("sample_dna2.txt")
print "sample_dna2",'\n'
print "a",  "    ", "t","     ","c","     ","g","     ","gc"
print output["a"]," ",output["t"]," ", output["c"]," ",output["g"]," ",output["gc"]

print '\n'
print '\n'

output= bases_freq("Escherichia coli.txt")
print "Escherichia coli K-12 substr. MG1655","\n"
print "a",  "    ", "t","     ","c","     ","g","     ","gc"
print output["a"]," ",output["t"]," ", output["c"]," ",output["g"]," ",output["gc"]
print '\n'
print '\n'


with open("DNA.txt","a+")as f:
    f.write("random DNA\n")
    for i in range(2000):
        line=random.choice("atgc")
        f.write(line)
    data=f.read()
f.close()


output= bases_freq("DNA.txt")
print "random DNA",'\n'
print "a",  "    ", "t","     ","c","     ","g","     ","gc"
print output["a"]," ",output["t"]," ", output["c"]," ",output["g"]," ",output["gc"],
print '\n'
print '\n'

def deleteContent(fName):
    with open(fName, "w"):
        pass
    
deleteContent("DNA.txt")


output= bases_freq("chromosome 22.txt")
print "chromosome 22","\n"
print "a",  "    ", "t","     ","c","     ","g","     ","gc"
print output["a"]," ",output["t"]," ", output["c"]," ",output["g"]," ",output["gc"]
print '\n'
print '\n'


output= bases_freq("Human adenovirus B2.txt")
print "Human adenovirus B2","\n"
print "a",  "    ", "t","     ","c","     ","g","     ","gc"
print output["a"]," ",output["t"]," ", output["c"]," ",output["g"]," ",output["gc"]
print '\n'
print '\n'


