'''
Created by auto_sdk on 2016.01.12
'''
from   app.top.api.base import RestApi
class WlbTradeorderGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.sub_trade_id = None
		self.trade_id = None
		self.trade_type = None

	def getapiname(self):
		return 'taobao.wlb.tradeorder.get'
