'''
Created by auto_sdk on 2016.07.13
'''
from   app.top.api.base import RestApi
class OcTradetagsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.history = None
		self.tag_names = None
		self.tag_types = None
		self.tid = None

	def getapiname(self):
		return 'taobao.oc.tradetags.get'
