'''
Created by auto_sdk on 2016.03.17
'''
from   app.top.api.base import RestApi
class PromotionActivityGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.activity_id = None

	def getapiname(self):
		return 'taobao.promotion.activity.get'
