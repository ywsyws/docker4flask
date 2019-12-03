import pandas as pd
import random
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


def create_figure():

    path = 'epldata_final.csv'
    df = pd.read_csv(path, sep=',')
    df = df[['name', 'nationality']]
    df = df.groupby(['nationality']).count().sort_values(by='name', ascending=False)
    df = df.head(10)

    # fig = Figure(figsize=(12,9))
    fig = Figure(figsize=(9,6))
    axis = fig.add_subplot(1,1,1, xlabel='Nationality')
    axis.tick_params(axis='x', labelsize=8)
    plt.setp(axis.xaxis.get_majorticklabels(), rotation=24)
    axis.bar(x=df.index, height=df.name)

    return fig
