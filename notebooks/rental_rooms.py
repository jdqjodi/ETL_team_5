import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('paolapoblete', 'AH15of7VDbJeKyPbfnpS')
trace1 = {
  "x": ["Hawaiian Monarch -Studio with Canal View/Partial Ocean View/Wifi", "Fresh Renovated Inn on the Park Studio near Beach with Park & Ocean Views!", "1009 KING BED Modern/Waikiki Beach", "Fully Renovated Condo by Ocean with Full Kitchen in Boutique Style Building", "Spacious 1BR with 180-Degree Ocean Views! Prime Waikiki Location!", "((( Ocean Views! ))) Newly Upgraded Studio!", "Waikiki Grand - Diamond Head & Ocean Views, Kitchenette & Lanai Free WiFi", "Fairway Villa 804 / Studio - Free Wifi, TV & Parking", "Grand Opening Discount - Renovated Studio - Awesome Unobstructed Ocean Views", "Easy Access to Amazing Beaches in this Beautiful Condo by the Sea", "Brand New Waikiki Diamond Head Favorite", "Wyndham Royal Garden Waikiki - Free WIFI In Room - Beautiful Views", "New Listing! Modern Condo on the 29th Floor in Waikiki with Incredible Views", "Charming Beachfront Studio at Waikiki Shore", "Paradise Dream in Hawaii å¤©å ä¹å¤¢", "Ocean View Penthouse Studio By The Beach With Huge Lanai And Great Amenities", "Diamond Head Beach - Queen Studio with Balcony - Ocean View", "BEST VALUE downtown Honolulu Executive Centre ocean view parking included", "Waikiki Hotel Studio @ Hawaiian Monarch Hotel Building", "Cozy Downtown Honolulu Apt w/ Pool Access by HPU!"], 
  "y": ["$85", "$75", "$90", "$85", "$120", "$90", "$118", "$135", "$125", "$99", "$94", "$110", "$99", "$180", "$108", "$82", "$135", "$160", "$75", "$96"], 
  "name": "Price per Night", 
  "orientation": "v", 
  "type": "bar", 
  "visible": True, 
  "xsrc": "paolapoblete:42:883b73", 
  "ysrc": "paolapoblete:42:00a588"
}
trace2 = {
  "x": ["Hawaiian Monarch -Studio with Canal View/Partial Ocean View/Wifi", "Fresh Renovated Inn on the Park Studio near Beach with Park & Ocean Views!", "1009 KING BED Modern/Waikiki Beach", "Fully Renovated Condo by Ocean with Full Kitchen in Boutique Style Building", "Spacious 1BR with 180-Degree Ocean Views! Prime Waikiki Location!", "((( Ocean Views! ))) Newly Upgraded Studio!", "Waikiki Grand - Diamond Head & Ocean Views, Kitchenette & Lanai Free WiFi", "Fairway Villa 804 / Studio - Free Wifi, TV & Parking", "Grand Opening Discount - Renovated Studio - Awesome Unobstructed Ocean Views", "Easy Access to Amazing Beaches in this Beautiful Condo by the Sea", "Brand New Waikiki Diamond Head Favorite", "Wyndham Royal Garden Waikiki - Free WIFI In Room - Beautiful Views", "New Listing! Modern Condo on the 29th Floor in Waikiki with Incredible Views", "Charming Beachfront Studio at Waikiki Shore", "Paradise Dream in Hawaii å¤©å ä¹å¤¢", "Ocean View Penthouse Studio By The Beach With Huge Lanai And Great Amenities", "Diamond Head Beach - Queen Studio with Balcony - Ocean View", "BEST VALUE downtown Honolulu Executive Centre ocean view parking included", "Waikiki Hotel Studio @ Hawaiian Monarch Hotel Building", "Cozy Downtown Honolulu Apt w/ Pool Access by HPU!"], 
  "y": ["108.5", "108.5", "108.5", "108.5", "108.5", "108.5", "108.5", "108.5", "108.5", "108.5", "108.5", "108.5", "108.5", "108.5", "108.5", "108.5", "108.5", "108.5", "108.5", "108.5"], 
  "mode": "lines", 
  "name": "Average Price", 
  "type": "scatter", 
  "xsrc": "paolapoblete:42:883b73", 
  "ysrc": "paolapoblete:42:dcf96e"
}
data = Data([trace1, trace2])
layout = {
  "autosize": True, 
  "hoverlabel": {"font": {"size": 9}}, 
  "margin": {"t": 92}, 
  "title": {
    "x": 0.5, 
    "font": {
      "family": "Open Sans", 
      "size": 23
    }, 
    "text": "<b>Rooms for Rent in Honolulu</b>"
  }, 
  "xaxis": {
    "autorange": True, 
    "range": [-0.5, 19.5], 
    "title": {"text": "Rental Room"}, 
    "type": "category"
  }, 
  "yaxis": {
    "autorange": True, 
    "range": [0, 189.473684211], 
    "title": {"text": "$ Price per Night"}
  }
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)