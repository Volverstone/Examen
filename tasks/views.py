from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from tasks.models import Tasks
from tasks.form import SearchForm
from django.db.models import Q

def main_page_view(request):
    if request.method == "GET":
        return render(request,"base.html")

def task_list_view(request):
    if request.method == "GET":
        tasks = Tasks.objects.all()
        form = SearchForm(request.GET)
        ordering = request.GET.get("ordering")
        category = request.GET.getlist("tag")
        search = request.GET.get("search")
        if search:
            tasks = tasks.filter(Q(title__icontains=search) | Q(content__icontains=search))
        if category:
            tasks = tasks.filter(tags__id__in=category)
        if ordering:
            tasks = tasks.order_by(ordering)

        page = request.GET.get("page", 1)
        page = int(page)
        limit = 3
        max_pages = tasks.count() / limit
        if round(max_pages) < max_pages:
            max_pages = round(max_pages) +1
        else:
            max_pages = round(max_pages)

        start = (page-1) * limit
        end = page * limit

        posts = posts[start:end]
        context = {"posts": posts, "form": form, "max_pages": range(1, max_pages+1)}
        return render(request,"posts/post_list.html", context=context)


class TaskListView(ListView):
    model = Tasks
    template_name = "tasks/tasks_list.html"
    context_object_name = "tasks"

class TaskCreateView(CreateView):
    model = Tasks
    template_name = "tasks/task_create.html"
    form_class = PostForm
    success_url = "main"

class TaskDetailView(DetailView):
    model = Tasks
    pk_url_kwarg = "post_id"
    template_name = "tasks/task_detail.html"
    context_object_name = "tasks"
    success_url = "main/"


