'''
Created by auto_sdk on 2015.01.19
'''
from   app.top.api.base import RestApi
class RefundMessagesGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.page_no = None
		self.page_size = None
		self.refund_id = None
		self.refund_phase = None

	def getapiname(self):
		return 'taobao.refund.messages.get'
