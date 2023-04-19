
from django.urls import path
from . import views
app_name="urls"
urlpatterns = [
    path('' , views.startpage , name='startpage'),
    path('home/' , views.index , name='index'),
    # <Teaches>-------------------------------------------
    path('paye7/' , views.theaches7 , name='paye7'),
    path('paye8/' , views.theaches8 , name='paye8'),
    path('paye9/' , views.theaches9 , name='paye9'),
    #-----------------------------------------------------
    # <Seasons>----------------------------------------------------------------
    # <Paye7>----------------------------------------------------------
    path('paye7/season1/' , views.Paye7_season1 , name='paye7_season1'),
    path('paye7/season2/' , views.Paye7_season2 , name='paye7_season2'),
    path('paye7/season3/' , views.Paye7_season3 , name='paye7_season3'),
    path('paye7/season4/' , views.Paye7_season4 , name='paye7_season4'),
    path('paye7/season5/' , views.Paye7_season5 , name='paye7_season5'),
    path('paye7/season6/' , views.Paye7_season6 , name='paye7_season6'),
    path('paye7/season7/' , views.Paye7_season7 , name='paye7_season7'),
    path('paye7/season8/' , views.Paye7_season8 , name='paye7_season8'),
    path('paye7/season9/' , views.Paye7_season9 , name='paye7_season9'),
    # -----------------------------------------------------------------
    # <Paye8>----------------------------------------------------------
    path('paye8/season1/' , views.Paye8_season1 , name='paye8_season1'),
    path('paye8/season2/' , views.Paye8_season2 , name='paye8_season2'),
    path('paye8/season3/' , views.Paye8_season3 , name='paye8_season3'),
    path('paye8/season4/' , views.Paye8_season4 , name='paye8_season4'),
    path('paye8/season5/' , views.Paye8_season5 , name='paye8_season5'),
    path('paye8/season6/' , views.Paye8_season6 , name='paye8_season6'),
    path('paye8/season7/' , views.Paye8_season7 , name='paye8_season7'),
    path('paye8/season8/' , views.Paye8_season8 , name='paye8_season8'),
    path('paye8/season9/' , views.Paye8_season9 , name='paye8_season9'),
    # -----------------------------------------------------------------
    # <Paye9>----------------------------------------------------------
    path('paye9/season1/' , views.Paye9_season1 , name='paye9_season1'),
    path('paye9/season2/' , views.Paye9_season2 , name='paye9_season2'),
    path('paye9/season3/' , views.Paye9_season3 , name='paye9_season3'),
    path('paye9/season4/' , views.Paye9_season4 , name='paye9_season4'),
    path('paye9/season5/' , views.Paye9_season5 , name='paye9_season5'),
    path('paye9/season6/' , views.Paye9_season6 , name='paye9_season6'),
    path('paye9/season7/' , views.Paye9_season7 , name='paye9_season7'),
    path('paye9/season8/' , views.Paye9_season8 , name='paye9_season8'),
    # -----------------------------------------------------------------
    # -------------------------------------------------------------------------
    # <Lessons>----------------------------------------------------------------
    path('<slug:slug>' , views.Lesson , name='lessons'),
    # -------------------------------------------------------------------------
    # <register user>----------------------------------------------------------
    # <signup>
    path('signup/' , views.user_signup , name="signup"),
    # <signin>
    path('signin/' , views.user_signin , name="signin"),
    # <logout>
    path('logout/' , views.user_logout , name="logout"),
    # -------------------------------------------------------------------------
    # # <Contact>----------------------------------------------------------------
    # path('contact/' , views.user_Contact , name='contact'),
    # # -------------------------------------------------------------------------
    path('firstlogin/' , views.firstlogin , name='firstlogin'),
    
    path('addafter/' , views.addafter , name='addafter'),
]

