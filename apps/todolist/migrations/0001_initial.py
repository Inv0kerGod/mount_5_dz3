# Generated by Django 5.0.7 on 2024-08-01 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TodoList",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Заголовок")),
                ("description", models.TextField(verbose_name="Описание")),
                (
                    "completed",
                    models.BooleanField(
                        default=False, verbose_name="Стаутс выполнения"
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Добавление задачи",
            },
        ),
    ]