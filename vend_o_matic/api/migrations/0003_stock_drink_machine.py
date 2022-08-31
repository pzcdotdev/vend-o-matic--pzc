from django.db import migrations

def stock_drink_machine(apps, schema_editor):

    drinks = [
        {
            "type": "Butterbeer",
            "quantity": 5
        },
        {
            "type": "Ent Draught",
            "quantity": 5
        },
        {
            "type": "Ambrosia",
            "quantity": 5
        },
    ]

    InventoryModel = apps.get_model('api', 'InventoryModel')
    for drink in drinks:
        d = InventoryModel(type=drink["type"], quantity=drink["quantity"])
        d.save()

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_inventorymodel'),
    ]

    operations = [
        migrations.RunPython(stock_drink_machine),
    ]