
"""

MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.




author email : 1037096435@qq.com



"""




from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Appkey(models.Model):
	appkey = models.CharField("appkey",max_length=16)
	secret = models.CharField("secret",max_length=32)
	session = models.CharField("授权码",max_length=64)
	codelength = models.BooleanField("编码方式",default=False)# 默认编码方式为短编码
	class Meta:
		verbose_name = "appkey淘宝API"
		verbose_name_plural= "appkey淘宝API"
	def __str__(self):
		return self.appkey



class User_ex(models.Model):
	belong = models.OneToOneField(User,related_name="User_ex",verbose_name="用户扩展")
	appkey = models.ForeignKey(Appkey,verbose_name="淘宝api",related_name="User_ex")




class Size(models.Model):
	belong = models.ForeignKey(User)
	name = models.CharField("尺码名称",max_length=10)
	value = models.CharField("尺码值",max_length=2)
	guid = models.CharField("guid",max_length=32)
	class Meta:
		verbose_name ="尺码类型"
		verbose_name_plural = '尺码类型'
	def __str__(self):
		return self.name





class Color(models.Model):
	belong = models.ForeignKey(User)
	name = models.CharField("颜色类型",max_length=16)
	value = models.CharField("颜色值",max_length=2)	
	guid = models.CharField("guid",max_length=32)
	pic_url = models.CharField("商品图片",null=True,max_length=128)

	class Meta:
		verbose_name="颜色类型"
		verbose_name_plural = '颜色类型'

	def __str__(self):
		return self.name


class Clothe(models.Model):
	belong = models.ForeignKey(User,verbose_name="产品类型",related_name="Clothe")
	name = models.CharField("衣服类型",max_length = 32)
	guid = models.CharField("唯一编码",max_length=32)  ###3 同时处理的一批可以是同样的编码
	color = models .ManyToManyField(Color,related_name="clothe")
	size = models.ManyToManyField(Size,related_name="clothe")
	value = models.CharField("类型值",max_length = 32)


	stock = models.PositiveIntegerField("衣服库存",default=10)
	class Meta:
		verbose_name = "纯色衣服"
		verbose_name_plural = '纯色衣服'
	def __str__(self):
		return self.name



class Pic(models.Model):
	belong = models.ForeignKey(User)
	pic_url = models.CharField("图片路径",max_length=64,null=True)
	name = models.CharField("名称",max_length=16)    #### 这个就是图片编码
	author = models.CharField("作者",max_length=16,default="zema")
	stock = models.PositiveIntegerField("图片库存",default=10)

	class Meta :
		verbose_name="画师图片"
		verbose_name_plural="画师图片"
	def __str__(self):
		return self.name

class ClotheSku(models.Model):
	belong = models.ForeignKey(User)
	clothe = models.ForeignKey(Clothe,related_name="ClotheSku",verbose_name="产品")
	color = models.ForeignKey(Color,related_name="ClotheSku",verbose_name="颜色")
	size=models.ForeignKey(Size,related_name="ClotheSku",verbose_name="尺码")
	class Meta:
		verbose_name="产品SKU"
		verbose_name_plural="产品SKU"
	def __str__(self):
		return self.clothe.name+"-"+self.color.name+"-"+self.size.name


class Commodity(models.Model):
	belong = models.ForeignKey(User)
	clothes = models.ManyToManyField(Clothe,verbose_name="产品",related_name="Clothe")
	num_iid = models.CharField("商品ID",unique = True,max_length=16)
	title = models.CharField("商品标题",max_length=32)
	pic_url = models.CharField("主图地址",max_length=128)
	od_outer_id = models.CharField("老主商品外部编码",max_length=32)
	onsale = models.BooleanField("商品是否在出售")
	sync = models .BooleanField("是否已同步",default=False)

	class Meta:
		verbose_name="商品信息"
		verbose_name_plural = '商品信息' 
	def __str__(self):
		return self.title


class SkuInner(models.Model):
	belong = models.ForeignKey(User)
	clothe_sku = models.ForeignKey(ClotheSku,related_name="SkuInner",verbose_name="sku里层")
	guid = models.CharField("唯一标识符",max_length=32)
	pic = models.ManyToManyField(Pic,verbose_name="包含图片",related_name="SkuInner")
	class Meta:
		verbose_name = "商品里层sku"
		verbose_name_plural = "商品里层sku"
	def __str__(self):
		return str(self.clothe_sku)+"---"+str(self.pic.all())









class SKU(models.Model):   ### 因为可能出现套装  一件商品 包含多个产品表层sku
	belong = models.ForeignKey(User)
	num_iid =  models.ForeignKey(Commodity,related_name="SKU")
	skuinner = models.ManyToManyField(SkuInner,verbose_name="多个产品",related_name="SKU")
	
	guid = models.CharField("唯一标识符",max_length=10,blank=True,default="" )
	sku_id = models.PositiveIntegerField("SKU_ID(淘宝编码)",unique = True)   ### 这里定唯一性

	pic_url = models.CharField("sku图片",max_length=128)
	long_guid = models.CharField("长SKU外部编码",max_length=64,blank=True)
	
	
	od_outer_id=models.CharField("老外部编码",max_length=32,blank=True,default="")
	od_size =models .CharField("老尺码信息",max_length=16)
	od_color = models.CharField("老颜色信息",max_length = 16)

	class Meta:
		verbose_name="现实SKU表层"
		verbose_name_plural="现实SKU表层"


	def __str__(self):
		return self.num_iid.title









