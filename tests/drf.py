from rest_framework import routers, serializers, viewsets
from ordered_model.serializers import OrderedModelSerializer
from tests.models import CustomItem, CustomOrderFieldModel


class ItemSerializer(OrderedModelSerializer):
    class Meta:
        model = CustomItem
        fields = "__all__"


class ItemViewSet(viewsets.ModelViewSet):
    queryset = CustomItem.objects.all()
    serializer_class = ItemSerializer


class CustomOrderFieldModelSerializer(OrderedModelSerializer):
    class Meta:
        model = CustomOrderFieldModel
        fields = "__all__"


class CustomOrderFieldModelViewSet(viewsets.ModelViewSet):
    queryset = CustomOrderFieldModel.objects.all()
    serializer_class = CustomOrderFieldModelSerializer


class RenamedItemSerializer(OrderedModelSerializer):
    renamedOrder = serializers.IntegerField(source="order")

    class Meta:
        model = CustomItem
        fields = ("pkid", "name", "renamedOrder")


class RenamedItemViewSet(viewsets.ModelViewSet):
    queryset = CustomItem.objects.all()
    serializer_class = RenamedItemSerializer


# bulk item test
class BulkOrderedModelSerializer(serializers.ModelSerializer):
    orderedmodels = ItemSerializer(many=True)
    class Meta:
        fields = ['orderedmodels']

    def create(self, validated_data):
        create_models = []
        #for data in validated_data:
        #       create_models.append(OrderedModelSerializer(**data))

        return BulkItem.objects.bulk_create(create_models)


router = routers.DefaultRouter()
router.register(r"items", ItemViewSet)
router.register(r"customorderfieldmodels", CustomOrderFieldModelViewSet)
router.register(r"renameditems", RenamedItemViewSet, basename="renameditem")
router.register(r"bulkitems", BulkOrderedModelSerializer)
