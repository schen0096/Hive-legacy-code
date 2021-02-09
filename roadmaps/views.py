# from django.shortcuts import render,get_object_or_404,redirect
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
# from django.views.generic import UpdateView, CreateView
# from .models import arcade_weekly_roadmap,roadmap_urls
# from .forms import RoadmapForm,RoadmapUrlMap
# from django.contrib.auth.mixins import UserPassesTestMixin
# from django.urls import reverse_lazy
# # Create your views here.

# @login_required
# def roadmapList(request):
#     roadmaps = roadmap_urls.objects.all()
#     return render(request, 'roadmaps/roadmap_list.html', {'roadmaps':roadmaps})

# @login_required
# def roadmapPage(request, pk):
#     roadmap = get_object_or_404(roadmap_urls, pk=pk)
#     return render(request, 'roadmaps/roadmap_page.html', {'roadmap':roadmap})



# @method_decorator(login_required, name='dispatch')
# class CreateRoadmapUrlView(UserPassesTestMixin, CreateView):
#     model = roadmap_urls
#     form_class = RoadmapUrlMap
#     template_name = 'roadmaps/add_roadmap_url.html'
#     success_url = reverse_lazy('roadmap_list')
#     def test_func(self):
#         return self.request.user.groups.filter(name="Roadmaps").exists()
#     def handle_no_permission(self):
#         return redirect('roadmap_list')

# @method_decorator(login_required, name='dispatch')
# class UpdateRoadmapUrlView(UserPassesTestMixin,UpdateView):
#     model = roadmap_urls
#     form_class = RoadmapUrlMap
#     template_name = 'roadmaps/edit_roadmap_url.html'
#     pk_url_kwarg = 'pk'
#     def test_func(self):
#         return self.request.user.groups.filter(name="Roadmaps").exists()
#     def handle_no_permission(self):
#         return redirect('roadmap_list')
#     def get_success_url(self):
#         return reverse_lazy('roadmap_page',kwargs={'pk':self.object.pk})

# @login_required
# def arcadeWeeklyPage(request):
#     image = arcade_weekly_roadmap.objects.order_by('-id')[0]
#     return render(request, 'roadmaps/weekly_roadmap.html', {'i':image})


# @method_decorator(login_required, name='dispatch')
# class CreateRoadmapView(UserPassesTestMixin, CreateView):
#     model = arcade_weekly_roadmap
#     form_class = RoadmapForm
#     template_name = 'roadmaps/upload.html'
#     success_url = reverse_lazy('roadmap')
#     def test_func(self):
#         return self.request.user.groups.filter(name="Roadmap").exists()
#     def handle_no_permission(self):
#         return redirect('home')