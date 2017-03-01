import csv
import os

class CsvReader:
	"""Reads CSV file containing NYSE stock information"""
	def __init__( self, folder, csv_file, capacity ):
		# self._path = os.path.join(os.getcwd(),folder,csv_file)
		self._path = '{}/{}'.format(folder, csv_file)
		self._capacity = capacity + 1	# taking row header into consideration; later ignored.
		self.stocks = [None] * self._capacity

	def _get_item( self, row ):
		# ['Symbol', 'Name', 'LastSale', 'MarketCap', 'IPOyear', 'Sector', 'industry', 'Summary Quote']
		return row[0]

	def _read_file( self ):
		with open( self._path, 'rb' ) as file_obj:
			contents = csv.reader( file_obj )
			for i in xrange(self._capacity): 	# ignoring header row
				self.stocks[i] = self._get_item( contents.next() )
			file_obj.close()

	def get_stocks( self ):
		self._read_file()
		return self.stocks[1:]