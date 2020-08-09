from django.shortcuts import render
from django.views import View
from Quiz.models import Question,Quiz
from .import forms
from django.shortcuts import redirect
# Create your views here.
class CreateQuiz(View):
    template_name ='Create.html'
    def get(self, request, *args, **kwargs):
        form=forms.Createform()
        context={
            'number':range(1, 11),
            'form':form
        }
        print("helloooo")
        return render(request,self.template_name ,context)

    def post(self, request, *args, **kwargs):
        form=forms.Createform(request.POST)
        if form.is_valid():
            for i in range(1,11):
                question=Question.objects.create(questions=request.POST.get(str('Question')+str(i)),choice_1=request.POST.get(str('choice1')+str(i)),choice_2=request.POST.get(str('choice2')+str(i)),choice_3=request.POST.get(str('choice3')+str(i)),choice_4=request.POST.get(str('choice4')+str(i)),correct_answer=request.POST.get(str('Answer')+str(i)))
                quiz=Quiz.objects.create(q_id=i,Title=request.POST.get('Title'),Description=request.POST.get('Description'),Question=question)
                question.save()
                quiz.save()
            return redirect('/')
        else:
            list = [(k, v) for k, v in dict(form.errors).items()]
            error=list[0][1]
            print(error)
            form=forms.Createform()
            context={
                'form':form,
                'error':error,
                'number':range(1, 11),
            }
            return render(request,self.template_name ,context)
class Home(View):
    template_name='Home.html'
    def get(self,request,*args,**kwargs):
        home=Quiz.objects.values_list('Title','Description').distinct()
        context={
                'home':home,
        }
        print(context)
        return render(request,self.template_name,context)

