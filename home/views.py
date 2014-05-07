from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Welcome to Scott's portal to FRED! Care to head to the <a href = '/search/'>search page</a>?")