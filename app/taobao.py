

import app.top as top
from app.models import *
import datetime

import traceback as tk

class GetCommodity:
	def __init__(self,request):
		self.url = "http://gw.api.taobao.com/router/rest"
		self.port = "80"
		self.appkey = request.user.User_ex.appkey.appkey
		self.secret = request.user.User_ex.appkey.secret	
		self.session = request.user.User_ex.appkey.session
		self.user = request.user




	def get_onsale (self,page,star ="2000-01-01 00:00:00",end=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') ):
		req=top.api.ItemsOnsaleGetRequest(self.url,self.port)
		req.set_app_info(top.appinfo(self.appkey,self.secret))
		req.page_size="200"
		req.page_no=page
		req.start_modified = star
		req.end_modified=end
		 
		req.fields="num_iid,title,price,outer_id,pic_url"
	
		try:
			resp= req.getResponse(self.session)
			# print(resp)
			return resp['items_onsale_get_response']['items']['item']
			# print("总数:",len(resp['items_onsale_get_response']['items']['item']))

		except Exception as e:
			print(tk.format_exc())
	def get_invertory(self,page,star ="2000-01-01 00:00:00",end=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') ):
		req=top.api.ItemsInventoryGetRequest(self.url,self.port)
		req.set_app_info(top.appinfo(self.appkey,self.secret))
		 
		req.fields="num_iid,title,price,outer_id,pic_url"
		req.start_modified = star
		req.end_modified=end
		req.page_no=page
		req.page_size="200"
	
		try:
			resp= req.getResponse(self.session)
			# print(resp)
			print(len(resp['items_inventory_get_response']['items']['item']))
			return resp['items_inventory_get_response']['items']['item']
		except Exception as e:
			pass


	def get_all_commodity(self):
	
		for x in range(30):
			commodity = self.get_onsale(x)
			if  commodity is None:
				break
			for comm in commodity:
				try:
					Commodity(
						num_iid=comm["num_iid"],
						title = comm["title"],
						od_outer_id = comm["outer_id"],
						pic_url = comm["pic_url"],
						onsale = True,
						belong = self.user
						).save()
				except:
					pass
		for x in range(30):
			commodity = self.get_invertory(x)
			if  commodity is None:
				break
			for comm in commodity:
				try:
					Commodity(
						num_iid=comm["num_iid"],
						title = comm["title"],
						od_outer_id = comm["outer_id"],
						pic_url = comm["pic_url"],
						onsale = False,
						belong = self.user
						).save()
				except:
					pass
		return True
	def get_3day(self):
		for x in range(3):
			commodity = self.get_onsale(x,star=(datetime.datetime.now()-datetime.timedelta(days=3)).strftime('%Y-%m-%d %H:%M:%S'))
			if  commodity is None:
				break
			for comm in commodity:
				try:
					Commodity(
						num_iid=comm["num_iid"],
						title = comm["title"],
						od_outer_id = comm["outer_id"],
						pic_url = comm["pic_url"],
						onsale = True,
						belong = self.user
						).save()
				except:
					print(tk.format_exc())
		for x in range(3):
			commodity = self.get_invertory(x,star=(datetime.datetime.now()-datetime.timedelta(days=3)).strftime('%Y-%m-%d %H:%M:%S'))
			if  commodity is None:
				break
			for comm in commodity:
				try:
					Commodity(
						num_iid=comm["num_iid"],
						title = comm["title"],
						od_outer_id = comm["outer_id"],
						pic_url = comm["pic_url"],
						onsale = False,
						belong = self.user
						).save()
				except:
					pass
		return True


	def get_new(self,num_iid):

		req=top.api.ItemSellerGetRequest(self.url,self.port)
		req.set_app_info(top.appinfo(self.appkey,self.secret))
		 
		req.fields="pic_url,title,outer_id,approve_status,num_iid"
		req.num_iid=num_iid
		try:
			resp= req.getResponse(self.session)
			comm =resp['item_seller_get_response']["item"]
			if comm["approve_status"] =="onsale":
				onsale = True
			else:
				onsale =False
			try:
				Commodity(num_iid=comm["num_iid"],
					title = comm["title"],
					od_outer_id = comm["outer_id"],
					pic_url = comm["pic_url"],
					onsale = onsale,
					belong = self.user
					).save()
				return True
			except:
				return False
		except Exception as e:
			pass
			return False








class Sku:
	def __init__(self,request):
		self.url = "http://gw.api.taobao.com/router/rest"
		self.port = "80"
		self.appkey = request.user.User_ex.appkey.appkey
		self.secret = request.user.User_ex.appkey.secret	
		self.session = request.user.User_ex.appkey.session
		self.user = request.user

	def  get_detail(self,num_iid):
		pass


	def  get_sku(self,num_iid):
		req=top.api.ItemSellerGetRequest(self.url,self.port)
		req.set_app_info(top.appinfo(self.appkey,self.secret))
		import pprint
		req.fields="num_iid,prop_img,sku"
		req.num_iid=num_iid
		try:
			resp= req.getResponse(self.session)    
		except Exception as e:
			print(tk.format_exc())
			return 

		prop_imglis = resp["item_seller_get_response"]["item"]["prop_imgs"]["prop_img"]
		sku_lis = resp["item_seller_get_response"]["item"]["skus"]["sku"]
		img_list = {}		
		for x in prop_imglis:		   
			img_list[x["properties"]] = x["url"]
		for x in sku_lis:
			x["url"] = img_list[x["properties"].split(";")[0]]
		
		return sku_lis

	def update(self,num_iid,longs=False):
		try:
			num_iid = Commodity.objects.get(num_iid = num_iid,
						belong = self.user)
		except:
			return
		skus = num_iid.SKU.all()		
		sku_lis =[]
		for x in skus:
			if longs:
				code = x.long_guid
			else:
				code = x.guid
			sku_lis.append({
				"sku_id":x.sku_id,
				"outer_id":code

				})

		req=top.api.TmallItemOuteridUpdateRequest(self.url,self.port)
		req.set_app_info(top.appinfo(self.appkey,self.secret))
		 
		req.item_id=num_iid.num_iid

		req.sku_outers=str(sku_lis)
		# print(str(sku_lis))
		try:
			resp= req.getResponse(self.session)
			print(resp)
			if "tmall_item_outerid_update_response" in resp:
				return True


		except Exception as e:

			pass






