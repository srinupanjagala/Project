from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView, productDetails, loginpage, register, cart

urlpatterns = [
    path('', HomeView.as_view(), name='Home'),
    path('productDetails/<int:pk>', productDetails, name='productDetails'),
    path('login', loginpage, name='login'),
    path('register', register, name='register'),
    path('cart/<str:name>', cart, name='cart')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
