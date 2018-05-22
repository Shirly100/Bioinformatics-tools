#Shirly Ohanona 314793910
from __future__ import division
import random
#===================================================================================================================================================================#
def extractInformation(file):#extracts the sequences and their names from the fasta file
    name=[]
    seq=[]
    for line in file:
        line=line.replace('\n',"")
        if line.startswith(">" or "<"):
            name.append(line)
        else:
            seq.append(line)
    return name,seq
#==================================================================================================================================================================#
def path(pointers,i,j,x):#finds the path in the pointers matrix
    if (i==1 and j==1):
        x=""
        return x


    elif pointers[i][j]=="D":
        return  x+pointers[i][j]+path(pointers,i-1,j-1,x)
    elif pointers[i][j]=="H":
        return x+pointers[i][j]+path(pointers,i,j-1,x)
    elif pointers[i][j]=="V":
        return x+pointers[i][j]+path(pointers,i-1,j,x)
        
#==================================================================================================================================================================#
def finalAlignment(x,first,second,choice):
    if choice=="1":#for the first part of the question: finds the alignment of the sequences according to the path string
        print "Path:",'\n'
        print x
        print '\n'
    seq1=""
    seq2=""
    j=0
    k=0
    for i in range(len(x)):
        if x[i]=="D":
            seq1+=first[j]
            seq2+=second[k]
            j+=1
            k+=1
        elif x[i]=="H":
            seq1+=first[j]
            seq2+="_"
            j+=1
        elif x[i]=="V":
            seq1+="_"
            seq2+=second[k]
            k+=1
        
    if choice=="1":
        print "Pairwise Alignment:",'\n'
        print seq1
        print seq2

    if choice=="2":
        count=countIdentites(seq1,seq2)#for the second part of the question: sends the sequences of the alignment to another function to count the identites
        return count
            
            
#=================================================================================================================================================================#   
        
def countIdentites(seq1,seq2):#count the identities of the sequences (for the second part of the question)
    count=0
    for (c1,c2) in zip(seq1,seq2):
        if c1==c2:
            count+=1       
    return count
        
#==================================================================================================================================================================#        

def fillMatrix(alignment,pointers,match,mismatch,gap,seq,choice):#fills the alignment matrix and the pointers matrix
    flag=int(gap)
    for j in range(len(seq[0])):#fill the firs row with gaps
        alignment[1][j+2]=flag
        pointers[1][j+2]="H"
        flag+=int(gap)
    flag=int(gap)
    for i in range(len(seq[1])):#fill the first column with gaps
        alignment[i+2][1]=flag
        pointers[i+2][1]="V"
        flag+=int(gap)

    
          
    for i in range(len(seq[1])):
        for j in range(len(seq[0])):
            dictionary={}#fills the dictionary with the values of "H", "D" and "V" for the next spot in the matrix
            H=alignment[i+2][j+1]+int(gap)
            dictionary["H"]=(int(H))
            V=alignment[i+1][j+2]+int(gap)
            if (alignment[i+2][0]==alignment[0][j+2]):
                D=int(alignment[i+1][j+1])+int(match)
                dictionary["D"]=(int(D))
            else:
                 D=int(alignment[i+1][j+1])+int(mismatch)
                 dictionary["D"]=(int(D))
            dictionary["V"]=(int(V))
            maxi=max(dictionary, key=dictionary.get)#find the maximum value for the next spot in the matrix 
            pointers[i+2][j+2]=maxi#fills the pointers matrix with the right letter ("H","D" or  "V") according to the highset value
            alignment[i+2][j+2]=int(alignment[i+2][j+2])+dictionary[maxi]#fills the alignment matrix with the highest value
                        
            
            
    if choice=="1":#for the first part of the question: will print the matrixes
       matrix=[[0 for x in range(1+len(seq[0]))] for x in range(1+len(seq[1]))]
       print '\n'
    
       for i in range(1+len(seq[1])):
           for j in range(1+len(seq[0])):
               matrix[i][j]=alignment[i+1][j+1]
            

       alignment[0][0] =" "
       pointers[0][0] =" "
       print "Alignment Matrix:",'\n'
       for j in range(2+len(seq[0])):
                print '{:4}'.format(alignment[0][j]),     
       print '\n'
    
       for i in range(1+len(seq[1])):
           print alignment[i+1][0],
           for j in range(1+len(seq[0])):
               print '{:4}'.format(matrix[i][j]),
           print '\n'
       print '\n'

       print "Pointers Matrix:",'\n'
       for i in range(2+len(seq[1])):
           for j in range(2+len(seq[0])):
               print pointers[i][j]," ",
           print '\n'
    i=1+len(seq[1])
    j=1+len(seq[0])
    x=""
    x=path(pointers,i,j,x)#function to find the path of the alignment
    x=x[::-1]#reverse the path
    first= seq[0]
    second=seq[1]
    if choice=="1":
        finalAlignment(x,first,second,choice)
    if choice=="2":#for the second part of the question: send the sequence to function to count the identites
        count=finalAlignment(x,first,second,choice)
        return count
    
            

    
    
#==================================================================================================================================================================#    
    
    

def addSeqData(alignment,seq):#first step of building the matrix: inserts the sequences to the matrix 
    row="0"+seq[0]
    column="0"+seq[1]
    for i in range(len(seq[0])+1):
        alignment[0][i+1]=row[i]
    for i in range(len(seq[1])+1):
        alignment[i+1][0]=column[i]
    return alignment
#====================================================================================================================================================================#    
        
def buildMatrix(seq):#finds the size of the matrixes according to the size of the sequences
    alignment=[[0 for x in range(2+len(seq[0]))] for x in range(2+len(seq[1]))]
    pointers=[[0 for x in range(2+len(seq[0]))] for x in range(2+len(seq[1]))]
    alignment=addSeqData(alignment,seq)
    pointers=addSeqData(pointers,seq)
    return alignment,pointers
    
#===================================================================================================================================================================#
   
def randomDNA():#for the second part of the question: find a random DNA in length of 100 bases
    seq=[]
    for i in range(2):
        sequence=""
        for j in range(100):
            nucleotide=random.choice("ATGC")
            sequence+=nucleotide
        seq.append(sequence)
    return seq 
#===================================================================================================================================================================#            
def randomProtein():#for the first part of the question: find a random DNA in length of 100 bases
    seq=[]
    aalist=['M', 'T', 'Q', 'A', 'P', 'F', 'L', 'S', 'V', 'E', 'G', 'H', 'I', 'W', 'R', 'D', 'K', 'N', 'Y', 'C']

    for i in range(2):
        sequence=""
        for j in range(100):
            nucleotide=random.choice(aalist)
            sequence+=nucleotide
        seq.append(sequence)
    return seq 
    
#====================================================================================================================================================================#    

#main program
choice=raw_input("choose the part of the question: ")

if choice=='1':#first part of the question
    file=raw_input("Enter Filename: ")
    data=open(file,'r')
    name,seq=extractInformation(data)
    match = raw_input("Please enter a match value:") or 1
    mismatch=raw_input("Please enter a mismatch value:") or -1
    gap=raw_input("Please enter a gap value:") or -1
    alignment,pointers=buildMatrix(seq)
    fillMatrix(alignment,pointers,match,mismatch,gap,seq,choice)

elif choice=='2':#second part of the question
    match=1
    mismatch=0
    gap=0
    amount=0
    for i in range(50):#DNA with gaps
        seq=randomDNA()
        alignment,pointers=buildMatrix(seq)
        count=fillMatrix(alignment,pointers,match,mismatch,gap,seq,choice)
        amount+=count
    average1="{0:.2f}".format(amount/50)

    amount=0
    for i in range(50):#DNA without gaps
        seq=randomDNA()
        count=countIdentites(seq[0],seq[1])
        amount+=count
    average2=("{0:.2f}".format(amount/50))

    amount=0
    for i in range(50):#protein with gaps
        seq=randomProtein()
        alignment,pointers=buildMatrix(seq)
        count=fillMatrix(alignment,pointers,match,mismatch,gap,seq,choice)
        amount+=count
    average3="{0:.2f}".format(amount/50)

    amount=0
    for i in range(50):#protein without gaps
        seq=randomProtein()
        count=countIdentites(seq[0],seq[1])
        amount+=count
    average4=("{0:.2f}".format(amount/50))

    print '\n'
    print "Average of random 50 sequences in length 100:"
    print"             with gaps               without gaps"
    print "DNA           ",average1,"                ",average2
    print "Protein        ",average3,"               ",average4

    

   
else:
    print "ERROR",'\n'






