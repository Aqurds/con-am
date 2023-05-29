from django.db import models


class User(models.Model):
    class Meta:
        verbose_name_plural = "Users"

    name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    language = models.CharField(max_length=100, null=True, blank=True)
    display_picture = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Prayer(models.Model):
    class Meta:
        verbose_name_plural = "Prayers"

    name = models.CharField(max_length=200)
    user_id = models.ForeignKey(
        "User", related_name="users", on_delete=models.CASCADE, null=True, blank=True
    )
    region = models.ForeignKey(
        "Region",
        related_name="Regions",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    prayer_type = models.CharField(max_length=200)
    prayer_resource = models.ForeignKey(
        "PrayerResource",
        related_name="PrayerResources",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    time = models.CharField(max_length=50, null=True, blank=True)
    is_weekly = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateField(null=True, blank=True)
    prayer_notification = models.ForeignKey(
        "PrayerNotification",
        related_name="PrayerNotification",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    social_prayers = models.ForeignKey(
        "SocialPrayer",
        related_name="SocialPrayer",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    image = models.CharField(max_length=200, null=True, blank=True)
    updates = models.CharField(max_length=50, null=True, blank=True)
    rpts = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class PrayerResource(models.Model):
    class Meta:
        verbose_name_plural = "PrayerResources                                  "

    name = models.CharField(max_length=200)
    story = models.ForeignKey(
        "Story", related_name="Stories", on_delete=models.CASCADE, null=True, blank=True
    )
    region = models.ForeignKey(
        "Region", related_name="Region", on_delete=models.CASCADE, null=True, blank=True
    )
    resource_video = models.CharField(max_length=250, null=True, blank=True)


class Story(models.Model):
    class Meta:
        verbose_name_plural = "Stories"

    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
        "Category",
        related_name="Categories",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    region = models.ForeignKey(
        "Region",
        related_name="StoryRegion",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    resource_video = models.CharField(max_length=250, null=True, blank=True)


class SocialPrayer(models.Model):
    class Meta:
        verbose_name_plural = "SocialPrayers"

    link = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    social_media_name = models.CharField(max_length=50, null=True, blank=True)


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class ResourceImage(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    prayer_resource = models.ForeignKey(
        "PrayerResource",
        related_name="PrayerResourceImage",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )


class RegionImage(models.Model):
    class Meta:
        verbose_name_plural = "RegionImages"

    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)


class StoryImage(models.Model):
    class Meta:
        verbose_name_plural = "StoryImages"

    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)


class RegionVideo(models.Model):
    class Meta:
        verbose_name_plural = "RegionImages"

    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)


class Region(models.Model):
    class Meta:
        verbose_name_plural = "Regions"

    name = models.CharField(max_length=200)
    region_image = models.ForeignKey(
        "RegionImage",
        related_name="RegionImage",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    region_video = models.ForeignKey(
        "RegionVideo",
        related_name="RegionVideo",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    region_stats = models.IntegerField()


class PrayerNotification(models.Model):
    class Meta:
        verbose_name_plural = "PrayerNotifications"

    time = models.CharField(max_length=200)
    day = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
