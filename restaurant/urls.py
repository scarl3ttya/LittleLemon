from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = DefaultRouter()
router.register(r'bookings', views.BookingAPIViewset, basename = 'bookings')

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('book/', views.book, name="book"),
    path('bookings/', views.bookings, name='bookings'), 
    path('reservations/', views.reservations, name= 'reservations'),
    path('menu/', views.menu, name="menu"),
    path('menu/<int:pk>/', views.menu_item, name="menu_item"), 

    path('api/menu/', views.MenuItemsView.as_view()),
    path('api/menu/<int:pk>', views.SingleMenuItemView.as_view()),    
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
   
]