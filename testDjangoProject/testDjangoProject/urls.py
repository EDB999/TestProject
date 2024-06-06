from django.contrib import admin
from django.urls import path
# from testapp1 import index_page
from testapp1.views import index_page, add_to_payment_and_delivery, remove_from_payment_and_delivery
from testapp1.views import menu_page
from testapp1.views import payment_and_delivery
from testapp1.views import contacts_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name='index'),
    path('menu/', menu_page, name='menu'),
    path('payment_and_delivery/', payment_and_delivery, name='payment_and_delivery_page'),
    path('contacts/', contacts_page, name='contacts'),
    path('add_to_payment_and_delivery/<int:id>/', add_to_payment_and_delivery, name='add_to_payment_and_delivery'),
    path('remove_from_payment_and_delivery/<int:id>/', remove_from_payment_and_delivery, name='remove_from_payment_and_delivery'),
]
