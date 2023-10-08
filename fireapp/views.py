from django.shortcuts import render, redirect
from django.db import connection, transaction
import datetime
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect
import os
from .forms import ImageUploadForm
from .color import calculate_red_percentage

cursor = connection.cursor()

# Create your views here.

def fireapp(request):
	return render(request,'index.html')

 
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the uploaded file to a location
            uploaded_image = form.cleaned_data['image']
            image_path = f"static/images/{uploaded_image.name}"
            with open(image_path, 'wb') as destination:
                for chunk in uploaded_image.chunks():
                    destination.write(chunk)

            # Now, calculate the red percentage using your existing code
            red_percentage = calculate_red_percentage(image_path)
            print(f"Percentage of red color in the image: {red_percentage:.2f}%")

            return redirect('success')  # Redirect to a success page or handle as needed
    else:
        form = ImageUploadForm()

    return render(request, 'upload_image.html', {'form': form})

def success_page(request):
    return render(request, 'success_page.html')

