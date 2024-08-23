import requests
from bs4 import BeautifulSoup

def get_youtube_title(url):
    try:
        # Send a GET request to the YouTube video page
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the title tag
        title_tag = soup.find('title')

        if title_tag:
            # Extract the title and remove the " - YouTube" suffix
            full_title = title_tag.string
            video_title = full_title.rsplit(' - YouTube', 1)[0]
            return video_title
        else:
            return "Title not found"

    except requests.RequestException as e:
        return f"An error occurred: {e}"

# Example usage
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
title = get_youtube_title(url)
print(f"The title of the video is: {title}")