from django.shortcuts import render
from .models import PostModel
from .models import CommentModel

# Create your views here.
def index(request):

    allpost = PostModel.objects.all()
    comment = CommentModel.objects.all()

    d = {

        'posts': allpost,
        'comments': comment

    }

    return render(request, 'photo_app/index.html', d)