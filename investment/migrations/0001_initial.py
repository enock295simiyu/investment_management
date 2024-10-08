# Generated by Django 5.1.1 on 2024-09-15 13:06

import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InvestmentAccount',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False,
                                                                verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False,
                                                                      verbose_name='modified')),
                ('id',
                 model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_by', models.CharField(blank=True, db_index=True, editable=False, max_length=64, null=True)),
                ('modified_by', models.CharField(blank=True, db_index=True, editable=False, max_length=64, null=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InvestmentAccountUser',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False,
                                                                verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False,
                                                                      verbose_name='modified')),
                ('id',
                 model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_by', models.CharField(blank=True, db_index=True, editable=False, max_length=64, null=True)),
                ('modified_by', models.CharField(blank=True, db_index=True, editable=False, max_length=64, null=True)),
                ('permission', models.CharField(
                    choices=[('view', 'View only'), ('full', 'Full access'), ('post', 'Post transactions only')],
                    default='view', max_length=10)),
                ('investment_account',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='investment.investmentaccount')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'investment_account')},
            },
        ),
        migrations.AddField(
            model_name='investmentaccount',
            name='users',
            field=models.ManyToManyField(related_name='investment_accounts', through='investment.InvestmentAccountUser',
                                         to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False,
                                                                verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False,
                                                                      verbose_name='modified')),
                ('id',
                 model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_by', models.CharField(blank=True, db_index=True, editable=False, max_length=64, null=True)),
                ('modified_by', models.CharField(blank=True, db_index=True, editable=False, max_length=64, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions',
                                              to='investment.investmentaccount')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
