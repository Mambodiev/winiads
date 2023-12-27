from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .models import Product


class ProductPermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        product = get_object_or_404(Product, slug=self.kwargs["slug"])
        subscription = request.user.subscription
        pricing_tier = subscription.pricing
        if not pricing_tier in product.pricing_tiers.all():
            messages.info(request, "You do not have access to this product")
            return redirect("content:product-list")
        return super().dispatch(request, *args, **kwargs)