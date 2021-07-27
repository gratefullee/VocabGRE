import fitz # pip install PyMuPDF==1.18.15
import numpy as np
import os

os.system('clear')

# Convert PDF to String
with fitz.open("manhattan1000.pdf") as doc:
    text = ""
    for page in doc:
        text += page.getText()
        
# Separate the string to words and meanings.
index = 1
words = []
meanings = []

# Words
for t in text.splitlines():
    if str(index)+'. ' in t:
        words.append(t.replace(str(index)+'. ', ''))
        index += 1


# Meanings 
meaning = ''
for t in text.splitlines():
    if t[0].isdigit() == False:
        meaning += t+' '
    else:
        meanings.append(meaning[:-1])
        meaning =''

meanings.append(text.splitlines()[-1])
meanings = meanings[1:]

# Lists to a dictionary 
vocab = {}
for i,v in zip(words,meanings):
    vocab[i] = v
    

first = int(input('Input the index of the first word. (1-995): '))-1
last = int(input('Input the index of the last word. (1-995). This number should be larger than the previous number: '))-1
learn_quiz = int(input('Input 1 for learning, 2 for spelling test: '))

# Lists to a dictionary
vocab = {}
for i,v in zip(words[first:last+1],meanings[first:last+1]):
    vocab[i] = v

def OneByOne():
    global vocab
    if learn_quiz == 1:
        shuffle = int(input('Input 1 for shuffle, 2 for no shuffle: '))
        if shuffle == 2:
            index =1
            for i,v in vocab.items():
                print ('\n'+str(index) +' out of '+ str(last-first+1)) 
                print (i+': '+v)
                next = int(input('\n'+'Input any letter for the next word: '))
                index += 1
            print('Great work!')
        elif shuffle == 1:
            index = 1
            d_set = list(set(vocab))
            vocab = {i:vocab[i] for i in d_set}
            for i,v in vocab.items():
                print ('\n'+str(index) +' out of '+ str(last-first+1)) 
                print (i+': '+v)
                next = int(input('\n'+'Input any letter for the next word: '))
                index += 1
            print('Great work!')
        else:
            OneByOne()
    elif learn_quiz == 2:
        index = 1
        d_set = list(set(vocab))
        vocab = {i:vocab[i] for i in d_set}
        while len(vocab.keys()) > 0 :
            for i,v in list(vocab.items()):
                print (str(len(vocab.keys())) +' words left \n')
                answer = str(input(v + ': '))
                if answer == i:
                    del vocab[i]
                else:
                    print ('Answer: '+i)

        print ("Great job!")
        
        
        
        
    else:
        OneByOne()

        
        
if __name__ == "__main__":
     print (OneByOne())