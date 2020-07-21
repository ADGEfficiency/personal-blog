from sklearn.feature_extraction.text import TfidfVectorizer

from pathlib import Path

p = Path.home() / 'git' / 'personal' 

# text_files = [
#     '/Users/adam/git/personal/projects/principles/0-foundation/acceptance.md'
# ]

text_files = p.glob('**/*.md')

documents = [open(f).read() for f in text_files]
tfidf = TfidfVectorizer().fit_transform(documents)
# no need to normalize, since Vectorizer will return normalized tf-idf
pairwise_similarity = tfidf * tfidf.T
print(pairwise_similarity)

pairwise_similarity = pairwise_similarity.toarray()
import numpy as np
arr = pairwise_similarity
np.fill_diagonal(arr, np.nan)

input_idx = np.random.randint(0, arr.shape[0], size=1)[0]
result_idx = np.nanargmax(arr[input_idx])
print('FIRST')
print(documents[input_idx])
print('SECOND')
print(documents[result_idx])
