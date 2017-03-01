# from bs4 import BeautifulSoup as bsoup
# import grequests

# url = "https://www.google.com/finance?q=NYSE:MMM"
# html = requests.get()
# # stock value
# ux = [url,url]
# ureq = ( grequests.get(u, hooks={'response':print_text}) for u in ux )
# responses = grequests.map( ureq )
# def print_text( r, *args, **kwargs ):
# 	print( r.url )
# 	print( r.text )

# bx = soup.find_all( 'span', attrs={'class':'pr'} )

# data is dictionary
# a = cPickle.dumps(data).encode('base64','strict')
# cPickle.loads(a.decode('base64','strict') )

from ConfigParser import SafeConfigParser
from src import CsvReader, Request, Kinesis
import json

def main():
	parser = SafeConfigParser()
	parser.read( "config.ini" )

	capacity = parser.get( 'stocks', 'number' )
	
	folder = parser.get( 'csv', 'folder' )
	csv_file = parser.get( 'csv', 'filename' )
	csv = CsvReader( folder, csv_file, int(capacity) )
	stocks = iter( csv.get_stocks() )

	url = parser.get( 'stocks', 'url' )
	request = Request( url, stocks, int(capacity) )
	stock_info = request.get_url_info()

	# print stock_info

	stream = parser.get( 'kinesis', 'stream_name' )
	shards = json.loads( parser.get('kinesis', 'shards') )
	kinesis = Kinesis( stream, shards )
	responses = kinesis.stream_stock( stock_info )

	# print( responses )

	print('{},{},{},{},{},{}'.format('Timestamp','StatusCode','ShardId', 'Sequence Number', 'Stock', 'Stock Price'))
	for s,r in zip(stock_info,responses):
		t = ( s + r )
		print( ','.join(str(i) for i in t) )

if __name__ == '__main__':
	main()