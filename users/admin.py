from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationsForm
from .models import CustomUser

class UserAdmin(BaseUserAdmin):
  form = UserChangeForm
  add_form = UserCreationsForm
  
  list_display = ('username', 'year', 'is_admin')
  list_filter = ('is_admin',)
  fieldsets =(
    (None, {'fields':('username','password')}),
    ('Personal info', {'fields' : ('year',)}),
    ('Permissions', {'fields' : ('is_admin',)}),                   
  )
  
  add_fieldsets = (
    (None,{
      'classes' :('wide',), 
      'fields': ('username', 'year', 'password1', 'password2')
    }),
  )

  search_fields = ('username',)
  ordering = ('username',)
  filter_horizontal = ()
  


admin.site.register(CustomUser, UserAdmin)
# admin.site.register(Group)