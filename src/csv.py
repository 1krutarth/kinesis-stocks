import csv

class CsvReader:
	def __init__( self, folder, csv_file ):
		self._path = '{}/{}'.format(folder, csv_file)
		self._capacity = 101	# taking row header into consideration; later ignored.
		self.stocks = [None] * self._capacity

	def _get_item( self, row ):
		# ['Symbol', 'Name', 'LastSale', 'MarketCap', 'IPOyear', 'Sector', 'industry', 'Summary Quote']
		return row[0]

	def _read_file():
		with open( self._path, 'r' ) as file_obj:
			contents = csv.reader( file_obj )
			for i in xrange( 1, self._capacity ): 	# ignoring header row
				self.stocks[i] = self._get_item( contents.next() )
			file_obj.close()

	def get_stocks():
		self._read_file()
		return self.stocks