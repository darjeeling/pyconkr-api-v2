from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    visible = models.BooleanField(default=True)
    year = models.IntegerField(default=2023)

    class Meta:
        verbose_name = "세션 카테고리"
        verbose_name_plural = "세션 카테고리들"

    def __str__(self):
        return self.name


class Proposal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    brief = models.TextField(max_length=1000, help_text="리뷰용: 발표에 대한 간단한 설명.")
    desc = models.TextField(max_length=4000, help_text="리뷰용: 발표에 대한 자세한 설명")
    comment = models.TextField(
        max_length=4000, null=True, blank=True, help_text="리뷰용: 파준위에게 전하고 싶은 말"
    )

    difficulty = models.CharField(
        max_length=15,
        choices=(
            ("BEGINNER", "Beginner"),
            ("INTERMEDIATE", "Intermediate"),
            ("EXPERIENCED", "Experienced"),
        ),
    )

    duration = models.CharField(
        max_length=15,
        choices=(
            ("SHORT", "25min"),
            ("LONG", "40min"),
        ),
    )

    language = models.CharField(
        max_length=15,
        choices=(
            ("", "---------"),
            ("KOREAN", "Korean"),
            ("ENGLISH", "English"),
        ),
        default="",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_DEFAULT,
        null=True,
        blank=True,
        default=14,
    )
    accepted = models.BooleanField(default=False)
    slide_url = models.CharField(
        max_length=255, null=True, blank=True, help_text="발표 자료 URL"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "발표 제안"
        verbose_name_plural = "발표 제안들"

    def __str__(self):
        return self.title


class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    host_name = models.CharField(max_length=50, null=True, blank=True)
    host_introduction = models.TextField(null=True, blank=True)
    host_profile_image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255)
    introduction = models.TextField(
        max_length=3000,
        null=True,
        blank=True,
        help_text="발표 소개 페이지에 들어가는 내용입니다.",
    )

    difficulty = models.CharField(
        max_length=15,
        choices=(
            ("BEGINNER", "Beginner"),
            ("INTERMEDIATE", "Intermediate"),
            ("EXPERIENCED", "Experienced"),
        ),
    )

    start_at = models.DateTimeField()
    finish_at = models.DateTimeField(null=True, blank=True)
    duration = models.CharField(
        max_length=15,
        choices=(
            ("SHORT", "20min"),
            ("LONG", "40min"),
        ),
    )

    language = models.CharField(
        max_length=15,
        choices=(
            ("", "---------"),
            ("KOREAN", "Korean"),
            ("ENGLISH", "English"),
        ),
        default="",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_DEFAULT,
        null=True,
        blank=True,
        default=14,
    )
    video_url = models.CharField(
        max_length=255, null=True, blank=True, help_text="발표 영상 URL"
    )
    slide_url = models.CharField(
        max_length=255, null=True, blank=True, help_text="발표 자료 URL"
    )
    room_num = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        help_text="발표장소",
        choices=(
            ("101", "101"),
            ("102", "102"),
            ("103", "103"),
            ("104", "104"),
            ("105", "105"),
        ),
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "세션"
        verbose_name_plural = "세션들"

    def __str__(self):
        return self.title
