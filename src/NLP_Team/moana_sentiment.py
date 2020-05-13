import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
from random import *
import seaborn
seaborn.set_style("darkgrid")
import pprint
pp = pprint.PrettyPrinter(indent=4)
import indicoio

indicoio.config.api_key = '03701901ee9d3c26d414eabe7ad995e1'

#Functions for parsing the script

def sample_window(seq, window_size=20, stride=1):
    for pos in range(0, len(seq), stride):
        yield seq[pos : pos + window_size]

def merge(seq, stride=4):
    for pos in range(0, len(seq), stride):
        yield seq[pos : pos + stride]


# generating hex val

def hex_generate():
    n = ['0','1','2','3','4','5','6','7','8','9','A','B','C', 'D', 'E','F']
    val = '#'
    for i in range(0, 6, 1):
        x = randint(0, 15)
        val = val + n[x]
    return val

# use one txt file to test

corpus = [
"moana.txt"
]


d={}

root_fp = os.getcwd()
corpus_fp = os.path.join(root_fp, "NDL-Disney-Movie-Tool/NLP_Team")


for text in corpus:
    fp = os.path.join(corpus_fp, text)
    print("Reading '%s'"%text)
    with open(fp, 'r', encoding="utf8") as f:
        text_name = text.split(".")[0]
        sample_col = text_name + "_sample"
        score_col = text_name + "_sentiment"
        lines = []

        for line in f:
            if str(line) == str(""):
                continue
            else:
                line = line.replace("\n", "").lower().strip().strip('*')
                lines.append(line)
        print(" %i lines read from '%s' with size: %5.2f kb" %(len(lines), text, sys.getsizeof(lines)/1024))

        text = " ".join(line for line in lines)

        delim = ". "
        sentences = [_+delim for _ in text.split(delim)]
        merged_sentences = [delim.join(s) for s in merge(sentences, 10)]

        delim = " "
        words = [_ for _ in text.split()]
        merged_words = [" ".join(w) for w in merge(words, 120)]

        delim = " "
        samples = [delim.join(s) for s in sample_window(merged_words, 10, 1)]
        d[sample_col] = samples

        print(" submitting %i sample for '%s'" %(len(samples), text_name))

        scores = indicoio.sentiment(samples)
        d[score_col] = scores

print("\n...complete!")

df = pd.DataFrame()
for k, v in sorted(d.items()):
    df[k] = pd.Series(v)

#draw sentiment graph

for text in corpus:
    text_name = text.split(".")[0]
    text_name = text_name + "_sentiment"
    file_name = text_name + ".png"

    ax = df[text_name].plot(colormap='jet', figsize=(16,8))
    ax.set_xlabel("Sample")
    ax.set_ylabel("Sentiment Score")
    ax.set_title(text_name)
    plt.savefig(file_name)
    plt.close()


for text in corpus:
    text_name = text.split(".")[0]
    text_name = text_name + "_sentiment"
    clr = hex_generate()

    ax = df[text_name].plot(figsize=(16,8), color=clr)
    ax.set_xlabel("Sample")
    ax.set_ylabel("Sentiment Score")
    ax.set_title("Moana")
plt.savefig('overlay.png')
plt.close()