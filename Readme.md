#Stocks
##A quick demonstration of Amazon Kinesis Streams on NYSE Stocks.

In order to use AWS Kinesis on a fresh system, you'd need to run:

 - `aws configure`
 - And set your `access key`, `secret access key`, `default region` and `output format`

Dependent Libraries:

 - [boto3](https://github.com/boto/boto3)
 - [grequests](https://github.com/kennethreitz/grequests)
 - [BeautifulSoup](https://pypi.python.org/pypi/beautifulsoup4)

Adding on EC2 instance as a cron-job or as TaskQueue on GAE (with minor tweaks) are some ways this application can be deployed. 