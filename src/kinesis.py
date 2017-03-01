import boto3
import cPickle as pickle
import threading

class Kinesis:
	def __init__( self, stream, shards ):
		self._stream_name = stream
		self._shards = shards
		self._capacity = None
		self._stocks = None

	def stream_stock( self, stocks_info ):
		self._stocks = stocks_info
		self._capacity = len( self._stocks )
		self.responses = [None]*self._capacity
		self._threads = [None]*self._capacity

		for i, stock in enumerate( self._stocks ):
			self._s_id = i % len(self._shards)
			t = KinesisThreads( args=(self.responses, i, self._stream_name, self._shards[self._s_id], stock) )
			self._threads[i] = t
			t.start()

		for t in self._threads:
			t.join()
		
		return self.responses


class KinesisThreads( threading.Thread ):
	def __init__( self, args=() ):
		threading.Thread.__init__(self, group=None, target=None, name=None, verbose=None)
		self._responses, self._response_id ,self._stream_name, self._shard, self.stock = args
		self.client = boto3.client( 'kinesis' )

	def run( self ):
		self._response = self.client.put_record(
							StreamName = self._stream_name,
							Data = pickle.dumps(self.stock).encode('base64','strict'),
							PartitionKey = self._shard
						)
		self._temp = (
				self._response['ResponseMetadata']['HTTPHeaders']['date'],
				self._response['ResponseMetadata']['HTTPStatusCode'],
				self._response['ShardId'],
				self._response['SequenceNumber'], 
			)
		self._responses[self._response_id] = self._temp

	def join( self ):
		threading.Thread.join( self )
		return 1
