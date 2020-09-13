
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index),
    path('google/',views.google),
    path('product/<int:id>',views.product),
    path('catprod/<int:id>',views.catprod),
    path('contact/',views.contact),
    path('allcat/',views.allcat),
    path('createprod/',views.createProduct),
    path('updateprod/<int:id>/',views.updateProduct),
    path('deleteprod/<int:id>/',views.deleteProduct)
]