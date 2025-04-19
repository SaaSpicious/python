from bs4 import BeautifulSoup
import lxml
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

base_url = "https://www.billboard.com/charts/hot-100/"
credentials_file = "./credentials/spotify.cred"

def get_soup(request_url):
    # Download the web page
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
    webpage = requests.get(url=request_url,headers=header).text

    # Create BS4 out of the response.
    content = BeautifulSoup(webpage,"html.parser")

    return content

def read_credentials(credentials_file):
    api_keys = {}
    file = open(credentials_file, "r")
    lines = file.readlines()
    for line in lines:
        list = line.split("=")
        key = list[0].strip()
        value = list[1].strip()
        api_keys[key] = value
    return api_keys

# Uses a BeautifulSoup object and scrapes for song names
def scrape_songs_from_webpage(soup,count):
    song_names_spans = soup.select("li ul li h3")
    song_names = [song.getText().strip() for song in song_names_spans]
    del song_names[count:]
    return song_names

# Create the Spotify app via Spotipy
def authenticate_to_spotify(credentials):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=credentials["SPOTIFY_CLIENT_ID"],
                                                   client_secret=credentials["SPOTIFY_CLIENT_SECRET"],
                                                   redirect_uri="https://example.com/",
                                                   scope="playlist-modify-private",
                                                   show_dialog=True,
                                                   cache_path="token.txt",
                                                   username=credentials["SPOTIFY_DISPLAY_NAME"]
                                                   )
                         )
    return sp

# Extract the year from the query date as a string
def get_year_from_date(date):
    date_list = date.split("-")
    return date_list[0].strip()

# Searches for a single song in Spotify and returns the song uri of the first hit (if found)
def search_a_song(spotify_app,title,year):
    result = spotify_app.search(q='track: '+ title +',year: '+year,type='track')
    try:
        uri = result["tracks"]["items"][0]["uri"]
        print(f"Uri found for {title}: {uri}")
        return uri
    except IndexError:
        print(f"{title} doesn't exist in Spotify. Skipped.")
        return None

# Iterates through a list of songs and returns a list of song URIs
def search_for_songs(spotify_app,songs,year):
    song_uri_list = []
    for song in songs:
        song_uri = search_a_song(spotify_app, song, year)
        # Only append to list if None is not returned (which means the song was not found!)
        if song_uri:
            song_uri_list.append(song_uri)

    return song_uri_list

def create_spotify_playlist(spotify_app,song_uri_list,spotify_user_id,date):
    playlist_name = f"Billboard Top 10 from {date}"
    playlist = spotify_app.user_playlist_create(user=spotify_user_id,name=playlist_name,public=False,collaborative=False)
    playlist_id = playlist["id"]
    spotify_app.playlist_add_items(playlist_id=playlist_id,items=song_uri_list)


date = input("Which date you want to travel back to? (Format: YYYY-MM-DD) : ")
#date = "1987-04-24"
request_url = base_url + date
songs = scrape_songs_from_webpage(get_soup(request_url),50)
spotify_app = authenticate_to_spotify(read_credentials(credentials_file))
spotify_user_id = spotify_app.current_user()["id"]
year = get_year_from_date(date)

song_uri_list = search_for_songs(spotify_app,songs,year)

create_spotify_playlist(spotify_app,song_uri_list,spotify_user_id,date)