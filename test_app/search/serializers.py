from rest_framework import serializers

from .models import freelancer
from .models import skill


class skillSerializer(serializers.ModelSerializer):
    class Meta:
        model=skill
        fields=('skill_name')

class freelancerSerializer(serializers.ModelSerializer):
    skills=serializers.StringRelatedField(many=True)

    class Meta:
        model = freelancer
        fields=('id','first_name','last_name','age','skills')