from django.shortcuts import render

# Create your views here.
def portfolio_view(request):
    template_name = 'portfolio/pf_index.html'
    def mycontext():
        data = requests.get("https://example.com")

        return data
    return render(request, template_name,{"data":mycontext})

def sample_a(request):
    template_name = 'sample_a.html'
    return render(request, template_name, context={})

def sample_b(request, **kwargs):
    template_name = "portfolio/tmp.html"
    return render(request, template_name)