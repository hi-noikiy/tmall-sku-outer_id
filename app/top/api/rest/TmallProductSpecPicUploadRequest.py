'''
Created by auto_sdk on 2016.04.12
'''
from   app.top.api.base import RestApi
class TmallProductSpecPicUploadRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.certify_pic = None
		self.certify_type = None

	def getapiname(self):
		return 'tmall.product.spec.pic.upload'

	def getMultipartParas(self):
		return ['certify_pic']
