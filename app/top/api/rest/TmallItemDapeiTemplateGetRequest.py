'''
Created by auto_sdk on 2016.07.06
'''
from   app.top.api.base import RestApi
class TmallItemDapeiTemplateGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)

	def getapiname(self):
		return 'tmall.item.dapei.template.get'
