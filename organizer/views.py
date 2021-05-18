from django.shortcuts import render

# Create your views here.

# Startup List
def startup_list(request):
	return render(request,'organizer/startup_list.html')


# Startup Detail
def startup_detail(request):
	return render(request,'organizer/startup_detail.html')


# Tag list 
def tag_list(request):
	return render(request, 'organizer/tag_list.html')


# Tag detail page
def tag_detail(request):
	return render(request, 'organizer/tag_detail.html')




