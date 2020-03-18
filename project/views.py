from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy


from project.forms import ActivityForm
from project.models import Activity
from django.http import HttpResponse, HttpResponseRedirect



class Home(generic.CreateView):
    def get(self, request):
        return render(request, 'base.html')

class ActivityListView(generic.ListView):
    """ Renders a list of all projects. """
    model = Activity

    def get(self, request):
        """ GET a list of projects. """
        activities = self.get_queryset().all()
        return render(request, 'list.html', {
          'activities': activities
        })

class ActivityDetailView(generic.DetailView):
    """ Renders a specific project based on it's slug."""
    model = Activity

    def get(self, request, slug):
        """ Returns a specific projects project by slug. """
        activity = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'activity.html', {
          'activity': activity
        })
class ActivityCreateView(generic.CreateView):
    form_class = ActivityForm
    template_name = "new_activity.html"

    def post(self, request, *args, **kwargs):
        form = ActivityForm(request.POST)
        if form.is_valid():
            project = form.save()
            project.save()
            return HttpResponseRedirect(reverse_lazy("activity-details-project", args=[project.slug]))

class ActivityUpdateView(generic.UpdateView):
    model = Activity
    fields = ['title','content']
    template_name = 'new_activity.html'

class ActivityDeleteView(generic.DeleteView):
    model = Activity
    success_url = reverse_lazy('activity-list-project')
    template_name = 'confirm_delete.html'
