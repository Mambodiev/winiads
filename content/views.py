from django.views import generic
from django.shortcuts import get_object_or_404, reverse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django_filters.views import FilterView

from .models import Product, Video, City, OrderItem, AliexpressOrderGrowth
from .mixins import ProductPermissionMixin
from .filters import ProductFilter 
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from django.http import JsonResponse
from .forms import ContactForm, AddToCartForm
from .utils import get_or_set_order_session


class FilteredListView(ListView):
    filterset_class = None

    def get_queryset(self):
        # Get the queryset however you usually would.  For example:
        queryset = super().get_queryset()
        # Then use the query parameters and the queryset to
        # instantiate a filterset and save it as an attribute
        # on the view instance for later.
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        # Return the filtered queryset
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the filterset to the template - it provides the form.
        context['filterset'] = self.filterset
        return context



class ProductListView(FilteredListView):
    
    model = Product
    filterset_class = ProductFilter
    # product_total = len(Product.objects.filter())
    
    template_name = "content/product_list.html"
    paginate_by = 10

    def get_queryset(self, **kwargs):
       qs = super().get_queryset(**kwargs)
       return qs.filter(product_status='published')
    

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        product_total= Product.objects.count()
        return context

class ProductDetailView(generic.FormView):
    template_name = "content/product_detail.html"
    model = Product
    form_class = AddToCartForm
    # queryset = Product.objects.all()
    
    def get_object(self):
        return get_object_or_404(Product, slug=self.kwargs["slug"])
    
    def get_success_url(self):
        return reverse("content:summary")
    
    def form_valid(self, form):
        order = get_or_set_order_session(self.request)
        Product = self.get_object()

        item_filter = order.items.filter(product=product)

        if item_filter.exists():
            item = item_filter.first()
            item.quantity = int(form.cleaned_data['quantity'])
            item.save()

        else:
            new_item = form.save(commit=False)
            new_item.product = product
            new_item.order = order
            new_item.save()

        return super(ProductDetailView, self).form_valid(form)
    
    # def get_context_data(self, **kwargs):
    #     context = super(ProducteDetailView, self).get_context_data(**kwargs)
    #     product = self.get_product()
    #     subscription = self.request.user.subscription
    #     pricing_tier = subscription.pricing
    #     subscription_is_active = subscription.status == "active" or subscription.status == "trialing" 
                
    #     context.update({
    #         "has_permission": pricing_tier in product.pricing_tiers.all() and subscription_is_active
    #     })
    #     return context
    
    def get_product(self):
        return get_object_or_404(Product, slug=self.kwargs["slug"])
    
    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['product'] = self.get_object()
        return context
    
# def product_chart(request):
#     labels = []
#     data = []

#     queryset = City.objects.all()
#     for city in queryset:
#         labels.append(city.name)
#         data.append(city.population)
    
#     return JsonResponse(data={
#         'labels': labels,
#         'data': data,
#     })


def product_chart(request):
    labels = []
    data = []

    queryset = AliexpressOrderGrowth.objects.all()
    for aliexpressOrderGrowth in queryset:
        labels.append(aliexpressOrderGrowth.name)
        data.append(aliexpressOrderGrowth.order_quantity)
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

class VideoDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "content/video_detail.html"

    def get_context_data(self, **kwargs):
        context = super(VideoDetailView, self).get_context_data(**kwargs)
        product = self.get_product()
        subscription = self.request.user.subscription
        pricing_tier = subscription.pricing
        subscription_is_active = subscription.status == "active" or subscription.status == "trialing" 
        context.update({
            "has_permission": pricing_tier in product.pricing_tiers.all() and subscription_is_active
        })
        return context

    def get_product(self):
        return get_object_or_404(Product, slug=self.kwargs["slug"])

    def get_object(self):
        video = get_object_or_404(Video, slug=self.kwargs["video_slug"])
        return video

    def get_queryset(self):
        product = self.get_product()
        return product.videos.all()
    

class ProductView(generic.TemplateView):
    template_name = "content/add_to_favorite.html"

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context["order"] = get_or_set_order_session(self.request)
        return context
    
    
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


class RemoveFromProductView(generic.View):
    def get(self, request, *args, **kwargs):
        order_item = get_object_or_404(OrderItem, id=kwargs['pk'])
        order_item.delete()
        return redirect("content:summary")