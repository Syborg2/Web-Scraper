<h1 align="center"> Web Scraper for News Headlines </h1>

A Python web scraper that extracts top headlines from news websites and saves them to a text file. This project demonstrates web scraping techniques, HTTP requests, and HTML parsing.

## 🎯 Objective
Scrape top headlines from news websites using HTTP requests and HTML parsing to automate data collection from public websites.

## 🛠️ Tools & Technologies
- **Python 3.x**
- **requests** - For making HTTP requests to fetch web pages
- **BeautifulSoup4** - For parsing HTML and extracting headline data
- **datetime** - For timestamping scraped data
- **os** - For file operations

## 📦 Deliverables
- `news_scraper.py` - Main Python script for web scraping
- `news_headlines.txt` - Output text file containing scraped headlines
- `requirements.txt` - Python dependencies list

## 🔑 Key Concepts Demonstrated
- **HTTP Requests** - Fetching web page content using requests library
- **Web Scraping** - Extracting structured data from HTML content
- **HTML Parsing** - Using BeautifulSoup to parse and navigate HTML elements
- **Error Handling** - Managing network timeouts and request failures
- **File I/O Operations** - Writing structured data to text files
- **Data Processing** - Filtering and organizing scraped content

## 🚀 Installation & Setup

1. **Clone or download** the project files to your local machine

2. **Install required dependencies**:
   ```bash
   pip install requests beautifulsoup4 lxml
   ```
   
   Or use the requirements file:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

Run the news scraper:
```bash
python news_scraper.py
```

The script will automatically:
1. Fetch HTML content from configured news websites
2. Parse headline elements using CSS selectors
3. Display results in the console with source attribution
4. Save all headlines to `news_headlines.txt` with timestamp

## ✨ Features

### Data Sources
- **NY Times International** - Scrapes world news headlines
- **Example Demo Source** - Fallback demonstration headlines

### Smart Scraping
- **Multiple CSS Selectors** - Uses various selectors to find headlines across different page structures
- **Duplicate Prevention** - Filters out duplicate headlines automatically
- **Length Filtering** - Only captures meaningful headlines (>10 characters)
- **Respectful Requests** - Includes proper User-Agent headers and request delays

### Output Features
- **Console Display** - Real-time progress and results display
- **File Export** - Timestamped text file with organized headlines
- **Error Reporting** - Clear error messages for failed requests
- **Source Attribution** - Headlines organized by news source

## 📊 Sample Output

### Console Output
```
Starting News Headlines Web Scraper...
This tool demonstrates HTTP requests, web scraping, and HTML parsing.

--- Scraping News ---
Fetching News headlines...
✓ Found 8 headlines from News

--- Scraping Example ---
Fetching example headlines...
✓ Found 3 headlines from Example

============================================================
                    SCRAPED NEWS HEADLINES
============================================================

NEWS (8 headlines):
----------------------------------------
 1. Global Climate Summit Reaches Historic Agreement
 2. Technology Sector Shows Unprecedented Growth
 3. International Markets React to Policy Changes
...

EXAMPLE (3 headlines):
----------------------------------------
 1. Example Headline: Technology Advances in 2025
 2. Sample News: Global Markets Show Strong Growth
 3. Demo Article: Climate Change Solutions Emerge

Total headlines scraped: 11
============================================================
```

### File Output (`news_headlines.txt`)
```
NEWS HEADLINES SCRAPER
==================================================
Scraped on: 2025-08-05 14:30:22
==================================================

NEWS HEADLINES:
------------------------------
1. Global Climate Summit Reaches Historic Agreement
2. Technology Sector Shows Unprecedented Growth
3. International Markets React to Policy Changes
...

Total headlines scraped: 11
```

## 📁 Project Structure

```
news-scraper/
├── news_scraper.py         # Main scraper script
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
└── news_headlines.txt     # Generated output file
```

## 🔧 Technical Implementation

### Following Project Requirements
The scraper implements the core requirements:

1. **✅ Uses requests** to fetch HTML content from news websites
2. **✅ Uses BeautifulSoup** to parse `<h2>`, `<h3>`, and title tags
3. **✅ Saves headlines** to a `.txt` file with proper formatting

### Code Architecture
- **Modular Functions** - Separate functions for each scraping source
- **Error Handling** - Try-catch blocks for network and parsing errors
- **Configurable Selectors** - Easy to modify CSS selectors for different sites
- **Scalable Design** - Easy to add new news sources

## 🛡️ Ethical Considerations

- **Respectful Scraping** - Includes delays between requests (2 seconds)
- **Proper Headers** - Uses realistic User-Agent strings
- **Rate Limiting** - Limits requests to avoid overwhelming servers
- **Public Content Only** - Only scrapes publicly available headlines
- **Error Graceful** - Handles failures without crashing

## 🎯 Learning Outcomes

This project demonstrates practical skills in:
- Web scraping methodologies and best practices
- HTTP request handling and response processing
- HTML parsing and CSS selector usage
- File I/O operations and data persistence
- Error handling in network operations
- Code organization and modularity

## 🔄 Future Enhancements

Potential improvements could include:
- RSS feed parsing for more reliable data extraction
- Database storage instead of text files
- Sentiment analysis of headlines
- Email notifications for specific keywords
- Web dashboard for visualization
- Multiple language support

## 📝 Requirements

```
requests>=2.25.1
beautifulsoup4>=4.9.3
lxml>=4.6.3
```

## 🏆 Outcome

Successfully automates data collection from public news websites, demonstrating practical web scraping techniques and providing a foundation for more advanced data extraction projects.
