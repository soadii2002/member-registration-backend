from rest_framework import serializers
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    cv_url = serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = ['id', 'name', 'phone_number', 'college', 'email', 'major', 'cv', 'cv_url', 'created_at']
        read_only_fields = ['id', 'created_at']

    def get_cv_url(self, obj):
        request = self.context.get('request')
        if obj.cv and request:
            return request.build_absolute_uri(obj.cv.url)
        return None