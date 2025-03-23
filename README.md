# Software Log Classification

## Overview
This project implements a **hybrid classification approach** to categorize software logs efficiently. The method follows a hierarchical classification pipeline:

1. **DBSCAN Clustering** – Groups logs to detect anomalies and similar patterns.
2. **Regular Expressions** – Classifies simple logs (e.g., “user logged in”).
3. **Logistic Regression** – Used when regex fails to classify logs.
4. **Word2Vec/BERT for Sentence Embeddings** – Converts log messages into dense vectors for better classification.
5. **Pretrained Large Language Models (LLMs)** – Used as the final fallback for complex log classification.

This approach enhances automated log analysis, improving system monitoring, debugging, and anomaly detection.

---

## Features
- **Hybrid Classification**: Combines clustering, rule-based, and machine learning techniques.
- **Anomaly Detection**: Uses DBSCAN to detect unusual logs.
- **Pattern Matching**: Leverages regex for simple log types.
- **Machine Learning Models**: Logistic Regression, Word2Vec/BERT embeddings, and LLMs for classification.
- **Scalability**: Can process large volumes of logs efficiently.

---

## Installation
### Prerequisites
Ensure you have Python 3.8+ installed along with the following dependencies:

```sh
pip install numpy pandas scikit-learn gensim transformers torch regex nltk
```



## Classification Pipeline
### **Step 1: DBSCAN Clustering**
- Groups log messages based on similarity.
- Helps detect anomalies in logs.

### **Step 2: Regular Expression Matching**
- Classifies logs with predefined regex patterns (e.g., authentication, system errors).
- If regex fails, move to Step 3.

### **Step 3: Logistic Regression Model**
- Uses traditional ML classification on structured log messages.
- If classification fails, move to Step 4.

### **Step 4: Sentence Embeddings with Word2Vec/BERT**
- Converts log messages into dense vector representations.
- Enhances model understanding of semantic relationships.

### **Step 5: Pretrained LLM Classification**
- Uses models like GPT/BERT for contextual classification.
- Final fallback if other methods fail.

---

## Example Output
### **Input Log Messages**
```txt
[INFO] User logged in successfully.
[ERROR] Database connection failed!
[WARNING] CPU usage exceeded threshold.
```

### **Classifications**
```json
{
  "log_1": "Authentication Event",
  "log_2": "Database Error",
  "log_3": "System Warning"
}
```

---

## Future Improvements
- Fine-tuning LLMs for better classification.
- Adding more NLP techniques for log normalization.
- Integrating real-time log monitoring and alerting.

---

