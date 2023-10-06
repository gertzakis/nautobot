# Generated by Django 3.2.21 on 2023-10-06 15:30

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.serializers.json
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import nautobot.core.models.fields
import nautobot.users.models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128)),
                ("last_login", models.DateTimeField(blank=True, null=True)),
                ("is_superuser", models.BooleanField(default=False)),
                (
                    "username",
                    models.CharField(
                        error_messages={"unique": "A user with that username already exists."},
                        max_length=150,
                        unique=True,
                        validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                    ),
                ),
                ("first_name", models.CharField(blank=True, max_length=150)),
                ("last_name", models.CharField(blank=True, max_length=150)),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                ("date_joined", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                (
                    "config_data",
                    models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True, related_name="user_set", related_query_name="user", to="auth.Group"
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True, related_name="user_set", related_query_name="user", to="auth.Permission"
                    ),
                ),
            ],
            options={
                "db_table": "auth_user",
                "ordering": ["username"],
            },
            managers=[
                ("objects", nautobot.users.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="AdminGroup",
            fields=[],
            options={
                "verbose_name": "Group",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("auth.group",),
            managers=[
                ("objects", django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name="Token",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("expires", models.DateTimeField(blank=True, null=True)),
                (
                    "key",
                    models.CharField(
                        max_length=40, unique=True, validators=[django.core.validators.MinLengthValidator(40)]
                    ),
                ),
                ("write_enabled", models.BooleanField(default=True)),
                ("description", models.CharField(blank=True, max_length=200)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="tokens", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "ordering": ["created"],
            },
        ),
        migrations.CreateModel(
            name="ObjectPermission",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
                ("description", models.CharField(blank=True, max_length=200)),
                ("enabled", models.BooleanField(default=True)),
                ("actions", nautobot.core.models.fields.JSONArrayField(base_field=models.CharField(max_length=30))),
                (
                    "constraints",
                    models.JSONField(blank=True, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True),
                ),
                ("groups", models.ManyToManyField(blank=True, related_name="object_permissions", to="auth.Group")),
                (
                    "object_types",
                    models.ManyToManyField(
                        limit_choices_to=models.Q(
                            models.Q(
                                models.Q(
                                    ("app_label__in", ["admin", "auth", "contenttypes", "sessions", "taggit", "users"]),
                                    _negated=True,
                                ),
                                models.Q(("app_label", "auth"), ("model__in", ["group", "user"])),
                                models.Q(("app_label", "users"), ("model__in", ["objectpermission", "token"])),
                                _connector="OR",
                            )
                        ),
                        related_name="object_permissions",
                        to="contenttypes.ContentType",
                    ),
                ),
                (
                    "users",
                    models.ManyToManyField(blank=True, related_name="object_permissions", to=settings.AUTH_USER_MODEL),
                ),
            ],
            options={
                "verbose_name": "permission",
                "ordering": ["name"],
            },
        ),
    ]
