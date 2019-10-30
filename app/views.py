from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi

from . import appbuilder, db

from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface

from app.models import *
"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

class PaymentModelView(ModelView):
    datamodel = SQLAInterface(Payment)

    # label_columns = {'contact_group':'Contacts Group'}
    list_columns = ['vehicle_reg','driver','payment_date']

    show_fieldsets = [
        (
            'Summary',
            {'fields': ['vehicle_reg', 'driver', 'payment_date']}
        ),
        (
            'Payment Details',
            {'fields': ['name_on_card','card_type', 'card_number', 'expiry_date'], 'expanded': False}
        ),
    ]

appbuilder.add_view(
    PaymentModelView,
    "List Payments",
    icon = "fa-folder-open-o",
    category = "Payments",
    category_icon = "fa-envelope"
)

"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()
