# from .filters import NippoModelFilter    

class ...

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # ctx["filter"] = NippoModelFilter(self.request.GET, queryset=self.get_queryset())
        return ctx
