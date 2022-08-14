#!/usr/bin/env python3

from email.mime import image
from urllib.request import urlopen, urljoin
import re

def download_page(url):
    return urlopen(url).read().decode('utf-8')

def exctract_image_location(page):
    img_regex = re.compile('<img[^>]+src=["\'](.*?)["\']',re.IGNORECASE)
    return img_regex.findall(page)


if __name__ == "__main__":
    target_url = 'http://fitm.kmutnb.ac.th'
    site = download_page(target_url)
    image_locations = exctract_image_location(site)
    for src in image_locations:
        print(urljoin(target_url,src))

        