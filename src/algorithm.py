import pandas as pd

import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

# Function to preprocess text
def preprocess(text):
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalnum()]
    tokens = [token for token in tokens if token not in stop_words]
    return tokens

# Function to get word embeddings
def get_sentence_embedding(sentence):
    tokens = preprocess(sentence)
    word_embeddings = model.encode(sentence, convert_to_tensor=True, show_progress_bar=False).numpy().tolist()
    
    return word_embeddings

# Function to calculate cosine similarity
# Function to calculate cosine similarity
def cosine_sim(text1, text2):
    embedding1 = get_sentence_embedding(text1)
    embedding2 = get_sentence_embedding(text2)

    if embedding1 == [] or embedding2 == []:
        return 0.0

    similarity_score = cosine_similarity([embedding1], [embedding2])[0][0]
    return similarity_score

# Function to calculate Jaccard similarity
def jaccard_sim(text1, text2):
    # Tokenize the texts
    tokens1 = set(word_tokenize(text1.lower()))
    tokens2 = set(word_tokenize(text2.lower()))

    # Compute Jaccard similarity
    intersection = len(tokens1.intersection(tokens2))
    union = len(tokens1.union(tokens2))
    
    if union == 0:
        return 0.0  # Return 0 if union is zero to avoid division by zero
    
    return intersection / union