from django.contrib import admin
from .models import Venue, Event, Booking, Expense, Feedback

admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(Booking)
admin.site.register(Expense)
admin.site.register(Feedback)
admin.site.site_header = "Smart Event Portal Admin"
admin.site.site_title = "Smart Event Portal"
admin.site.index_title = "Smart Event Management"