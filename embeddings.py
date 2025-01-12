# -*- coding: utf-8 -*-
"""HW3: Embeddings.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iNwhIEK52Sye_gAHMI9TDajOhQS8h72E

# Data Prep

Data Loading
"""

import os

directory_path = '/content/drive/MyDrive/emb_data '

documents = []
file_names = []

for filename in os.listdir(directory_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(directory_path, filename)

        with open(file_path, 'r', encoding = 'utf-8', errors = 'ignore') as file:

            documents.append(file.read())
            file_names.append(filename)

print(f"Number of documents: {len(documents)}")
print(f"Number of file names: {len(file_names)}")

import pandas as pd
df = pd.DataFrame({'file_name': file_names,'content': documents})
df.head()

df.shape

"""Data preprocessing"""

import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def pre_processing(text):
  #convert to lower case
  text = text.lower()
  #remove punctuations and non-alphabatic characters
  text = re.sub(r'[^a-z\s]', '', text)
  #tokenize the texts
  tokens = word_tokenize(text)
  #remove stopwords
  tokens = [word  for word in tokens if word not in stop_words]
  #lemmatize the words
  tokens = [lemmatizer.lemmatize(word) for word in tokens]

  return ' '.join(tokens)

df['processed_content'] = df['content'].apply(pre_processing)

# Clean up the text by removing the "title" prefix
df['processed_content'] = df['processed_content'].str.replace(r'^\s*title\s+', '', regex=True)
df['processed_content'] = df['processed_content'].str.strip()
df['processed_content'].head()

"""# 1)Embeddings using tf-idf and k-means clustering algorithm"""

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
import gensim.downloader as api
from transformers import BertTokenizer, BertModel, GPT2Tokenizer, GPT2Model, pipeline
import torch

# Term Frequency-Inverse Document Frequency (TF-IDF)
vectorizer_tfidf = TfidfVectorizer()
X_tfidf = vectorizer_tfidf.fit_transform(df['processed_content'])
tfidf_df = pd.DataFrame(X_tfidf.toarray(), columns=vectorizer_tfidf.get_feature_names_out())
tfidf_df.head()
#print("TF-IDF Embedding:\n", X_tfidf.toarray())

"""K-means clustering"""

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Number of clusters (you can adjust this based on your data)
n_clusters = 5

# Apply KMeans clustering
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(tfidf_df)

# Add cluster labels to the DataFrame
tfidf_df['cluster'] = kmeans.labels_

# Check the DataFrame with clusters
tfidf_df.head()

"""Evaluation using silhouette score"""

from sklearn.metrics import silhouette_score

scores = []
cluster_range = range(2, 10)  # Adjust the range as needed

for n_clusters in cluster_range:
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(tfidf_df.drop('cluster', axis=1))
    score = silhouette_score(tfidf_df.drop('cluster', axis=1), kmeans.labels_)
    scores.append(score)
    print(f'Silhouette Score for {n_clusters} clusters: {score}')

# Reduce dimensions using PCA to visualize clusters
pca = PCA(n_components=2)
pca_result = pca.fit_transform(tfidf_df.iloc[:, :-1])  # Exclude the 'cluster' column

# Plot the clusters
plt.figure(figsize=(10, 7))
plt.scatter(pca_result[:, 0], pca_result[:, 1], c=kmeans.labels_, cmap='viridis', marker='o')
plt.title("KMeans Clustering of TF-IDF Features")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.colorbar(label='Cluster')
plt.show()





"""# 2)Embeddings using sentence bert and k-means clustering algorithm"""

!pip install sentence_transformers

import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np

"""Embeddings using sentence bert"""

# Load SBERT model (BERT-based)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate embeddings for each document in the processed_content column
embeddings = model.encode(df['processed_content'].tolist())

# Convert embeddings into a DataFrame for clustering
embeddings_df = pd.DataFrame(embeddings)

"""K-means clustering"""

# Apply KMeans clustering
n_clusters = 5
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(embeddings_df)

# Add cluster labels to the embeddings DataFrame
embeddings_df['cluster'] = kmeans.labels_

# Create a new DataFrame with file number (or document index) and cluster label
output_df = pd.DataFrame({
    'filename': df.index,  # Assuming you want the index as filename
    'cluster': kmeans.labels_
})

"""evaluation using silhouette"""

# Calculate metrics for each cluster
cluster_metrics = []
for cluster in range(n_clusters):
    cluster_data = embeddings_df[embeddings_df['cluster'] == cluster]

    # Count number of documents in the cluster
    num_documents = cluster_data.shape[0]

    # Calculate the Silhouette Score for the cluster
    if num_documents > 1:  # Silhouette Score is undefined for 1 or fewer points
        cluster_silhouette_score = silhouette_score(embeddings_df.drop('cluster', axis=1), kmeans.labels_, sample_size=num_documents)
    else:
        cluster_silhouette_score = np.nan  # Undefined for single document clusters

    cluster_metrics.append({
        'cluster': cluster,
        'num_documents': num_documents,
        'silhouette_score': cluster_silhouette_score
    })

# Convert to DataFrame for better readability
cluster_metrics_df = pd.DataFrame(cluster_metrics)

# Display metrics for each cluster
cluster_metrics_df

# Save the new DataFrame to a CSV file
output_df.to_csv('clustered_documents_sbert.csv', index=False)

"""Plots for visualization"""

import matplotlib.pyplot as plt
# Plot number of documents per cluster
plt.figure(figsize=(10, 5))
plt.bar(cluster_metrics_df['cluster'], cluster_metrics_df['num_documents'], color='skyblue')
plt.title('Number of Documents per Cluster')
plt.xlabel('Cluster')
plt.ylabel('Number of Documents')
plt.xticks(cluster_metrics_df['cluster'])
plt.show()

# Plot Silhouette Score per cluster
plt.figure(figsize=(10, 5))
plt.bar(cluster_metrics_df['cluster'], cluster_metrics_df['silhouette_score'], color='lightgreen')
plt.title('Silhouette Score per Cluster')
plt.xlabel('Cluster')
plt.ylabel('Silhouette Score')
plt.xticks(cluster_metrics_df['cluster'])
plt.show()

from sklearn.decomposition import PCA
# Reduce embeddings to 2 dimensions for visualization using PCA
pca = PCA(n_components=2)
pca_embeddings = pca.fit_transform(embeddings)

# Plot the clusters
plt.figure(figsize=(10, 7))
plt.scatter(pca_embeddings[:, 0], pca_embeddings[:, 1], c=kmeans.labels_, cmap='rainbow', alpha=0.7, edgecolors='b')
plt.title('Clusters of Documents (SBERT Embeddings)')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.colorbar(label='Cluster Label')
plt.show()



"""# 3)Embeddings using sentence-bert and Agglomerative clustering algorithm"""

from sklearn.cluster import AgglomerativeClustering
# Convert column names to strings to avoid TypeError
embeddings_df.columns = embeddings_df.columns.astype(str)

# Apply Agglomerative Clustering
n_clusters = 5
agg_clustering = AgglomerativeClustering(n_clusters=n_clusters)
agg_labels = agg_clustering.fit_predict(embeddings_df)

# Add cluster labels to the embeddings DataFrame
embeddings_df['cluster'] = agg_labels

# Create a new DataFrame with file number (or document index) and cluster label
output_df = pd.DataFrame({
    'filename': df.index,
    'cluster': agg_labels
})

# Calculate metrics for each cluster
cluster_metrics = []
for cluster in range(n_clusters):
    cluster_data = embeddings_df[embeddings_df['cluster'] == cluster]

    # Count number of documents in the cluster
    num_documents = cluster_data.shape[0]

    # Calculate the Silhouette Score for the cluster
    if num_documents > 1:  # Silhouette Score is undefined for 1 or fewer points
        cluster_silhouette_score = silhouette_score(embeddings_df.drop('cluster', axis=1), agg_labels, sample_size=num_documents)
    else:
        cluster_silhouette_score = np.nan  # Undefined for single document clusters

    cluster_metrics.append({
        'cluster': cluster,
        'num_documents': num_documents,
        'silhouette_score': cluster_silhouette_score
    })

# Convert to DataFrame for better readability
cluster_metrics_df = pd.DataFrame(cluster_metrics)

# Display metrics for each cluster
cluster_metrics_df

import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Reduce dimensionality to 2D using PCA
pca = PCA(n_components=2)
reduced_embeddings = pca.fit_transform(embeddings_df.drop('cluster', axis=1))

# Create a scatter plot
plt.figure(figsize=(10, 8))
scatter = plt.scatter(reduced_embeddings[:, 0], reduced_embeddings[:, 1], c=agg_labels, cmap='viridis', marker='o')

# Create a legend
legend1 = plt.legend(*scatter.legend_elements(), title="Clusters")
plt.gca().add_artist(legend1)

# Add title and labels
plt.title('Agglomerative Clustering of Document Embeddings')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')

# Show plot
plt.grid()
plt.show()