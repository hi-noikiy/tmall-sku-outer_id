'''
Created by auto_sdk on 2016.08.24
'''
from   app.top.api.base import RestApi
class CainiaoCloudprintCustomareaUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.custom_area_content = None
		self.custom_area_id = None
		self.custom_area_name = None

	def getapiname(self):
		return 'cainiao.cloudprint.customarea.update'
