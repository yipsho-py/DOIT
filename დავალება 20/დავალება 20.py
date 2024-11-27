####### დავალება 20 ########

# import requests
# import json

# url = "https://rickandmortyapi.com/api/character"

# def fetch_characters(url):
#     characters = {}
#     while url:
#         response = requests.get(url).json()
#         for character in response['results']:
#             name = character['name']
#             episodes = [ep.split('/')[-1] for ep in character['episode']]
#             characters[name] = episodes
#         url = response.get('next')  
#     return characters

# characters_info = fetch_characters(url)

# with open('characters_episodes.json', 'w') as f:
#     json.dump(characters_info, f, indent=4)

# print("Data saved to 'characters_episodes.json'.")



####### დავალება 20 ########
