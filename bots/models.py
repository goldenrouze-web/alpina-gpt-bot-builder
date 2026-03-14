from django.db import models
from django.contrib.auth.models import User


class Bot(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    telegram_token = models.CharField(
        max_length=200,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class Scenario(models.Model):

    bot = models.ForeignKey(
        Bot,
        on_delete=models.CASCADE,
        related_name="scenarios"
    )

    name = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Step(models.Model):

    scenario = models.ForeignKey(
        Scenario,
        on_delete=models.CASCADE,
        related_name="steps"
    )

    order = models.IntegerField()

    prompt = models.TextField()

    next_step = models.IntegerField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Step {self.order}"
