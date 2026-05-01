# Luggage Competitive Intelligence Dashboard

## Overview
This project analyzes Amazon India luggage brands using scraped product and review data.

## Features
- Sentiment analysis of reviews
- Price comparison across brands
- Interactive dashboard
- Brand-level insights

## Tech Stack
- Python
- Playwright (Scraping)
- Pandas (Data Processing)
- TextBlob (Sentiment)
- Streamlit (Dashboard)

## How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Run scraper:
python scraper/amazon_scraper.py

3. Clean data:
python analysis/preprocess.py

4. Run sentiment:
python analysis/sentiment.py

5. Launch dashboard:
streamlit run dashboard/app.py

## Insights
- American Tourister shows higher price but better sentiment
- Safari focuses on budget segment
- VIP shows mixed sentiment due to durability complaints