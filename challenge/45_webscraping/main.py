from bs4 import BeautifulSoup
import lxml
import requests

# The URL to retrieve movie titles from
url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Get Website Content and parse to BeautifulSoup Object
webpage = requests.get(url=url).text
content = BeautifulSoup(webpage,"html.parser")

# Check for titles in h3 elements and create a list
titles = content.find_all(name="h3",class_="title")
title_list = [title.getText() for title in titles]

# Although the list is sorted descending and would just need to flip around,
# let's treat the list as if it isn't sorted in ay way.
# All titles will be written inside a list
titles_sorted=[None] * 101
for title in title_list:
    try:
        movie_info = title.split(") ")
        movie_rank = int(movie_info[0])
        movie_title = movie_info[1]
    except:
        movie_info = title.split(": ")
        movie_rank = int(movie_info[0])
        movie_title = movie_info[1]
    titles_sorted[movie_rank] = movie_title

# Delete the first entry which will be of value 0
titles_sorted.pop(0)

# write this to a txt file
with open("./movies.txt","w") as file:
    for rank in range(100):
        string = f"{rank+1}. {titles_sorted[rank]}\n"
        try:
            file.write(string)
        # If there's invalid characters, just don't print anything, it's fine!
        except:
            print(string)
