'''
Created by auto_sdk on 2016.07.07
'''
from   app.top.api.base import RestApi
class RegionWarehouseQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.store_code = None

	def getapiname(self):
		return 'taobao.region.warehouse.query'
