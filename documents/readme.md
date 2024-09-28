
# Data Extraction and NLP Test Assignment

## Overview

This project involves extracting text data from specified URLs and performing a comprehensive text analysis to compute several linguistic and sentiment-based metrics. The analysis is tailored for financial texts, focusing on sentiment, readability, and various textual characteristics. The project was implemented using Python, primarily utilizing the BeautifulSoup library for web scraping and the Natural Language Toolkit (nltk) for text processing.

## Objective

The main objective of this assignment is to extract article texts from a list of URLs provided in `Input.xlsx` and perform a detailed text analysis to compute various metrics. The results of this analysis are stored in an output file structured according to the specifications in `Output Data Structure.xlsx`.

## Approach

### 1. Data Extraction

**Input File:** `Input.xlsx`  
**Output:** Text files for each article

The extraction process involved the following steps:

- **URL Processing:** Each URL from `Input.xlsx` was processed using BeautifulSoup to scrape the article's title and body text.
- **Content Filtering:** The scraper was configured to exclude non-relevant content such as headers, footers, advertisements, and other non-article elements.
- **Saving Articles:** The cleaned article text was saved in individual text files, named according to their corresponding URL_ID.

### 2. Text Analysis

After extracting the text data, a detailed analysis was performed to compute the following variables:

#### Readability Analysis

The readability of each article was assessed using the Gunning Fox Index, which is a measure of text complexity based on sentence length and word difficulty:

- **Average Sentence Length:** Calculated by dividing the total number of words by the number of sentences.
  
- **Percentage of Complex Words:** The proportion of words in the text with more than two syllables.
  
- **Fog Index:** A readability test that estimates the years of formal education needed to understand the text on a first reading. It was calculated as:
  \[
  \text{Fog Index} = 0.4 \times (\text{Average Sentence Length} + \text{Percentage of Complex Words})
  \]

#### Additional Metrics

- **Average Number of Words Per Sentence:** Total word count divided by the number of sentences.
  
- **Complex Word Count:** The number of words in the text containing more than two syllables.
  
- **Word Count:** The total number of words in the text, excluding stop words and punctuation.
  
- **Syllable Count Per Word:** Syllables were counted by identifying vowels in each word, with special rules for endings like "es" and "ed."
  
- **Personal Pronouns:** Counted using regular expressions to find instances of "I," "we," "my," "ours," and "us," while ensuring that "US" (as in the country) was not included.
  
- **Average Word Length:** Calculated by dividing the total number of characters by the total number of words.

#### Sentimental Analysis

The sentiment analysis was specifically designed for financial texts, involving several key steps:

- **Stop Words Removal:** Texts were cleaned using predefined stop words lists found in the `StopWords` folder. This step ensured that common, non-informative words were excluded from the analysis.
  
- **Dictionary Creation:** Using the `MasterDictionary`, words were classified as either positive or negative, provided they were not present in the stop words list. This dictionary was crucial for the subsequent calculation of sentiment scores.
  
- **Variable Extraction:**
  - **Positive Score:** Calculated by counting the number of words in the text that matched the positive dictionary and summing these counts.
  - **Negative Score:** Similarly, the negative score was derived by counting words in the negative dictionary. The final score was positive, as it was multiplied by -1.
  - **Polarity Score:** This metric indicates whether the sentiment of the text is positive or negative. It was calculated using the formula:
    \[
    \text{Polarity Score} = \frac{\text{Positive Score} - \text{Negative Score}}{(\text{Positive Score} + \text{Negative Score}) + 0.000001}
    \]
    The score ranges from -1 to +1.
  - **Subjectivity Score:** This measures the subjectivity of the text, calculated by:
    \[
    \text{Subjectivity Score} = \frac{\text{Positive Score} + \text{Negative Score}}{\text{Total Words after cleaning} + 0.000001}
    \]
    The score ranges from 0 (objective) to 1 (subjective).


### 3. Output

**Output File:** `output.csv`

The final results of the text analysis were compiled into a CSV file structured according to the `Output Data Structure.xlsx` file. This file includes all the input variables from `Input.xlsx` alongside the calculated metrics.

## Dependencies

The project requires the following Python libraries, as specified in `requirements.txt`:

- beautifulsoup4==4.12.3
- certifi==2024.7.4
- charset-normalizer==3.3.2
- click==8.1.7
- colorama==0.4.6
- et-xmlfile==1.1.0
- idna==3.8
- joblib==1.4.2
- nltk==3.9.1
- numpy==2.1.0
- openpyxl==3.1.5
- pandas==2.2.2
- python-dateutil==2.9.0.post0
- pytz==2024.1
- regex==2024.7.24
- requests==2.32.3
- six==1.16.0
- soupsieve==2.6
- tqdm==4.66.5
- tzdata==2024.1
- urllib3==2.2.2

## How to Run

1. **Install Dependencies:** Ensure all required libraries are installed using the command:
   ```
   pip install -r requirements.txt
   ```
   
2. **Run the Script:** Execute the Python script to perform data extraction and analysis:
   ```
   python main.py
   ```


3. **Output:** The script will generate a CSV file (`output.csv`) containing the calculated metrics as per the output structure defined.

