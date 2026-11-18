
from django.shortcuts import render
from .models import Topic

def index(request):
    return render(request, 'learning_logs/index.html')


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('date_added')

    context = {
        'topic': topic,
        'entries': entries
    }

    return render(request, 'learning_logs/topic.html', context)
