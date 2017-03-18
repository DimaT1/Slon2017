import re

f1 = open("in.txt", 'r', encoding='utf-8')

sentences = []

for line in f1:
    sentences += re.findall(r'[^\.\!\?]+[\.\!\?]', line)

sentences.sort(key=lambda one_sentence: len(one_sentence.split()), reverse=True)
print(sentences[0])
print()
print(sentences[1])
print()
print(sentences[2])
