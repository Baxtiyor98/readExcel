from django.shortcuts import render
from .models import Person
from .resources import PersonReource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
def simple_upload(request):
    messages.debug(request, 'Test message...')
    if request.method =='POST':
        person_resource = PersonReource()
        dataset = Dataset()
        new_person=request.FILES['myfile']
        if not new_person.name.endswith('xlsx'):
            messages.error(request, 'wrong format')
            print('Xato format')
            return render(request,'file.html')
        imported_data=dataset.load(new_person.read(),format='xlsx')
        for data in imported_data:
            print(data)
            Person.objects.create(name=data[1],email=data[2],loaction=data[3])
    return render(request,'file.html')