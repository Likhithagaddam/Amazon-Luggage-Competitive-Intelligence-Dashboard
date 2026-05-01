from playwright.sync_api import sync_playwright
import pandas as pd
import time
import random

BRANDS = [
    "Safari luggage",
    "Skybags luggage",
    "American Tourister luggage",
    "VIP luggage"
]

def scrape_amazon():
    data = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
        )
        page = context.new_page()

        for brand in BRANDS:
            print(f"Scraping {brand}...")

            page.goto(f"https://www.amazon.in/s?k={brand.replace(' ', '+')}", timeout=60000)
            page.wait_for_timeout(5000)

            # Scroll like human
            for _ in range(3):
                page.mouse.wheel(0, 3000)
                time.sleep(random.uniform(1, 2))

            products = page.locator("div.s-main-slot div[data-component-type='s-search-result']").all()

            for product in products[:5]:  # keep small to avoid blocking
                try:
                    title = product.locator("h2 span").inner_text(timeout=5000)
                    price = product.locator(".a-price-whole").inner_text(timeout=5000)
                    rating = product.locator(".a-icon-alt").inner_text(timeout=5000)

                    link = product.locator("h2 a").get_attribute("href")
                    product_url = "https://www.amazon.in" + link

                    # Open product page
                    page.goto(product_url)
                    page.wait_for_timeout(4000)

                    reviews = page.locator("span[data-hook='review-body']").all()
                    review_texts = [r.inner_text() for r in reviews[:3]]

                    for review in review_texts:
                        data.append({
                            "brand": brand,
                            "title": title,
                            "price": price,
                            "rating": rating,
                            "review": review
                        })

                    time.sleep(random.uniform(2, 4))

                except Exception as e:
                    print("Skipping product:", e)
                    continue

        browser.close()

    df = pd.DataFrame(data)
    df.to_csv("data/raw_data.csv", index=False)
    print("✅ Data saved!")

if __name__ == "__main__":
    scrape_amazon()
