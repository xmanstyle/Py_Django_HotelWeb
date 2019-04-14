# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import re
import os,sys
import base64
import time
import hashlib
import collections

from django.conf import settings
from .models import *


# 获取当前时间的13 毫秒字符串
cur_time = lambda:str(int(round(time.time()*1000)))

# 主页获取---------------------------------------------- 普通用户的数据请求 -------------------
def web(request):
	pg_cur = 1
	pg_size = 4
	pg_all = 0
	spg_all = 0
	rlist = []
	slist = []
	rpage = collections.OrderedDict()
	spage = collections.OrderedDict()
	all_list = Tabroom.objects.order_by('id').all()
	sall_list = Tabspe.objects.order_by('id').all()
	# room pageall------------------------ get room page
	if len(all_list)%pg_size == 0:
		pg_all = int(len(all_list)/pg_size)
	else:
		pg_all = int(len(all_list)/pg_size)+1
	if pg_cur<=int(pg_all):
		# foot page
		# <<
		if pg_cur!=1:
			rpage['pre'] = pg_cur-1
		else:
			rpage['pre'] = -1
		# cur
		rpage['cur'] = pg_cur 

		# >>
		if pg_cur < pg_all:
			rpage['nex'] = pg_cur+1
		else:
			rpage['nex'] = -1

		# page content
		start_index = 0
		if pg_cur>1:
			start_index = (pg_cur-1)*pg_size
		add_pg = 0
		while add_pg<pg_size:
			rlist.append(all_list[start_index])
			start_index += 1
			add_pg += 1
			if start_index == len(all_list):
				break
	# spe pageall------------------------------ get spe page
	if len(sall_list)%pg_size == 0:
		spg_all = int(len(sall_list)/pg_size)
	else:
		spg_all = int(len(sall_list)/pg_size)+1
	if pg_cur<=int(spg_all):
		# foot page
		# <<
		if pg_cur!=1:
			spage['pre'] = pg_cur-1
		else:
			spage['pre'] = -1
		# cur
		spage['cur'] = pg_cur 
		# >>
		if pg_cur < pg_all:
			spage['nex'] = pg_cur+1
		else:
			spage['nex'] = -1

		start_index = 0
		if pg_cur>1:
			start_index = (pg_cur-1)*pg_size
		add_pg = 0
		while add_pg<pg_size:
			slist.append(sall_list[start_index])
			start_index += 1
			add_pg += 1
			if start_index == len(sall_list):
				break
	return render(request,'room.html',{'rlist':rlist,'rpage':rpage,'slist':slist,'spage':spage})

# 房间分页数据获取
def room(request):
	pg_cur = int(request.GET.get('curpg',1))
	pg_size = 4
	pg_all = 0
	rlist = []
	rpage = collections.OrderedDict()
	all_list = Tabroom.objects.order_by('id').all()
	if len(all_list)%pg_size == 0:
		pg_all = int(len(all_list)/pg_size)
	else:
		pg_all = int(len(all_list)/pg_size)+1
	# 请求页不合法，返回空
	if pg_cur<1 or pg_cur>int(pg_all):
		return render(request,'ro.html',{'rlist':rlist,'rpage':rpage})

	# foot page
	# <<
	if pg_cur!=1:
		rpage['pre'] = pg_cur-1
	else:
		rpage['pre'] = -1
	# cur
	rpage['cur'] = pg_cur 

	# >>
	if pg_cur < pg_all:
		rpage['nex'] = pg_cur+1
	else:
		rpage['nex'] = -1

	start_index = 0
	if pg_cur>1:
		start_index = (pg_cur-1)*pg_size
	add_pg = 0
	while add_pg<pg_size:
		rlist.append(all_list[start_index])
		start_index += 1
		add_pg += 1
		if start_index == len(all_list):
			break
	return render(request,'ro.html',{'rlist':rlist,'rpage':rpage})

# 特产分页信息获取
def spe(request):
	pg_cur = int(request.GET.get('curpg',1))
	pg_size = 4
	pg_all = 0
	slist = []
	spage = collections.OrderedDict()
	all_list = Tabspe.objects.order_by('id').all()
	if len(all_list)%pg_size == 0:
		pg_all = int(len(all_list)/pg_size)
	else:
		pg_all = int(len(all_list)/pg_size)+1

	if pg_cur<1 or pg_cur>int(pg_all):
		return render(request,'spe.html',{'slist':slist,'spage':spage})

	# foot page
	# <<
	if pg_cur!=1:
		spage['pre'] = pg_cur-1
	else:
		spage['pre'] = -1
	# cur
	spage['cur'] = pg_cur 
	# >>
	if pg_cur < pg_all:
		spage['nex'] = pg_cur+1
	else:
		spage['nex'] = -1

	start_index = 0
	if pg_cur>1:
		start_index = (pg_cur-1)*pg_size
	add_pg = 0
	while add_pg<pg_size:
		slist.append(all_list[start_index])
		start_index += 1
		add_pg += 1
		if start_index == len(all_list):
			break
	return render(request,'spe.html',{'slist':slist,'spage':spage})

# 菜色 分页数据获取
def food(request):
	pg_cur = int(request.GET.get('curpg',1))
	pg_size = 4
	pg_all = 0
	flist = []
	fpage = collections.OrderedDict()
	all_list = Tabfood.objects.order_by('id').all()
	if len(all_list)%pg_size == 0:
		pg_all = int(len(all_list)/pg_size)
	else:
		pg_all = int(len(all_list)/pg_size)+1

	if pg_cur<1 or pg_cur>int(pg_all):
		return render(request,'food.html',{'flist':flist,'fpage':fpage})

	# foot page
	# <<
	if pg_cur!=1:
		fpage['pre'] = pg_cur-1
	else:
		fpage['pre'] = -1
	# cur
	fpage['cur'] = pg_cur 

	# >>
	if pg_cur < pg_all:
		fpage['nex'] = pg_cur+1
	else:
		fpage['nex'] = -1

	start_index = 0
	if pg_cur>1:
		start_index = (pg_cur-1)*pg_size
	add_pg = 0
	while add_pg<pg_size:
		flist.append(all_list[start_index])
		start_index += 1
		add_pg += 1
		if start_index == len(all_list):
			break
	return render(request,'food.html',{'flist':flist,'fpage':fpage})

# 交易分页数据获取
def mon(request):
	pg_cur = int(request.GET.get('curpg',1))
	pg_size = 4
	pg_all = 0
	mlist = []
	mpage = collections.OrderedDict()
	all_list = Tabmoney.objects.order_by('id').all()
	if len(all_list)%pg_size == 0:
		pg_all = int(len(all_list)/pg_size)
	else:
		pg_all = int(len(all_list)/pg_size)+1

	if pg_cur<1 or pg_cur>int(pg_all):
		return render(request,'mon.html',{'mlist':mlist,'mpage':mpage})

	# foot page
	# <<
	if pg_cur!=1:
		mpage['pre'] = pg_cur-1
	else:
		mpage['pre'] = -1
	# cur
	mpage['cur'] = pg_cur 

	# >>
	if pg_cur < pg_all:
		mpage['nex'] = pg_cur+1
	else:
		mpage['nex'] = -1

	start_index = 0
	if pg_cur>1:
		start_index = (pg_cur-1)*pg_size
	add_pg = 0
	while add_pg<pg_size:
		mlist.append(all_list[start_index])
		start_index += 1
		add_pg += 1
		if start_index == len(all_list):
			break
	return render(request,'mon.html',{'mlist':mlist,'mpage':mpage})

#------------------------------------------------------ 普通用户登录、注册、退出 ------------------------------------
#登录
def login(request):
	userName = request.POST.get('userName','')
	userPswd = request.POST.get('userPswd','')
	res = {}
	if userName=='' or userPswd=='':
		res['ifSuccess'] = 'false'
		res['errMsg'] = '信息填写不完整!'
	else:
		tar = None
		tar = Tabuser.objects.filter(tel=userName,pswd=userPswd)
		if tar!=None and len(tar)>0:
			user = tar[0]
			res['ifSuccess'] = 'true'
			res['cacheTel'] = user.tel
			res['cacheName'] = user.name 
			request.session['sessionTel'] = user.tel
			request.session['sessionName'] = user.name 
			print('name:{},tel:{}'.format(user.tel,user.name))
		else:
			res['ifSuccess'] = 'false'
			res['errMsg'] = '用户名或密码不正确!'
	return JsonResponse(res)

#注册
def sign(request):
	if request.method == 'GET':
		tel = request.GET.get('tel','')
		# sign new
		if tel=='':
			return render(request,'sign.html',{'isadd':''})
		# modify 
		else:
			users = Tabuser.objects.filter(tel=tel)
			if users==None or len(users)<1:
				pass
			else:
				return render(request,'sign.html',{'isadd':tel,'var':users[0]})
	# sign or modify
	else:
		res = {}
		name = request.POST.get('name','')
		tel = request.POST.get('tel','')
		email = request.POST.get('email','')
		pswd = request.POST.get('pswd','')
		address = request.POST.get('address')
		isadd = request.POST.get('isadd','')

		pswd1 = re.findall(r'^[_.#*@%&A-Za-z0-9]{6,20}$', str(pswd))

		# new sign
		if isadd=='':
			ifTelUsed = Tabuser.objects.filter(tel=tel)
			if ifTelUsed:
				res['isOk'] = 'false'
				res['msg'] = '手机号被使用!'
				return JsonResponse(res)
			else:
				if name!='' and tel!='' and pswd!='':
					if not pswd1:
						res['isOk'] = 'false'
						res['msg'] = '密码格式错误!'
						return JsonResponse(res)

					user = Tabuser()
					user.name = name
					user.tel = tel
					user.email = email
					user.pswd = pswd
					user.address = address
					user.imgpath = '/static/zjc.jpg'
					try:
						user.save()
					except Exception as e:
						print('user.save() exception:\n{}.'.format(repr(e)))
						res['isOk'] = 'false'
						res['msg'] = '添加用户时，数据库错误!'
						return JsonResponse(res)
					res['isOk'] = 'true'
					res['msg'] = '注册成功!'
				else:
					print("name:{},tel:{},pswd:{}.".format(name,tel,pswd))
					res['isOk'] = 'false'
					res['msg'] = '信息填写不完整!'
				print('isOK:{},msg:{}.'.format(res['isOk'],res['msg']))
				return JsonResponse(res)
		# modify
		else:
			old = Tabuser.objects.filter(tel=isadd)
			if old==None or len(old)<1:
				res['isOk'] = 'false'
				res['msg'] = '更改的用户不存在!'
				return JsonResponse(res)
			mod = old[0]
			mod.name = name
			mod.tel = tel
			mod.email = email
			mod.pswd = pswd
			mod.address = address
			try:
				mod.save()
				res['isOk'] = 'true'
				res['msg'] = '修改成功!'
				return JsonResponse(res)
			except Exception as e:
				print('modify user exception:\n{}'.format(repr(e)))
				res['isOk'] = 'false'
				res['msg'] = '修改失败!'
				return JsonResponse(res)

#关于
def about(request):
	return render(request,"about.html")

#退出
def exit(request):
	res = {}
	try:
		del request.session['sessionTel']
		del request.session['sessionName']
		res['isok'] = 'true'
	except Exception as e:
		print('exit exception:\n{}'.format(repr(e)))
		res['isok'] = 'false'
	return JsonResponse(res)

#发布交易 -------------------------------------------------- 发布交易、网站关于 ----------------------
def post(request):
	if request.method == 'GET':
		print("base_dir:{}.".format(settings.BASE_DIR))
		return render(request,"post.html")
	else:
		sender = request.POST.get('sender','')
		tel = request.POST.get('tel','')
		info = request.POST.get('info','')
		img = request.FILES.get('img',None)
		if sender=='' or tel=='' or info=='':
			return render(request,"post.html",{'errMsg':'错误:发布人、联系电话、信息说明请填写完整!'})
		else:
			if img != None:
				img_dir = settings.BASE_DIR+'\\testapp\\static\\postimg\\'
				if not os.path.exists(img_dir):
					os.makedirs(img_dir)
				t = time.time()
				time_sec = str(int(round(t*1000)))
				time_str = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(t))
				img_nm = sender+'_' + time_sec+'.jpg'
				img_name = img_dir + img_nm 
				try:
					img_file = open(img_name,'wb')
					img_file.write(img.read())
					img_file.close()
					img.close()
					print("save img {} ok !".format(img_name))
					# save post to mysql
					post = Tabmoney()
					post.sender = sender
					post.tel = tel
					post.imgpath = img_nm
					post.time_sec = time_sec
					post.time_str = time_str
					post.info = info 
					try:
						post.save()
						print("post发布成功!")
						return web(request)  #跳转到主界面  
					except Exception as ex:
						print("save post exception:\n{}".format(repr))
						return render(request,"post.html",{'errMsg':'发布失败！保存到数据库异常'})
				except Exception as e:
					print("save img failed !")
					print(repr(e))
					return render(request,"post.html",{'errMsg':'发布失败！保存图片异常'})
			else:
				return render(request,"post.html",{'errMsg':'错误:上传图片为空！'})

# 个人信息
def info(request):
	if request.method == 'GET':
		te = request.GET.get('tel','')
		if te == '':
			return render(request,'info.html',{'person':None})
		else:
			persons = Tabuser.objects.filter(tel=te)
			if persons == None:
				return render(request,'info.html',{'person':None})
			else:
				person = None 
				if len(persons)>=1:
					person = persons[0]
				return render(request,'info.html',{'person':person})

#------------------------------------------------- 管理员用户管理 ------------------------------------------
def rhyadm(request):
	if request.method == 'GET':
		if request.session.get('admName',None) == None:
			return render(request,'admlog.html')
		# 之前登录过，信息合法
		else:
			pg_cur = 1
			pg_size = 3
			pg_all = 0
			rlist = []
			rpage = collections.OrderedDict()
			all_list = Tabroom.objects.order_by('id').all()
			if len(all_list)%pg_size == 0:
				pg_all = int(len(all_list)/pg_size)
			else:
				pg_all = int(len(all_list)/pg_size)+1

			if pg_cur<1 or pg_cur>int(pg_all):
				return render(request,'adm.html',{'rlist':rlist,'rpage':rpage})

			# foot page
			# <<
			if pg_cur!=1:
				rpage['pre'] = pg_cur-1
			else:
				rpage['pre'] = -1
			# cur
			rpage['cur'] = pg_cur 
			# >>
			if pg_cur < pg_all:
				rpage['nex'] = pg_cur+1
			else:
				rpage['nex'] = -1

			start_index = 0
			if pg_cur>1:
				start_index = (pg_cur-1)*pg_size
			add_pg = 0
			while add_pg<pg_size:
				rlist.append(all_list[start_index])
				start_index += 1
				add_pg += 1
				if start_index == len(all_list):
					break
			return render(request,'adm.html',{'rlist':rlist,'rpage':rpage})
	# post 方式，从登录界面过来的		
	else:
		admName = request.POST.get('admName','')
		admPswd = request.POST.get('admPswd','')
		print('admName:{}\nadmPswd:{}'.format(admName,admPswd))

		# 管理员登录信息填写不完整
		if admName=='' or admPswd=='':
			return render(request,'admlog.html',{'errMsg':'请输入用户名和密码!'})
		# 填写完整
		else:
			ps = hashlib.md5(admPswd.encode('utf-8')).hexdigest()
			print('judge-name:{}\njudge-pass:{}'.format(admName,ps))
			adm = Tabadmin.objects.filter(name=admName,pswd=ps)
			# 验证用户名和密码
			if adm!=None and len(adm)>=1:
				request.session['admName'] = admName
				request.session['admTel'] = adm[0].tel 
				# 获取数据,返回adm.html
				pg_cur = 1
				pg_size = 3
				pg_all = 0
				rlist = []
				rpage = collections.OrderedDict()
				all_list = Tabroom.objects.order_by('id').all()
				if len(all_list)%pg_size == 0:
					pg_all = int(len(all_list)/pg_size)
				else:
					pg_all = int(len(all_list)/pg_size)+1

				if pg_cur<1 or pg_cur>int(pg_all):
					return render(request,'adm.html',{'rlist':rlist,'rpage':rpage})

				# foot page
				# <<
				if pg_cur!=1:
					rpage['pre'] = pg_cur-1
				else:
					rpage['pre'] = -1
				# cur
				rpage['cur'] = pg_cur 
				# >>
				if pg_cur < pg_all:
					rpage['nex'] = pg_cur+1
				else:
					rpage['nex'] = -1

				start_index = 0
				if pg_cur>1:
					start_index = (pg_cur-1)*pg_size
				add_pg = 0
				while add_pg<pg_size:
					rlist.append(all_list[start_index])
					start_index += 1
					add_pg += 1
					if start_index == len(all_list):
						break
				return render(request,'adm.html',{'rlist':rlist,'rpage':rpage})
			else:
				return render(request,'admlog.html',{'errMsg':'用户名和密码错误!'})

# adm 退出操作
def admexit(request):
	res = {}
	try:
		del request.session['admName']
		del request.session['admTel']
		res['isok'] = 'true'
	except Exception as e:
		print('exit exception:\n{}'.format(repr(e)))
		res['isok'] = 'false'
	return JsonResponse(res)

# adm 添加、修改操作
def admaddmod(request):
	if request.session.get('admName',None) == None:
		return render(request,'admlog.html')
	# GET add/modify
	if request.method == 'GET':
		admName = request.GET.get('admName','')
		# add
		if admName =='':
			return render(request,"admaddmod.html",{'isadd':''})
		# modify
		else:
			adms = Tabadmin.objects.filter(name=admName)
			# adm not exists
			if adms==None or len(adms)<1:
				pass 
			else:
				return render(request,"admaddmod.html",{'isadd':admName,'var':adms[0]})
	# POST adddata/modifydata
	else:
		res = {}
		isadd = request.POST.get('isadd','')
		if isadd=='':
			adm = Tabadmin()
			adm.name = request.POST.get('name','admin')
			adm.tel = request.POST.get('tel','18788261701')
			adm.pswd = hashlib.md5(request.POST.get('pswd','password').encode('utf-8')).hexdigest()
			try:
				adm.save()
				print('adm save() ok:\n{},{},{}'.format(adm.name,adm.tel,adm.pswd))
				res['isOk'] = 'true'
				return JsonResponse(res)
			except Exception as e:
				print('adm save() error:\n{}'.format(repr(e)))
				res['isOk'] = 'false'
				res['msg'] = '数据库保存异常！'
				return JsonResponse(res)
		else:
			adms = Tabadmin.objects.filter(name=isadd)
			if adms==None or len(adms)<1:
				print("modify adm not exist")
				res['isOk'] = 'false'
				res['msg'] = '要修改的管理员不存在!'
				return JsonResponse(res)
			else:
				adm = adms[0]
				adm.name = request.POST.get('name','admin')
				adm.tel = request.POST.get('tel','18788261701')
				ps = request.POST.get('pswd','password')
				# change pswd
				if len(ps)<20:
					adm.pswd = hashlib.md5(ps.encode('utf-8')).hexdigest()
				try:
					adm.save()
					print('modify adm ok')
					res['isOk'] = 'true'
					return JsonResponse(res)
				except:
					print('modify adm error:\n{}'.format(repr(e)))
					res['isOk'] = 'false'
					res['msg'] = '修改的管理员信息保存失败!'
					return JsonResponse(res)


# 管理房间信息-------------------------------------------- 管理员获取数据 -------------------------------
def admroom(request):
	pg_cur = int(request.GET.get('curpg',1))
	pg_size = 3
	pg_all = 0
	rlist = []
	rpage = collections.OrderedDict()
	all_list = Tabroom.objects.order_by('id').all()
	if len(all_list)%pg_size == 0:
		pg_all = int(len(all_list)/pg_size)
	else:
		pg_all = int(len(all_list)/pg_size)+1

	if pg_cur<1 or pg_cur>int(pg_all):
		return render(request,'admroom.html',{'rlist':rlist,'rpage':rpage})

	# foot page
	# <<
	if pg_cur!=1:
		rpage['pre'] = pg_cur-1
	else:
		rpage['pre'] = -1
	# cur
	rpage['cur'] = pg_cur 
	# >>
	if pg_cur < pg_all:
		rpage['nex'] = pg_cur+1
	else:
		rpage['nex'] = -1

	start_index = 0
	if pg_cur>1:
		start_index = (pg_cur-1)*pg_size
	add_pg = 0
	while add_pg<pg_size:
		rlist.append(all_list[start_index])
		start_index += 1
		add_pg += 1
		if start_index == len(all_list):
			break
	return render(request,'admroom.html',{'rlist':rlist,'rpage':rpage})

#管理食物分页信息
def admfood(request):
	pg_cur = int(request.GET.get('curpg',1))
	pg_size = 3
	pg_all = 0
	flist = []
	fpage = collections.OrderedDict()
	all_list = Tabfood.objects.order_by('id').all()
	if len(all_list)%pg_size == 0:
		pg_all = int(len(all_list)/pg_size)
	else:
		pg_all = int(len(all_list)/pg_size)+1

	if pg_cur<1 or pg_cur>int(pg_all):
		return render(request,'admfood.html',{'flist':flist,'fpage':fpage})

	# foot page
	# <<
	if pg_cur!=1:
		fpage['pre'] = pg_cur-1
	else:
		fpage['pre'] = -1
	# cur
	fpage['cur'] = pg_cur 
	# >>
	if pg_cur < pg_all:
		fpage['nex'] = pg_cur+1
	else:
		fpage['nex'] = -1

	start_index = 0
	if pg_cur>1:
		start_index = (pg_cur-1)*pg_size
	add_pg = 0
	while add_pg<pg_size:
		flist.append(all_list[start_index])
		start_index += 1
		add_pg += 1
		if start_index == len(all_list):
			break
	return render(request,'admfood.html',{'flist':flist,'fpage':fpage})

# 管理特产分页数据
def admspe(request):
	pg_cur = int(request.GET.get('curpg',1))
	pg_size = 3
	pg_all = 0
	slist = []
	spage = collections.OrderedDict()
	all_list = Tabspe.objects.order_by('id').all()
	if len(all_list)%pg_size == 0:
		pg_all = int(len(all_list)/pg_size)
	else:
		pg_all = int(len(all_list)/pg_size)+1

	if pg_cur<=int(pg_all):
		# foot page
		# <<
		if pg_cur!=1:
			spage['pre'] = pg_cur-1
		else:
			spage['pre'] = -1
		# cur
		spage['cur'] = pg_cur 
		# >>
		if pg_cur < pg_all:
			spage['nex'] = pg_cur+1
		else:
			spage['nex'] = -1

		start_index = 0
		if pg_cur>1:
			start_index = (pg_cur-1)*pg_size
		add_pg = 0
		while add_pg<pg_size:
			slist.append(all_list[start_index])
			start_index += 1
			add_pg += 1
			if start_index == len(all_list):
				break
	return render(request,'admspe.html',{'slist':slist,'spage':spage})

#管理交易分页信息
def admmon(request):
	pg_cur = int(request.GET.get('curpg',1))
	pg_size = 3
	pg_all = 0
	mlist = []
	mpage = collections.OrderedDict()
	all_list = Tabmoney.objects.order_by('id').all()
	if len(all_list)%pg_size == 0:
		pg_all = int(len(all_list)/pg_size)
	else:
		pg_all = int(len(all_list)/pg_size)+1

	if pg_cur<1 or pg_cur>int(pg_all):
		return render(request,'admmon.html',{'mlist':mlist,'mpage':mpage})

	# foot page
	# <<
	if pg_cur!=1:
		mpage['pre'] = pg_cur-1
	else:
		mpage['pre'] = -1
	# cur
	mpage['cur'] = pg_cur 
	# >>
	if pg_cur < pg_all:
		mpage['nex'] = pg_cur+1
	else:
		mpage['nex'] = -1

	start_index = 0
	if pg_cur>1:
		start_index = (pg_cur-1)*pg_size
	add_pg = 0
	while add_pg<pg_size:
		mlist.append(all_list[start_index])
		start_index += 1
		add_pg += 1
		if start_index == len(all_list):
			break
	return render(request,'admmon.html',{'mlist':mlist,'mpage':mpage})

#管理用户分页信息
def admuser(request):
	pg_cur = int(request.GET.get('curpg',1))
	pg_size = 3
	pg_all = 0
	ulist = []
	upage = collections.OrderedDict()
	all_list = Tabuser.objects.order_by('id').all()
	if len(all_list)%pg_size == 0:
		pg_all = int(len(all_list)/pg_size)
	else:
		pg_all = int(len(all_list)/pg_size)+1

	if pg_cur<1 or pg_cur>int(pg_all):
		return render(request,'admuser.html',{'ulist':ulist,'upage':upage})

	# foot page
	# <<
	if pg_cur!=1:
		upage['pre'] = pg_cur-1
	else:
		upage['pre'] = -1
	# cur
	upage['cur'] = pg_cur 
	# >>
	if pg_cur < pg_all:
		upage['nex'] = pg_cur+1
	else:
		upage['nex'] = -1

	start_index = 0
	if pg_cur>1:
		start_index = (pg_cur-1)*pg_size
	add_pg = 0
	while add_pg<pg_size:
		ulist.append(all_list[start_index])
		start_index += 1
		add_pg += 1
		if start_index == len(all_list):
			break
	return render(request,'admuser.html',{'ulist':ulist,'upage':upage})

# roomadd 管理员添加房间-------------------------------------------- 管理员添加 ---------------------------------------
def roomadd(request):
	# ajax request
	if request.method == 'GET':
		return render(request,"addroom.html")
	# ajax request
	else:
		kindof = request.POST.get('kindof','')
		price = request.POST.get('price','')
		info = request.POST.get('info','暂无说明')
		img = request.FILES.get('img',None)

		if kindof=='' or price=='':
			return render(request,"addroom.html",{'errMsg':'请填写完整的房间信息！'})
		if img != None:
			img_dir = settings.BASE_DIR+'\\testapp\\static\\roomimg\\'
			if not os.path.exists(img_dir):
				os.makedirs(img_dir)
			dateuid = str(int(round(time.time()*1000)))
			img_nm = dateuid+'.jpg'
			img_name = img_dir + img_nm 
			try:
				img_file = open(img_name,'wb')
				img_file.write(img.read())
				img_file.close()
				img.close()
				print("save img {} ok !".format(img_name))

				room = Tabroom()
				room.kindof = kindof
				room.price = price
				room.dateuid = dateuid
				room.info = info
				room.imgpath = img_nm
				try:
					room.save()
					return render(request,"addroom.html",{'errMsg':'ok'})
				except Exception as e:
					print("save room failed:\n{}.".format(repr(e)))
					return render(request,"addroom.html",{'errMsg':'添加房间失败，数据库保存错误!'})
			except Exception as e:
				print("save img exception:\n{}.".format(repr(e)))
				return render(request,"addroom.html",{'errMsg':'添加房间失败，图片保存错误!'})

# foodadd 管理员添加菜品
def foodadd(request):
	# ajax request
	if request.method == 'GET':
		return render(request,"addfood.html")
	# ajax request
	else:
		kindof = request.POST.get('kindof','')
		price = request.POST.get('price','')
		info = request.POST.get('info','暂无说明')
		img = request.FILES.get('img',None)

		if kindof=='' or price=='':
			return render(request,"addfood.html",{'errMsg':'请填写完整的菜品信息！'})
		if img != None:
			img_dir = settings.BASE_DIR+'\\testapp\\static\\foodimg\\'
			if not os.path.exists(img_dir):
				os.makedirs(img_dir)
			dateuid = str(int(round(time.time()*1000)))
			img_nm = dateuid+'.jpg'
			img_name = img_dir + img_nm 
			try:
				img_file = open(img_name,'wb')
				img_file.write(img.read())
				img_file.close()
				img.close()
				print("save img {} ok !".format(img_name))

				food = Tabfood()
				food.kindof = kindof
				food.price = price
				food.dateuid = dateuid
				food.info = info
				food.imgpath = img_nm
				try:
					food.save()
					return render(request,"addfood.html",{'errMsg':'ok'})
				except Exception as e:
					print("save food failed:\n{}.".format(repr(e)))
					return render(request,"addfood.html",{'errMsg':'添加菜品失败，数据库保存错误!'})
			except Exception as e:
				print("save img exception:\n{}.".format(repr(e)))
				return render(request,"addfood.html",{'errMsg':'添加菜品失败，图片保存错误!'})

# 管理员添加特产
def speadd(request):
	# ajax request
	if request.method == 'GET':
		return render(request,"addspe.html")
	# ajax request
	else:
		name = request.POST.get('kindof','')
		tel = request.POST.get('price','')
		info = request.POST.get('info','暂无说明')
		img = request.FILES.get('img',None)

		if name=='' or tel=='':
			return render(request,"addspe.html",{'errMsg':'请填写完整的特产信息！'})
		if img != None:
			img_dir = settings.BASE_DIR+'\\testapp\\static\\speimg\\'
			if not os.path.exists(img_dir):
				os.makedirs(img_dir)
			dateuid = str(int(round(time.time()*1000)))
			img_nm = dateuid+'.jpg'
			img_name = img_dir + img_nm 
			try:
				img_file = open(img_name,'wb')
				img_file.write(img.read())
				img_file.close()
				img.close()
				print("save img {} ok !".format(img_name))

				spe = Tabspe()
				spe.name = name
				spe.tel = tel
				spe.dateuid = dateuid
				spe.info = info
				spe.imgpath = img_nm
				try:
					spe.save()
					return render(request,"addspe.html",{'errMsg':'ok'})
				except Exception as e:
					print("save spe failed:\n{}.".format(repr(e)))
					return render(request,"addspe.html",{'errMsg':'添加菜品失败，数据库保存错误!'})
			except Exception as e:
				print("save img exception:\n{}.".format(repr(e)))
				return render(request,"addspe.html",{'errMsg':'添加菜品失败，图片保存错误!'})

# 修改房间信息------------------------------------------------- 管理员更新 -------------------------------------
def roommod(request):
	if request.method == 'GET':
		dateuid = request.GET.get('dateuid')
		room = Tabroom.objects.filter(dateuid=dateuid)
		if room!=None and len(room)>=1:
			return render(request,'roommod.html',{'var':room[0]})
		else:
			return render(request,'roommod.html',{'errMsg':'请求更改的数据不存在!'})
	# ajax post modify request
	else:
		dateuid = request.POST.get('dateuid','')
		kindof = request.POST.get('kindof','')
		price = request.POST.get('price','')
		info = request.POST.get('info','')
		img = request.FILES.get('img',None)
		modroom = Tabroom.objects.filter(dateuid=dateuid)
		if dateuid=='' or len(modroom)<1:
			return render(request,'roommod.html',{'errMsg':'请求更改的数据不存在!'})
		tar = modroom[0]
		img_nm = dateuid+".jpg"
		if img != None:
			img_dir = settings.BASE_DIR+'\\testapp\\static\\roomimg\\'
			if not os.path.exists(img_dir):
				os.makedirs(img_dir)
			img_nm = dateuid+'.jpg'
			img_name = img_dir + img_nm
			try:
				img_file = open(img_name,'wb')
				img_file.write(img.read())
				img_file.close()
				img.close()
				print("--------- cover img {} ok !".format(img_name))
			except Exception as e:
				print("save img exception:\n{}.".format(repr(e)))
				return render(request,"roommod.html",{'errMsg':'更改房间信息失败，图片保存错误!'})
		else:
			print("------------- cover img is None ---------------")
		tar.kindof = kindof
		tar.price = price
		tar.dateuid = dateuid
		tar.info = info
		tar.imgpath = img_nm
		try:
			tar.save()
			return render(request,"roommod.html",{'errMsg':'ok'})
		except Exception as e:
			print("save room failed:\n{}.".format(repr(e)))
			return render(request,"roommod.html",{'errMsg':'更改房间信息失败，数据库保存错误!'})

# 修改菜品信息
def foodmod(request):
	if request.method == 'GET':
		dateuid = request.GET.get('dateuid')
		food = Tabfood.objects.filter(dateuid=dateuid)
		if food!=None and len(food)>=1:
			return render(request,'foodmod.html',{'var':food[0]})
		else:
			return render(request,'foodmod.html',{'errMsg':'请求更改的数据不存在!'})
	# ajax post modify request
	else:
		dateuid = request.POST.get('dateuid','')
		kindof = request.POST.get('kindof','')
		price = request.POST.get('price','')
		info = request.POST.get('info','')
		img = request.FILES.get('img',None)
		modfood = Tabfood.objects.filter(dateuid=dateuid)
		if dateuid=='' or len(modfood)<1:
			return render(request,'foodmod.html',{'errMsg':'请求更改的数据不存在!'})
		tar = modfood[0]
		img_nm = dateuid+".jpg"
		if img != None:
			img_dir = settings.BASE_DIR+'\\testapp\\static\\foodimg\\'
			if not os.path.exists(img_dir):
				os.makedirs(img_dir)
			img_nm = dateuid+'.jpg'
			img_name = img_dir + img_nm
			try:
				img_file = open(img_name,'wb')
				img_file.write(img.read())
				img_file.close()
				img.close()
				print("--------- cover img {} ok !".format(img_name))
			except Exception as e:
				print("save img exception:\n{}.".format(repr(e)))
				return render(request,"foodmod.html",{'errMsg':'更改房间信息失败，图片保存错误!'})
		else:
			print("------------- cover img is None ---------------")
		tar.kindof = kindof
		tar.price = price
		tar.dateuid = dateuid
		tar.info = info
		tar.imgpath = img_nm
		try:
			tar.save()
			return render(request,"foodmod.html",{'errMsg':'ok'})
		except Exception as e:
			print("save food failed:\n{}.".format(repr(e)))
			return render(request,"foodmod.html",{'errMsg':'更改房间信息失败，数据库保存错误!'})

# 各类数据的删除操作--------------------------------------------- 管理员删除 ---------------------------------------
def roomdel(request):
	res = {}
	if request.method == 'GET':
		res['isOk'] = 'false'
		res['errMsg'] = '请求方式错误!'
		return JsonResponse(res)
	if request.session.get('admin',None)==None:
		res['isOk'] = 'false'
		res['errMsg'] = '管理员登录异常,无权操作!'
		return JsonResponse(res)
	else:
		unique = request.POST.get('unique','')
		if unique=='':
			res['isOk'] = 'false'
			res['errMsg'] = '请求参数错误!'
			return JsonResponse(res)
		tar = Tabroom.objects.filter(dateuid=unique)
		if tar!=None and len(tar)>=1:
			try:
				img = settings.BASE_DIR+'\\testapp\\static\\roomimg\\'+tar[0].imgpath
				if os.path.exists(img):
					try:
						os.remove(img)
						print('delete img ok!')
					except Exception as e:
						print('delete img {} exception:\n{}'.format(img,repr(e)))
				tar[0].delete()
				res['isOk'] = 'true'
				return JsonResponse(res)
			except Exception as e:
				print('delete obj exception:\n{}',repr(e))
				res['isOk'] = 'false'
				res['errMsg'] = '数据库删除异常!'
				return JsonResponse(res)
		else:
			res['isOk'] = 'false'
			res['errMsg'] = '待删除数据不存在!'
			return JsonResponse(res)

# 删除菜品
def fooddel(request):
	res = {}
	if request.method == 'GET':
		res['isOk'] = 'false'
		res['errMsg'] = '请求方式错误!'
		return JsonResponse(res)
	if request.session.get('admin',None)==None:
		res['isOk'] = 'false'
		res['errMsg'] = '管理员登录异常,无权操作!'
		return JsonResponse(res)
	else:
		unique = request.POST.get('unique','')
		if unique=='':
			res['isOk'] = 'false'
			res['errMsg'] = '请求参数错误!'
			return JsonResponse(res)
		tar = Tabfood.objects.filter(dateuid=unique)
		if tar!=None and len(tar)>=1:
			try:
				img = settings.BASE_DIR+'\\testapp\\static\\foodimg\\'+tar[0].imgpath
				if os.path.exists(img):
					try:
						os.remove(img)
						print('delete img ok!')
					except Exception as e:
						print('delete img {} exception:\n{}'.format(img,repr(e)))
				tar[0].delete()
				res['isOk'] = 'true'
				return JsonResponse(res)
			except Exception as e:
				print('delete obj exception:\n{}',repr(e))
				res['isOk'] = 'false'
				res['errMsg'] = '数据库删除异常!'
				return JsonResponse(res)
		else:
			res['isOk'] = 'false'
			res['errMsg'] = '待删除数据不存在!'
			return JsonResponse(res)

# 管理员删除特产
def spedel(request):
	res = {}
	if request.method == 'GET':
		res['isOk'] = 'false'
		res['errMsg'] = '请求方式错误!'
		return JsonResponse(res)
	if request.session.get('admin',None)==None:
		res['isOk'] = 'false'
		res['errMsg'] = '管理员登录异常,无权操作!'
		return JsonResponse(res)
	else:
		unique = request.POST.get('unique','')
		if unique=='':
			res['isOk'] = 'false'
			res['errMsg'] = '请求参数错误!'
			return JsonResponse(res)
		tar = Tabspe.objects.filter(dateuid=unique)
		if tar!=None and len(tar)>=1:
			try:
				img = settings.BASE_DIR+'\\testapp\\static\\speimg\\'+tar[0].imgpath
				if os.path.exists(img):
					try:
						os.remove(img)
						print('delete img ok!')
					except Exception as e:
						print('delete img {} exception:\n{}'.format(img,repr(e)))
				tar[0].delete()
				res['isOk'] = 'true'
				return JsonResponse(res)
			except Exception as e:
				print('delete obj exception:\n{}',repr(e))
				res['isOk'] = 'false'
				res['errMsg'] = '数据库删除异常!'
				return JsonResponse(res)
		else:
			res['isOk'] = 'false'
			res['errMsg'] = '待删除数据不存在!'
			return JsonResponse(res)

# 管理员删除交易
def mondel(request):
	res = {}
	if request.method == 'GET':
		res['isOk'] = 'false'
		res['errMsg'] = '请求方式错误!'
		return JsonResponse(res)
	if request.session.get('admin',None)==None:
		res['isOk'] = 'false'
		res['errMsg'] = '管理员登录异常,无权操作!'
		return JsonResponse(res)
	else:
		unique = request.POST.get('unique','')
		if unique=='':
			res['isOk'] = 'false'
			res['errMsg'] = '请求参数错误!'
			return JsonResponse(res)
		tar = Tabmoney.objects.filter(time_sec=unique)
		if tar!=None and len(tar)>=1:
			try:
				img = settings.BASE_DIR+'\\testapp\\static\\postimg\\'+tar[0].imgpath
				if os.path.exists(img):
					try:
						os.remove(img)
						print('delete img ok!')
					except Exception as e:
						print('delete img {} exception:\n{}'.format(img,repr(e)))
				tar[0].delete()
				res['isOk'] = 'true'
				return JsonResponse(res)
			except Exception as e:
				print('delete obj exception:\n{}',repr(e))
				res['isOk'] = 'false'
				res['errMsg'] = '数据库删除异常!'
				return JsonResponse(res)
		else:
			res['isOk'] = 'false'
			res['errMsg'] = '待删除数据不存在!'
			return JsonResponse(res)

# 管理员删除用户
def userdel(request):
	res = {}
	if request.method == 'GET':
		res['isOk'] = 'false'
		res['errMsg'] = '请求方式错误!'
		return JsonResponse(res)
	if request.session.get('admin',None)==None:
		res['isOk'] = 'false'
		res['errMsg'] = '管理员登录异常,无权操作!'
		return JsonResponse(res)
	else:
		unique = request.POST.get('unique','')
		if unique=='':
			res['isOk'] = 'false'
			res['errMsg'] = '请求参数错误!'
			return JsonResponse(res)
		tar = Tabuser.objects.filter(tel=unique)
		if tar!=None and len(tar)>=1:
			try:
				tar[0].delete()
				res['isOk'] = 'true'
				return JsonResponse(res)
			except Exception as e:
				print('delete obj exception:\n{}',repr(e))
				res['isOk'] = 'false'
				res['errMsg'] = '数据库删除异常!'
				return JsonResponse(res)
		else:
			res['isOk'] = 'false'
			res['errMsg'] = '待删除数据不存在!'
			return JsonResponse(res)
