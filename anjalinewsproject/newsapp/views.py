from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,"newsapp/home.html")
def newspage(request):
    head_msg="latest movies news "
    msg1='sonali slowly getting cured'
    msg2='sunny is a charming actress'
    msg3='modi is a charming actress'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,"newsapp/sports.html",context=my_dict)
def moviesinfo(request):
    head_msg="latest movies news "
    msg1='sonali slowly getting cured'
    msg2='sunny is a charming actress'
    msg3='modi is a charming actress'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,"newsapp/movies.html",context=my_dict)
def politicalinfo(request):
    head_msg="latest movies news "
    msg1='sonali slowly getting cured'
    msg2='sunny is a charming actress'
    msg3='modi is a charming actress'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,"newsapp/political.html",context=my_dict)

