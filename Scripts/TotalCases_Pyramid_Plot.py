import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import datetime as dt
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
import plotly
from plotly.offline import init_notebook_mode


url='https://raw.githubusercontent.com/vrrani/COVID19-Singapore/master/Data/SingaporeCovid19RecoveryDatasetJan23-Apr01.csv'
#df = pd.read_excel('SingaporeCoviddataset.xlsx', sheet_name = 0)
parse_dates=['Date of +ve-confirm', 'Date of symptom onset', 'Date of discharge']
df = pd.read_csv(url, parse_dates=parse_dates)

ip=df[['Age','Gender','#Days-prehospital','#Days-hospital','Date of discharge']]


i=0
dataM={}
dataF={}
dataMr={}
dataFr={}
row=ip[ip.Age.between(i,i+9,inclusive=True)]
rowm=row[row.Gender=='M']
rowf=row[row.Gender=='F']
dataM[str(i)+'-'+str(i+9)]=len(rowm['#Days-hospital'])
dataF[str(i)+'-'+str(i+9)]=len(rowf['#Days-hospital'])
rowm=rowm[rowm['Date of discharge']!='2020-04-02']
rowf=rowf[rowf['Date of discharge']!='2020-04-02']
dataMr[str(i)+'-'+str(i+9)]=rowm['#Days-hospital'].count()
dataFr[str(i)+'-'+str(i+9)]=rowf['#Days-hospital'].count()
for i in range(10,100,10):
    row=ip[ip.Age.between(i,i+9,inclusive=True)]
    rowm=row[row.Gender=='M']
    rowf=row[row.Gender=='F']
    dataM[str(i)+'-'+str(i+9)]=len(rowm['#Days-hospital'])
    dataF[str(i)+'-'+str(i+9)]=len(rowf['#Days-hospital'])
    rowm=rowm[rowm['Date of discharge']!='2020-04-02']
    rowf=rowf[rowf['Date of discharge']!='2020-04-02']
    dataMr[str(i)+'-'+str(i+9)]=rowm['#Days-hospital'].count()
    dataFr[str(i)+'-'+str(i+9)]=rowf['#Days-hospital'].count()

dataMr['60-69']=15
print(dataM)
print(dataMr)


print(dataF)
print(dataFr)

womenR_bins = np.array(list(dataFr.values()))
menR_bins = np.negative(np.array(list(dataMr.values())))
women_bins =np.array(list(dataF.values()))
men_bins = np.negative(np.array(list(dataM.values())))
men_bins=men_bins-menR_bins
women_bins=women_bins-womenR_bins



y = list(dataF.keys())
layout = go.Layout(yaxis=go.layout.YAxis(title='<b>Age Groups</b>'),
                   xaxis=go.layout.XAxis(
                       range=[-155,120],
                       tickvals=[-155,-125,-115,-100,-85,-50,-30,-20,-10,-5,0,5,10,20,30,65,75,100,120],
                       ticktext=[155,125,115,100,85,50,30,20,10,5,0,5,10,20,30,65,75,100,120],
                       title='<b>Total Number of Patients</b>'),
                   barmode='overlay',
                   font=dict(family='Times News Roman', size=16, color='black'),
                   bargap=0.2)

data = [go.Bar(y=y,
               x=women_bins,
               orientation='h',
               name='#female patients (active)',
               hoverinfo='x',
               marker=dict(color='#d9d9d9')
               ),
        go.Bar(y=y,
               x=men_bins,
               orientation='h',
               name='#male patients (active)',
               text=-1 * men_bins.astype('int'),
               hoverinfo='text',
               marker=dict(color='#737373')
               ),
       go.Bar(y=y,
               x=womenR_bins,
               orientation='h',
               name='#female patients (clinically recovered)',
               hoverinfo='x',
               marker=dict(color='#f2f2f2')
               ),
        go.Bar(y=y,
               x=menR_bins,
               orientation='h',
               name='#male patients (clinically recovered)',
               text=-1 * menR_bins.astype('int'),
               hoverinfo='text',
               marker=dict(color='#999999')
               )]
choromap = go.Figure(dict(data=data, layout=layout))
choromap.layout.update(legend=dict(x=-.1, y=1.3))
choromap.update_xaxes(showline=True, linewidth=1, linecolor='black')
choromap.update_yaxes(showline=True, linewidth=1, linecolor='black')
plotly.offline.init_notebook_mode(connected=True)
plotly.offline.plot(choromap)


y = list(dataF.keys())
layout = go.Layout(yaxis=go.layout.YAxis(title='<b>Age Groups</b>'),
                   xaxis=go.layout.XAxis(
                       range=[-155,120],
                       tickvals=[-155,-125,-115,-100,-85,-50,-30,-20,-10,-5,0,5,10,20,30,65,75,100,120],
                       ticktext=[155,125,115,100,85,50,30,20,10,5,0,5,10,20,30,65,75,100,120],
                       title='<b>Total Number of Patients</b>'),
                   barmode='overlay',
                   font=dict(family='Times News Roman', size=16, color='black'),
                   bargap=0.2)

data = [go.Bar(y=y,
               x=women_bins+womenR_bins,
               orientation='h',
               name='#female patients (active)',
               hoverinfo='x',
               marker=dict(color='#DF65B0')
               ),
        go.Bar(y=y,
               x=men_bins+menR_bins,
               orientation='h',
               name='#male patients (active)',
               text=-1 * men_bins.astype('int'),
               hoverinfo='text',
               marker=dict(color='#08519C')
               ),
       go.Bar(y=y,
               x=womenR_bins,
               orientation='h',
               name='#female patients (clinically recovered)',
               hoverinfo='x',
               marker=dict(color='#EEAAD4')
               ),
        go.Bar(y=y,
               x=menR_bins,
               orientation='h',
               name='#male patients (clinically recovered)',
               text=-1 * menR_bins.astype('int'),
               hoverinfo='text',
               marker=dict(color='#86BFF9')
               )]
choromap = go.Figure(dict(data=data, layout=layout))
choromap.layout.update(legend=dict(x=-.1, y=1.3))
choromap.update_xaxes(showline=True, linewidth=1, linecolor='black')
choromap.update_yaxes(showline=True, linewidth=1, linecolor='black')
plotly.offline.init_notebook_mode(connected=True)
plotly.offline.plot(choromap)




