from rest_framework import serializers


class ItemSerializer(serializers.Serializer):

    name = serializers.SerializerMethodField()
    item_type = serializers.SerializerMethodField()
    view_count = serializers.SerializerMethodField()
    banner = serializers.SerializerMethodField()

    @staticmethod
    def get_name(instance):
        return instance.title

    @staticmethod
    def get_item_type(instance):
        return instance.content_type.name

    @staticmethod
    def get_view_count(instance) -> int:
        return instance.get_view().count()

    @staticmethod
    def get_banner(instance) -> str:
        return instance.banner

