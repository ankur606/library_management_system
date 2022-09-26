from django import views
from django.urls import path
from . import views



urlpatterns = [
    
    path('admin-dashboard/', views.adminPanel, name="homePageDashboard"),
    path('', views.login , name="adminLogin"),
    path('user-logout/', views.userlogout, name ='logouts'),
    path('user-details/', views.ShowUserView.as_view(), name ='showUser'),
    path('add-new-user/', views.AddNewUserView.as_view(), name ='addUser'),
    path("delete-user/<int:id>", views.UserDeleteView.as_view(), name="deleteUser" ),
    path('update-user-profile/<int:id>', views.UpdateUserProfileView.as_view(), name="editUser"),
    path("admin-forget-password/",views.forgetPassword, name='forgetPassword'),
    path("add-new-books/",views.AddNewBooksView.as_view(), name="addBooks"),
    path('books-details/', views.ShowBookDetailsView.as_view(), name ='showBooks'),
    path('update-book-recoard/<int:id>', views.UpdateBooksRecoardView.as_view(), name="updaterecoard"),
    path('delete-book-recoard/<int:id>', views.BookDeleteViews.as_view(), name="deleteBook"),
    
    
    
    
    
    
    
    
    
]