import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import datetime
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
import plotly
from plotly.offline import init_notebook_mode



url='https://raw.githubusercontent.com/vrrani/COVID19-Singapore/master/Data/SingaporeCovid19RecoveryDatasetJan23-Apr01.csv'
df = pd.read_csv(url)

df


cip1=df[df['Date of +ve-confirm'].between('2020-01-23','2020-02-03',inclusive=True)]
dip1=df[df['Date of discharge'].between('2020-01-23','2020-02-03',inclusive=True)]
cip1=cip1[['Age','Gender','#Days-prehospital','#Days-hospital']]
dip1=dip1[['Age','Gender','#Days-prehospital','#Days-hospital']]


cip2=df[df['Date of +ve-confirm'].between('2020-02-04','2020-03-16',inclusive=True)]
dip2=df[df['Date of discharge'].between('2020-02-04','2020-03-16',inclusive=True)]
cip2=cip2[['Age','Gender','#Days-prehospital','#Days-hospital']]
dip2=dip2[['Age','Gender','#Days-prehospital','#Days-hospital']]


cip3=df[df['Date of +ve-confirm'].between('2020-03-17','2020-04-01',inclusive=True)]
dip3=df[df['Date of discharge'].between('2020-03-17','2020-04-01',inclusive=True)]
cip3=cip3[['Age','Gender','#Days-prehospital','#Days-hospital']]
dip3=dip3[['Age','Gender','#Days-prehospital','#Days-hospital']]


cip1


i=0
dataM1={}
dataF1={}
dataM2={}
dataF2={}
dataM3={}
dataF3={}
row1=cip1[cip1.Age.between(i,i+9,inclusive=True)]
rowm1=row1[row1.Gender=='M']
rowf1=row1[row1.Gender=='F']
row2=cip2[cip2.Age.between(i,i+9,inclusive=True)]
rowm2=row2[row2.Gender=='M']
rowf2=row2[row2.Gender=='F']
row3=cip3[cip3.Age.between(i,i+9,inclusive=True)]
rowm3=row3[row3.Gender=='M']
rowf3=row3[row3.Gender=='F']
dataM1[str(i)+'-'+str(i+9)]=len(rowm1['#Days-hospital'])
dataF1[str(i)+'-'+str(i+9)]=len(rowf1['#Days-hospital'])
dataM2[str(i)+'-'+str(i+9)]=len(rowm2['#Days-hospital'])
dataF2[str(i)+'-'+str(i+9)]=len(rowf2['#Days-hospital'])
dataM3[str(i)+'-'+str(i+9)]=len(rowm3['#Days-hospital'])
dataF3[str(i)+'-'+str(i+9)]=len(rowf3['#Days-hospital'])
for i in range(10,100,10):
    row1=cip1[cip1.Age.between(i,i+9,inclusive=True)]
    rowm1=row1[row1.Gender=='M']
    rowf1=row1[row1.Gender=='F']
    dataM1[str(i)+'-'+str(i+9)]=len(rowm1['#Days-hospital'])
    dataF1[str(i)+'-'+str(i+9)]=len(rowf1['#Days-hospital'])
    row2=cip2[cip2.Age.between(i,i+9,inclusive=True)]
    rowm2=row2[row2.Gender=='M']
    rowf2=row2[row2.Gender=='F']
    dataM2[str(i)+'-'+str(i+9)]=len(rowm2['#Days-hospital'])
    dataF2[str(i)+'-'+str(i+9)]=len(rowf2['#Days-hospital'])
    row3=cip3[cip3.Age.between(i,i+9,inclusive=True)]
    rowm3=row3[row3.Gender=='M']
    rowf3=row3[row3.Gender=='F']
    dataM3[str(i)+'-'+str(i+9)]=len(rowm3['#Days-hospital'])
    dataF3[str(i)+'-'+str(i+9)]=len(rowf3['#Days-hospital'])



i=0
dataMr1={}
dataFr1={}
dataMr2={}
dataFr2={}
dataMr3={}
dataFr3={}
row1=dip1[dip1.Age.between(i,i+9,inclusive=True)]
rowm1=row1[row1.Gender=='M']
rowf1=row1[row1.Gender=='F']
row2=dip2[dip2.Age.between(i,i+9,inclusive=True)]
rowm2=row2[row2.Gender=='M']
rowf2=row2[row2.Gender=='F']
row3=dip3[dip3.Age.between(i,i+9,inclusive=True)]
rowm3=row3[row3.Gender=='M']
rowf3=row3[row3.Gender=='F']
dataMr1[str(i)+'-'+str(i+9)]=len(rowm1['#Days-hospital'])
dataFr1[str(i)+'-'+str(i+9)]=len(rowf1['#Days-hospital'])
dataMr2[str(i)+'-'+str(i+9)]=len(rowm2['#Days-hospital'])
dataFr2[str(i)+'-'+str(i+9)]=len(rowf2['#Days-hospital'])
dataMr3[str(i)+'-'+str(i+9)]=len(rowm3['#Days-hospital'])
dataFr3[str(i)+'-'+str(i+9)]=len(rowf3['#Days-hospital'])
for i in range(10,100,10):
    row1=dip1[dip1.Age.between(i,i+9,inclusive=True)]
    rowm1=row1[row1.Gender=='M']
    rowf1=row1[row1.Gender=='F']
    dataMr1[str(i)+'-'+str(i+9)]=len(rowm1['#Days-hospital'])
    dataFr1[str(i)+'-'+str(i+9)]=len(rowf1['#Days-hospital'])
    row2=dip2[dip2.Age.between(i,i+9,inclusive=True)]
    rowm2=row2[row2.Gender=='M']
    rowf2=row2[row2.Gender=='F']
    dataMr2[str(i)+'-'+str(i+9)]=len(rowm2['#Days-hospital'])
    dataFr2[str(i)+'-'+str(i+9)]=len(rowf2['#Days-hospital'])
    row3=dip3[dip3.Age.between(i,i+9,inclusive=True)]
    rowm3=row3[row3.Gender=='M']
    rowf3=row3[row3.Gender=='F']
    dataMr3[str(i)+'-'+str(i+9)]=len(rowm3['#Days-hospital'])
    dataFr3[str(i)+'-'+str(i+9)]=len(rowf3['#Days-hospital'])


menR1_bins = np.negative(np.array(list(dataMr1.values())))
womenR1_bins = np.array(list(dataFr1.values()))
menR2_bins = np.negative(np.array(list(dataMr2.values())))
womenR2_bins = np.array(list(dataFr2.values()))
menR3_bins = np.negative(np.array(list(dataMr3.values())))
womenR3_bins = np.array(list(dataFr3.values()))


men1_bins = np.negative(np.array(list(dataM1.values())))
women1_bins = np.array(list(dataF1.values()))
men2_bins = np.negative(np.array(list(dataM2.values())))
women2_bins = np.array(list(dataF2.values()))
men3_bins = np.negative(np.array(list(dataM3.values())))
women3_bins = np.array(list(dataF3.values()))


print(women3_bins)
print(women2_bins)
print(women1_bins)
print(men3_bins)
print(men2_bins)
print(men1_bins)
print(womenR3_bins)
print(menR3_bins)
print(womenR2_bins)
print(menR2_bins)
print(womenR1_bins)
print(menR1_bins)

a=[-160,-150,-125,-100,-75,-50,-20,-10,-5,0,5,10,20,50,75,100,110,120]

y = list(dataF1.keys())
layout = go.Layout(yaxis=go.layout.YAxis(title='<b>Age Groups</b>'),
                   xaxis=go.layout.XAxis(
                       range=[-160, 120],
                       tickvals=a,
                       ticktext= [abs(ele) for ele in a],
                       title='<b>Total Number of Patients</b>'),
                   barmode='overlay',
                   font=dict(family='Times News Roman', size=16, color='black'),
                   bargap=0.2)

data = [go.Bar(y=y,
               x=women3_bins+women2_bins+women1_bins,
               orientation='h',
               name='#Confirmed Patients during P_3 (Mar 17,2020 - Apr 01,2020)',
               hoverinfo='x',
               marker=dict(color='#969696')
               ),
        go.Bar(y=y,
               x=women2_bins+women1_bins,
               orientation='h',
               name='#Confirmed Patients during P_2 (Feb 04,2020 - Mar 16,2020)',
               hoverinfo='x',
               marker=dict(color='#737373')
               ),
       go.Bar(y=y,
               x=women1_bins,
               orientation='h',
               name='#Confirmed Patients during P_1 (Jan 23,2020 - Feb 03,2020)',
               hoverinfo='x',
               marker=dict(color='#525252')
               ),
        go.Bar(y=y,
               x=men3_bins+men2_bins+men1_bins,
               orientation='h',
               text=-1 * men3_bins.astype('int'),
               hoverinfo='text',
               showlegend=False,
               marker=dict(color='#969696')
               ),
        go.Bar(y=y,
               x=men2_bins+men1_bins,
               orientation='h',
               text=-1 * men2_bins.astype('int'),
               hoverinfo='text',
               showlegend=False,
               marker=dict(color='#737373')
               ),
        go.Bar(y=y,
               x=men1_bins,
               orientation='h',
               text=-1 * men1_bins.astype('int'),
               hoverinfo='text',
               showlegend=False,
               marker=dict(color='#525252')
               )
       ]
choromap = go.Figure(dict(data=data, layout=layout))
choromap.layout.update(legend=dict(x=-.1, y=1.2))
choromap.update_xaxes(showline=True, linewidth=1, linecolor='black')
choromap.update_yaxes(showline=True, linewidth=1, linecolor='black')
plotly.offline.init_notebook_mode(connected=True)
plotly.offline.plot(choromap)


b=[-35,-30,-25,-20,-15,-10,-5,-3,0,3,5,10,15,20,25,30,35]


y = list(dataF1.keys())
layout = go.Layout(yaxis=go.layout.YAxis(title='<b>Age Groups</b>'),
                   xaxis=go.layout.XAxis(
                       range=[-35,35],
                       tickvals=b,
                       ticktext=[abs(ele) for ele in b],
                       title='<b>Total Number of Patients</b>'),
                   barmode='overlay',
                   font=dict(family='Times News Roman', size=16, color='black'),
                   bargap=0.2)

data = [go.Bar(y=y,
               x=womenR3_bins+womenR2_bins,
               orientation='h',
               name='#Clinically Recovered Patients during P_3 (Mar 17,2020 - Apr 01,2020)',
               hoverinfo='x',
               marker=dict(color='#d9d9d9')
               ),
        go.Bar(y=y,
               x=womenR2_bins,
               orientation='h',
               name='#Clinically Recovered Patients during P_2 (Feb 04,2020 - Mar 16,2020)',
               hoverinfo='x',
               marker=dict(color='#bdbdbd')
               ),
        go.Bar(y=y,
               x=menR3_bins+menR2_bins,
               orientation='h',
               text=-1 * menR3_bins.astype('int'),
               hoverinfo='text',
               showlegend=False,
               marker=dict(color='#d9d9d9')
               ),
        go.Bar(y=y,
               x=menR2_bins,
               orientation='h',
               text=-1 * menR2_bins.astype('int'),
               hoverinfo='text',
               showlegend=False,
               marker=dict(color='#bdbdbd')
               )
       ]
choromap = go.Figure(dict(data=data, layout=layout))
choromap.layout.update(legend=dict(x=-.1, y=1.2))
choromap.update_xaxes(showline=True, linewidth=1, linecolor='black')
choromap.update_yaxes(showline=True, linewidth=1, linecolor='black')
plotly.offline.init_notebook_mode(connected=True)
plotly.offline.plot(choromap)


print(dataM1.values())
print(dataF1.values())
print(dataM2.values())
print(dataF2.values())
print(dataM3.values())
print(dataF3.values())





