'''
Created by auto_sdk on 2016.04.13
'''
from   app.top.api.base import RestApi
class TmallProductSuitespecsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.cat_id = None
		self.id = None
		self.properties = None

	def getapiname(self):
		return 'tmall.product.suitespecs.get'
