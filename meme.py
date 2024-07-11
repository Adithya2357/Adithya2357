import requests

api_key = '5aac42ee75mshd75d3ee03793a22p1c88b4jsna14c72eb6b72'
url = "https://reddit-meme.p.rapidapi.com/memes/trending"

headers = {
    "x-rapidapi-key": api_key,
    "x-rapidapi-host": "reddit-meme.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    meme_data = response.json()
    
    # Check the structure of the response
    if 'data' in meme_data and 'children' in meme_data['data']:
        memes = meme_data['data']['children']
        
        # Ensure there is at least one meme in the list
        if memes:
            meme_url = memes[0]['data']['url']
            
            # Read the README file
            with open('README.md', 'r') as file:
                readme_content = file.readlines()
                
            # Add the meme URL to the README content
            readme_content.append(f"\n![Random Dev Meme]({meme_url})\n")
            
            # Write the updated content back to the README file
            with open('README.md', 'w') as file:
                file.writelines(readme_content)
        else:
            print("No memes found in the response.")
    else:
        print("Unexpected response structure.")
else:
    print("Failed to get meme")
