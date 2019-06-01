from django.shortcuts import render

from pandas import pandas   #for storing the data

# Create your views here.
from .forms import ProductForm

from .models import personal_info_add


def product_create_view(request):
	form = ProductForm()
	if request.method == "POST":
		form = ProductForm(request.POST)
		if form.is_valid():
			personal_info_add.objects.create(**form.cleaned_data)
			df = pandas.DataFrame(form.cleaned_data,index=[0])
			df.to_csv('data.txt', header = True , index=False , sep='\t', mode='a')
			print(df)
			form = ProductForm()
	context = {
		'form' : form
	}
	return render(request,'user_add.html', context)
#	if request.method == "POST":
#		user_title = request.POST.get('title')
#		user_profession = request.POST.get('profession')
#		user_address = request.POST.get('address')
#	print(user_title)



#df = pandas.DataFrame([[1,2,3],[user_title,user_profession,user_address]])

