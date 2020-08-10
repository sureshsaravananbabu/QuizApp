# QuizApp
It is a simple Quiz conducting application where student can attend quiz
there will issue in multiforloop package



You need to replace the code with this patch

1 -> Copy multiforloop/templatetags to a templatetags folder in your project.



2 -> replace from itertools import izip_longest with from itertools import zip_longest

replace from django.template.base import Library with from django import template

replace register = Library() with register = template.Library()

And then it works fine!!!!!
