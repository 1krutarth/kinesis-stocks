import copy
import grequests
from response import Response

class Request:
	def __init__( self, url, stocks, capacity ):
		self._capacity = capacity
		self._urls = [None]*self._capacity
		self._url = url + '{}'
		self._stocks = list(stocks)
		self.info = [None]*self._capacity

	def _generate_urls( self ):
		return ( self._url.format(stock) for stock in self._stocks )

	def _send_requests( self ):
		self._urls = self._generate_urls()
		self._req_objects = ( grequests.get(url) for url in self._urls )
		return grequests.imap( self._req_objects )

	def _generate_threads( self ):
		self._threads = [None]*self._capacity
		for i, response in enumerate(self._responses):
			t = Response( args=(response, self.info, i, self._stocks[i]) )
			self._threads[i] = t
			t.start()

		for t in self._threads:
			t.join()

		self._threads = None

	def get_url_info( self ):
		self._responses = self._send_requests()
		self._generate_threads()
		return copy.deepcopy(self.info)