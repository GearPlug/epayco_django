# Generated by Django 2.2.8 on 2020-08-12 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epayco_django', '0002_transaction_id_max_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='amount',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='amount_base',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='amount_country',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='amount_ok',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='approval_code',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='bank_name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='business',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='cardnumber',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='cod_response',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='cod_transaction_state',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='currency_code',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='cust_id_cliente',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='customer_city',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='customer_country',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='customer_doctype',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='customer_document',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='customer_email',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='customer_ind_pais',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='customer_ip',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='customer_lastname',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='customer_movil',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='customer_name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='customer_phone',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='errorcode',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='franchise',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='invoice_id',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='ref_payco',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='response',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='response_reason_text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='signature',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='tax',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='transaction_date',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='transaction_id',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='transaction_state',
            field=models.TextField(),
        ),
    ]