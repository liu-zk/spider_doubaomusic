import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar

data = pd.read_excel('doubanmusic.xls')

def getsingerbar(data):
    singers_counts = data['singer'].value_counts()
    singers_counts.columns = ['singer', 'num']
    singers_counts = singers_counts.sort_values(ascending=True)
    c = (
        Bar()
        .add_xaxis(list(singers_counts.index)[-10:])
        .add_yaxis('singers', singers_counts.values.tolist()[-10:])
        .reversal_axis()
        .set_global_opts(
        title_opts=opts.TitleOpts(title='巅峰歌手榜'),
        yaxis_opts=opts.AxisOpts(name='singer'),
        xaxis_opts=opts.AxisOpts(name='num'),
        )
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .render('巅峰歌手榜.html')
        )
getsingerbar(data)
