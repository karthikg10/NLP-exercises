# Text Clustering and Prompting Exploration

This repository provides two complementary projects focusing on text clustering using embeddings and effective prompting techniques for large language models (LLMs).

---

## **1. Document Clustering and Embedding Analysis**

### Overview
This project demonstrates text clustering techniques by generating embeddings using TF-IDF and Sentence-BERT (SBERT). It includes:
- Preprocessing and cleaning text data.
- Generating embeddings.
- Applying clustering algorithms like K-Means and Agglomerative Clustering.
- Evaluating clusters with metrics such as Silhouette Scores.
- Visualizing clusters using PCA and plots.

### Key Features
1. **Text Preprocessing**: Includes tokenization, stopword removal, lemmatization, and lowercasing.
2. **Embedding Techniques**:
   - TF-IDF vectorization.
   - Contextual embeddings using SBERT.
3. **Clustering Methods**:
   - K-Means clustering for both TF-IDF and SBERT embeddings.
   - Agglomerative clustering on SBERT embeddings.
4. **Cluster Evaluation**: Silhouette Scores and cluster statistics.
5. **Visualization**: PCA-based scatter plots and bar charts for insights.
6. **Output**: Clustered documents saved to `clustered_documents_sbert.csv`.

### Requirements
- Libraries: `pandas`, `numpy`, `nltk`, `scikit-learn`, `sentence-transformers`, `transformers`, `torch`, and `matplotlib`.

### How to Run
1. Place text files in the directory specified in the script.
2. Run the `embeddings.py` file to preprocess, embed, and cluster the data.
3. Review outputs in CSV files and visual plots.

---

## **2. Prompting Assignment for Language Models**

### Overview
This project explores the art of crafting effective prompts for LLMs, focusing on how well-structured queries improve model performance across various tasks.

### Key Features
1. **Prompting Basics**:
   - Explanation of prompting and its importance.
   - Real-world use cases: content generation, chatbots, code assistance, and more.
2. **Model Integration**:
   - Uses `google/gemma-2b` and `google/flan-t5-base` models.
   - Implements text generation pipelines.
3. **Prompt Quality Analysis**:
   - Comparison of effective and ineffective prompts.
   - Domains explored: Common reasoning, math, coding, and literary skills.
4. **Insights**:
   - Impacts of vague, biased, or overly complex prompts.
   - Recommendations for crafting clear and actionable prompts.

### Requirements
- Libraries: `transformers`, `torch`.

### How to Run
1. Set up your environment with necessary libraries.
2. Replace `HF_TOKEN` with your Hugging Face token for authentication.
3. Execute `prompting_lab.py` to test different prompt designs and analyze the outputs.

---

## Repository Structure
- `embeddings.py`: Script for text clustering using embeddings.
- `prompting_lab.py`: Script for prompting experiments with LLMs.
- `clustered_documents_sbert.csv`: Output file for clustered text data.

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/karthikg10-NLP-exercises.git
   ```
2. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Follow the instructions for each script to run the respective projects.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

