from django.shortcuts import render, redirect
from django.urls import reverse

from .models import ToDo
from .forms import ToDoForm, ToDoEditForm
# Create your views here.

__empty_reminders__ = [
    {
        "title": 'No Reminders Here.',
        "data": "Start by creating one above.",
        "updated_date_time": "",
        "dead_line": ""
    }
]


def to_do(request):
    reminder_list = ToDo.objects.order_by('-dead_line')
    form = ToDoForm()
    # Edge Case for no reminders
    if len(reminder_list) == 0: reminder_list = __empty_reminders__
    
    context = {
        'form': form.as_table(),
        'to_do_list': reminder_list,
    }

    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('to_do')
        else:
            context['form'] = form.as_table()  # Reprints form with errors too.
            return render(request, 'to_do/to_do.html', context=context)

    return render(request, 'to_do/to_do.html', context=context)


def edit(request, identifier):
    item = ToDo.objects.get(id=identifier)
    
    if request.method == 'POST':
        form = ToDoEditForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('to_do')
        else:
            context = {
                'content': {},
                'form': form.as_table(),
            }
            return render(request, 'to_do/to_do_edit.html', context=context)
    
    else:
        form = ToDoEditForm(instance=item)
        context = {
            'form': form.as_table(),
        }
        return render(request, 'to_do/to_do_edit.html', context=context)


def remove(request, identifier):
    item = ToDo.objects.get(id=identifier)
    item.delete()
    return redirect('to_do')


def index(request):
    context = {}
    return render(request, 'to_do/index.html', context=context)
