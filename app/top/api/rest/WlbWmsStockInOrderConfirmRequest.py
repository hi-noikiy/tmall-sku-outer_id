'''
Created by auto_sdk on 2015.09.17
'''
from   app.top.api.base import RestApi
class WlbWmsStockInOrderConfirmRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.content = None

	def getapiname(self):
		return 'taobao.wlb.wms.stock.in.order.confirm'
