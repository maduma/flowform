from django.contrib import admin
from models import Flow, Form, Field
# Register your models here.


class FieldInline(admin.TabularInline):
	model = Field
	extra = 0

class FormAdmin(admin.ModelAdmin):
	inlines = [FieldInline]
	
class FormInline(admin.TabularInline):
	model = Form
	extra = 0
	
class FlowAdmin(admin.ModelAdmin):
	inlines = [FormInline]

admin.site.register(Flow, FlowAdmin)
admin.site.register(Form, FormAdmin)

