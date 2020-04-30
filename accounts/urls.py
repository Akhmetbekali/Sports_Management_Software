from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from accounts import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', LoginView.as_view(template_name='log_in.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(template_name='log_out.html'), name='logout'),
    url(r'^register/$', views.register, name='register'),

    url(r'^profile/(?P<id>\d+)$', views.profile, name='profile'),
    url(r'^profile/edit/$', views.profile_edit, name='profile_edit'),
    url(r'^profiles/$', views.all_profiles, name='all_profiles'),

    url(r'^change_password/$', views.change_password, name='change_password'),
    url(r'^reset_password/$', PasswordResetView.as_view(template_name="registration/password_reset_form.html"),
        name='password_reset'),
    url(r'^reset_password/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset_password/complete/$',
        PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"),
        name='password_reset_complete'),

    url(r'^create_club/$', views.create_club, name='create_club'),
    url(r'^club_page/(?P<id>\d+)$', views.club_page, name='club_page'),
    url(r'^participate/(?P<id>\d+)$', views.participate, name='participate'),
    url(r'^clubs/$', views.all_clubs, name='all_clubs'),
    url(r'^edit_club/(?P<id>\d+)$', views.edit_club, name='edit_club'),
    url(r'^club/delete/(?P<id>\d+)', views.delete_club, name='delete_club'),
]