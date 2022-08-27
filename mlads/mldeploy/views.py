#Importing the required libraries
from django.shortcuts import render 
import sklearn
from sklearn.preprocessing import LabelEncoder
from numpy import asarray
import numpy as np
from joblib import load

oe = LabelEncoder()

model = load("../model.joblib") #Importing the model

def index(request):
    return render(request, 'index.html')

def form(request):
    return render(request, 'forms.html')

def result(request):
        user_id = request.POST['user_id']
        category = request.POST['category']
        price = request.POST['price']
        event_type = request.POST['event_type']
        activity_count = request.POST['activity_count']
        day = request.POST['day']
        income = request.POST['income']
        age = request.POST['age']
        marriage_status = request.POST['marriage_status']
        profession = request.POST['profession']
        country = request.POST['country']

        pred = model.predict([[event_type, price, user_id, category, activity_count, income, age, marriage_status, profession, country, day]])

        if pred[0] == 3:
            return render(request, 'acer.html')
        elif pred[0] == 0:
            return render(request, 'samsung.html')
        elif pred[0] == 2:
            return render(request, 'huawei.html')
        elif pred[0] == 1:
            return render(request, 'xiaomi.html')
        elif pred[0] == 4:
            return render(request, 'apple.html')
        else:
            return render(request, 'others.html')
