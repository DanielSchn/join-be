from rest_framework import serializers
from join_app.models import Users, Contacts, Tasks


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'

# class MarketSerializer(serializers.ModelSerializer):

#     sellers = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='seller_editing')

# # Siehe Screenshot_3 am 16.09.24 für die ausführliche Version
#     class Meta:
#         model = Market
#         exclude = []


# class MarketHyperlinkedSerializer(MarketSerializer, serializers.HyperlinkedModelSerializer):

#     def __init__(self, *args, **kwargs):
#         fields= kwargs.pop('fields', None)
#         super().__init__(*args, **kwargs)

#         if fields is not None:
#             allowed = set(fields)
#             existing = set(self.fields)
#             for field_name in existing - allowed:
#                 self.fields.pop(field_name)
#     class Meta:
#         model = Market
#         exclude = ['net_worth']

# class SellerSerializer(serializers.ModelSerializer):
# # Siehe Screenshot_4 am 16.09.24 für die ausführliche Version
#     markets = MarketSerializer(many=True, read_only=True)
#     market_ids = serializers.PrimaryKeyRelatedField(
#         queryset=Market.objects.all(),
#         many=True,
#         write_only=True,
#         source='markets'
#     )

#     market_count = serializers.SerializerMethodField()

#     class Meta:
#         model = Seller
#         fields = ["id", "name", "market_ids", "market_count", "markets", "contact_info"]

#     def get_market_count(self, obj):
#         return obj.markets.count()
    

# class SellerListSerializer(SellerSerializer, serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Seller
#         fields = ["url", "name", "market_ids", "market_count", "contact_info"]