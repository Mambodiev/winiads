from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django_filters.views import FilterView

from .models import Course, Video, City
from .mixins import CoursePermissionMixin
from .filters import CourseFilter 
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from django.http import JsonResponse
from .forms import ContactForm

class CourseListView(LoginRequiredMixin, FilterView):
    
    model = Course
    filterset_class = CourseFilter
    template_name = "content/course_list.html"
    paginate_by = 6
    

class CourseDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "content/course_detail.html"
    queryset = Course.objects.all()

    
    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        course = self.get_course()
        subscription = self.request.user.subscription
        pricing_tier = subscription.pricing
        subscription_is_active = subscription.status == "active" or subscription.status == "trialing" 
                
        context.update({
            "has_permission": pricing_tier in course.pricing_tiers.all() and subscription_is_active
        })
        return context
    
    def get_course(self):
        return get_object_or_404(Course, slug=self.kwargs["slug"])
    
def product_chart(request):
    labels = []
    data = []

    queryset = City.objects.all()
    for city in queryset:
        labels.append(city.name)
        data.append(city.population)
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

    

class VideoDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "content/video_detail.html"

    def get_context_data(self, **kwargs):
        context = super(VideoDetailView, self).get_context_data(**kwargs)
        course = self.get_course()
        subscription = self.request.user.subscription
        pricing_tier = subscription.pricing
        subscription_is_active = subscription.status == "active" or subscription.status == "trialing" 
        context.update({
            "has_permission": pricing_tier in course.pricing_tiers.all() and subscription_is_active
        })
        return context

    def get_course(self):
        return get_object_or_404(Course, slug=self.kwargs["slug"])

    def get_object(self):
        video = get_object_or_404(Video, slug=self.kwargs["video_slug"])
        return video

    def get_queryset(self):
        course = self.get_course()
        return course.videos.all()
    
    
class ContactView(generic.FormView):
    form_class = ContactForm
    template_name = 'pages/contact.html'

    def get_success_url(self):
        return reverse("contact")

    def form_valid(self, form):
        messages.info(
            self.request, "Thanks for getting in touch. We have received your message.")
        email = form.cleaned_data.get(_('email'))
        message = form.cleaned_data.get(_('message'))

        full_message = f"""
            Received message below from , {email}
            ________________________


            {message}
            """
        send_mail(
            subject="Received contact form submission",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL]
        )
        return super(ContactView, self).form_valid(form)
