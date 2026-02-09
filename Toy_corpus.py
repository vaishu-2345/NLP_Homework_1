#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import defaultdict

# Toy corpus
corpus = [
    "low", "low", "low", "low", "low",
    "lowest", "lowest",
    "newer", "newer", "newer", "newer", "newer", "newer",
    "wider", "wider", "wider",
    "new", "new"
]

# Add end-of-word marker and split into characters
def prepare_corpus(corpus):
    return [" ".join(list(word) + ["_"]) for word in corpus]

corpus = prepare_corpus(corpus)

def get_bigram_counts(corpus):
    counts = defaultdict(int)
    for word in corpus:
        symbols = word.split()
        for i in range(len(symbols) - 1):
            counts[(symbols[i], symbols[i+1])] += 1
    return counts

def merge_pair(pair, corpus):
    merged = " ".join(pair)
    replacement = "".join(pair)
    new_corpus = []
    for word in corpus:
        new_word = word.replace(merged, replacement)
        new_corpus.append(new_word)
    return new_corpus

# Run BPE for a few steps
num_merges = 10
vocab = set()

print("Learning BPE merges:\n")

for step in range(1, num_merges + 1):
    bigram_counts = get_bigram_counts(corpus)
    if not bigram_counts:
        break
    top_pair = max(bigram_counts, key=bigram_counts.get)
    corpus = merge_pair(top_pair, corpus)

    # Update vocabulary
    for word in corpus:
        vocab.update(word.split())

    print(f"Step {step}: Top pair = {top_pair}, Vocabulary size = {len(vocab)}")

print("\nFinal Vocabulary:")
print(vocab)


# In[2]:


def segment_word(word, vocab):
    symbols = list(word) + ["_"]
    word = "".join(symbols)

    tokens = []
    i = 0
    while i < len(word):
        match = None
        for j in range(len(word), i, -1):
            sub = word[i:j]
            if sub in vocab:
                match = sub
                break
        if match:
            tokens.append(match)
            i += len(match)
        else:
            tokens.append(word[i])
            i += 1
    return tokens

words = ["new", "newer", "lowest", "widest", "newestest"]

print("\nWord Segmentations:\n")
for w in words:
    print(w, "→", segment_word(w, vocab))


# In[ ]:




