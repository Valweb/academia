# Generated by Django 3.0.3 on 2020-03-14 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagamento', '0008_auto_20200314_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagamento',
            name='data_baixa',
            field=models.DateField(blank=True, null=True),
        ),
    ]
