import tushare as ts
import logging
import threading

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] %(name)s: %(levelname)s: %(message)s"
)

#print(ts.get_hist_data(code='000887',start='2017-02-01'))
#print(ts.sh_margin_details(start='2017-02-01', end='2017-02-19',symbol='600000'))

#print(ts.get_latest_news()) #默认获取最近80条新闻数据，只提供新闻类型、链接和标题

# content=ts.get_latest_news(top=5,show_content=True) #显示最新5条新闻，并打印出新闻内容
# pos=0
# for x in content.title:
#     logging.info(x + "-->" + content.url[pos])
#     pos +=1




# filename   = '002288'
# fileHandle = open ( filename+'.txt', 'w' )
# df = ts.get_today_ticks(filename)
# results = df.head(100)
# logging.info(results.to_string())
# fileHandle.write (results.to_string())
# fileHandle.close()
def getStock():
    # df = ts.get_realtime_quotes('002288')  # Single stock symbol
    # logging.info(df[['code', 'name', 'price', 'bid', 'ask', 'volume', 'amount', 'time']])
    df = ts.get_today_ticks('000887')
    logging.info(df.head(20))
while True:
    timer = threading.Timer(10,getStock)
    timer.start()
    timer.join()



# logging.info(ts.get_growth_data(2016,4))