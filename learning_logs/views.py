from django.shortcuts import render

def index(request):
    return render(request, 'learning_logs/index.html')

def topic(request, topic_id):
    return render(request, 'learning_logs/topic.html',
                  {'topic_id': topic_id})