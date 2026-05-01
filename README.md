# 🧳 Amazon Luggage Competitive Intelligence Dashboard

## 📌 Overview
This project is an interactive dashboard built to analyze and compare luggage brands available on Amazon India.  
It focuses on extracting insights from product pricing and customer reviews to understand brand positioning and customer sentiment.

The goal is to help a decision-maker quickly identify which brands are performing well and why.

---

## 🎯 Objectives
- Compare multiple luggage brands based on price, rating, and sentiment
- Identify customer satisfaction trends using review analysis
- Understand which brands are premium vs budget-focused
- Highlight common customer complaints and positive feedback

---

## 🛠 Tech Stack
- **Python**
- **Pandas** – Data processing
- **Streamlit** – Dashboard UI
- **Plotly** – Visualizations
- **TextBlob** – Sentiment analysis

---

## 📊 Features

### 🔹 Dashboard Overview
- Total products analyzed
- Total reviews processed
- Average sentiment score
- Brand-wise performance snapshot

### 🔹 Brand Comparison
- Average price per brand
- Sentiment comparison
- Ratings distribution

### 🔹 Review Insights
- Positive vs negative sentiment
- Sample customer reviews
- Identification of common feedback patterns

### 🔹 Interactive Filters
- Brand selection
- Dynamic updates on charts and tables

---

## 📁 Project Structure

<img width="388" height="269" alt="image" src="https://github.com/user-attachments/assets/0842ec0d-7bfa-46ba-ad43-7f2f8719c210" />


---

## ⚙️ How to Run

1. Install dependencies:

   pip install -r requirements.txt

   
2. Run the dashboard:

   streamlit run dashboard/app.py

   
3. Open in browser:

   http://localhost:8501

   
---

## 📌 Dataset Note
Due to Amazon’s anti-scraping restrictions, a sampled dataset was used to simulate real-world product and review data.  
The structure reflects actual marketplace data, including brand, pricing, ratings, and customer reviews.

---

## 📈 Key Insights

- **American Tourister** appears to be positioned as a premium brand with higher pricing and strong sentiment.
- **Safari** and **VIP** cater more to budget-conscious customers with moderate sentiment.
- **Skybags** balances style and affordability but shows mixed feedback.
- Common positive themes: durability, design, spaciousness  
- Common complaints: wheel quality, handle durability

---

## 🚀 Future Improvements

- Aspect-based sentiment analysis (wheels, handle, durability)
- Real-time data scraping with robust anti-bot handling
- Discount and price trend analysis
- Automated "Agent Insights" generation
- Enhanced UI/UX with advanced filtering

---

## 🙋‍♀️ Author
Sai Likhitha Gaddam

---

