from decimal import *

from rest_framework import serializers

from .models import Ingrediente
from unidades_medida.serializers import UnidadeMedidaSerializer

class CreateIngredienteSerializer(serializers.ModelSerializer):
    unidades_medida = UnidadeMedidaSerializer
    class Meta:
        model = Ingrediente
        fields = [
            'id_ingrediente',
            'nome_ingrediente',
            'quantidade_calorica_ingrediente',
            'aproveitamento_ingrediente',
            #'quantidade_estoque_ingrediente',
            #'quantidade_reservada_ingrediente',
            #'valor_ingrediente',
            #'motivo_retirada_estoque',
            'id_unidade_medida'
        ]


class ListIngredienteSerializer(serializers.ModelSerializer):
    unidades_medida = UnidadeMedidaSerializer
    class Meta:
        model = Ingrediente
        fields = [
            'id_ingrediente',
            'nome_ingrediente',
            'quantidade_calorica_ingrediente',
            'aproveitamento_ingrediente',
            'quantidade_estoque_ingrediente',
            'quantidade_reservada_ingrediente',
            'valor_ingrediente',
            'motivo_retirada_estoque',
            'id_unidade_medida'
        ]

class EditIngredienteSerializer(serializers.ModelSerializer):
    unidades_medida = UnidadeMedidaSerializer
    class Meta:
        model = Ingrediente
        fields = [
            'id_ingrediente',
            'nome_ingrediente',
            'quantidade_calorica_ingrediente',
            'aproveitamento_ingrediente',
            'quantidade_estoque_ingrediente',
            'quantidade_reservada_ingrediente',
            'valor_ingrediente',
            'motivo_retirada_estoque',
            'id_unidade_medida'
        ]

   