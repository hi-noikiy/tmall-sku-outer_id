'''
Created by auto_sdk on 2016.08.07
'''
from   app.top.api.base import RestApi
class CainiaoCloudprintMystdtemplatesGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)

	def getapiname(self):
		return 'cainiao.cloudprint.mystdtemplates.get'
