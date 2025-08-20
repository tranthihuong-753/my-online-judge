from django.shortcuts import render, redirect, get_object_or_404
from .models import Problem
from .forms import ProblemForm

def problem_list(request):
    problems = Problem.objects.all()
    return render(request, 'judge/problem_list.html', {'problems': problems})

def problem_create(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('problem_list')
    else:
        form = ProblemForm()
    return render(request, 'judge/problem_form.html', {'form': form})

def problem_update(request, pk):
    problem = get_object_or_404(Problem, pk=pk)
    if request.method == 'POST':
        form = ProblemForm(request.POST, instance=problem)
        if form.is_valid():
            form.save()
            return redirect('problem_list')
    else:
        form = ProblemForm(instance=problem)
    return render(request, 'judge/problem_form.html', {'form': form})

def problem_delete(request, pk):
    problem = get_object_or_404(Problem, pk=pk)
    if request.method == 'POST':
        problem.delete()
        return redirect('problem_list')
    return render(request, 'judge/problem_confirm_delete.html', {'problem': problem})
