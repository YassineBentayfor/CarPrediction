# CarPrediction
model.py provides the model that predictes the car prices from the dataset.cvs 

app.py is a simple flask app that used index.html

The model.py work well in colab and here is the link for it: https://colab.research.google.com/drive/1pR6qYYCYPZd4WRYkoNFlkY4SjGcvd6LX#scrollTo=E0FIbFMqX-hH

I want to run the app on a container by creating a Dockerfile and running: 

    docker build -t car-prediction .
    
    docker run -p 5000:5000 car-prediction
    
But erros pop in the building phase of the image.

  
