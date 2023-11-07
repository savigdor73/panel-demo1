import panel as pn
import pandas as pd
import numpy as np
from bokeh.plotting import figure

# Dashboard Page
class CyberIndexDashboard:
    np.random.seed(7)
    pn.extension('tabulator')
    #static variable: df
    df=pd.read_csv("cyber-security-indexes.csv")
    def __init__(self,index_col,values_col,values_header):
        self.id = values_col
        pivot_table=pd.pivot_table(self.df, index=index_col, values=values_col, aggfunc='mean')
        bar_chart = self.echarts_bar_chart(np.array(pivot_table.index.values),
                                           np.array(pivot_table[values_col].values), 
                                           values_header)
        self.a_dataframe = self.dataframe_show(pivot_table)
        row = [pn.Row(pn.Column(self.a_dataframe)), pn.Column(bar_chart)]
        col = pn.Column(row[0],row[1])
        self.content = col

    def dataframe_show(self,pivot_table):
        return pn.widgets.Tabulator(pivot_table)
    
    def echarts_bar_chart(self,x,y,y_title):
        echart_bar = {
            'title': {
                'text': y_title
            },
            'tooltip': {},
            'legend': {
                'data':['Index']
            },
            'xAxis': {
                'data': x.tolist()
            },
            'yAxis': {},
            'series': [{
                'name': 'Index',
                'type': 'bar',
                'data': y.tolist()
            }],
        };
        echart_pane = pn.pane.ECharts(echart_bar, height=480, width=640)
        return echart_pane


    def view(self):
        return self.content