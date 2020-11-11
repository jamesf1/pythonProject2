import pytest
from Invoice import Invoice

@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price':3.75, 'discount': 5},
                'Notebook':{'qnt':5,'unit_price':7.5, 'discount':10}}
    return products

@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice

def testAddProduct():
    invoice = Invoice()
    product = invoice.addProduct(1, 2, 3)
    print(product)
    assert product.get('qnt') == 1
    
def testAddProductUnitPrice():
    invoice = Invoice()
    product = invoice.addProduct(1,2,3)
    assert product.get('unit_price') == 2

def testAddProductDiscount():
    invoice = Invoice()
    product = invoice.addProduct(1,2,3)
    assert product.get('discount') == 3

def test_CanCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62

def test_CanCalculateTotalImpurePrice(products):
    invoice = Invoice()
    assert invoice.totalImpurePrice(products)==75

def test_CanCalculateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38
