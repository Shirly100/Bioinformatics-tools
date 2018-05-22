# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 00:24:32 2018

@author: Shirly
"""
#Shirly Ohanona 314793910
'''
The script creates a class "seq" for a protein sequence (string of amino acids). 
The class seq have three methods: 
1. "pI" – returns the pI of the protein.
2. "mass" - returns the molecular mass (using the package Bio).
3. "numRes" - returns the number of residues.

'''
from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis









class seq():
    
    def __init__(self,seq,try_PH):
        #ProteinAnalysis.__init__(self,seq)
        self.PH=try_PH
        self.sequence=seq
        self.charges = {'D':-1, 'E':-1, 'H':1, 'C':-1, 'Y':-1, 'K':1, 'R':1, 'N-ter':1, 'C-ter':-1}#The charges of ionic amino acids
        self.pKa = {'C': 9.0,'D': 4.05,'E': 4.45,'H': 5.98,'K': 10.0,'R': 12.0,'Y': 10.0,'N-ter': 7.5,'C-ter': 3.55}#The pka of the ionic amino acids
        #self.weights = {'A': 89, 'C': 121, 'D': 133, 'E': 147, 'F': 165,'G': 75, 'H': 155, 'I': 131, 'K': 146, 'L': 131,'M': 149, 'N': 132, 'P': 115, 'Q': 146, 'R': 174,'S': 105, 'T': 119, 'V': 117, 'W': 204, 'Y': 181 }
    def pI(self):#returns the pI of the protein.
        total_charge=self.aa_charge('N-ter')
        total_charge+=self.aa_charge('C-ter')
               
        for aAcid in self.pKa:
            total_charge+=self.sequence.count(aAcid)*self.aa_charge(aAcid)
            
        return total_charge
        
    def aa_charge(self,aAcid):#calculate the charge of a single amino acid
        if(self.charges[aAcid]==1):
            charge= 1 / (1 + 10**(self.PH - self.pKa[aAcid]))
        else:
            charge= -1 / (1 + 10**(self.pKa[aAcid]-self.PH))
        return charge
    
    def mass(self):#returns the molecular mass (using the package Bio).
        
        analysed_seq = ProteinAnalysis(self.sequence)
        weight=analysed_seq.molecular_weight()
        #weight=self.molecular_weight()
        return weight
    
    def numRes(self):# returns the number of residues.
        count=0
        for aa in sequence:
            count+=1
        return count
            
        


proteins={}

if __name__ == "__main__":
    fasta_sequences = SeqIO.parse(open("protSeq.txt"),'fasta')
    for fasta in fasta_sequences:
        name, sequence = fasta.id, str(fasta.seq)
        proteins[name]=sequence
    
               
    for k in proteins:#gets the pI for each sequence
        sequence= proteins[k]
        min_pH = 0
        max_pH=14
        try_PH=0.5 * (max_pH + min_pH)
        flag=True
        while(flag==True ):#will try different values of PH until it will find the right PI
            result=seq(sequence,try_PH)
            charge=result.pI()
            if(charge>0.001):
                flag=True
                min_pH = try_PH
                try_PH=0.5 * (max_pH + min_pH)
                
            elif(charge<-0.001):
                flag=True
                max_pH = try_PH
                try_PH=0.5 * (max_pH + min_pH)
            else:
                flag=False
        print("The protein: "+k+" The PI: "+str("{0:.2f}".format(try_PH)))
     
    print()
    for k in proteins:#gets the molecular weight for each sequence
        sequence= proteins[k]
        result=seq(sequence,0)
        mw=result.mass()
        print("The mass of the protein "+k+" is: "+str("{0:.2f}".format(mw))+" Daltons" )
    
    print()    
    for k in proteins:#gets the number of residues for each sequence
        sequence= proteins[k]
        result=seq(sequence,0)
        count=result.numRes()
        print("The number of residues in protein "+k+" is: "+str(count) )

     


    
             
        
