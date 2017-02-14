
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



from django.shortcuts import render,get_object_or_404
from django.http import HttpRequest,HttpResponse ,HttpResponseRedirect,Http404,JsonResponse
from django.template import RequestContext
from datetime import datetime
import os ,json,re,time,random,hashlib
from app.models import *
import traceback as tk
import string
from django.db.models import Q as djangoQ ,QuerySet,Count
from django.contrib import auth
from zema_recognition import settings
from app.taobao import GetCommodity,Sku
from django.db.utils import IntegrityError


def logintest(fun):
    """  这个装饰器  是为了检测是否账户登录成功, 如未登录成功 将重定向到 登录页面"""

    def login(request):
        if request.user.is_authenticated():        
            return fun(request)
        else:
            return HttpResponseRedirect("/login/")    
    return login

@logintest
def get_3day(request):
    if request.user.is_authenticated() and request.method=="GET":

        comm = GetCommodity(request)
        req = comm.get_3day()
        if req:
            return HttpResponse(json.dumps({"code":"ok",
                "message":"最近3天新上传的商品已经更新完成!"}),content_type="application/json")




@logintest
def show_img(request):
    if request.user.is_authenticated() and request.method=="GET" :
        if "pid" in request.GET:
            pass
        elif "id" in request.GET:
            pass
    ur = os.path.join(settings.STATIC_URL,"app","image","1.jpg").replace("\\","/")

    return HttpResponse(open(ur,"rb"),content_type="image/png")







@logintest
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    # sku = SKU.objects.all()
    # for x in sku:
    #     print(x.od_size)
    if request.method =="POST" :
        comm = GetCommodity()
        req = comm.get_new(int(request.POST["newid"]))
        if req :
            x ="成功导入数据"
        else:
            x = "导入数据出错"
        return render(
            request,
            'app/index.html',
            context_instance = RequestContext(request,
            {

                'title':'首页',
                "x":x,
                'year':datetime.now().year,
            })
        )
    else:
        return render(
            request,
            'app/index.html',
            context_instance = RequestContext(request,
            {

                'title':'首页',
               
                'year':datetime.now().year,
            })
        )
@logintest
def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    sku = SKU.objects.filter(num_iid__num_iid="538509971701")
    # sku.group_by = ["od_color"]
    # sku =( QuerySet(query = sku, model = SKU) )
    print(sku)
    print(len(sku))
    for x in sku :
        print(x.od_size,x.od_color)
    






    return JsonResponse({"data":str(sku)})
@logintest
def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    if  request.user.is_authenticated() and request.method=="GET":
        
        if  "page" in request.GET and request.GET["page"]!="":
            try:
                page = int(request.GET["page"])
            except :
                page = 0
            else:
                if page < 0:
                    page = 0 
        else:
            page = 0
        index =[(30*page),(30*(page+1)-1)]



        q={}
        Q = djangoQ()
        if "wd" in request.GET and request.GET['wd'].isdigit():
            try:
                q["num_iid__exact"]= int( request.GET['wd'])                
            except:
                pass
         
        if "types" in request.GET :
            if request.GET["types"] =="0":
                q["sync"] = True
            elif request.GET["types"]=="1":
                q["sync"] = False              
        if "onsale" in request.GET :
            if request.GET["onsale"] =="1":
                q["onsale"] = True
            elif request.GET["onsale"]=="0":
                q["onsale"] = False
            
        for i in q:
            Q.add(djangoQ(**{i:q[i]}),Q.AND)



        comm = Commodity.objects.filter(Q).order_by("id")[index[0]:index[1]]
      

        return render(
            request,
            'app/about.html',
            context_instance = RequestContext(request,
            {
                'title':'商品列表',
              "comm":comm,
              "page":page,
                'year':datetime.now().year,
            })
        )
    else:
        return HttpResponseRedirect("/login/") 




def login(request):
    if request.method =="GET":
        if request.user.is_authenticated():
            return HttpResponseRedirect("/")
        return render(
                request,
                'app/login.html',
                {"title":"登录账户", 
               }
                                   )
    elif request.method == "POST":

        if "username" in request.POST and "password" in request.POST:
            if len(re.findall(r"\s",request.POST['username']))<= 0 or  len(re.findall(r"[\x3a-\x40]",request.POST['username'])) <= 0:
                username = request.POST['username']
                password = request.POST['password']
                user = auth.authenticate(username=username, password=password)
                if user is not None:
                    auth.login(request, user)    
                    
                    return HttpResponseRedirect("/")
                else:
                    return HttpResponseRedirect("/")
            else:
                return HttpResponseRedirect("/")
        else:
           return HttpResponseRedirect("/")
        return HttpResponseRedirect("/")
    return HttpResponseRedirect("/")



def register(request):
    if request.method =="GET":
        return render(request,"app/register.html",{"title":"账户注册"})
    elif request.method =="POST":
        if ("username" in request.POST and
            "password" in request.POST and
            "password1" in request.POST and 
            "appkey" in request.POST and
            "secret" in request.POST and
            "session" in request.POST ) and \
        (request.POST["username"] !="" and request.POST["password"]==request.POST["password1"] and
            request.POST["password"]!="" and request.POST["appkey"] !="" and
            request.POST["appkey"].isdigit()  and
            len(request.POST["session"])>32 and
            len(request.POST["secret"])==32):
            if request.POST["code"] =="long":
                code = True
            else:
                code = False
            try:
                appkey = Appkey.objects.get(appkey=request.POST["appkey"],secret=request.POST["secret"],session=request.POST["session"])
            except:
                Appkey(appkey=request.POST["appkey"],secret=request.POST["secret"],session=request.POST["session"],codelength = code).save()
                appkey = Appkey.objects.get(appkey=request.POST["appkey"],secret=request.POST["secret"])
            try:
                user = User.objects.create_user(username = request.POST['username'],password = request.POST['password1'])
                user.is_active = True  
                user.save()
            except:
                message = t.format_exc()
                return render(request,"app/register.html",{"title":"账户注册","error":"注册失败,%s"%message})

            username = request.POST['username']
            password = request.POST['password1']
            user = auth.authenticate( username=username, password=password )
            if user is not None:
                auth.login( request, user )

            User_ex(belong = request.user,appkey=appkey,).save()
            return HttpResponseRedirect("/")
        else:
            return render(request,"app/register.html",{"title":"账户注册","error":"注册失败,请认真填写必须的内容!"})














@logintest
def sync(request):
    if request.method =="GET":
        print("开始下载")

        ids =GetCommodity(request)
        comm = ids.get_all_commodity()
        return render(request,
            "app/commlist.html",
            { 
            'title':'商品列表',
                'comm':Commodity.objects.all()[:50],
                'year':datetime.now().year,
            })



        return HttpResponse(json.dumps({"code":"ok"}),content_type = "application/json")











@logintest

def detail(request):
    if  request.method=="GET" :
        
       
        if "id" in request.GET:
           
            objects = get_object_or_404(Commodity,id=int(request.GET["id"]))
            sku_lis = SKU.objects.filter(num_iid = objects)
            if len(sku_lis)==0:
                skus= Sku(request)
                sku_lis= skus.get_sku(objects.num_iid)
                for x in sku_lis:
                    

                    sku = SKU(belong=request.user,
                        num_iid=objects,
                        sku_id = x["sku_id"],
                        pic_url = x["url"],                
                        od_color = x["properties_name"].split(";")[0].split(":")[-1],
                        od_size =x["properties_name"].split(";")[1].split(":")[-1],)
                    if "outer_id" in x and x['outer_id'] is not None and x['outer_id']!="":
                        sku.od_outer_id = x["outer_id"]
                    sku.save()
            sku_lis = SKU.objects.filter(num_iid = objects,belong=request.user,)
            sku2 = []
            tt = []     
            for x in sku_lis:
                if x.od_color in tt:
                    continue
                else:

                    tt.append(x.od_color)
                    sku2.append({
                        "id":x.id,
                        "url":x.pic_url,
                        "od_color":x.od_color,
                        "od_size":x.od_size,
                        "od_outer_id":x.od_outer_id,
                                
                        "pic":x.pic_url})
            return render(request,"app/detail.html",{"title":"商品详情","comm":objects,"sku":sku2,
                "clothe":Clothe.objects.all()})
    if request.method=="POST" :
        if "id" in request.POST :
            objects = get_object_or_404(Commodity,id=int(request.POST["id"]))
            sku_lis = SKU.objects.filter(num_iid = objects)
            for x in sku_lis:
                x.delete()
            skus= Sku(request)
            sku_lis= skus.get_sku(objects.num_iid)
            for x in sku_lis:
                sku = SKU(
                    belong=request.user,
                    num_iid=objects,
                    sku_id = x["sku_id"],
                    pic_url = x["url"],                
                    od_color = x["properties_name"].split(";")[0].split(":")[-1],
                    od_size =x["properties_name"].split(";")[1].split(":")[-1],)
                if "outer_id" in x and x['outer_id'] is not None and x['outer_id']!="":
                    sku.od_outer_id = x["outer_id"]
                sku.save()
            return JsonResponse({"code":"ok"})

@logintest
def  addclothe(request):
    if request.user.is_authenticated() and request.method=="GET":
        return render(request,
            "app/add_clothe.html",
            {"title":"新建产品类型" }
            )
    elif request.user.is_authenticated() and request.method=="POST":
        try:
            color = json.loads(request.POST["color"])
            size =json.loads(request.POST["size"])
            name = request.POST["name"]
            code = request.POST["code"]
        except:
            print(tk.format_exc())

        
        guid = getguid()            
        Clothe(
            belong=request.user,
            name=name,
        
            guid = guid,
            value=code).save()
      
        clothe = get_object_or_404(Clothe,name=name,guid = guid,belong = request.user)
        for x in color:
            guid = getguid()
            Color(belong=request.user,name=x,value=color[x] ,guid=guid).save()
            clothe.color.add( get_object_or_404(Color,guid=guid))
        for x in size:
            guid = getguid()
            si = getsizename(x)
            Size(belong=request.user,name=si,value=size[x] ,guid=guid).save()
            clothe.size.add( get_object_or_404(Size,guid=guid))
        for c in clothe.color.all():
            for s in clothe.size.all():
                ClotheSku(belong=request.user,clothe = clothe,color=c,size=s).save()






        return HttpResponse(json.dumps({"code":"ok"}),content_type="application/json")
@logintest
def clothe(request):
    if request.user.is_authenticated() and request.method=="GET":
        return render(request,
            "app/clothe.html",
            {"title":"查看衣服类型",
            "clothe":Clothe.objects.all()}
            )






@logintest
def deal(request):
    if request.user.is_authenticated() and request.method == "GET":
        return render(request,"app/deal.html",{
            "title":"待处理交易列表"

            })



@logintest
def get_color(request):
    if request.user.is_authenticated() and request.method =="GET":
        if "id" in request.GET and request.GET["id"] .isdigit():
            color_objects = get_object_or_404(Clothe,id=int(request.GET["id"]),belong = request.user)
            color = color_objects.color.all()
            colors =[]
            for  x in color:
                colors.append(x.name)
            return HttpResponse(json.dumps(colors),content_type="application/json")




@logintest
def updata(request):

    if request.user.is_authenticated() and request.method =="POST":

        data = json.loads(request.POST["data"])  ##载入数据        
        for x in data:            
            clothes = []
            guid = getguid()
            try:
                sku = SKU.objects.get(id=int(x["skuid"]))
            except:
                raise Http404            
            sku2 = SKU.objects.filter(od_color=sku.od_color,num_iid=sku.num_iid,belong = request.user)
            for sku in sku2 :

                sku.skuinner.clear()
          
                si = getsizename(sku.od_size)
                if si =="NUL":
                    return JsonResponse({"code":"error","message":"淘宝编码尺码信息不能识别!!"})
                codes = []                
                for e in x["data"]:                 
                    try:
                        clothe = Clothe.objects.get(id=int(e["clothe"])) 
                        clothe_sku = ClotheSku.objects.get(clothe= clothe,color__name= e["color"],size__name=si,belong = request.user)                       
                    except:
                        raise Http404
                    
                    pic = [] 
                    pp = True
                    piccode = []
                    if len(e["code"])>0:
                        for p in e["code"]:
                            pic1 = Pic.objects.get_or_create(name=p,belong = request.user,
                                author = request.user.username)
                            piccode.append(p)
                            if pic1[1] and pp:
                                pp = True
                            else:
                                pp = False
                            pic .append(pic1[0])
                        if pp:
                            skuinner = pic[0].SkuInner.annotate(Count("pic"))
                            for skui in pic:
                                skuinner = skuinner.filter(pic=skui,belong = request.user)
                            skuinner = skuinner.filter(clothe_sku = clothe_sku,belong = request.user)
                            if len(skuinner)>1:
                                for sku2 in skuinner :
                                    if len(sku2.pic.all())==len(pic):
                                        skuinner = sku2
                                        break
                            if len(skuinner) != 1 or len(skuinner.pic.all()) != len(pic):                            
                                guid = getguid()
                                SkuInner(clothe_sku =clothe_sku,guid = guid ,belong = request.user).save()
                                skuinner = SkuInner.objects.get(clothe_sku = clothe_sku,guid=guid,belong = request.user)
                                for skui in pic :
                                    skuinner.pic.add(skui)
                        else:
                                guid = getguid()
                                SkuInner(clothe_sku =clothe_sku,guid = guid,belong = request.user ).save()
                                skuinner = SkuInner.objects.get(clothe_sku = clothe_sku,guid=guid,belong = request.user)
                                for skui in pic :
                                    skuinner.pic.add(skui)
                    else:
                        skuinner = SkuInner.objects.filter(clothe_sku = clothe_sku,belong = request.user,pic__isnull=True)
                        if len(skuinner)>0:
                            skuinner = skuinner[0]
                        else:
                            guid = getguid()
                            skuinner = SkuInner.objects.get_or_create(clothe_sku = clothe_sku,belong = request.user,guid=guid)[0]
                    
                    piccode = ",".join(piccode)
                    codes.append(clothe.value+clothe_sku.color.value+clothe_sku.size.value+":"+piccode) 
                    sku.skuinner.add(skuinner)
                long_guid = ";".join(codes)
                while True:
                    sort_guid = getguid(0)
                    try:
                        SKU.objects.get(guid = sort_guid,belong = request.user)
                        continue
                    except:                  
                        
                        sku.guid = sort_guid
                        if len(long_guid)>64 and request.user.User_ex.appkey.codelength :

                            sku.skuinner.clear()
                            return JsonResponse({"code":"error","message":"商品长编码生成过长,已经超过淘宝规定数值,请稍后再试"})
                        else:
                            if len(long_guid)>64:
                                sku.long_guid = ""
                            else:
                                sku.long_guid = long_guid
                            sku.save()
                            break
        up = Sku(request)
        rep = up.update(sku.num_iid.num_iid,request.user.User_ex.appkey.codelength)
        if rep:
            sku.num_iid.sync = True
            sku.num_iid.save()
            return HttpResponse(json.dumps({"code":"ok","message":"保存并更新成功"}),content_type="application/json")











       













    else:
        raise Http404
@logintest
def detail_sku(request):
    if request.user.is_authenticated() and request.method =="GET":
        if  "id" in request.GET:

            return render(request,
                "app/detail_2.html",
                {
                "title":"已存sku详情",
                "sku":SKU.objects.filter(num_iid_id=int(request.GET["id"]),belong = request.user),


                })
        else:
            raise Http404













def  getguid(i=1):
    if i ==0:
        return ''.join(random.sample(string.ascii_letters + string.digits, 10))
    else:

        tim = str(time.time())
        for x in range(5):
            tim = tim+str(random.uniform(0, 1))
        m =hashlib.md5()
        m.update(tim.encode("utf8"))
        return m.hexdigest()






def getsizename(size=None):
    sk = str(size).upper()
    if "3XS" in sk:
        si =  "3XS"
    elif "XXXS" in sk:
        si = "3XS"
    elif "2XS" in sk:
        si = "2XS"
    elif "XXS" in sk:
        si = "XXS"
    elif "XS" in sk:
        si = "0XS"
    elif "S" in sk:
        si = "00S"
    elif "M" in sk:
        si = "00M"  
    elif "6XL" in sk:
        si ="6XL"
    elif "XXXXXXL" in sk:
        si ="6XL"
    elif "5XL" in sk:
        si  = "5XL"
    elif "XXXXXL" in sk:
        si = "5XL"
    elif "4XL" in sk:
        si = "4XL"
    elif "XXXXL" in sk:
        si = "4XL"
    elif "3XL" in sk:
        si = "3XL"
    elif "XXXL" in sk:
        si = "3XL"
    elif "2XL" in sk:
        si = "2XL"
    elif "XXL" in sk:
        si = "2XL"
    elif "XL" in sk:
        si ="0XL"
    elif "L" in sk:
        si ="00L"
    else:
        si = "NUL"


    return si
