# 🎬 Movie Recommendation System

A **machine learning-based movie recommendation system** built using **Python and Streamlit**. This application suggests movies similar to a selected movie using **content-based filtering techniques**.

---

## 🚀 Live Demo

👉 https://movie-recommendation-system-7bxmfshrdba4uqj5rfwk2u.streamlit.app/

---

## 📌 Features

* 🔍 Search and select a movie
* 🎯 Get top similar movie recommendations
* ⚡ Fast results using precomputed similarity matrix
* 🖥️ Interactive and user-friendly UI with Streamlit
* 📊 Efficient data handling using Pandas

---

## 🧠 How It Works

This system uses **content-based filtering**, which recommends movies based on similarity between their features.

### Steps:

1. Movie data is collected and preprocessed
2. Features like genres, keywords, and metadata are combined
3. Text data is vectorized
4. Similarity between movies is computed (e.g., cosine similarity)
5. When a user selects a movie, the system returns the most similar ones

---

## 🛠️ Tech Stack

* **Python**
* **Pandas & NumPy**
* **Scikit-learn**
* **Streamlit**

---

## 📂 Project Structure

```
Movie-Recommendation-System/
│── app.py                # Main Streamlit app
│── movies.pkl            # Movie dataset
│── requirements.txt      # Dependencies
│── .streamlit/           # Streamlit config
│── README.md             # Project documentation
```

---

## ▶️ Run Locally

### 1. Clone the repository

```
git clone https://github.com/Prince3636/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

### 2. Create virtual environment (optional but recommended)

```
python -m venv myenv
myenv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run the app

```
streamlit run app.py
```

---

## 🌐 Deployment

This app can be deployed easily using **Streamlit Community Cloud**:

1. Push your code to GitHub
2. Go to https://share.streamlit.io
3. Select your repository
4. Choose:

   * Branch → `main`
   * File → `app.py`
5. Click **Deploy**

---

## 🎯 Use Cases

* Movie discovery platforms
* Personalized recommendation systems
* Learning project for ML beginners
* Demonstration of real-world ML applications

---

## ⚠️ Notes

* Large model files (like similarity matrices) should not be pushed to GitHub
* Use external storage (Google Drive / AWS S3) if needed

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 👨‍💻 Author

**Prince Kumar**
GitHub: https://github.com/Prince3636

---

⭐ If you like this project, give it a star!
