#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 18:09:26 2020

@author: kapil
"""

from django.urls import path

from . import views

urlpatterns=[
        
        path('',views.home,name='home'),
        path('addition',views.add,name='add')
]