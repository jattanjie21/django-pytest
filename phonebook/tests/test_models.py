import pytest
from phonebook.models import Contact

def test_create_contact(db):
    contact = Contact.objects.create(name='John Doe', phone=1234567890,
    email='doe@gmail.com', address='123 Main St')

    assert contact.name    == 'John Doe'
    assert contact.phone   == 1234567890
    assert contact.email   == 'doe@gmail.com'
    assert contact.address == '123 Main St'

def test_string_representation():
    contact = Contact(name='John Doe', phone=1234567890,
    email='doe@gmail.com', address='123 Main St')

    assert str(contact) == 'John Doe - 1234567890'


def check_for_duplicate_phone_number(db):
    contact = Contact.objects.create(name='Michael Doe', phone=1234567890,
    email='michael@gmail.com', address='123 Main St')

    assert Contact.objects.filter(phone=1234567890).exists()