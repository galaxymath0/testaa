from pprint import pp
from django.shortcuts import render , get_object_or_404 , redirect
from .models import *
from .forms import *
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login , authenticate , logout 
from django.contrib.auth.models import User
from .models import *

# Create your views here.

def startpage(request):
    return render(request , "startpage.html")

def index(request):
    return render(request , "index.html")
   
# <Teaches>-------------------------------------------------------
def theaches7(request):
    return render(request , "theaches-html/theaches7.html")

def theaches8(request):
    return render(request , "theaches-html/theaches8.html")

def theaches9(request):
    return render(request , "theaches-html/theaches9.html")    
#-----------------------------------------------------------------
# <Seasons>-------------------------------------------------------
# <Paye7>------------------------------------------------
def Paye7_season1(request):
    lessons = Lessons.objects.filter(status='paye7_season1')
    return render(request , "Seasons/Paye7/season1.html" , {'lesson' : lessons})

def Paye7_season2(request):
    lessons = Lessons.objects.filter(status='paye7_season2')
    return render(request , "Seasons/Paye7/season2.html" , {'lesson' : lessons})

def Paye7_season3(request):
    lessons = Lessons.objects.filter(status='paye7_season3')
    return render(request , "Seasons/Paye7/season3.html" , {'lesson' : lessons})

def Paye7_season4(request):
    lessons = Lessons.objects.filter(status='paye7_season4')
    return render(request , "Seasons/Paye7/season4.html" , {'lesson' : lessons})

def Paye7_season5(request):
    lessons = Lessons.objects.filter(status='paye7_season5')
    return render(request , "Seasons/Paye7/season5.html" , {'lesson' : lessons})

def Paye7_season6(request):
    lessons = Lessons.objects.filter(status='paye7_season6')
    return render(request , "Seasons/Paye7/season6.html" , {'lesson' : lessons})

def Paye7_season7(request):
    lessons = Lessons.objects.filter(status='paye7_season7')
    return render(request , "Seasons/Paye7/season7.html" , {'lesson' : lessons})

def Paye7_season8(request):
    lessons = Lessons.objects.filter(status='paye7_season8')
    return render(request , "Seasons/Paye7/season8.html" , {'lesson' : lessons})

def Paye7_season9(request):
    lessons = Lessons.objects.filter(status='paye7_season9')
    return render(request , "Seasons/Paye7/season9.html" , {'lesson' : lessons})
# ------------------------------------------------------
# <Paye8>-----------------------------------------------
def Paye8_season1(request):
    lessons = Lessons.objects.filter(status='paye8_season1')
    return render(request , "Seasons/Paye8/season1.html" , {'lesson' : lessons}) 

def Paye8_season2(request):
    lessons = Lessons.objects.filter(status='paye8_season2')
    return render(request , "Seasons/Paye8/season2.html" , {'lesson' : lessons}) 

def Paye8_season3(request):
    lessons = Lessons.objects.filter(status='paye8_season3')
    return render(request , "Seasons/Paye8/season3.html" , {'lesson' : lessons}) 

def Paye8_season4(request):
    lessons = Lessons.objects.filter(status='paye8_season4')
    return render(request , "Seasons/Paye8/season4.html" , {'lesson' : lessons}) 

def Paye8_season5(request):
    lessons = Lessons.objects.filter(status='paye8_season5')
    return render(request , "Seasons/Paye8/season5.html" , {'lesson' : lessons}) 

def Paye8_season6(request):
    lessons = Lessons.objects.filter(status='paye8_season6')
    return render(request , "Seasons/Paye8/season6.html" , {'lesson' : lessons}) 

def Paye8_season7(request):
    lessons = Lessons.objects.filter(status='paye8_season7')
    return render(request , "Seasons/Paye8/season7.html" , {'lesson' : lessons}) 

def Paye8_season8(request):
    lessons = Lessons.objects.filter(status='paye8_season8')
    return render(request , "Seasons/Paye8/season8.html" , {'lesson' : lessons}) 

def Paye8_season9(request):
    lessons = Lessons.objects.filter(status='paye8_season9')
    return render(request , "Seasons/Paye8/season9.html" , {'lesson' : lessons})     
# ------------------------------------------------------
# <Paye9>-----------------------------------------------  
def Paye9_season1(request):
    lessons = Lessons.objects.filter(status='paye9_season1')
    return render(request , "Seasons/Paye9/season1.html" , {'lesson' : lessons})  

def Paye9_season2(request):
    lessons = Lessons.objects.filter(status='paye9_season2')
    return render(request , "Seasons/Paye9/season2.html" , {'lesson' : lessons}) 

def Paye9_season3(request):
    lessons = Lessons.objects.filter(status='paye9_season3')
    return render(request , "Seasons/Paye9/season3.html" , {'lesson' : lessons}) 

def Paye9_season4(request):
    lessons = Lessons.objects.filter(status='paye9_season4')
    return render(request , "Seasons/Paye9/season4.html" , {'lesson' : lessons}) 

def Paye9_season5(request):
    lessons = Lessons.objects.filter(status='paye9_season5')
    return render(request , "Seasons/Paye9/season5.html" , {'lesson' : lessons}) 

def Paye9_season6(request):
    lessons = Lessons.objects.filter(status='paye9_season6')
    return render(request , "Seasons/Paye9/season6.html" , {'lesson' : lessons}) 

def Paye9_season7(request):
    lessons = Lessons.objects.filter(status='paye9_season7')
    return render(request , "Seasons/Paye9/season7.html" , {'lesson' : lessons}) 

def Paye9_season8(request):
    lessons = Lessons.objects.filter(status='paye9_season8')
    return render(request , "Seasons/Paye9/season8.html" , {'lesson' : lessons}) 
# ------------------------------------------------------  
# ---------------------------------------------------------------- 
# <Lessons>-------------------------------------------------------
def Lesson(request , slug):
    lesson = get_object_or_404 (Lessons , slug=slug)
    return render(request , 'Lessons.html' , {'lessons':lesson})
# ---------------------------------------------------------------- 


# <register user>-------------------------------------------------
# <sign up>---------------------------------------------
def user_signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass']
        cpass = request.POST['cpass']

        if User.objects.filter(username=username):
            messages.error(request , '!این نام کاربری قبلا استفاده شده است')
            return redirect('urls:signup')

        if len(username)<4 or len(username)>20:
            messages.error(request , '!نام کاربری حداقل باید شامل 4 کرکتر و حداکثر 20 کرکتر باشد')
            return redirect('urls:signup')       

        if User.objects.filter(email=email):
            messages.error(request , '!این ایمیل قبلا استفاده شده است') 
            return redirect('urls:signup')   

        if pass1 != cpass:
            messages.error(request , '!رمز عبور مطابقت ندارد')
            return redirect('urls:signup')


        myuser = User.objects.create_user( username , email , pass1 )

        myuser.save()

        messages.success(request , '!حساب کاربری شما با موفقیت ساخته شد')
        return redirect('urls:signin')

    return render(request , 'register-pages/signup.html')
# ------------------------------------------------------
# <signin>----------------------------------------------
def user_signin(request):
    if request.method == 'POST':
        form = loginforms(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request , username = cd['username'] , password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request , user)
                    messages.success(request , 'شما با موفقیت وارد حساب کاربری خود شدید!')
                    return redirect("urls:index")
                else:
                    messages.error(request , '!حساب کاربری شما مسدود شده است')
            else:
                messages.error(request , "!اطلاعات وارد شده صحیح نمیباشد")
                return redirect('urls:signin')
    else:
        form = loginforms()
    return render(request , 'register-pages/signin.html')
# ------------------------------------------------------
# <logout>----------------------------------------------
def user_logout(request):
    logout(request)
    messages.success(request , 'شما با موفقیت از حساب کاربری خود خارج شدید!')
    return redirect("urls:index")
# ------------------------------------------------------
# ----------------------------------------------------------------
# # <Contact>-------------------------------------------------------
# def user_Contact(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         message = request.POST['message']
#         Contact.objects.create(email=email , message=message)
#         messages.success(request , "پیام شما به دست ما رسید! به زودی از طریق ایمیل به ان پاسخ خواهیم داد")
#         return redirect('urls:contact')

#         return render(request , 'contact.html')
#     else:
#         return render(request , 'contact.html')
# # ----------------------------------------------------------------
def firstlogin(request):
    return render(request , 'includes/firstlogin.html')   

def addafter(request):
    return render(request , 'addafter.html')  

def error404(request , exception):
    return render(request , 'error404.html')
