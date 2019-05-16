from django.contrib.admin import AdminSite

class Custom_site(AdminSite):
    site_header = "Typeidea"
    site_title = "Typeidea后台管理"
    index_title = '首页'

custon_site = Custom_site(name='cus_admin')