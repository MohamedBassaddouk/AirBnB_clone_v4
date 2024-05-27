#!/usr/bin/python3
"""
this is the main init view page
"""

from flask import Blueprint

app_views = Blueprint('/api/v1', __name__, url_prefix="/api/v1")

from index import *
from states import *
from amenities import *
from cities import *
from places import *
from places_reviews import *
from users import *
from places_amenities import *
