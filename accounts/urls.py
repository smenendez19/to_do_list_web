from django.urls import path
from accounts.views import user_signup, user_login, user_logout

urlpatterns = [
    path('signup/', user_signup, name="accounts_signup"),
    path('login/', user_login, name="accounts_login"),
    path('logout/', user_logout, name="accounts_logout"),
]
