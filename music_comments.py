
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar

data = pd.read_excel('doubanmusic.xls')

def getcommentsbar(data):
    df = data.sort_values(by='comments', ascending=True)
    c = (
        Bar()
        .add_xaxis(df['song'].values.tolist()[-20:])
        .add_yaxis('comments', df['comments'].values.tolist()[-20:])
        .reversal_axis()
        .set_global_opts(
            title_opts=opts.TitleOpts(title='歌曲热议榜'),
            yaxis_opts=opts.AxisOpts(name='song'),
            xaxis_opts=opts.AxisOpts(name='num'),
            datazoom_opts=opts.DataZoomOpts(type_='inside'),
            )
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .render('歌曲热议榜.html')
        )
getcommentsbar(data)