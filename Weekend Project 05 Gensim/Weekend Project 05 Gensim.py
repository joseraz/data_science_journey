
# Import the modules
from gensim.summarization.summarizer import summarize
from gensim import keywords
import wikipedia

#pull in the document
text = wikipedia.summary("Intel")

# remove some newlines and whitespace for pretty strings

data = '' 
for i in text.splitlines():
    data += i.strip()
print(data)

#summarize the data
summary = summarize(data)
print(summary)

# Identify keywords
words = keywords(data, words = 3)
print(words)