## Name
## Date
## Day 34: Intro to GitHub

''' 
---QUESTIONS---
1. What branch do you start on? How do you know?

2. Create a new branch called "feature". What command do you use to do this?
How do you know it worked? Can you see the branch online on GitHub yet?

3. Switch to the feature branch and work on this assignment. What command do
you use to do this? How do you know it worked? 

4. Start working on today's programming assignment. Every time you make a 
meaningful change, commit that change with a useful commit message. What
command do you use to commit with a message? Can you see your commits online
on GitHub yet?

5. Now try to add and push your commits. You should get an error message.
Copy/paste the error message (or specific pieces you don't quite understand)
into a search engine. Did you find any helpful explanations for the error 
message? (I recommend looking for highly upvoted responses on StackOverflow)
What does the error message mean? What should you do to push your work to GitHub?

6. After committing and pushing your work, log back into GitHub on your browser. Do
you see your commits? Can you see the history of your edits?

7. Finally, merge the work from your branch 'feature' into the branch 'master'. What
command do you use to do this? (Hint: switch to the master branch, then type 
git merge feature, before pushing your changes) What changes when you look at your 
work online on GitHub?
'''

def readFASTA(filePath):
    '''Given the path to a FASTA file, returns....
    TODO: Complete this docstring once you decide what to return
    '''
    
    # this is a placeholder, replace this with your answer
    return []

def GCcontent(nucSeq):
    '''Returns (as a float) the percentage GC content 
    of a given nucleotide sequence.

    nucSeq: str of A,T,C,G character
    '''
    pass

def main(filePath):
    '''Use the helper functions readFASTA and GCcontent
    to read in a FASTA file and print out each gene name
    and its GC content in this format:
    
    Gene Name 1: 68%
    Gene Name 2: 43%
    ...
    Gene Name N: 52%
    '''
    pass

if __name__ == '__main__':
    # call helper functions to print your answer

    # use this example code to learn how to read in files
    # Delete this once you understand how to read in files
    f = open('sample_fasta.txt','r')
    flines = f.readlines()
    lineNum = 0
    for line in flines:
        lineNum += 1
        print('this is line: '+ str(lineNum))
        print(line)