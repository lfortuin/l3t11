import spacy

nlp = spacy.load('en_core_web_sm')

gardenpathSentences = [
    'Mary gave the child the dog bit a Band-Aid.',
    'The horse raced past the barn fell.',
    'The old man the boat.',
    'The cotton clothing is made of grows in Mississippi.',
    'I told the girl the cat scratched Bill would help her.'
]

for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print([token.text for token in doc])
    if doc.ents:
        print([(i, i.label_, i.label) for i in doc.ents])
    else: 
        print('No named entities found')

print(spacy.explain('GPE'))
print(spacy.explain('PERSON'))

#Entity - GPE
#Explanation - Countries, cities, states
#The entity made sense in terms of the word associated with it

#Entity - PERSON
#Explanation - People, including fictional
#The entity made sense in terms of the word associated with it