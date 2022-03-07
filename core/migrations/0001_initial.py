# Generated by Django 3.2.12 on 2022-03-03 16:37

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('created', 'created'), ('opened', 'opened'), ('packing', 'packing'), ('ready to ship', 'ready to ship'), ('shipped', 'shipped'), ('delivered', 'delivered')], default=('created', 'created'), max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('sku', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('image_url', models.CharField(max_length=600)),
                ('product_type', models.CharField(choices=[('Apparels', 'Apparels'), ('Awards & Recognition', 'Awards & Recognition'), ('Bags & Luggage', 'Bags & Luggage'), ('Electronics', 'Electronics'), ('Combo', 'Combo'), ('Office & Stationary', 'Office & Stationary'), ('Premium Gifts', 'Premium Gifts'), ('Promotional Gifts', 'Promotional Gifts'), ('Leather & Leatherites', 'Leather & Leatherites'), ('Homeware', 'Homeware'), ('Drinkware', 'Drinkware'), ('Festivals', 'Festivals'), ('Covid-19', 'Covid-19'), ('Eco Friendly', 'Eco Friendly')], max_length=50)),
                ('name', models.CharField(max_length=200)),
                ('options', jsonfield.fields.JSONField(default=dict)),
                ('highlights', models.TextField(max_length=800)),
                ('specifications', jsonfield.fields.JSONField(default=dict)),
                ('offers', models.TextField(max_length=200)),
                ('gender', models.CharField(max_length=2)),
                ('category', models.CharField(choices=[('Aroma Candles', 'Aroma Candles'), ('Folders', 'Folders'), ('Hot & Cold Flasks', 'Hot & Cold Flasks'), ('Inspirational', 'Inspirational'), ('Plants', 'Plants'), ('Recogonition', 'Recogonition'), ('Pouches', 'Pouches'), ('T-Shirt', 'T-Shirt'), ('Sippers', 'Sippers'), ('Crossbody & Messenger Bags', 'Crossbody & Messenger Bags'), ('Gift Packaging', 'Gift Packaging'), ('Hand Bagags', 'Hand Bagags'), ('Fitness Bands', 'Fitness Bands'), ('Office & Desktops', 'Office & Desktops'), ('Diary & Note Pads', 'Diary & Note Pads'), ('Home Decor', 'Home Decor'), ('Backpack', 'Backpack'), ('Jacket', 'Jacket'), ('Button Buddies', 'Button Buddies'), ('Home Accessories', 'Home Accessories'), ('Festive Gift Combo', 'Festive Gift Combo'), ('Premium Metal', 'Premium Metal'), ('Water Bottles', 'Water Bottles'), ('Bags', 'Bags'), ('Strolley', 'Strolley'), ('Sweets and Dry Fruits', 'Sweets and Dry Fruits'), ('Pens', 'Pens'), ('Tote', 'Tote'), ('Trophy-Fiber', 'Trophy-Fiber'), ('Lanyards', 'Lanyards'), ('Sanitizer', 'Sanitizer'), ('Bluetooth Speakers', 'Bluetooth Speakers'), ('Plaques', 'Plaques'), ('Overnighters', 'Overnighters'), ('PPE-Kit', 'PPE-Kit'), ('Gym Set', 'Gym Set'), ('Generals', 'Generals'), ('Duffles', 'Duffles'), ('Short', 'Short'), ('Mask', 'Mask'), ('Rollers', 'Rollers '), ('Dairy & Organizer', 'Dairy & Organizer'), ('Appliances', 'Appliances'), ('Kurtha', 'Kurtha'), ('Trouser', 'Trouser'), ('Food Hampers', 'Food Hampers'), ('Formal Shirt', 'Formal Shirt'), ('Chocolates', 'Chocolates'), ('Flowers & Plants', 'Flowers & Plants'), ('Mugs', 'Mugs'), ('Sleeves and Slipcases', 'Sleeves and Slipcases'), ('Covid Kit', 'Covid Kit'), ('Security Uniforms', 'Security Uniforms'), ('Handwash', 'Handwash'), ('Wallets', 'Wallets'), ('Cap', 'Cap'), ('Medal', 'Medal'), ('Personal Gifts - Key chains', 'Personal Gifts- Key chains'), ('Frames', 'Frames'), ('Home Utilities', 'Home Utilities'), ('Cardholders', 'Cardholders'), ('Timekeepers', 'Timekeepers'), ('Others', 'Others'), ('Gift Bags', 'Gift Bags'), ('Cookies and Cakes', 'Cookies and Cakes'), ('Gift Sets', 'Gift Sets'), ('Tech Accessories', 'Tech Accessories'), ('Headphones', 'Headphones'), ('Sports Trophy', 'Sports Trophy'), ('Accessories', 'Accessories'), ('Gadgets', 'Gadgets'), ('Wellness Gifts', 'Wellness Gifts'), ('Laptop Bags', 'Laptop Bags'), ('Earphones', 'Earphones'), ('Desktop', 'Desktop'), ('Salvers', 'Salvers'), ('Powerbanks', 'Powerbanks'), ('Travel Accessories', 'Travel Accessories'), ('Lapel Pins', 'Lapel Pins')], max_length=50)),
                ('subcategory', models.CharField(choices=[('Wind Cheater', 'Wind Cheater'), ('NA', 'NA'), ('Bomber Jacket', 'Bomber Jacket'), ('Customized T-Shirts', 'Customized T-Shirts'), ('Polo With Tipping', 'Polo With Tipping'), ('Track Pant', 'Track Pant'), ('Dry Fit', 'Dry Fit'), ('Formal Pant', 'Formal Pant'), ('Round Neck', 'Round Neck'), ('Polo', 'Polo'), ('Jean', 'Jean')], max_length=50)),
                ('related', jsonfield.fields.JSONField(null=True)),
                ('brand', models.ForeignKey(default='NA', on_delete=django.db.models.deletion.SET_DEFAULT, to='core.brand')),
            ],
        ),
        migrations.CreateModel(
            name='OrderCatalogue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=50)),
                ('option', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.order')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=20)),
                ('pin', models.IntegerField()),
                ('address_line_1', models.TextField(max_length=100)),
                ('address_line_2', models.TextField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('email_id', models.EmailField(max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('organization', models.CharField(max_length=60, null=True)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.order')),
            ],
        ),
    ]
