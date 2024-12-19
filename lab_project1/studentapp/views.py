
from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Address, Student2, Address2, ImageModel
from .forms import StudentForm, AddressForm, Student2Form, Address2Form, ImageForm

def list_students(request):
    students = Student.objects.all()
    return render(request, 'studentapp/student_list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm()
    return render(request, 'studentapp/student_form.html', {'form': form})

def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'studentapp/student_form.html', {'form': form})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('list_students')
    return render(request, 'studentapp/student_confirm_delete.html', {'student': student})

# Create your views here.
