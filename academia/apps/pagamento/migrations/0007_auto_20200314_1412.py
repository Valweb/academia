# Generated by Django 3.0.3 on 2020-03-14 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagamento', '0006_auto_20200314_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagamento',
            name='data_baixa',
            field=models.DateField(blank=True),
        ),
    ]
