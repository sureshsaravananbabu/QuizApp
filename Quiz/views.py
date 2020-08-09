from django.shortcuts import render
from django.views import View
from .models import Question,Quiz
class QuizTest(View):
    template_name = 'Quiz.html'
    template_name1='answer.html'
    def get(self, request, *args, **kwargs):
        Quizes=Quiz.objects.filter(Title=self.kwargs['Title'])
        context={
            'Quiz':Quizes,
            'Title': getattr(Quizes[0],'Title'),
			'number':range(1, 11)
        }
        return render(request, self.template_name,context)

    def post(self, request, *args, **kwargs):
        correct_answer=0
        unanswer=0
        ans=0
        Your_answer=list()
        Quizes=Quiz.objects.all()
        Answer=Quiz.objects.filter(Title=request.POST.get("Title"))
        for temp in Answer:
            Your_answer.append(request.POST.get(str(temp.q_id)))
            if request.POST.get(str(temp.q_id)) == None :
                unanswer=unanswer+1
            else:
                ans=ans+1
            if temp.Question.correct_answer==request.POST.get(str(temp.q_id)):
                correct_answer=correct_answer+1
        
        Your_answer = [str(i or 'Not Answered') for i in Your_answer]
        context={
            'correct':correct_answer,
            'Unanswer':unanswer,
            'Answered':ans,
            'Quiz':Quizes,
            'Title':request.POST.get("Title"),
            'number':range(1, 11),
            'Your_answer':Your_answer
            }
        return render(request,self.template_name1,context)
