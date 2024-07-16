from django.shortcuts import render

def blog(request):
    context = {
        'posts': [
            {'title': 'Post 1', 'content': 'Content of post 1'},
            {'title': 'Post 2', 'content': 'Content of post 2'},
        ],
    }
    return render(request, 'blog/blog.html', context)

