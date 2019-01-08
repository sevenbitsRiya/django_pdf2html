from django.db import models

class Profile(models.Model):
   name = models.CharField(max_length = 50)
   file = models.FileField(upload_to = 'media')

   def __unicode__(self):  
        return self.name
   
class patient_profile_conclusion(models.Model):
   patient_name = models.CharField(max_length = 50,default="")
   hemoglobin_cnt = models.CharField(max_length = 5,default="0")
   pcv_cnt= models.CharField(max_length = 5,default="0")
   RBC_cnt=models.CharField(max_length = 5,default="0")
   MCV_cnt=models.CharField(max_length = 5,default="0")
   MCH_cnt=models.CharField(max_length = 5,default="0")
   
   def __unicode__(self):  
        return self.patient_name
   