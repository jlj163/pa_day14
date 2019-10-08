import requests

# http://music.163.com/song/media/outer/url?id=" + str(id[i]) + ".mp3

url = 'https://m10.music.126.net/20190927195901/1eca90ca4d218c44d8436a766fefb7a4/yyaac/050e/0008/065a/2d9e6712797bd04784bb1025b1da8583.m4a'
url = 'https://m10.music.126.net/20190927200235/ed62b9715e5b9533b27127ba1c3d8981/yyaac/560b/035d/5109/aa9316fc7647b003a62dfcce3ab3e0a2.m4a'
headers = {
    'Referer': 'https://music.163.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
res = requests.get(url=url,headers=headers).content
with open('花都开了.mp3','wb') as w:
    w.write(res)
