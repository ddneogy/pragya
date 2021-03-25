from django.db import models
from django.db.models.signals import pre_delete,pre_save,post_save
from django.dispatch import receiver

# Create your models here. 
class Booktype(models.Model):
    book_name= models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    level=models.CharField(max_length=20)
    publisher=models.CharField(max_length=200)
    price=models.IntegerField()
    publication_year = models.IntegerField()
    reprint_year=models.IntegerField()
    remarks=models.CharField(max_length=200,blank= True, null= True)
    def __str__(self):
        return f"{self.book_name} by {self.author}"
    

    

class Member(models.Model):
    member_code=models.CharField(max_length=100)
    name= models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone= models.CharField(max_length=50)
    email=models.EmailField(max_length=200)
    level=models.CharField(max_length=50)
    reference_code= models.CharField(max_length=100)
    remarks = models.CharField(max_length=200,blank= True,null= True)
    def __str__(self):
        return f"{self.member_code}-{self.name}-Class:{self.level}"
    


    


class Book(models.Model):
    book = models.ForeignKey(Booktype,on_delete=models.CASCADE)
    book_code=models.CharField(max_length=100)
    member = models.ForeignKey(Member,on_delete=models.PROTECT,default='',blank = True,null= True,editable=False,unique= True)
    status= models.CharField(max_length=100,default= 'Available',editable= False)
    remarks = models.CharField(max_length=200,blank= True,null= True)
    def __str__(self):
        return self.book_code
    


    

class Lending(models.Model):
    member = models.ForeignKey(Member,on_delete=models.PROTECT,editable= True)
    book = models.ForeignKey(Book,on_delete=models.PROTECT,editable= True ,unique= True)
    lending_date= models.DateField()
    due_date= models.DateField()
    remarks= models.CharField(max_length=200,blank= True,null= True)
   # def save(self,*args,**kwargs):
      #  if not self.pk:
          # Book.objects.filter(pk=self.book_id).update(status='Lent',member=self.member)
       # super().save(*args,**kwargs)
    
    list_display_links = None
    
    def has_change_permission(self,request,obj= None):
        return False
    
    
@receiver(pre_delete,sender= Lending,dispatch_uid='update_book_lending_delete')
def update_book_lending_delete(sender,**kwargs):
    lend = kwargs['instance']
    if lend.pk:
     Book.objects.filter(pk=lend.book_id).update(status= 'Available',member='')
@receiver(pre_save,sender= Lending,dispatch_uid='update_book_lending_change_pre')
def update_book_lending_change_pre(sender,**kwargs):
    lend = kwargs['instance']
    if lend.pk:
        lending_old= Lending.objects.filter(pk=lend.pk).values_list('book',flat= True).first()
    
        Book.objects.filter(pk=lending_old).update(status= 'Available',member='')
    
@receiver(post_save,sender= Lending,dispatch_uid='update_book_lending_change_post')
def update_book_lending_change_post(sender,**kwargs):
    lend = kwargs['instance']
    if lend.pk:
      Book.objects.filter(pk=lend.book_id).update(status=  'Lent',member=lend.member)
    
    
  
