'''
Created by auto_sdk on 2016.07.07
'''
from   app.top.api.base import RestApi
class RegionSaleQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.item_id = None
		self.sale_region_level = None
		self.sku_id = None

	def getapiname(self):
		return 'taobao.region.sale.query'
