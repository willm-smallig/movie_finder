import re

regex = r"^((https?://(www\.)?)|www\.)\w{3,}\.[a-z]{2,3}$"
findall = re.search(regex, "https://www.github.es")
print(findall)