"""raptar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from raptar.data_service.view.startpipeline_view import StartPipelineView
from raptar.data_service.view.startpipeline_view import StartPipelineRUDView
from raptar.data_service.view.testsuite_view import TestSuiteView
from raptar.data_service.view.testcase_view import StartTestCaseView
from raptar.data_service.view.testcase_view import TestCaseRUDView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pipeline/start', StartPipelineView.as_view()),
    path('pipeline/finish', StartPipelineRUDView.as_view()),
    path('testsuite/add', TestSuiteView.as_view()),
    path('testcase/start', StartTestCaseView.as_view()),
    path('testcase/finish', TestCaseRUDView.as_view())
]
