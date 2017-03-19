import re

f1 = open("in.txt", 'r', encoding='utf-8')

max_sentences = ['', '', '']

for line in f1:
    line_sentences = re.findall(r'[^\.\!\?]+[\.\!\?]', line)
    for one_line_sentence in line_sentences:
        if len(one_line_sentence.split()) > len(max_sentences[2].split()):
            max_sentences[2] = one_line_sentence
            max_sentences.sort(key=lambda one_sentence: len(one_sentence.split()), reverse=True)

print(max_sentences[0], end='\n\n')
print(max_sentences[1], end='\n\n')
print(max_sentences[2])
