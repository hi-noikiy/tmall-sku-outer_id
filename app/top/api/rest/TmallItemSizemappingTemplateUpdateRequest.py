'''
Created by auto_sdk on 2016.02.23
'''
from   app.top.api.base import RestApi
class TmallItemSizemappingTemplateUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.template_content = None
		self.template_id = None
		self.template_name = None

	def getapiname(self):
		return 'tmall.item.sizemapping.template.update'
