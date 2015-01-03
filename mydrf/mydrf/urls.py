from django.conf.urls import include,url
from rest_framework import routers
from bank import views

router = routers.DefaultRouter()
router.register(r'customer',views.customerViewSet)
router.register(r'customer/[0-9]/',views.customerViewSet)
router.register(r'account',views.accountViewSet)
router.register(r'account/c/[0-9]/',views.accountViewCredit)
router.register(r'account/d/[0-9]/',views.accountViewDebit)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
