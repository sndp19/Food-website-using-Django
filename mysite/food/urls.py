from .  import views
from django.urls import path


app_name ='food'
urlpatterns = [
    #/food/
    path('index/', views.index, name ="index" ),
    #/food/id
    path('<int:item_id>/',views.detail,name="detail"),
    path('hello/',views.index, name ="index" ),
    path('sndp/',views.sndp, name = 'sndp'),
    path('index1/', views.Index_1, name = 'Index_1'),
    path('add/',views.create_item,name='create_item'),
    path('update/<int:id>/',views.uptade_item,name='update_item'),
    path('delete/<int:id>/>',views.delete_item,name='delete_item'),

]
