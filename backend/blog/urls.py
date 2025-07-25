from .views import BlogView, CommentsView,BlogDetailsView, CommentDetailsView

#define url patterns for the blog app
from django .urls import path




urlpatterns = [
    path('blog/',BlogView.as_view()),
    path('comment/', CommentsView.as_view()),

    path('blog/<int:pk>/' ,BlogDetailsView.as_view()),
    path('comment/<int:pk>/',CommentDetailsView.as_view()),



]
