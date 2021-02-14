from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def add(request):
    from random import randint

    num_1 = randint(0,10)
    num_2 = randint(0,10)
    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        if not answer:
            my_answer = "Hey, you forgot to fill out the form."
            color = "warning"
            return render(request, 'add.html', {
            "color":color,
            "my_answer":my_answer,
            "answer":answer,
            "num_1":old_num_1,
            "num_2":old_num_2})
        correct_answer = int(old_num_1) + int(old_num_2)
        if int(answer) == correct_answer:
            my_answer = f"Correct, {old_num_1} + {old_num_2} = {correct_answer}"
            color = "success"
        else:
            my_answer = f"Incorrect, {old_num_1} + {old_num_2} does not equal {answer}. It equals {correct_answer}"
            color = "danger"

        # widget=forms.Select(attrs={'onchange': 'submit();'})
        return render(request, 'add.html', {
            "color":color,
            "my_answer":my_answer,
            "correct_answer":correct_answer,
            "answer":answer,
            "num_1":old_num_1,
            "num_2":old_num_2
        })
    return render(request, 'add.html', {
        "num_1":num_1,
        "num_2":num_2
    })

def subtract(request):
    return render(request, 'subtract.html', {})

def multiply(request):
    return render(request, 'multiply.html', {})

def divide(request):
    return render(request, 'divide.html', {})