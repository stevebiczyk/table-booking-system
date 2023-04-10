from django.contrib import admin
from .models import Customer, Reservation, Staff, Table


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('customer', 'table', 'date', 'time')
    list_filter = ('date', 'time', 'customer', 'table')
    search_fields = ['customer__first_name', 'customer__last_name', 'email']


admin.site.register((Customer, Staff, Table))
admin.site.register(Reservation, ReservationAdmin)
