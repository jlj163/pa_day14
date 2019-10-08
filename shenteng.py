import time
import requests
from bs4 import BeautifulSoup
import jieba


headers = {
    'Cookie': 'SINAGLOBAL=5876008809418.709.1568203602184; Ugrow-G0=6fd5dedc9d0f894fec342d051b79679e; login_sid_t=063716dcd8c34a5c44995e633cb06ef1; cross_origin_proto=SSL; TC-V5-G0=04dc502e635144031713f186989293c7; _s_tentry=passport.weibo.com; wb_view_log=1536*8641.25; Apache=6015495991966.364.1569651044197; ULV=1569651044207:3:3:2:6015495991966.364.1569651044197:1569243630759; ALF=1601187001; SSOLoginState=1569651002; SUB=_2A25wiolqDeRhGeBK41QW9i3Pyz6IHXVT4f2irDV8PUNbmtAKLRXukW9NR281fSCmRv2RtIPXxvVx16pxy-L45PoM; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW12j-nM_wgKFqw8KlbjllK5JpX5KzhUgL.FoqX1hqNSoe0ehz2dJLoIEBLxKML1h-L1-eLxKqL1hMLB.qLxKML1K2L1--LxK.LB.2L1-qt; SUHB=0pHB_grHkcIpGJ; wvr=6; UOR=,,login.sina.com.cn; wb_view_log_6486763302=1536*8641.25; TC-Page-G0=b32a5183aa64e96302acd8febeb88ce4|1569651755|1569651517; webim_unReadCount=%7B%22time%22%3A1569651864072%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A34%2C%22msgbox%22%3A0%7D',
    'Host': 'weibo.com',
    'Referer': 'https://weibo.com/hejiong?is_search=0&visible=0&is_hot=1&is_tag=0&profile_ftype=1&page=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
pagebar = 0
page = 1
while page<4:
    print(pagebar)
    rnd = int(time.time()*1000)
    if pagebar == 2:
        page += 1
        pagebar = 0
    # url = 'https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100605&profile_ftype=1&is_all=1&pagebar='+str(pagebar)+'&pl_name=Pl_Official_MyProfileFeed__22&id=1006051782432341&script_uri=/shenteng&feed_type=0&page=1&pre_page=1&domain_op=100605&__rnd='+ str(rnd)
    url = 'https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100306&topnav=1&wvr=6&topsug=1&is_hot=1&pagebar='+str(pagebar)+'&pl_name=Pl_Official_MyProfileFeed__21&id=1003061195230310&script_uri=/hejiong&feed_type=0&page=' + str(page) + '&pre_page=1&domain_op=100306&__rnd='+ str(rnd)
    pagebar += 1
    res = requests.get(url=url,headers=headers).json()
    soup = BeautifulSoup(res['data'].strip(),'lxml')
    text_list = soup.find_all('div',class_='WB_text W_f14')

    for i in text_list:
        text = i.text.strip()
        text = text.replace(' ','')
        text = text.replace('，','')
        text = text.replace('？','')
        text = text.replace('#','')
        text = text.replace('@','')
        text = text.replace('\xa0','')
        text = text.replace('\u200b','')

        words = jieba.cut(text)
        words = list(words)
        print(words,'words')
        with open('hejiong.txt', 'a+', encoding='utf-8') as w:
            for j in words:
                w.write(j + '\n')
