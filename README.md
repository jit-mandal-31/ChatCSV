# ChatCSV
Built a Chat with CSV app using Streamlit, Pandas, and Hugging Face’s Mistral-7B LLM. Users can upload CSV files and ask natural language questions to analyze data. The system processes CSV context and provides insights, making data exploration simple for non-technical users.

Here’s a clean **README.md** for your project 👇

---



## 📌 Overview

This project allows users to upload CSV files and interact with them using natural language queries. Instead of writing SQL or code, users can simply ask questions, and the app provides insights powered by **Mistral-7B (Hugging Face LLM)**.

## 🚀 Features

* Upload any CSV file.
* View data preview in an interactive table.
* Ask natural language questions about the CSV.
* Get instant answers powered by **LLM**.
* Simple web app built with **Streamlit**.

## 🛠️ Tech Stack

* **Python**
* **Pandas** – for CSV handling
* **Streamlit** – for UI
* **Hugging Face Hub** – Mistral-7B model for Q\&A

## ⚙️ Installation

1. Clone this repo:

   ```bash
   git clone https://github.com/your-username/chat-with-csv-llm.git
   cd chat-with-csv-llm
   ```
2. Create virtual environment & activate:

   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## 🔑 Hugging Face API Setup

* Get your free token from [Hugging Face](https://huggingface.co/settings/tokens).
* Add it inside your code:

  ```python
  client = InferenceClient("mistralai/Mistral-7B-Instruct-v0.2", token="your_hf_token")
  ```

## ▶️ Run the App

```bash
streamlit run app.py
```

## 📂 Sample Usage

* Upload `large_employees.csv`
* Example questions:

  * *“Which department has the highest average salary?”*
  * *“List employees who joined after 2020.”*
  * *“Show top 5 highest salaries.”*

---

👉 Do you want me to also generate a **requirements.txt file** for this project so you can just run `pip install -r requirements.txt`?
