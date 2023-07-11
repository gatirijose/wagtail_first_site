from django.urls import path, reverse
from wagtail import hooks 
from wagtail.admin.menu import MenuItem, Menu, SubmenuMenuItem
from .views import index

@hooks.register('register_admin_urls')
def register_calender_url():
    return [
        path('calender/', index, name='calender'),
        path('calender/month', index, name='calender-month'),
    ]

# @hooks.register('register_admin_menu_item')
# def register_calender_menu_item():
#     return MenuItem('Calender', reverse('calender'), icon_name='date')

@hooks.register('register_admin_menu_item')
def register_calender_menu_item():
    submenu = Menu(items=[
        MenuItem('Calender', reverse('calender'), icon_name='date'),
        MenuItem('Current month', reverse('calender-month'), icon_name='date'),
    ])
    return SubmenuMenuItem('Calender', submenu, icon_name='date')