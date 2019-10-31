from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from datetime import date

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""

class Payment(Model):
    id = Column(Integer, primary_key=True)
    vehicle_reg = Column(String(10), nullable=False)
    driver = Column(String(50))
    name_on_card = Column(String(60),nullable=False)
    card_type = Column(String(20), nullable=False)
    card_number = Column(String(20), nullable=False)
    expiry_date = Column(String(5), nullable=False)
    payment_date = Column(Date, nullable=False, default=date.today())

    def __repr__(self):
        return self.vehicle_reg
