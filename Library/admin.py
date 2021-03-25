from django.contrib import admin
from.models import Booktype,Book,Member,Lending
from import_export.admin import ExportActionMixin
# Register your models here.
class BooktypeInLine(admin.StackedInline):
    model= Booktype
    extra= 3
class BooktypeAdmin(ExportActionMixin,admin.ModelAdmin):
    search_fields=['book_name','author','level','publisher'],
    list_display=['book_name','author','level','publisher','price','publication_year','reprint_year','remarks']
class BookAdmin(ExportActionMixin,admin.ModelAdmin):
    search_fields=['book_code','status']
    list_display=['book','book_code','member','status','remarks']
    #inlines =[BooktypeInLine]

class MemberAdmin(ExportActionMixin,admin.ModelAdmin):
    search_fields=['name','address','level']
    list_display=['member_code','name','address','phone','email','level','reference_code','remarks']

class LendingAdmin(ExportActionMixin,admin.ModelAdmin):
    search_fields=['due_date']
    list_display=['member','book','lending_date','due_date','remarks']
admin.site.register(Booktype,BooktypeAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Member,MemberAdmin)
admin.site.register(Lending,LendingAdmin)