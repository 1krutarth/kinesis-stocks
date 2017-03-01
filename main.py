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