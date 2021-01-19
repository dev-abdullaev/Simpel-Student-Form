from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm


def indexView(request):
    form = StudentForm()
    students = Student.objects.all()
    form_class = StudentForm
    if request.method == "POST":
        form = StudentForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form, 'students': students}
    return render(request, 'index.html', context)


def updateView(request, id):
    students = Student.objects.get(id=id)
    form = StudentForm(instance=students)

    if request.method == "POST":
        form = StudentForm(request.POST or None, instance=students)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form, 'students': students}
    return render(request, 'update.html', context)


def deleteView(request, id):
    students = Student.objects.get(id=id)
    if request.method == "POST":
        students.delete()
        return redirect('index')

    context = {'students': students}
    return render(request, 'delete.html', context)
