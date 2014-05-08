from django.template import RequestContext
from django.shortcuts import render_to_response

import fred_api

# Create your views here.

def search(request):
	context = RequestContext(request)
	result_list = []

	#send the search request to the FRED's API and return results
	if request.method == 'POST':
		search_text = request.POST['query'].strip()

		if search_text:
			searcher = fred_api.searcher()
			searcher('query')
			searcher.shorten_data()
			result_list = searcher.make_title_list()
			print result_list
			
	return render_to_response('search/base.html', {'result_list': result_list}, context)