'''
Created by auto_sdk on 2016.07.15
'''
from   app.top.api.base import RestApi
class RegionPriceQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.item_id = None
		self.regional_price_dtos = None
		self.sku_id = None

	def getapiname(self):
		return 'taobao.region.price.query'
