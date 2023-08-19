from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('oauth/', include('social_django.urls', namespace='social')),
]


# https://oauth.vk.com/authorize?client_id=51731830&scope=email&redirect_uri=http://127.0.0.1:9999/callback

# http://127.0.0.1:9999/callback?code=358ba1b18b2af9f633
# https://oauth.vk.com/access_token?client_id=51731830&client_secret=f2b5BdabzcltJ0g3mbj2&code=358ba1b18b2af9f633&redirect_uri=http://127.0.0.1:9999/callback
# VK_OAUTH2_KEY=51731830
# VK_OAUTH2_SECRET=f2b5BdabzcltJ0g3mbj2

# https://api.vk.com/method/users.get?access_token="vk1.a.hd087zqRfVJO7NNZKHsTRtGfjWkNqnkuD_fBQvKvN-sGiYg-3RgRW4ZYq_rb5K4px4m_ZnjjkSP1cJs5-Irnt3RYLwDgNQOcUx0PbL7-ekw5RN2dKAnQHnbydYmbtzVcXXvEzRFR60TabIracYiUlPLNtbnAphvbD5Kfq1Xjw8ZiJXlWm3pXl_1E-Ot6UZbVoKSH9gXwg0ho2eyWHPrunQ"&v=5.131&fields=photo_400_orig
# {"access_token":"vk1.a.hd087zqRfVJO7NNZKHsTRtGfjWkNqnkuD_fBQvKvN-sGiYg-3RgRW4ZYq_rb5K4px4m_ZnjjkSP1cJs5-Irnt3RYLwDgNQOcUx0PbL7-ekw5RN2dKAnQHnbydYmbtzVcXXvEzRFR60TabIracYiUlPLNtbnAphvbD5Kfq1Xjw8ZiJXlWm3pXl_1E-Ot6UZbVoKSH9gXwg0ho2eyWHPrunQ","expires_in":86368,"user_id":815780213}
# {"response":[{"id":815780213,"photo_400_orig":"https:\/\/sun37-2.userapi.com\/s\/v1\/ig2\/YMyYGKvCItgrDjI5cu5YFpcB1h7V5eJVVD6reSZfEedz_vDJYh1tZ6EB13XFLcNkKUdlF-nZQ-utdLU1wg7Kr_eQ.jpg?size=400x400&quality=95&crop=420,0,999,1000&ava=1","first_name":"Андрей","last_name":"Баркан","can_access_closed":true,"is_closed":false}]}
