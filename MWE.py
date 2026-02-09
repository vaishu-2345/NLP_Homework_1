#!/usr/bin/env python
# coding: utf-8

# In[9]:


# English sentence
text = "I live in New York and even in spite of the rain, he kicked the bucket."

# List of MWEs (Multiword Expressions)
mwes = [
    "New York",
    "in spite of",
    "kick the bucket"
]

# Replace MWEs with underscore-joined versions
processed_text = text
for mwe in mwes:
    processed_text = processed_text.replace(mwe, mwe.replace(" ", "_"))

# Remove punctuation to make tokenization clean (optional)
processed_text = processed_text.replace(".", "").replace(",", "")

# Space-based tokenization
tokens = processed_text.split()

print("Processed Text:")
print(processed_text)

print("\nFinal Tokens (MWEs as single tokens):")
print(tokens)


# In[ ]:




