import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn


phrase1 = input("Give me the first phrase.")
phrase2 = input("Give me the second phrase.")

phrase1 = word_tokenize(phrase1)
phrase2 = word_tokenize(phrase2)


frash1 = []
frash2 = []


plithos1 = nltk.pos_tag(phrase1)
plithos2 = nltk.pos_tag(phrase2)

verbs = []
nouns = []
adj = []
asc = []

for i in plithos1:
    if(i[1].startswith('VB') or i[1].startswith('VBD') or i[1].startswith('VBG') or i[1].startswith('VBN') or i[1].startswith('VBP') or i[1].startswith('VBZ')):
        frash1.append(i[0])
        verbs.append(i)

for i in plithos2:
    if(i[1].startswith('VB') or i[1].startswith('VBD') or i[1].startswith('VBG') or i[1].startswith('VBN') or i[1].startswith('VBP') or i[1].startswith('VBZ')):
        frash2.append(i[0])
        verbs.append(i)

for i in plithos1:
    if(i[1].startswith('JJ') or i[1].startswith('JJR') or i[1].startswith('JJS')):
        frash1.append(i[0])
        adj.append(i)
        asc.append(wn.synset(i))

for i in plithos2:
    if(i[1].startswith('JJ') or i[1].startswith('JJR') or i[1].startswith('JJS')):
        frash2.append(i[0])
        adj.append(i)

for i in plithos1:
    if(i[1].startswith('NN') or i[1].startswith('NNS') or i[1].startswith('NNP') or i[1].startswith('NNPS')):
        frash1.append(i[0])
        nouns.append(i)

for i in plithos2:
    if(i[1].startswith('NN') or i[1].startswith('NNS') or i[1].startswith('NNP') or i[1].startswith('NNPS')):
        frash2.append(i[0])
        nouns.append(i)


print (frash1)
print (frash2)


print (verbs)
print (nouns)
print (adj)
print (asc)
        
            
            





        
           

        









