from rest_framework import serializers

from program.models import Proposal, ProposalCategory


class ProposalSerializer(serializers.ModelSerializer):
    accepted = serializers.BooleanField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Proposal
        fields = [
            "id",
            "user",
            "title",
            "brief",
            "desc",
            "comment",
            "difficulty",
            "duration",
            "language",
            "category",
            "accepted",
            "introduction",
            "video_url",
            "slide_url",
            "room_num",
            "created_at",
            "updated_at",
        ]


class ProposalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = [
            "id",
            "title",
            "brief",
            "difficulty",
            "duration",
            "language",
            "category",
        ]


class ProposalCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProposalCategory
        fields = [
            "name",
        ]
