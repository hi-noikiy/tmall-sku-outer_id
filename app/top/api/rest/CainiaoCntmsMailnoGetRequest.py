'''
Created by auto_sdk on 2016.05.11
'''
from   app.top.api.base import RestApi
class CainiaoCntmsMailnoGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.content = None

	def getapiname(self):
		return 'cainiao.cntms.mailno.get'
