from django.contrib import admin
import web.models

# Register your models here.
admin.site.register(web.models.Event)
admin.site.register(web.models.VenueType)
admin.site.register(web.models.EventType)
admin.site.register(web.models.EventCost)
admin.site.register(web.models.CostType)