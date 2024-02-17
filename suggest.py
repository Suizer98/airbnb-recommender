import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.neighbors import BallTree


# Load the data with specified encoding
def suggest(input):
    encodings = ["utf-8", "latin1", "ISO-8859-1"]
    for encoding in encodings:
        try:
            data = pd.read_csv("mocksurveydata.csv", encoding=encoding)
            airbnb_data = pd.read_csv("airbnblistings.csv")
            tourist_spots_data = pd.read_csv("spot.csv", encoding="latin1")
            break
        except UnicodeDecodeError:
            continue

    # Split the data into features and target
    X = data["purpose"]
    y = data["destination"]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Create a pipeline with CountVectorizer and Multinomial Naive Bayes classifier
    model = make_pipeline(CountVectorizer(), MultinomialNB())

    # Train the model
    model.fit(X_train, y_train)

    # Example prediction
    new_user_purpose = [input]
    predicted_destination = model.predict(new_user_purpose)[0]

    # Find the coordinates of the predicted destination in tourist_spots_data
    tourist_spot_coordinates = tourist_spots_data[
        tourist_spots_data["Name"] == predicted_destination
    ][["latitude", "longitude"]].iloc[0]

    # Find the coordinates of Marina Bay Sands
    destination = tourist_spots_data[
        tourist_spots_data["Name"] == predicted_destination
    ]

    # Find the 10 nearest Airbnb listings to the coordinates of the predicted destination
    airbnb_coordinates = airbnb_data[["latitude", "longitude"]]
    tree = BallTree(airbnb_coordinates, leaf_size=15, metric="haversine")
    distances, indices = tree.query([tourist_spot_coordinates], k=10)

    # Get the nearest Airbnb listings with selected columns
    nearest_airbnb_listings = airbnb_data.iloc[indices[0]][
        ["name", "latitude", "longitude"]
    ]
    return nearest_airbnb_listings, destination
