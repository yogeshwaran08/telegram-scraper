import requests
from linkpreview import link_preview

def github_email_harvesting(username):
    response = requests.get(f'https://api.github.com/users/{username}')
    if response.status_code == 200:
        user_data = response.json()
        if user_data.get('email'):
            # print(f"The email address of {username} is: {user_data['email']}")
            return user_data["email"]
        else:
            # print(f"{username} has not made their email address public on GitHub.")
            return None
    else:
        # print(f"GitHub user {username} not found or the API request failed.")
        return None
        1
        
def github_validater(uname):
    link = f"https://github.com/{uname}"
    try:
        preview = link_preview(link)
        return f"https://github.com/{uname}"
        # print("Git Hub title",preview.title)
    except requests.exceptions.HTTPError:
        return None
