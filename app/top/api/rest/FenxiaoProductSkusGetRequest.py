'''
Created by auto_sdk on 2014.12.12
'''
from   app.top.api.base import RestApi
class FenxiaoProductSkusGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.id = None

	def getapiname(self):
		return 'taobao.fenxiao.product.skus.get'
