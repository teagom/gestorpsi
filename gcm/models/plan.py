# -*- coding: utf-8 -*-

"""
Copyright (C) 2008 GestorPsi
"""

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Plan(models.Model):
    name = models.CharField(_('Nome do Plano'), help_text=_('Ex: de 1 a 9 profissionais'), max_length=255)
    value = models.DecimalField(_('Valor em R$'), max_digits=8, decimal_places=2, help_text=_('Utilizar pontos, nao virgulas'))
    duration = models.CharField(_('Duracao'), max_length=4, help_text=_('Duracao em MESES do plano. Preencher 1 para plano mensal, 3 para trimestral etc'))
    weight = models.IntegerField(_('Peso'), max_length=4, null=True, blank=True, help_text=_('Peso para ordenacao visual no formulario de cadastro. Utilizar valores inteiros aqui'))
    active = models.BooleanField(default=True)
    
    class Meta:
        app_label = 'gcm'
        ordering = ['weight',]
    
    def __unicode__(self):
        duration = self.duration

        if self.duration == '1':
            duration = _('Mensal')
        if self.duration == '3':
            duration = _('Trimestral')
        if self.duration == '6':
            duration = _('Semestral')
        if self.duration == '12':
            duration = _('Anual')
        if self.duration == '24':
            duration = _('Bianual')

        return u'%s - R$ %s/%s' % (self.name, self.value, duration)
