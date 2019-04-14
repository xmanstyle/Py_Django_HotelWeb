from django.db import models

# 房间表
class Tabroom(models.Model):
	kindof = models.CharField(max_length=30,null=False,) # type of room
	dateuid = models.CharField(max_length=15,null=False,) # unique mark the room record 
	price = models.IntegerField() # room price
	imgpath = models.TextField() # room pictures
	info = models.CharField(max_length=200,) # room info

# 菜品表
class Tabfood(models.Model):
	kindof = models.CharField(max_length=30,null=False,)
	dateuid = models.CharField(max_length=15,null=False,)
	price = models.IntegerField() #
	imgpath = models.TextField() #
	info = models.CharField(max_length=200,) #

# 交易表
class Tabmoney(models.Model):
	sender = models.CharField(max_length=20,null=False,)
	tel = models.CharField(max_length=12,null=False,)
	imgpath = models.TextField() #
	time_sec = models.CharField(max_length=15,null=False,)
	time_str = models.CharField(max_length=30,null=False,)
	info = models.CharField(max_length=200,) #

# 用户表
class Tabuser(models.Model):
	name = models.CharField(max_length=20,null=False,)
	tel = models.CharField(max_length=12,null=False,unique=True)
	email = models.CharField(max_length=20,)
	pswd = models.CharField(max_length=50,null=False,)
	address = models.CharField(max_length=100,)
	imgpath = models.CharField(max_length=100,)

# 管理员表
class Tabadmin(models.Model):
	name = models.CharField(max_length=20,null=False,unique=True)
	tel = models.CharField(max_length=12,null=False,unique=True)
	pswd = models.CharField(max_length=50,)

# 特产表
class Tabspe(models.Model):
	name = models.CharField(max_length=40,null=False,)
	tel = models.CharField(max_length=12,null=False,)
	info = models.TextField()
	imgpath = models.CharField(max_length=100,null=False,)
	dateuid = models.CharField(max_length=15,null=False,)