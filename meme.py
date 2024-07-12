import requests
import random

# RapidAPI credentials
api_key = '5aac42ee75mshd75d3ee03793a22p1c88b4jsna14c72eb6b72'
url = "https://programming-memes-images.p.rapidapi.com/v1/memes"


headers = {
	"x-rapidapi-key": api_key,
	"x-rapidapi-host": "programming-memes-images.p.rapidapi.com"
}


response = requests.get(url, headers=headers)

if response.status_code == 200:
    meme_data = response.json()
    
    # Check the structure of the response
    if 'data' in meme_data and 'children' in meme_data['data']:
        memes = meme_data['data']['children']
        
        # Ensure there is at least one meme in the list
        if memes:
            meme = random.choice(memes)
            meme_url = meme['data']['url']
            
            # Read the README file
            readme_file = 'README.md'
            with open(readme_file, 'r') as file:
                readme_content = file.readlines()
                
            # Flag to check if the placeholder was found and replaced
            placeholder_found = False

            # Replace the placeholder with the new meme URL
            with open(readme_file, 'w') as file:
                for line in readme_content:
                    if line.strip().startswith('![Random Dev Meme]'):
                        file.write(f'![Random Dev Meme]({meme_url})\n')
                        placeholder_found = True
                    else:
                        file.write(line)

            if not placeholder_found:
                print("Placeholder not found in README.md.")
            else:
                print("README.md updated successfully with the new meme URL.")
        else:
            print("No memes found in the response.")
    else:
        print("Unexpected response structure.")
else:
    print("Failed to get meme")
