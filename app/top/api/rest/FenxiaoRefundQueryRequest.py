'''
Created by auto_sdk on 2014.04.14
'''
from   app.top.api.base import RestApi
class FenxiaoRefundQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_date = None
		self.page_no = None
		self.page_size = None
		self.query_seller_refund = None
		self.start_date = None

	def getapiname(self):
		return 'taobao.fenxiao.refund.query'
