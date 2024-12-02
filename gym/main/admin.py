from django.contrib import admin
from .models import Upragneniya, Trenirovka, Groups, TrenirovkaGroup

@admin.register(Upragneniya)
class UpragneniyaAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'group_muscular',)
    list_editable = ('group', 'group_muscular',)
    list_filter = ('group', 'group_muscular',)


@admin.register(Trenirovka)
class TrenirovkaAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'max_weight', 'amount1', 'amount2', 'status', 'level',)
    list_editable = ('level', 'max_weight', 'amount1', 'amount2',)
    list_filter = ('date', 'name',)

@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(TrenirovkaGroup)
class TrenirovkaGroupAdmin(admin.ModelAdmin):
    list_display = ('date', 'group',)