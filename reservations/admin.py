from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Reservation, Staff, Table


class ReservationInline(admin.StackedInline):
    model = Reservation
    extra = 1


class UserAdmin(BaseUserAdmin):
    inlines = [ReservationInline]


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'table', 'date', 'time')
    list_filter = ('date', 'time', 'user', 'table')
    search_fields = ['user__first_name', 'user__last_name', 'user__email']


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register((Staff, Table))
admin.site.register(Reservation, ReservationAdmin)
