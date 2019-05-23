import random as r
import urllib.request as url
#
def downloadImage(imageURL):
    name = str(r.randrange(1,1000))+'.jpg'
    url.urlretrieve(imageURL,name)
#
imageURL = "https://s.abcnews.com/images/Technology/black-hole-ht-ml-190410_hpMain_16x9_992.jpg"
downloadImage(imageURL)
