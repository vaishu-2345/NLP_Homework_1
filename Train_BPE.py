#!/usr/bin/env python
# coding: utf-8

# In[4]:


from collections import defaultdict

# Paragraph
text = """
Natural language processing is an important area of artificial intelligence.
It helps computers understand human language.
Tokenization and subword modeling improve performance on rare words.
Learning meaningful representations is essential for modern NLP systems.
Subword methods reduce vocabulary size and handle unseen words.
"""

# Prepare corpus
words = text.lower().replace(".", "").split()

def prepare(words):
    return [" ".join(list(w) + ["_"]) for w in words]

corpus = prepare(words)

def get_bigram_counts(corpus):
    counts = defaultdict(int)
    for w in corpus:
        s = w.split()
        for i in range(len(s) - 1):
            counts[(s[i], s[i+1])] += 1
    return counts

def merge(pair, corpus):
    old = " ".join(pair)
    new = "".join(pair)
    return [w.replace(old, new) for w in corpus]

merges = []
vocab = set()

for i in range(30):
    counts = get_bigram_counts(corpus)
    if not counts:
        break
    best = max(counts, key=counts.get)
    merges.append((best, counts[best]))
    corpus = merge(best, corpus)

    for w in corpus:
        vocab.update(w.split())

print("Top 5 merges:")
for m in merges[:5]:
    print(m)

longest_tokens = sorted(vocab, key=len, reverse=True)[:5]
print("\nFive longest subword tokens:")
print(longest_tokens)


# In[5]:


def segment(word, vocab):
    word = word + "_"
    tokens = []
    i = 0
    while i < len(word):
        match = None
        for j in range(len(word), i, -1):
            if word[i:j] in vocab:
                match = word[i:j]
                break
        if match:
            tokens.append(match)
            i += len(match)
        else:
            tokens.append(word[i])
            i += 1
    return tokens

test_words = [
    "language",      # common
    "tokenization",  # derived
    "unseen",        # rare
    "processing",    # frequent
    "representations" # long/complex
]

for w in test_words:
    print(w, "→", segment(w, vocab))


# In[ ]:




