'''
Created by auto_sdk on 2016.04.13
'''
from   app.top.api.base import RestApi
class FenxiaoDistributorsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.nicks = None

	def getapiname(self):
		return 'taobao.fenxiao.distributors.get'
