from django.contrib import admin

# Register your models here.
from .models import Beverage, BeverageHistory
# Register your models here.
class BeverageAdmin(admin.ModelAdmin):
    list_display = ["name"]

class BeverageHistoryAdmin(admin.ModelAdmin):
    list_display = ["created_at", "created_by", "beverage"]
    ordering = ['-created_at']

admin.site.register(BeverageHistory, BeverageHistoryAdmin)
admin.site.register(Beverage, BeverageAdmin)