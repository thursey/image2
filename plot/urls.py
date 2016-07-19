from django.conf.urls import url

from . import views, plot

urlpatterns = [
	#url(r'^charts/simple.png$',plot.simple, 'myapp.views.charts.simple')
        #url(r'^$',plot.simple, name = 'simple.chart')
        url(r'^$',views.index,name='index'),
        url(r'^simple.png$',plot.simple,name='simple.chart'),
        #url(r'^/static/plot/image/optplot.png$',,name='optplot'),
]
