from bs4 import BeautifulSoup
import threading

class Response(threading.Thread):
	"""Fetches page for url, extracts stock price."""
	def __init__( self, args=() ):
		threading.Thread.__init__(self, group=None, target=None, name=None, verbose=None)
		self._response, self._info, self._index, self.stock = args

	def run( self ):
		if( self._response.status_code == 200 ):
			self._content = self._response.text
			self._soup = BeautifulSoup( self._content, 'html.parser' )
			self._span_tag = self._soup.find_all( 'span', attrs={'class':'pr'} )[0]
			self._info[self._index] = (self.stock, self._span_tag.span.string)

	def join( self ):
		threading.Thread.join(self)
		# return 1;