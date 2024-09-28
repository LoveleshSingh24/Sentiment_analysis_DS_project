import os
import views
import handle_data as hd
import scrape_data as sd


print("\nProgram Started....\n")
input_df = hd.get_input_df()
output_df = hd.get_output_df()
output_df.set_index('URL_ID', inplace=True)
print("\nData Scrapping Started....\n")
sd.scrape_url(input_df)
print("\nData Scraped Successfully !\n")

folder_path = 'scrapped_data'
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        with open(file_path, 'r',  encoding='utf-8') as file:
            text = file.read()
        filename = file_path.split("\\")[-1]
        filename = filename.replace('.txt', '')
        print("Working on file : ",filename)
        total_pronouns = views.count_total_personal_pronouns(text)
        total_complex_words = views.num_of_complex_word(text)
        avg_syllable_per_word = views.calculate_syllable_counts(text)
        average_sentence_length, percentage_complex_words, fog_index = views.calculate_readability(text)
        average_words_per_sentence = views.calculate_average_words_per_sentence(text)
        average_word_length = views.calculate_average_word_length(text)
        cleaned_text = views.fetch_and_clean_text(text)
        filtered_positive_words, filtered_negative_words = views.create_master_dictionary(cleaned_text)
        positive_score, negative_score, polarity_score, subjectivity_score = views.calculate_scores(cleaned_text,
                                                                                                    filtered_positive_words,
                                                                                                    filtered_negative_words)
        total_cleaned_words, cleaned_words = views.clean_and_count_words(cleaned_text)

        output_df.loc[filename, 'POSITIVE SCORE'] = positive_score
        output_df.loc[filename, 'NEGATIVE SCORE'] = negative_score
        output_df.loc[filename, 'POLARITY SCORE'] = polarity_score
        output_df.loc[filename, 'SUBJECTIVITY SCORE'] = subjectivity_score
        output_df.loc[filename, 'AVG SENTENCE LENGTH'] = average_sentence_length
        output_df.loc[filename, 'PERCENTAGE OF COMPLEX WORDS'] = percentage_complex_words
        output_df.loc[filename, 'FOG INDEX'] = fog_index
        output_df.loc[filename, 'AVG NUMBER OF WORDS PER SENTENCE'] = average_words_per_sentence
        output_df.loc[filename, 'COMPLEX WORD COUNT'] = total_complex_words
        output_df.loc[filename, 'WORD COUNT'] = total_cleaned_words
        output_df.loc[filename, 'SYLLABLE PER WORD'] = avg_syllable_per_word
        output_df.loc[filename, 'PERSONAL PRONOUNS'] = total_pronouns
        output_df.loc[filename, 'AVG WORD LENGTH'] = average_word_length


output_df = output_df.round(2)
output_df = output_df.reset_index()
output_df.to_csv("input_output_data/output_data.csv")

print("\nDone...!")