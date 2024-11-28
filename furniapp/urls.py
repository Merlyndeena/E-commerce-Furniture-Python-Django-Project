from django.urls import path
from furniapp import views
urlpatterns=[
    path('index/',views.index,name="index"),
    path('add_cat/',views.add_cat,name="add_cat"),
    path('view_cat/',views.view_cat,name="view_cat"),
    path('save_cat/',views.save_cat,name="save_cat"),
    path('edit_cat/<int:c_id>/',views.edit_cat,name="edit_cat"),
    path('update_cat/<int:ct_id>/',views.update_cat,name="update_cat"),
    path('delete_cat/<int:cate_id>/',views.delete_cat,name="delete_cat"),
    path('add_pro/',views.add_pro,name="add_pro"),
    path('view_pro/',views.view_pro,name="view_pro"),
    path('save_pro/',views.save_pro,name="save_pro"),
    path('edit_pro/<int:p_id>/',views.edit_pro,name="edit_pro"),
    path('update_pro/<int:p_id>/',views.update_pro,name="update_pro"),
    path('delete_pro/<int:p_id>/',views.delete_pro,name="delete_pro"),

    path('admin_login/',views.admin_login,name="admin_login"),
    path('login_page/',views.login_page,name="login_page"),
    path('logout/',views.logout,name="logout"),
    path('contact_data/',views.contact_data,name="contact_data"),
    path('delete_contact/<int:p_id>/',views.delete_contact,name="delete_contact"),


















]