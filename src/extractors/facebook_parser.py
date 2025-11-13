thonimport requests
from bs4 import BeautifulSoup

def parse_facebook_profile(url):
    print(f"Parsing profile data from {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    profile = {
        'user_id': extract_user_id(soup),
        'profile': extract_bio(soup),
        'followers': extract_followers_count(soup),
        'contact': extract_contact_info(soup)
    }
    return profile

def extract_user_id(soup):
    user_id_tag = soup.find('meta', {'property': 'profile:profile_id'})
    return user_id_tag['content'] if user_id_tag else 'N/A'

def extract_bio(soup):
    bio_tag = soup.find('div', {'class': 'bio'})
    return bio_tag.text.strip() if bio_tag else 'No bio available'

def extract_followers_count(soup):
    followers_tag = soup.find('span', {'class': 'followers_count'})
    return followers_tag.text.strip() if followers_tag else '0'

def extract_contact_info(soup):
    contact_info = []
    email_tag = soup.find('a', {'href': 'mailto:'})
    if email_tag:
        contact_info.append(email_tag['href'].replace('mailto:', ''))
    return contact_info