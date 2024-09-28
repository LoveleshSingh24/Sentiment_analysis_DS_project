import requests
from bs4 import BeautifulSoup

def scrape_url(df):
    for index, row in df.iterrows():
        # Assuming the URL is in a column named 'URL'
        URL = row['URL']
        URL_ID = row['URL_ID']
        response = requests.get(URL)
        content = ''

        if response.status_code == 200:
            # Parse HTML content
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find and append the title of the page
            page_title = soup.title.string if soup.title else 'No title found'
            content += f"{page_title}\n"

            # Find and append all paragraphs
            paragraphs = soup.find_all('p')
            for p in paragraphs:
                content += p.get_text() + '\n'
        else:
            content = f"Failed to retrieve {URL} with status code {response.status_code}\n"

        # Save content to a text file using URL_ID as the filename

        filename = f"scrapped_data/{URL_ID}.txt"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)

        print(f"Content for URL_ID {URL_ID} saved to {filename}")