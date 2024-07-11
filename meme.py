import requests

api_key = '5aac42ee75mshd75d3ee03793a22p1c88b4jsna14c72eb6b72'
url = "https://reddit-meme.p.rapidapi.com/memes/trending"

headers = {
	"x-rapidapi-key": "5aac42ee75mshd75d3ee03793a22p1c88b4jsna14c72eb6b72",
	"x-rapidapi-host": "reddit-meme.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    meme_data = response.json()
    meme_url = meme_data['url']
    
    #readme updation
    with open('README.md', 'r') as file:
        readme_content = file.readlines()
        
    readme_content.append(f"\n![Random Dev Meme]({meme_url})\n")
    
    with open('README.md', 'w') as file:
        file.writelines(readme_content)
else:
    print("Failed to get meme")
    