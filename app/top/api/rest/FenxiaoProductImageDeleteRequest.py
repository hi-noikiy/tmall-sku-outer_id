'''
Created by auto_sdk on 2016.04.11
'''
from   app.top.api.base import RestApi
class FenxiaoProductImageDeleteRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.position = None
		self.id = None
		self.properties = None

	def getapiname(self):
		return 'taobao.fenxiao.product.image.delete'
