import re

f1 = open("in.txt", 'r', encoding='utf-8')

wc = 0  # word count
sc = 0  # sentence count

for line in f1:
    sentences = re.findall(r'[^\.\!\?]+[\.\!\?]', line)
    sc += len(sentences)
    for one_sentence in sentences:
        wc += len(one_sentence.split())

print(wc / sc)
