# -*- coding: utf-8 -*-

"""
Copyright (C) 2008 GestorPsi

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""

"""
   This file contains all configurations for Admin Interface
   I{These models were created only for testing purposes}
   @author: Sergio Durand
   @version: 1.0
"""

from django.contrib import admin
from datetime import datetime

from gestorpsi.gcm.models.invoice import Invoice
from gestorpsi.gcm.models.plan import Plan
from gestorpsi.gcm.models.payment import PaymentType
from gestorpsi.gcm.forms.invoice import InvoiceForm

'''
    filter and action for Plan
'''
# ativo
def ativo(modeladmin, request, queryset):
    for obj in queryset:
        obj.active = True
        obj.save()
ativo.short_description = u"Ativar planos"

def inativo(modeladmin, request, queryset):
    for obj in queryset:
        obj.active = False
        obj.save()
inativo.short_description = u"Inativar planos"

# visivel para client
def visible_client(modeladmin, request, queryset):
    for obj in queryset:
        obj.visible_client = True
        obj.save()
visible_client.short_description = u"Tornar visivel para cliente"

def not_visible_client(modeladmin, request, queryset):
    for obj in queryset:
        obj.visible_client = False
        obj.save()
not_visible_client.short_description = u"Tornar nao visivel para cliente"


class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'value','duration','staff_size','active','visible_client')
    list_filter = ('active','visible_client')
    actions = [ativo, inativo, visible_client, not_visible_client]
admin.site.register(Plan, PlanAdmin)



'''
    filter and action invoice
'''
# pendente
def pendente(modeladmin, request, queryset):
    for obj in queryset:
        obj.date_payed = None
        obj.status = 0
        obj.save()
pendente.short_description = u"Pendente"

# pago pelo cliente - cartao
def pagoClienteCartao(modeladmin, request, queryset):
    for obj in queryset:
        obj.date_payed = datetime.today()
        obj.status = 1
        obj.bank = 1
        obj.save()
pagoClienteCartao.short_description = u"Pago pelo cliente / PagSeguro cartão crédito"

# pago pelo cliente - boleto
def pagoClienteBoleto(modeladmin, request, queryset):
    for obj in queryset:
        obj.date_payed = datetime.today()
        obj.status = 1
        obj.bank = 2
        obj.save()
pagoClienteBoleto.short_description = u"Pago pelo cliente / PagSeguro boleto"

# pago pelo cliente - boleto
def pagoClienteDeposito(modeladmin, request, queryset):
    for obj in queryset:
        obj.date_payed = datetime.today()
        obj.status = 1
        obj.bank = 3
        obj.save()
pagoClienteDeposito.short_description = u"Pago pelo cliente / depósito"


# pago pelo GestorPSI - gratis/teste/cortesia
def pagoGratis(modeladmin, request, queryset):
    for obj in queryset:
        obj.date_payed = datetime.today()
        obj.status = 2
        obj.save()
pagoGratis.short_description = u"Pago / Grátis"


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('organization','plan','start_date','end_date','expiry_date','status','date_payed','bank','situation_')
    list_filter = ('status',)
    actions = [pendente, pagoClienteCartao, pagoClienteBoleto, pagoClienteDeposito, pagoGratis]
    search_fields = ['organization__name','organization__id']
    readonly_fields = ('aud_author','aud_ip','aud_date')
    form = InvoiceForm

    class Media:
        js = ('/media/js/jquery-1.6.4.min.js','/media/js/invoiceAdd.js')


admin.site.register(Invoice, InvoiceAdmin)

class PaymentTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(PaymentType, PaymentTypeAdmin)
