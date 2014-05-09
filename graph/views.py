from django.shortcuts import render_to_response
from django.template import RequestContext
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

import fred_graph

# Create your views here.

def index(request):
	context = RequestContext(request)
	canvas = []

	if request.method == 'POST':
		search_text = request.POST['query'].strip()
		
		if search_text:
			df, series_id = fred_graph.fred_grapher(search_text)
			
			#plot this data and save to object to be passed to HttpResponse
			fig = plt.figure()
			ax = fig.add_subplot(111)

			df.value.plot(label = series_id)
			plt.legend(loc = 'best')

			canvas = FigureCanvas(fig)

	return render_to_response('graph/base.html', {'chart': canvas}, context)		



