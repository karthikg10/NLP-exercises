# Text Clustering and Prompting Exploration

This repository provides three complementary projects focusing on text clustering using embeddings, effective prompting techniques for large language models (LLMs), and text extraction from web, PPT, and PDF files.

## 1. Document Clustering and Embedding Analysis

### Overview
This project demonstrates text clustering techniques by generating embeddings using TF-IDF and Sentence-BERT (SBERT). It includes:
- Preprocessing and cleaning text data.
- Generating embeddings.
- Applying clustering algorithms like K-Means and Agglomerative Clustering.
- Evaluating clusters with metrics such as Silhouette Scores.
- Visualizing clusters using PCA and plots.

### Key Features
- **Text Preprocessing**: Includes tokenization, stopword removal, lemmatization, and lowercasing.
- **Embedding Techniques**:
  - TF-IDF vectorization.
  - Contextual embeddings using SBERT.
- **Clustering Methods**:
  - K-Means clustering for both TF-IDF and SBERT embeddings.
  - Agglomerative clustering on SBERT embeddings.
- **Cluster Evaluation**: Silhouette Scores and cluster statistics.
- **Visualization**: PCA-based scatter plots and bar charts for insights.
- **Output**: Clustered documents saved to `clustered_documents_sbert.csv`.

### Requirements
- Libraries: pandas, numpy, nltk, scikit-learn, sentence-transformers, transformers, torch, and matplotlib.

### How to Run
1. Place text files in the directory specified in the script.
2. Run the `embeddings.py` file to preprocess, embed, and cluster the data.
3. Review outputs in CSV files and visual plots.

---

## 2. Prompting Assignment for Language Models

### Overview
This project explores the art of crafting effective prompts for LLMs, focusing on how well-structured queries improve model performance across various tasks.

### Key Features
- **Prompting Basics**:
  - Explanation of prompting and its importance.
  - Real-world use cases: content generation, chatbots, code assistance, and more.
- **Model Integration**:
  - Uses `google/gemma-2b` and `google/flan-t5-base` models.
  - Implements text generation pipelines.
- **Prompt Quality Analysis**:
  - Comparison of effective and ineffective prompts.
  - Domains explored: Common reasoning, math, coding, and literary skills.
- **Insights**:
  - Impacts of vague, biased, or overly complex prompts.
  - Recommendations for crafting clear and actionable prompts.

### Requirements
- Libraries: transformers, torch.

### How to Run
1. Set up your environment with necessary libraries.
2. Replace `HF_TOKEN` with your Hugging Face token for authentication.
3. Execute `prompting_lab.py` to test different prompt designs and analyze the outputs.

---

## 3. Text Extraction from Web, PPT, and PDF Files

### Overview
This project demonstrates how to extract structured and meaningful information from web pages, PowerPoint presentations, and PDF documents using Python libraries.

### Key Features
- **Web Scraping**:
  - Techniques for static and dynamic websites using `requests`, `BeautifulSoup`, and `Selenium`.
  - Examples include scraping `ScrapeThisSite`, `GeeksforGeeks`, `CNBC`, and `Hoopshype`.
- **PPT Extraction**:
  - Text extraction from PowerPoint slides using `python-pptx`.
- **PDF Extraction**:
  - Extracting text content from PDFs using `PyPDF2`.

### Requirements
- Libraries: requests, beautifulsoup4, selenium, python-pptx, PyPDF2, pandas, json.

### How to Run
1. For web scraping:
   - Run the script and provide the URLs to scrape.
   - Extract structured data such as text, links, and tabular content.
2. For PPT extraction:
   - Use the `Presentation` class to load a `.pptx` file.
   - Extract text and analyze slide contents.
3. For PDF extraction:
   - Use `PyPDF2` to load a PDF file and extract text from individual pages.

---

## Repository Structure
- `embeddings.py`: Script for text clustering using embeddings.
- `prompting_lab.py`: Script for prompting experiments with LLMs.
- `textextraction_web_ppt_pdf.py`: Script demonstrating text extraction techniques from web, PPT, and PDF files.
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
This project is licensed under the MIT License. See the LICENSE file for more details.
