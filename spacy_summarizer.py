!pip install spacy


import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

stopwords = list(STOP_WORDS)

#print(stopwords)

with open('nlp_wiki.txt', 'r') as f:
    text = f.read()
    
#print(text)
nlp = spacy.load('en_core_web_sm')

doc = nlp(text)

#print(stopwords)


tokens = [token.text for token in doc]
#print(tokens)

#print(punctuation)


word_frequencies = {}
for word in doc:
    if word.text.lower() not in punctuation:
        if word.text.lower() not in stopwords:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text]+= 1
                
print(word_frequencies)
most_used = max(word_frequencies.values())
print(most_used)


sentence_tokens = [sent for sent in doc.sents]

print(len(sentence_tokens))


for word in word_frequencies.keys():
    word_frequencies[word] = word_frequencies[word] / most_used

print(word_frequencies)


sentence_scores= {
}

for sent in sentence_tokens:
    for word in sent:
        if word.text.lower() in word_frequencies.keys():
            if sent not in sentence_scores.keys():
                sentence_scores[sent] = word_frequencies[word.text.lower()]
            else:
                sentence_scores[sent] += word_frequencies[word.text.lower()]
            
print(sentence_scores)


from heapq import nlargest

select_length = int(len(sentence_tokens)*0.1)

summary = nlargest(select_length, sentence_scores, key = sentence_scores.get)

final_summary = [word.text for word in summary]
summary = ''.join(final_summary)

print(summary)
