'''
Created by auto_sdk on 2016.04.13
'''
from   app.top.api.base import RestApi
class FenxiaoProductQuantityUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.id = None
		self.properties = None
		self.quantity = None
		self.type = None

	def getapiname(self):
		return 'taobao.fenxiao.product.quantity.update'
