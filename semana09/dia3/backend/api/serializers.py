from rest_framework import serializers

from .models import Categoria,Producto,Pedido,PedidoDetalle

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['precio']

    def to_representation(self,instance):
        representation = super().to_representation(instance)
        representation['imagen'] = instance.imagen.url
        return representation

class PedidoDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoDetalle
        fields = ['producto','cantidad']

class PedidoSerializer(serializers.ModelSerializer):
    pedidodetalle = PedidoDetalleSerializer(many=True)
    class Meta:
        model = Pedido
        fields = ['usuario','fecha','estado','pedidodetalle']

        def create(self,validated_data):
            pedidos_data = validated_data.pop('pedidodetalle')
            pedido = Pedido.Objects.create(**validated_data)
            for pedido_data in pedidos_data:
                PedidoDetalle.objects.create(pedido_id=pedido,**pedido_data)
            return pedido
    




    

