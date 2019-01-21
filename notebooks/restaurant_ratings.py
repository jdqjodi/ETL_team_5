import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('paolapoblete', 'AH15of7VDbJeKyPbfnpS')
trace1 = {
  "x": ["Hicraft Kitchen", "Dukeâs Waikiki", "Marukame Udon", "Ono Seafood", "Helenaâs Hawaiian Food", "Tikis Grill & Bar", "Hula Grill Waikiki", "The Surfing Pig", "Tonkatsu Ginza Bairin", "The Pig & The Lady", "Royâs Waikiki", "Nicoâs Pier 38", "Tonkatsu Tamafuji", "Kona Brewing Company", "Steak Shack", "Cafe Asia", "Lucky Belly", "Musubi Cafe Iyasume", "Royâs Hawaii Kai", "Paia Fish Market Waikiki", "Haleiwa Joeâs", "Side Street Inn", "Moku Kitchen", "Tommy Bahama Restaurant | Bar | Store - Waikiki", "Off The Wall Craft Beer & Wine", "Uncle Boâs Pupu Bar & Grill", "Home Bar & Grill", "Aloha Table", "Raising Caneâs Chicken Fingers", "Piggy Smalls"], 
  "y": ["4", "4.5", "4.5", "4.5", "4", "4", "4.5", "4.5", "4", "4.5", "4", "4.5", "4", "4.5", "4", "4.5", "4.5", "4.5", "4.5", "4", "4", "4", "4.5", "4.5", "4", "4.5", "4", "4", "4", "4.5"], 
  "orientation": "h", 
  "type": "bar", 
  "xsrc": "paolapoblete:46:06631f", 
  "ysrc": "paolapoblete:46:1df8d9"
}
data = Data([trace1])
layout = {
  "autosize": True, 
  "title": {"text": "Ratings for Nearby Restaurants"}, 
  "xaxis": {
    "autorange": False, 
    "range": [-1.61111111111, 30.61], 
    "title": {"text": "Restaurants"}, 
    "type": "category"
  }, 
  "yaxis": {
    "autorange": True, 
    "range": [3.75, 4.75], 
    "title": {"text": "Yelp Ratings (out of 5)"}, 
    "type": "linear"
  }
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)