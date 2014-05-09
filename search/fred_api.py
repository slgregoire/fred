import requests
import pandas as pd

def fred_searcher(search_text):
	url = 'http://api.stlouisfed.org/fred/series/search'
	
	request_params = {'search_text': search_text,
			  'api_key':'82101274da6dbda5de2d568e76b9d6a4',
			  'file_type':'json',
			  'limit':'10', #default value of number of search results to return
			  'order_by':'popularity' #results ordered by popularity are by default sorted in desc order
	 }			

	results = requests.get(url, params = request_params).json()
	df = pd.DataFrame(results['seriess'])
	
	#set of columns from complete dataset that we wish to retain.
	columns_to_keep = ['id',
			'title',
			'observation_start',
			'observation_end',
			'frequency',
			'units_short',
			'seasonal_adjustment_short']
	
	df = df.ix[:, columns_to_keep]
	title_list = df.ix[:, 'title']

	return title_list 
