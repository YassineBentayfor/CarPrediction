# CarPrediction
model.py provides the model that predictes the car prices from the dataset.cvs 
app.py is a simple flask app that used index.htlm
I want to run the app on a container by creating a Dockerfile and running: 
    docker build -t car-prediction .
    docker run -p 5000:5000 car-prediction
But erros pop in the building phase of the image.

  
