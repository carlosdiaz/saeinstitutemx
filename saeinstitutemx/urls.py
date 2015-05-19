from django.conf.urls import patterns, include, url
from django.contrib import admin
import skillstudents.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'saeinstitutemx.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),    
    url(r'^accounts/login/$', skillstudents.views.login),
    url(r'^accounts/auth/$', skillstudents.views.auth_view),
    url(r'^accounts/logout/$', skillstudents.views.logout),
    #url(r'^accounts/loggedin/$', skillstudents.views.loggedin),
    url(r'^accounts/loggedin/$', skillstudents.views.CreateView.as_view(), name='create_students'),
    url(r'^accounts/studentlist/$', skillstudents.views.ListContactView.as_view(),name='student_list',),
    url(r'^accounts/invalid/$', skillstudents.views.invalid_login),
    url(r'^accounts/studentadded/$', skillstudents.views.studentadded,name='student_added',),
        
)
