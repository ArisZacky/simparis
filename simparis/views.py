from django.shortcuts import render

def index(request):
	context = {
		"title":"Simparis Hotel",
		"heading":"Welcome to",
		"subheading":"Simparis Hotel",
    }
	return render(request,'index.html', context)