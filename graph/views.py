from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

import fred_graph

# Create your views here.

def index(request):
	context = RequestContext(request)
	chart = [1]

	if request.method == 'POST':
		search_text = request.POST['query'].strip()
		
		if search_text:
			fred_graph.fred_grapher(search_text)
			'''return HttpResponse("<img src = 'C:/Users/Scott Gregoire/Desktop/fred/static/chart_output.png'> <p>return to <a href = '/graph/'>graph</a></p>")			
			'''

			return render_to_response('graph/chart.html', {'chart': chart}, context)

	return render_to_response('graph/base.html', {'chart': chart}, context)		



