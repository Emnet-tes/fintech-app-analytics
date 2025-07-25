# Fintech App Analytics

This project is focused on analyzing user reviews and extracting insights from fintech mobile applications, specifically targeting Ethiopian banks. The workflow includes scraping reviews, preprocessing text data, performing sentiment analysis, and conducting thematic analysis to uncover trends and user sentiments.

## Project Structure

```
fintech-app-analytics-week2/
├── app/
├── data/
│   ├── all_bank_reviews.csv
│   ├── boa_reviews.csv
│   ├── cbe_reviews.csv
│   └── dashen_reviews.csv
├── log/
│   └── scraper.log
├── notebooks/
│   ├── scraping_and_preprocessing.ipynb
│   └── sentiment_and_thematic.ipynb
├── scripts/
├── src/
│   ├── Preprocessing/
│   │   ├── play_store_scraper.py
│   │   └── preprocessor.py
│   └── ThematicSentiment/
│       ├── sentiment_analysis.py
│       └── thematic_analysis.py
├── tests/
├── requirements.txt
└── README.md
```

## Main Components

- **Data Collection**: Scrapes user reviews from the Google Play Store for various Ethiopian bank apps.
- **Preprocessing**: Cleans and prepares the text data for analysis.
- **Sentiment Analysis**: Classifies reviews as positive, negative, or neutral.
- **Thematic Analysis**: Identifies common themes and topics in user feedback.

## How to Use

1. **Install Dependencies**

   ```
   pip install -r requirements.txt
   ```

2. **Run Notebooks**

   - Use the notebooks in the `notebooks/` directory to run scraping, preprocessing, sentiment, and thematic analysis steps interactively.

3. **Scripts and Modules**
   - Core logic for scraping and analysis is in the `src/` directory.
   - You can run or import these modules in your own scripts or notebooks.

## Data

The `data/` directory contains CSV files with raw and processed reviews for each bank.

## Logging

Logs from scraping and processing are stored in the `log/` directory.

## Testing

Test files are located in the `tests/` directory.

## Requirements

See `requirements.txt` for a list of required Python packages.


## License

This project is for educational purposes.
