'''
Created by auto_sdk on 2016.05.19
'''
from   app.top.api.base import RestApi
class CainiaoCloudprintCustomaresGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.template_id = None

	def getapiname(self):
		return 'cainiao.cloudprint.customares.get'
