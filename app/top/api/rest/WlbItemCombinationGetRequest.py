'''
Created by auto_sdk on 2016.03.19
'''
from   app.top.api.base import RestApi
class WlbItemCombinationGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.item_id = None

	def getapiname(self):
		return 'taobao.wlb.item.combination.get'
