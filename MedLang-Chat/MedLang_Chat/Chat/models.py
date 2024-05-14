from django.db import models

class CHMED(models.Model):
    med_name = models.CharField(verbose_name='药物名称', max_length=128)
    med_pic = models.CharField(verbose_name='药物图片', max_length=256,blank=True,null=True)
    med_ingredience = models.CharField(verbose_name='成份',max_length=512)
    med_character = models.CharField(verbose_name='性状', max_length=512)
    med_use = models.CharField(verbose_name='功能主治',max_length=1024)
    clinic = models.CharField(verbose_name='诊疗科',max_length=32)

class WestMED(models.Model):
    med_name = models.CharField(verbose_name='药物名称', max_length=128)
    med_pic = models.CharField(verbose_name='药物图片', max_length=256,blank=True,null=True)
    med_ingredience = models.CharField(verbose_name='成份',max_length=512,blank=True,null=True)
    med_use = models.CharField(verbose_name='功能主治',max_length=1024,blank=True,null=True)
    med_warn = models.CharField(verbose_name='禁忌',max_length=1024,blank=True,null=True)