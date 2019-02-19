from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")
    
def student(request,name):
    students = {
        "홍길동":24,
        "박길동":28,
        "김길동":30
    }
    age = students.get(name)
    return render(request,"student.html",{"name":name,"age":age})