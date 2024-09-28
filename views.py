import re
import os
import string
import nltk
from nltk.corpus import stopwords
nltk.data.path.append('nltk_data')
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize, sent_tokenize


def count_total_personal_pronouns(text):
    # Tokenize the text into words
    words = word_tokenize(text)

    # Initialize a counter for the total number of personal pronouns
    total_pronouns = 0

    # List of personal pronouns to count
    personal_pronouns = ['i', 'we', 'my', 'ours', 'us']

    # Count the occurrences of each personal pronoun
    for word in words:
        if word.lower() in personal_pronouns:
            if word.lower() == 'us' and word != 'US':
                total_pronouns += 1
            else:
                total_pronouns += 1

    return total_pronouns


def count_syllables(word):
    word = word.lower()
    # Handle exceptions for words ending with "es" and "ed"
    if word.endswith('es') or word.endswith('ed'):
        word = word[:-2]
    # Define the pattern to match vowels
    syllable_pattern = re.compile(r'[aeiouy]+', re.I)
    syllables = syllable_pattern.findall(word)
    return len(syllables)


def num_of_complex_word(text):
    words = word_tokenize(text)
    count_complex_word = 0
    for word in words:
        if count_syllables(word) > 2:
            count_complex_word += 1
    return count_complex_word


def calculate_syllable_counts(text):
    # Tokenize the text into words
    words = word_tokenize(text)

    # Calculate the number of syllables for each word
    total_words = 0
    total_syllable = 0
    for word in words:
        total_words += 1
        total_syllable += count_syllables(word)

    avg_syllable_per_word = total_syllable / total_words
    return avg_syllable_per_word


def calculate_readability(text):
    # Tokenize the text into words and sentences
    words = word_tokenize(text)
    sentences = sent_tokenize(text)

    # Calculate the number of words and sentences
    num_words = len(words)
    num_sentences = len(sentences)

    # Calculate Average Sentence Length
    average_sentence_length = num_words / num_sentences

    # Calculate the number of complex words
    num_complex_words = sum(1 for word in words if count_syllables(word) > 2)

    # Calculate Percentage of Complex Words
    percentage_complex_words = (num_complex_words / num_words) * 100

    # Calculate Fog Index
    fog_index = 0.4 * (average_sentence_length + percentage_complex_words)

    return average_sentence_length, percentage_complex_words, fog_index


def calculate_average_words_per_sentence(cleaned_text):
    text = cleaned_text
    words = word_tokenize(text)
    sentences = sent_tokenize(text)

    # Calculate the number of words and sentences
    num_words = len(words)
    num_sentences = len(sentences)
    average_words_per_sentence = num_words / num_sentences

    return average_words_per_sentence


def calculate_average_word_length(text):
    # Tokenize the text into words
    words = word_tokenize(text)

    # Calculate the total number of characters
    total_characters = sum(len(word) for word in words)

    # Calculate the total number of words
    total_words = len(words)

    # Calculate the average word length
    average_word_length = total_characters / total_words if total_words > 0 else 0

    return average_word_length


def fetch_and_clean_text(text):
    stop_words_dir_path = 'stop_words'
    # Initialize an empty set for stop words
    stop_words = set()

    # Iterate over all files in the stop words directory
    for stop_words_file_name in os.listdir(stop_words_dir_path):
        stop_words_file_path = os.path.join(stop_words_dir_path, stop_words_file_name)
        with open(stop_words_file_path, 'r', encoding='latin-1') as stop_words_file:
            stop_words.update(word.lower() for word in stop_words_file.read().splitlines())

    # Tokenize the text into words
    words = text.split()

    # Remove punctuation from each word
    table = str.maketrans('', '', string.punctuation)
    stripped_words = [word.translate(table) for word in words]

    # Remove stop words
    cleaned_words = [word for word in stripped_words if word.lower() not in stop_words]

    # Join the cleaned words back into a single string
    cleaned_text = ' '.join(cleaned_words)

    return cleaned_text


def create_master_dictionary(cleaned_text):
    # Initialize sets for positive and negative words
    positive_words = list()
    negative_words = list()

    positive_words_path = "master_dictionary/positive-words.txt"
    negative_words_path = "master_dictionary/negative-words.txt"

    with open(positive_words_path, 'r', encoding='latin-1') as file:
        text = file.read()
        positive_words_list = word_tokenize(text)

    with open(negative_words_path, 'r', encoding='latin-1') as file:
        text = file.read()
        negative_words_list = word_tokenize(text)
    # Read the positive and negative words from the master dictionary files
    for word in word_tokenize(cleaned_text):
        word = word.lower()
        if word in positive_words_list:
            positive_words.append(word)
        elif word in negative_words_list:
            negative_words.append(word)

    return positive_words, negative_words


def calculate_scores(cleaned_text, positive_words, negative_words):
    # Tokenize the text
    tokens = word_tokenize(cleaned_text)

    # Calculate Positive Score
    positive_score = len(positive_words)

    # Calculate Negative Score
    negative_score = len(negative_words)

    # Calculate Polarity Score
    polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)

    # Calculate Subjectivity Score
    Total_Words_after_cleaning = len(tokens)

    subjectivity_score = (positive_score + negative_score)/ (Total_Words_after_cleaning + 0.000001)

    return positive_score, negative_score, polarity_score, subjectivity_score


def clean_and_count_words(text):
    # Tokenize the text
    tokens = word_tokenize(text)

    # Get the list of stop words
    stop_words = set(stopwords.words('english'))

    # Remove punctuation from each word
    table = str.maketrans('', '', string.punctuation)
    stripped_words = [word.translate(table) for word in tokens]

    # Remove stop words and empty strings (resulting from punctuation removal)
    cleaned_words = [word for word in stripped_words if word.lower() not in stop_words and word]

    # Count the cleaned words
    total_cleaned_words = len(cleaned_words)

    return total_cleaned_words, cleaned_words


