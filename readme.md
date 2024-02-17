# Airbnb Destination Recommender

This project aims to recommend Airbnb listings based on a user's input regarding their purpose of visit. It utilizes a machine learning model to predict the destination based on the purpose specified by the user. It then finds the nearest Airbnb listings to the predicted destination and visualizes them on a map using Folium.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/suizer98/airbnb-recommender.git
Navigate to the project directory:

```
cd airbnb-destination-recommender
pip install -r requirements.txt
```

Usage
Run the suggest.py script to load the data, train the machine learning model, and provide Airbnb recommendations based on user input:

```
python suggest.py
```

The script will display the nearest Airbnb listings to the predicted destination and save a map visualization in an HTML file named map_destination.html.

## Files
suggest.py: Python script containing the recommendation logic and map visualization.
mocksurveydata.csv: CSV file containing mock survey data with purpose and destination columns.
airbnblistings.csv: CSV file containing Airbnb listings data with latitude and longitude information.
spot.csv: CSV file containing tourist spot data with latitude and longitude information.
requirements.txt: Text file containing the required Python packages.