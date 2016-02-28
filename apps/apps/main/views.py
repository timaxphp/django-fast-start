# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

import decimal
import json


class IndexView(TemplateView):
    template_name = "index.html"
