import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import os

def scrape_news():
    """Scrape headlines from Top News"""
    url = "https://www.nytimes.com/international/section/world"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        print("Fetching News headlines...")
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        headlines = []

        # Look for various headline selectors on News URL
        selectors = [
            'h2[data-testid="card-headline"]',
            'h2.sc-4fedabc7-3',
            'h3[data-testid="card-headline"]',
            '.gs-c-promo-heading__title',
            'h2',
            'h3'
        ]

        for selector in selectors:
            elements = soup.select(selector)
            for element in elements[:10]:  # Limit to first 10 per selector
                text = element.get_text(strip=True)
                if text and len(text) > 10 and text not in headlines:
                    headlines.append(text)
            if len(headlines) >= 5:  # Stop if we have enough headlines
                break

        return headlines[:10]  # Return top 10 headlines

    except requests.RequestException as e:
        print(f"Error fetching News: {e}")
        return []


def scrape_example_news():
    """Scrape headlines from example.com (for demonstration)"""
    url = "https://httpbin.org/html"  # Safe testing URL
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    try:
        print("Fetching example headlines...")
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        # This is a demo - in real scenario, you'd parse actual news elements
        headlines = [
            "Example Headline: Technology Advances in 2025",
            "Sample News: Global Markets Show Strong Growth",
            "Demo Article: Climate Change Solutions Emerge"
        ]

        return headlines

    except requests.RequestException as e:
        print(f"Error fetching example news: {e}")
        return []

def save_headlines_to_file(all_headlines, filename="news_headlines.txt"):
    """Save headlines to a text file"""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            # Write header with timestamp
            file.write("NEWS HEADLINES SCRAPER\n")
            file.write("=" * 50 + "\n")
            file.write(f"Scraped on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("=" * 50 + "\n\n")

            if not all_headlines:
                file.write("No headlines found.\n")
                return

            # Write headlines by source
            for source, headlines in all_headlines.items():
                if headlines:
                    file.write(f"\n{source.upper()} HEADLINES:\n")
                    file.write("-" * 30 + "\n")
                    for i, headline in enumerate(headlines, 1):
                        file.write(f"{i}. {headline}\n")
                    file.write("\n")

            file.write(f"\nTotal headlines scraped: {sum(len(h) for h in all_headlines.values())}\n")

        print(f"Headlines saved to '{filename}'")

    except IOError as e:
        print(f"Error saving to file: {e}")

def display_headlines(all_headlines):
    """Display headlines in the console"""
    print("\n" + "="*60)
    print("             SCRAPED NEWS HEADLINES")
    print("="*60)

    if not any(all_headlines.values()):
        print("No headlines were successfully scraped.")
        return

    for source, headlines in all_headlines.items():
        if headlines:
            print(f"\n{source.upper()} ({len(headlines)} headlines):")
            print("-" * 40)
            for i, headline in enumerate(headlines, 1):
                print(f"{i:2d}. {headline}")

    total = sum(len(h) for h in all_headlines.values())
    print(f"\nTotal headlines scraped: {total}")
    print("="*60)

def main():
    """Main function to orchestrate the web scraping"""
    print("Starting News Headlines Web Scraper...")
    print("This tool demonstrates HTTP requests, web scraping, and HTML parsing.")

    # Dictionary to store headlines from different sources
    all_headlines = {}

    # Scrape from multiple sources
    sources = {
        'News': scrape_news,
        'Example': scrape_example_news
    }

    for source_name, scraper_func in sources.items():
        print(f"\n--- Scraping {source_name} ---")
        headlines = scraper_func()
        all_headlines[source_name] = headlines

        if headlines:
            print(f"✓ Found {len(headlines)} headlines from {source_name}")
        else:
            print(f"✗ No headlines found from {source_name}")

        # Add delay between requests to be respectful
        time.sleep(2)

    # Display results
    display_headlines(all_headlines)

    # Save to file
    save_headlines_to_file(all_headlines)

    print(f"\nScraping completed! Check 'news_headlines.txt' for saved results.")

if __name__ == "__main__":
    main()