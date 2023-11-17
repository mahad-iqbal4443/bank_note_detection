Bank Note Authenticity Prediction
Overview
This project demonstrates a simple web-based application for predicting the authenticity of banknotes using machine learning. The system is divided into two main components:

FastAPI Backend:

A FastAPI backend serves as the prediction engine, exposing a RESTful API endpoint for receiving input data.
Utilizes a pre-trained machine learning model (loaded from model.pkl) to predict whether a given set of features corresponds to a genuine or fake banknote.
The API returns the prediction result in JSON format.
Streamlit Frontend:

A Streamlit web application provides an intuitive user interface for interacting with the prediction model.
Users can input various features related to a banknote (variance, skewness, curtosis, entropy) and trigger predictions with a single click.
The result is displayed in real-time, indicating whether the predicted banknote is classified as real or fake.
Technologies Used
FastAPI: A modern, fast, web framework for building APIs with Python 3.7+.
Streamlit: An open-source Python library for creating web applications with minimal code.
Pickle: Python module used for serializing and deserializing machine learning models.
Requests: A simple HTTP library for making requests to the FastAPI backend.