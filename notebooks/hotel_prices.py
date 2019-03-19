import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('paolapoblete', 'AH15of7VDbJeKyPbfnpS')
trace1 = {
  "x": ["Holiday Inn Express Waikiki", "Hotel La Croix", "The Modern Honolulu", "Outrigger Waikiki Beach Resort", "Vive Hotel Waikiki", "Hilton Waikiki Beach", "Holiday Inn Express Waikiki", "Shoreline Hotel Waikiki", "Hyatt Regency Waikiki Beach Resort & Spa", "Alohilani Resort Waikiki Beach", "Park Shore Waikiki", "Hyatt Place Waikiki Beach", "Coconut Waikiki Hotel", "Aqua Oasis", "Hyatt Centric Waikiki Beach", "Outrigger Reef Waikiki Beach Resort", "Moana Surfrider, A Westin Resort & Spa, Waikiki Beach", "The Surfjack Hotel & Swim Club", "Embassy Suites by Hilton Waikiki Beach Walk", "Waikiki Resort Hotel", "Waikiki Beachcomber by Outrigger", "Royal Grove Hotel", "Luana Waikiki Hotel & Suites", "Ilikai Hotel & Luxury Suites", "The New Otani Kaimana Beach Hotel", "Hilton Garden Inn Waikiki Beach", "Lotus Honolulu at Diamond Head", "Sheraton Waikiki", "The Kahala Hotel & Resort", "Trump International Hotel Waikiki", "The Ritz-Carlton Residences, Waikiki Beach"], 
  "y": ["227", "198", "313", "328", "250", "245", "227", "211", "290", "322", "190", "232", "213", "185", "264", "264", "393", "247", "401", "178", "290", "131", "237", "321", "297", "231", "207", "573", "664", "528", "597"], 
  "name": "Price Per Night", 
  "orientation": "v", 
  "type": "bar", 
  "uid": "6334d0", 
  "xsrc": "paolapoblete:44:043510", 
  "ysrc": "paolapoblete:44:a71ea1"
}
trace2 = {
  "x": ["Holiday Inn Express Waikiki", "Hotel La Croix", "The Modern Honolulu", "Outrigger Waikiki Beach Resort", "Vive Hotel Waikiki", "Hilton Waikiki Beach", "Holiday Inn Express Waikiki", "Shoreline Hotel Waikiki", "Hyatt Regency Waikiki Beach Resort & Spa", "Alohilani Resort Waikiki Beach", "Park Shore Waikiki", "Hyatt Place Waikiki Beach", "Coconut Waikiki Hotel", "Aqua Oasis", "Hyatt Centric Waikiki Beach", "Outrigger Reef Waikiki Beach Resort", "Moana Surfrider, A Westin Resort & Spa, Waikiki Beach", "The Surfjack Hotel & Swim Club", "Embassy Suites by Hilton Waikiki Beach Walk", "Waikiki Resort Hotel", "Waikiki Beachcomber by Outrigger", "Royal Grove Hotel", "Luana Waikiki Hotel & Suites", "Ilikai Hotel & Luxury Suites", "The New Otani Kaimana Beach Hotel", "Hilton Garden Inn Waikiki Beach", "Lotus Honolulu at Diamond Head", "Sheraton Waikiki", "The Kahala Hotel & Resort", "Trump International Hotel Waikiki", "The Ritz-Carlton Residences, Waikiki Beach"], 
  "y": ["298.516129", "298.516129", "298.516129", "298.516129", "298.516129", "298.516129", "298.516129", "298.516129", "298.516129", "298.516129", "298.516129", "298.516129", "298.516129", "298.516129", "298.516129", "298.516129", "298.516129", "298.516129", "298.516129", "298.516129", "298.516129", "298.516129", "298.516129", "298.516129", "298.516129", "298.516129", "298.516129", "298.516129", "298.516129", "298.516129", "298.516129"], 
  "mode": "lines", 
  "name": "Average Price", 
  "type": "scatter", 
  "uid": "423bce", 
  "xsrc": "paolapoblete:44:043510", 
  "ysrc": "paolapoblete:44:8e1841"
}
data = Data([trace1, trace2])
layout = {
  "autosize": True, 
  "font": {
    "family": "Overpass", 
    "size": 12
  }, 
  "title": {
    "text": "Hotel Prices in Honolulu", 
    "font": {"size": 25}
  }, 
  "xaxis": {
    "autorange": True, 
    "range": [-0.5, 29.5], 
    "title": {"text": "Hotels"}, 
    "type": "category"
  }, 
  "yaxis": {
    "autorange": True, 
    "range": [0, 698.947368421], 
    "title": {"text": "$ CAD Per Night"}, 
    "type": "linear"
  }
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)