'''
Created by auto_sdk on 2016.02.29
'''
from   app.top.api.base import RestApi
class TmallProductSchemaGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.id = None

	def getapiname(self):
		return 'tmall.product.schema.get'
