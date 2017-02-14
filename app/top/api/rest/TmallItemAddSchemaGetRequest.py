'''
Created by auto_sdk on 2015.09.11
'''
from   app.top.api.base import RestApi
class TmallItemAddSchemaGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.category_id = None
		self.isv_init = None
		self.id = None
		self.type = None

	def getapiname(self):
		return 'tmall.item.add.schema.get'
