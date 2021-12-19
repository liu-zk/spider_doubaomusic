import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar

data = pd.read_excel('doubanmusic.xls')

def getzoombar(data):
    year_counts = data['time'].value_counts()
    print(year_counts)
    year_counts.columns = ['time', 'num']
    year_counts = year_counts.sort_index()
    c = (
        Bar()
        .add_xaxis(list(year_counts.index))
        .add_yaxis('num', year_counts.values.tolist())
        .set_global_opts(
            title_opts=opts.TitleOpts(title='上榜歌曲年份分布'),
            yaxis_opts=opts.AxisOpts(name='num'),
            xaxis_opts=opts.AxisOpts(name='time'),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_='inside')],)
        .render('上榜歌曲年份分布.html')
        )

getzoombar(data)