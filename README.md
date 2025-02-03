# Noon Company Review - Coursework

This repository contains the coursework for the **Noon Company Review** project, conducted by the following contributors:

- **Hariharakumar Rathinar**
- **Yadubanshi Pratibha**
- **Onafeso Fiyifoluwa**
- **Sattar Shaikh Eherar**

---

F21AA_TEXTANALYSTICS/
├── data/
│   ├── raw/                # Raw data collected from Reddit
│   └── processed/          # Processed data ready for analysis
├── notebooks/              # Jupyter notebooks for exploratory analysis and experiments
├── src/                    # Source code for data collection, preprocessing, analytics, and modeling
│   ├── data_collection.py  # Script for scraping data from Reddit
│   ├── data_preprocessing.py  # Script for cleaning and labeling the data
│   ├── text_analytics_pipeline.py  # Implementation of the text analytics pipeline
│   └── visualization.py    # Scripts for creating visualizations (e.g., word clouds, pyLDAvis)
├── reports/                # Generated reports and visualizations
├── docs/                   # Documentation, including the research summary on the history of NLP
├── README.md               # Project overview and instructions
└── requirements.txt        # List of Python dependencies


## Table of Contents

1. [Objectives and Problem Formulation](#objectives-and-problem-formulation)
2. [Learning Outcomes](#learning-outcomes)
3. [Implementation and Requirements](#implementation-and-requirements)
    - [A. Data Collection](#a-data-collection)
    - [B. Data Analysis, Selection, and Labeling](#b-data-analysis-selection-and-labeling)
    - [C. Text Analytics Pipeline](#c-text-analytics-pipeline)
    - [D. Visualization and Insights](#d-visualization-and-insights)
    - [E. Discussion and Conclusion from Experiments](#e-discussion-and-conclusion-from-experiments)
    - [F. Research Question: History of NLP](#f-research-question-history-of-nlp)
4. [Usage](#usage)
5. [License](#license)
6. [References](#references)

---

## Objectives and Problem Formulation

Studies have shown that sentiments from social media can provide valuable insights for businesses and government entities. In this coursework, our objective is to perform a detailed **Company Reputation Analysis** on Noon Company by examining customer and employee opinions expressed on Reddit. This analysis will help:

- Understand overall brand perception and reputation.
- Gain insights into customer satisfaction and internal work culture.
- Inform potential customers and job seekers regarding the company's products and work environment.

Using Reddit, a rich source of public discussions, we will analyze user comments to extract sentiments and major topics related to Noon Company. This project leverages text analytics and visualization techniques to build a robust sentiment classification model.

---

## Learning Outcomes

By completing this coursework, participants will gain hands-on experience in:

- **Data Extraction:** Automatically extracting reviews and discussions from social media platforms like Reddit.
- **Text Analysis:** Using tools such as TextBlob and Vader to preprocess and analyze social media comments.
- **Dataset Preparation:** Collecting data and creating train-test splits for model building.
- **Pipeline Development:** Designing a text analytics pipeline covering text processing, feature extraction, classification, and evaluation.
- **Visualization:** Using techniques like word clouds and topic modeling to visualize and interpret insights.
- **Research:** Understanding the evolution of NLP through landmark breakthroughs and research literature.

---

## Implementation and Requirements

The coursework is divided into the following stages:

### A. Data Collection (15%)

- **Objective:** Create a dataset of Reddit comments related to Noon Company.
- **Tasks:**
  - Register for a Reddit developer account.
  - Utilize the Python Reddit API (Async PRAW) to extract relevant comments.
  - Collect comments from various threads to enhance dataset diversity.
  - Develop a process to automatically scrape and curate the data.

### B. Data Analysis, Selection, and Labeling (15%)

- **Objective:** Curate the dataset by filtering relevant comments and labeling them by sentiment.
- **Tasks:**
  - Analyze the dataset to identify and select the most relevant comments.
  - Label each comment as **positive**, **negative**, or **neutral**.
  - Consider manual tagging or leverage existing sentiment analysis tools (e.g., TextBlob, Vader) for initial labeling.
  - Split the data into 80% for training and 20% for testing.
  - Document the methodology for filtering and labeling.

### C. Text Analytics Pipeline (20%)

- **Objective:** Develop a pipeline for text processing, representation, classification, and evaluation.
- **Tasks:**
  - Implement text processing techniques such as tokenization, stemming, normalization, and stop-word/punctuation removal.
  - Experiment with different feature extraction methods (e.g., unigram/n-gram features, binary/frequency count, tf-idf, word embeddings).
  - Build and evaluate a classification model using metrics like precision and recall.
  - Justify the selection of methods and compare different approaches.

### D. Visualization and Insights (20%)

- **Objective:** Visualize the analytical results to gain actionable insights.
- **Tasks:**
  - Analyze prevalent sentiments (e.g., separate visualizations for positive and negative comments).
  - Use visualization tools such as word clouds, pyLDAvis, or similar to display topics and sentiment distributions.
  - Document insights and observations regarding public opinion and key discussion topics.

### E. Discussion and Conclusion from Experiments (20%)

- **Objective:** Summarize and discuss the key findings from the analysis.
- **Tasks:**
  - Highlight the data curation and validation process.
  - Compare the performance of the text analytics pipelines and models.
  - Discuss insights regarding public sentiment toward Noon Company and their practical implications.
  - Provide recommendations on how these findings can inform business or recruitment decisions.

### F. Research Question: History of NLP (10%)

- **Objective:** Provide a concise overview of the historical advancements and key breakthroughs in Natural Language Processing.
- **Tasks:**
  - Each group member contributes by summarizing a different aspect of NLP’s evolution.
  - Compile a one-page summary (A4, Arial 11pt) covering landmark developments, supported by relevant references.
  - Use sources such as Chris Manning's article on language understanding and the Stanford CS324H course materials.

---

## Usage

- **Data Extraction:** Run the provided Python scripts to authenticate with Reddit and extract comments using Async PRAW.
- **Data Preparation:** Follow guidelines for filtering, labeling, and splitting the dataset.
- **Model Development:** Execute the text analytics pipeline to preprocess text, extract features, build classification models, and evaluate performance.
- **Visualization:** Generate visualizations to explore sentiment distributions and topic modeling outputs.
- **Research Documentation:** Prepare the research summary on the history of NLP as per the provided specifications.

---

## License

This coursework and its accompanying scripts are provided for educational purposes only. Please refer to your institution’s licensing policies for further details.

---

## References

- **Reddit API Documentation:** [https://www.reddit.com/dev/api/](https://www.reddit.com/dev/api/)
- **TextBlob Documentation:** [https://textblob.readthedocs.io/](https://textblob.readthedocs.io/)
- **Vader Sentiment Analysis:** [https://github.com/cjhutto/vaderSentiment](https://github.com/cjhutto/vaderSentiment)
- **Chris Manning's Article on Human Language Understanding:** [https://www.amacad.org/publication/human-language-understanding-reasoning](https://www.amacad.org/publication/human-language-understanding-reasoning)
- **Stanford Course CS324H:** [https://web.stanford.edu/class/cs324h/](https://web.stanford.edu/class/cs324h/)

---



*Contributors:*  
Hariharakumar Rathinar, Yadubanshi Pratibha, Onafeso Fiyifoluwa, and Sattar Shaikh Eherar.