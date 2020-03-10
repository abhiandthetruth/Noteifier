from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Topic, Note
from .forms import TopicForm,NoteForm
from django.http import Http404

def home(request):
    """The home page"""
    return render(request, 'notes/home.html')

@login_required
def topics(request):
    """The page with list of topics"""
    user = request.user
    topics = user.topic_set.order_by('date')
    context = {'topics': topics}
    return render(request, 'notes/topics.html', context)

@login_required
def topic(request, topic_id):
    """Page with list of notes under a topic"""
    user = request.user
    topic = get_object_or_404( Topic, id=topic_id)
    if topic.user != request.user:
        raise Http404
    notes = topic.note_set.order_by('date')
    context = {'topic': topic, 'notes': notes}
    return render(request, 'notes/topic.html', context)

@login_required
def create_topic(request):
    """Create a new topic"""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.user = request.user
            topic.save()
            return redirect('notes:topics')
    
    context = {'form': form}
    return render(request, 'notes/create.html', context)

@login_required
def delete_topic(request, topic_id):
    """Delete a topic"""
    topic = get_object_or_404( Topic, id=topic_id)
    if topic.user != request.user:
        raise Http404
    topic.delete()
    return redirect('notes:topics')

@login_required
def create_note(request, topic_id):
    """Create a new note"""
    topic = get_object_or_404( Topic, id=topic_id)
    if request.method != 'POST':
        form = NoteForm()
    else:
        form = NoteForm(data=request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.topic = topic
            note.save()
            return redirect('notes:topic', topic_id=topic_id)
    context = {'topic':topic, 'form':form}
    return render(request, 'notes/create_note.html', context)

@login_required
def edit_note(request, note_id):
    """Edit a note"""
    user = request.user
    note = get_object_or_404( Note, id=note_id)
    topic = note.topic
    if topic.user != user:
        raise Http404
    if request.method != 'POST':
        form = NoteForm(instance=note)
    else:
        form = NoteForm(instance=note, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes:topic', topic_id=topic.id)
    context = {'note' : note, 'topic':topic, 'form':form}
    return render(request, 'notes/edit_note.html', context)

@login_required
def delete_note(request, note_id):
    """Delete a note"""
    user = request.user
    note = get_object_or_404( Note, id=note_id)
    topic = note.topic
    if topic.user != user:
        raise Http404
    note.delete()
    return redirect('notes:topic', topic_id=topic.id)
