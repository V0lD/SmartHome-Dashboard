# -*- coding: utf-8 -*-
import plotly
from plotly.graph_objs import Scatter, Layout, Figure
import MySQLdb

db = MySQLdb.connect(host="localhost", user='heartnet', passwd='blackcat', db='SmartHome')
cursor = db.cursor()

query = """select CONVERT_TZ(YM_Timestamp, 'UTC', 'Australia/Sydney'), YM_Temperature, YM_Humidity from YoctoMeteo
  where YM_Timestamp > (now() - interval 1 day) group by UNIX_TIMESTAMP(YM_Timestamp) div 300"""

cursor.execute(query)

#for (YM_Timestamp, YM_Temperature, YM_Humidity) in cursor.fetchall():
#  print("T: {}, H: {} at {:%Y-%b-%d %H:%M}".format(YM_Temperature, YM_Humidity, YM_Timestamp))
rows = cursor.fetchall()

data = [Scatter(x=[row[0] for row in rows], y=[row[2] for row in rows], mode='lines'), Scatter(x=[row[0] for row in rows], y=[row[1] for row in rows], mode='lines', yaxis='y2')]

db.close()

plotly.offline.plot({
    "data": data,
    "layout": Layout(xaxis=dict(tickformat='%H:%M', nticks=12),
                     yaxis=dict(ticksuffix='%', tickfont=dict(color='rgb(31,119,180)')),
                     yaxis2=dict(ticksuffix=u'\u2103', tickfont=dict(color='rgb(255,127,14)'), overlaying='y', side='right'),
                     showlegend=False, margin=dict(t=30,b=30,l=50,r=50), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
}, show_link=False, filename='/var/www/html/graphs/Bedroom1.html')
