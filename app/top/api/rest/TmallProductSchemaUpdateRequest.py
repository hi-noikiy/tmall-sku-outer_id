'''
Created by auto_sdk on 2015.10.15
'''
from   app.top.api.base import RestApi
class TmallProductSchemaUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.id = None
		self.xml_data = None

	def getapiname(self):
		return 'tmall.product.schema.update'
