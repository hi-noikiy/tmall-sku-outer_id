'''
Created by auto_sdk on 2015.04.14
'''
from   app.top.api.base import RestApi
class TradeReceivetimeDelayRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.days = None
		self.tid = None

	def getapiname(self):
		return 'taobao.trade.receivetime.delay'
