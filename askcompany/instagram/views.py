from django.shortcuts import render
from .models import Post
# Create your views here.
def post_list(request):
    qs = Post.objects.all() # 전체 부른다
    q = request.GET.get('q', '') # q 인자가져온다
    # request.POST
    # request.FILES

    if q:
        qs = qs.filter(message__icontains=q)
    return render(request, 'instagram/post_list.html', {
        'post_list':qs,
        'q':q,
    })
    