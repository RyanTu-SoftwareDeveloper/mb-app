from django.views.generic import ListView
from .models import Post

class HomePageView(ListView): # make it a view that automatically queries the databaase for all Post objects
    model = Post # this tell Django that this view should retrieve all Post objects from the database
    template_name = 'home.html' # This specific which HTML template should be used to render the page
    context_object_name = 'all_posts_list'