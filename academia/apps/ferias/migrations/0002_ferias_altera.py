# Generated by Django 3.0.3 on 2020-03-01 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pagamento', '0002_auto_20200301_1353'),
        ('ferias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ferias',
            name='altera',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='pagamento.Pagamento'),
            preserve_default=False,
        ),
    ]
