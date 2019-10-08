from wordcloud.wordcloud import WordCloud

with open('shenteng.txt','r',encoding='utf-8') as r:
    datas = r.read()

word_c = WordCloud(font_path='STXINWEI.TTF',width=1000,height=1000,margin=10,background_color='pink')
word_c.generate(datas)
word_c.to_file('shenten_ciyun.jpg')