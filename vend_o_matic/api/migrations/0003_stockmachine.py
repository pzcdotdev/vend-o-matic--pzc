from django.db import migrations

def stock_drink_machine(apps, schema_editor):

    drinks = [
        {
            "type": "Butterbeer"
        },
    ]

    Inventory = apps.get_model('api', 'Inventory')
    for drink in drinks:
        d = Inventory(type=drinks["type"])
        d.save()

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_inventorymodel'),
    ]

    operations = [
        migrations.RunPython(stock_drink_machine),
    ]