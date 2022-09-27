from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth import authenticate,login as dj_login ,logout

from .models import*
from .forms import*
# Create your views here.

class IndexPageDashboard(View):
    
    def get(self, request):
        if request.user.is_superuser == True: 
            return render(request, 'dashboard/index.html')
        else:
            return redirect("adminLogin")
    
   

login_required(login_url='admin-login')
def adminPanel(request):

    user1 = User.objects.filter(is_superuser=True)
    user = User.objects.all()
    
    # ===========user counter=======

    counter=0
    superuser=0
    staff=0
    active = 0
    for i in user:
        counter+=1
        if i.is_superuser == True:
            superuser+=1

        if i.is_staff == True:
            staff+=1
        
        if i.is_active == True:
            active+=1

    d = { "user":user1,
          "all_user":user,
          "counter_user":counter,
          "superuser":superuser,
          'staff':staff,
          "active":active,
     
        }
    if request.user.is_superuser == True:
        return render(request,'dashboard/index.html',d)
    else:
        return redirect('loginAdmin')
    
#=============Admin LOGIN=============

def login(request):
    if request.method == 'POST':
        email_id = request.POST.get('email')
        passwords = request.POST.get('password')
        
        user = authenticate(request=request, email=email_id, password=passwords)
      
        if user is not None:
            if User.objects.filter(email=email_id,is_superuser=True):
                dj_login(request, user)
                return redirect('homePageDashboard')
            else:
                messages.error(request, 'You Are Not Admin User')    
        else:
            messages.error(request, 'Invalid Email or Password')

    return render(request,'dashboard/samples/login.html')    


#=============LOGOUT=============    

def userlogout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully..!!')
    return redirect('adminLogin')


#===== Show All Users In Admin Dashboard =======#

class ShowUserView(View):
    def get(self, request):
        user = User.objects.all()
        return render(request,  'dashboard/show-user.html', {'data':user})
    


class AddNewUserView(View):
    def get(self, request):

        return render(request,  'dashboard/add_user.html')
    
    def post(self, request):
        
       
    
        name = request.POST.get('name')
        
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
  
        password = request.POST.get('password')
        con_password = request.POST.get('password1')
        
        if password == con_password:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'User Email  Already Exist.. ')
            else:
                user = User.objects.create_user(name=name, phone_number=phone_number, email=email,password=password,)
          
                user.save()
                messages.success(request, 'User Added Successfully..!!')
                return redirect('showUser')
            messages.error(request, 'Password Not Match ..!!')
        if request.user.is_superuser == True:
            return render(request,'dasboard/add_user.html')

        else:
            return redirect("/")
    
    

#=============delete User=============
class UserDeleteView(View):
    def get(self, request, id):
        a = User.objects.get(pk=id)
        a.delete()
        messages.success(request, 'User Deleted Successfully..!!')
        return redirect('showUser')    
    
    
    
    

#====== Edit User Profile =========#
class   UpdateUserProfileView(View):
    
    def get(self, request, id):
        if request.user.is_superuser == True:      
            return render(request,'dashboard/edit_user.html',{"user":User.objects.get(pk=id)})
        else:
            return HttpResponseRedirect('/')
        
    
    

    def post(self, request, id):    
     
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
      
          
        super = request.POST.get('super')
        staff = request.POST.get('staff')
        active = request.POST.get('active')
        checklist = [False,False,False]
        
        if super == 'True':
            checklist[0]=True
        if staff == 'True':
            checklist[1]=True
        if active == 'True':
            checklist[2]=True
        
        user = User.objects.get(id=id)

   
        user.name = name
        user.email = email
        user.phone_number = phone_number
        
        user.is_superuser = checklist[0]
        user.is_admin = checklist[1]
        user.is_active = checklist[2]
        user.save()
        messages.success(request, 'User Edit Successfully..!!') 
        return  redirect('showUser')
        
    

def forgetPassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
    
        if User.objects.filter(email=email).exists():   
            password = request.POST.get('password')
           
            v = User.objects.get(email=email)
            if v.is_superuser == True:
                v.set_password(password)
                v.save()
           
                messages.success(request, 'Password Forget Successfully..!!')
                return redirect('adminLogin')
            else:
                messages.error(request, "Sorry! You Are Not Admin User . You Can't  Forget Password! ")
        else:
            messages.error(request, 'Invalid Email..')
    return render(request,'dashboard/samples/forget-password.html')
    


 ############### Add New Books Views #########
 
class AddNewBooksView(View):
    def get(self, request):
        return render(request, 'dashboard/add_books.html')
    def post(self, request):
        
        book_data = BooksModels()
    
        book_name = request.POST.get('book_name')
        author = request.POST.get('author')
        book_isbn = request.POST.get('book_isbn')
        book_category = request.POST.get('book_category')
        print(book_name, author, book_category, book_isbn)
        book_data.book_name = book_name
        book_data.auther = author
        book_data.book_isbn = book_isbn
        book_data.category = book_category
        
        book_data.save()
        messages.success(request, 'New Books Add Successfully..!!')
        return redirect("showBooks")
        

################# show All books recoard Details Views ##########

class ShowBookDetailsView(View):
    def get(self, request):
        data = BooksModels.objects.all()
        return render(request, 'dashboard/show_books_details.html', {'book_data':data})
        
        
               
        
 ############### Add New Books Views #########
 
class UpdateBooksRecoardView(View):
    def get(self, request, id):
        data  = BooksModels.objects.get(pk=id)
        print(data)
        return render(request, 'dashboard/edit_books_recoard.html', {'data':data})
    def post(self, request, id):
        
        book_data = BooksModels()
    
        book_name = request.POST.get('book_name')
        author = request.POST.get('author')
        book_isbn = request.POST.get('book_isbn')
        book_category = request.POST.get('book_category')
        book_date = request.POST.get('book_date')
        
        # print(book_name, author, book_category, book_isbn)
        data = BooksModels(id=id, book_name = book_name, auther = author, book_isbn = book_isbn, category = book_category, created_date=book_date)
        data.save()
        
     
        messages.success(request, ' Books Recoard update Successfully..!!')
        return redirect("showBooks")
                 
### Book Delete Views ###########

class BookDeleteViews(View):
    def get(self, request, id ):
        data = BooksModels.objects.get(id=id)
        data.delete()        
         
        messages.success(request, ' Books Recoard Delete Successfully..!!')
        return redirect("showBooks") 
        



  
