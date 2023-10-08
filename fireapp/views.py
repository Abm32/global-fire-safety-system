from django.shortcuts import render, redirect
from django.db import connection, transaction
import datetime
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect
import os

cursor = connection.cursor()

# Create your views here.

def fireapp(request):
	return render(request,'index.html')

 
def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        uploaded_image = request.FILES['image']

        # Specify the directory where you want to save the images
        upload_dir = '/home/abhi/Documents/GitHub/global-fire-safety-system/fireapp/media/'  # Change this to the actual path

        # Create the directory if it doesn't exist
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)

        # Save the uploaded image to the specified directory
        with open(os.path.join(upload_dir, uploaded_image.name), 'wb') as destination:
            for chunk in uploaded_image.chunks():
                destination.write(chunk)

        # After saving, you may want to redirect the user to a different page
        return HttpResponseRedirect(reverse('success_page'))  # You need to define 'success_page' in your urls.py

    return render(request, 'upload_page.html')  # You need to create an HTML template for the upload page


def success_page(request):
    return render(request, 'success_page.html')

