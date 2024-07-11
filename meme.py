import requests
import random

api_key = '5aac42ee75mshd75d3ee03793a22p1c88b4jsna14c72eb6b72'
url = "https://reddit-meme.p.rapidapi.com/memes/trending"

headers = {
    "x-rapidapi-key": api_key,
    "x-rapidapi-host": "reddit-meme.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    meme_data = response.json()
    memes = meme_data['memes']  # Assuming 'memes' is the key that holds the list of memes
    random_meme = random.choice(memes)  # Select a random meme
    meme_url = random_meme['url']  # Assuming each meme has a 'url' key
    
    # Read the current content of README.md
    with open('README.md', 'r') as file:
        readme_content = file.readlines()
        
    # Insert the meme URL at the desired location
    for i, line in enumerate(readme_content):
        if line.strip() == "<!-- MEME_SECTION -->":
            readme_content.insert(i + 1, f"![Random Dev Meme]({meme_url})\n")
            break
    
    # Write the updated content back to README.md
    with open('README.md', 'w') as file:
        file.writelines(readme_content)
else:
    print("Failed to get meme")
