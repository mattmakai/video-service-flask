import datetime

from . import db


class SupportTicket(db.Model):
    """
        Represents a single support ticket in the customer service system.
    """
    __tablename__ = 'support_tickets'
    id = db.Column(db.Integer, primary_key=True)
    endpoint = db.Column(db.String(512))
    product_url = db.Column(db.String(2048))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, endpoint, product_url):
        self.endpoint = endpoint
        self.product_url = product_url
