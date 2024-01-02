from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from app_hw.forms import PostForm
from app_hw.models import Post


def main_page_view(request):
    context = {'post_list': Post.objects.all()}

    return render(request, 'app_hw/index.html', context)


def detail_page_view(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {'post_id': post}

    return render(request, 'app_hw/post_detail.html', context)


class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'app_hw/post_create.html'
    success_url = reverse_lazy('main_page')


def create_page_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_page')
    else:
        form = PostForm()
    context = {'form': form}

    return render(request, 'app_hw/post_create.html', context)


def delete_post_view(request, pk):
    if request.method == 'POST':
        Post.objects.filter(pk=pk).delete()

        return redirect('main_page')
    return render(request, 'app_hw/post_delete.html')


def update_post_view(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('main_page')
    else:
        form = PostForm(instance=post)

    context = {'form': form}

    return render(request, 'app_hw/post_update.html', context)

