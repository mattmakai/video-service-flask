
from . import db


class SupportTicket(db.Model):
    """
        Represents a single support ticket in the customer service system.
    """
    __tablename__ = 'support_tickets'
    id = db.Column(db.Integer, primary_key=True)
    endpoint = db.Column(db.String(512))
    product_url = db.Column(db.String(2048))

