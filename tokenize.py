import spacy
import json
import sys
nlp = spacy.load('de_core_news_sm')
file_name = sys.argv[1]
file_text = open(file_name).read()
file_doc = nlp(file_text)
for token in file_doc:
    print ('Processing tokens.....')
    f = open('output_tokens.txt', 'a')
    print (token, token.idx, file=f)
    f.close()