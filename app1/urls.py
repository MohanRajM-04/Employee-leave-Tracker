from django.urls import path,include
from app1.views import login, signup, signout, apply_leave, delete_leave, home, update

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', signout),
    path('apply_leave/', apply_leave),
    path('delete_leave/<int:id>', delete_leave),
    path('update/', update, name='update'),
]









