from django.contrib import admin
from shorten.models import bitly
# Register your models here.


class bitlyAdmin(admin.ModelAdmin):
	models = bitly
	list_display = ["model_short_code", "count"]


admin.site.register(bitly, bitlyAdmin)
