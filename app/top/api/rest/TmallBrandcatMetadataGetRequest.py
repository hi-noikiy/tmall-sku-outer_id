'''
Created by auto_sdk on 2016.04.14
'''
from   app.top.api.base import RestApi
class TmallBrandcatMetadataGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.brand_id = None
		self.cat_id = None

	def getapiname(self):
		return 'tmall.brandcat.metadata.get'
