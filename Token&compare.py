#!/usr/bin/env python
# coding: utf-8

# In[6]:


import re

# Input paragraph
text = "Natural Language Processing is exciting. It helps computers understand human language. However, it's not always easy!"

# 1. Naïve space-based tokenization
naive_tokens = text.split()

print("Naïve Space-Based Tokens:")
print(naive_tokens)

# 2. Manually corrected tokenization
# - separates punctuation
# - splits clitics like "it's" -> "it", "'s"
corrected_tokens = re.findall(r"\b\w+\b|[.,!?]|'s", text)

print("\nManually Corrected Tokens:")
print(corrected_tokens)

# 3. Highlight differences
print("\nDifferences:")
for token in naive_tokens:
    if token not in corrected_tokens:
        print(f"Naïve token '{token}' was corrected")


# In[7]:


import re
import nltk
from nltk.tokenize import word_tokenize

# Download tokenizer data (run once)
nltk.download('punkt')

# Input paragraph
text = "Natural Language Processing is exciting. It helps computers understand human language. However, it's not always easy!"

# 1. Manual tokenization (corrected)
manual_tokens = re.findall(r"\b\w+\b|[.,!?]|'s", text)

print("Manual Tokens:")
print(manual_tokens)

# 2. NLTK tokenization
tool_tokens = word_tokenize(text)

print("\nNLTK Tokens:")
print(tool_tokens)

# 3. Compare differences
manual_only = set(manual_tokens) - set(tool_tokens)
tool_only = set(tool_tokens) - set(manual_tokens)

print("\nTokens only in Manual Tokenization:")
print(manual_only)

print("\nTokens only in NLTK Tokenization:")
print(tool_only)


# In[ ]:




