'''
Created by auto_sdk on 2016.01.20
'''
from   app.top.api.base import RestApi
class WlbOrderdetailDateGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_time = None
		self.page_no = None
		self.page_size = None
		self.start_time = None

	def getapiname(self):
		return 'taobao.wlb.orderdetail.date.get'
