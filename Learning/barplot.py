#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import plotly.plotly as py
from plotly.graph_objs import *

trace1 = {
  "y": ["0.42", "0.47", "0.55", "0.55", "0.61", "0.59"],
  "x": ["Naive Bayes", "Logistic Regression", "DT (entropy)", "DT (gini)","MLP", "SVM"],
  "marker": {"color": "rgb(58, 141, 199)"},
  "name": "Positif",
  #"orientation": "h",
  "type": "bar",
  "uid": "37661e"
}
trace2 = {
  "y": ["0.58", "0.53", "0.45", "0.45", "0.39", "0.41"],
  "x": ["Naive Bayes", "Logistic Regression", "DT (entropy)", "DT (gini)","MLP", "SVM"],
  "marker": {"color": "rgb(204, 204, 204)"},
  "name": "Négatif",
  #"orientation": "h",
  "type": "bar",
  "uid": "afc4b3"
}
data = Data([trace1, trace2])
layout = {
  "annotations": [
    {
      "x": 0.437384898711,
      "y": -0.0529197080292,
      "font": {
        "family": "Droid Serif, serif",
        "size": 14
      },
      "showarrow": False,
      "xref": "paper",
      "yref": "paper"
    }
  ],
  "autosize": False,
  "barmode": "stack",
  "height": 912,
  "legend": {
    "x": 0.597512416026,
    "y": 0.552581546358,
    "font": {"family": "Droid Serif, serif"},
    "xanchor": "left"
  },
  "margin": {
    "r": 2,
    "t": 125,
    "b": 125,
    "l": 50,
  },
  "showlegend": True,
  "width": 648,
  "yaxis": {
    "autorange": False,
    "range": [0.0, 1.0],
    "showgrid": False,
    "showline": True,
    "tickfont": {"family": "Droid Serif, serif"},
    "ticks": "outside",
    "titlefont": {"size": 14},
    "type": "-"
  },
  "xaxis": {
    "autorange": True,
    "range": [-0.5, 50.5],
    "showgrid": False,
    "tickfont": {
      "family": "Droid Serif, serif",
      "size": 12
    },
    "type": "category"
  }
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
