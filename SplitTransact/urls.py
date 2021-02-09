from django.conf.urls import url
from  . import views


urlpatterns = [
    # /balance/
    # url(r'^$', views.index, name ='index'),
    # /balance/add_transaction
    url(r'add_expense/$', views.AddUserExpenses.as_view(), name ='add_expenses'),
    url(r'add-to-group/^$', views.AddTOGroup.as_view(), name='user_add_t0_a_group'),
    url(r'balance/<?P<user_id>\d+>/^$', views.ShowBalance.as_view(), name='Show User Balance in Paritcular Group'),
    url(r'create_group/^$', views.CreateGroup.as_view(), name='create_group'),


    # /balance/details <id number>
    # url(r'^(?P<group_id>\w+)/$', views.detail, name='detail'),
]

