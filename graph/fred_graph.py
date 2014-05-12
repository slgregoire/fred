import requests
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

def fred_grapher(search_text):
	url = 'http://api.stlouisfed.org/fred/series/search'
	
	request_params = {'search_text': search_text,
			  'api_key':'82101274da6dbda5de2d568e76b9d6a4',
			  'file_type':'json',
			  'limit':'10', #default value of number of search results to return
			  'order_by':'popularity' #results ordered by popularity are by default sorted in desc order
	 }			

	results = requests.get(url, params = request_params).json()
	df = pd.DataFrame(results['seriess'])

	#grabbing the series id of the most popular search result
	series_id = df.ix[0, 'id']
	
	#now onto the portion of the code that imports and graphs the observations of the most popular series 
	url_data = 'http://api.stlouisfed.org/fred/series/observations'
	
	request_params = {'series_id': series_id,
				 'api_key':'82101274da6dbda5de2d568e76b9d6a4',
				 'file_type':'json'
			 	 }
		
	#req_json holds the json data that the get request returns		 	 
	raw_data = requests.get(url_data, params = request_params)
		
	#req_json holds the parsed json data, converted into a python dictinoary
	data = raw_data.json()
		
	#req_df holds the parsed json in a pandas dataframe
	data = pd.DataFrame(data['observations'])
		
	#transforming data
	data.drop(['realtime_start', 'realtime_end'], axis = 1, inplace = True)
	data.loc[:,'value'] = data.loc[:, 'value'].astype(float)
	data.set_index(pd.to_datetime(data['date']), inplace = True)
	data.drop('date', axis = 1, inplace = True)

	#plot this data and save to object as a png file to be returned
	fig = plt.figure()
	ax = fig.add_subplot(111)

	data.value.plot(label = series_id)
	plt.legend(loc = 'best')

	plt.savefig('C:/Users/Scott Gregoire/Desktop/fred/static/chart_output.png')


		