from io import StringIO
from src import app

print("File test __name__ is set to: {}" .format(__name__))

if __name__ == "__main__":
   print("File two executed when ran directly")


def test_get_name(capsys, monkeypatch):
    name_input = StringIO("Yonis")
    monkeypatch.setattr("sys.stdin", name_input)

    actual = app.get_name()

    assert actual == "Yonis"


def test_create_greeting(capsys):
    app.create_greeting("Abz")
    out, err = capsys.readouterr()
    assert err == ""
    assert out == "                                HELLO, Abz\n"


# def creating_new_product():
#     name = get_new_product_name()
#     price = get_new_product_price()
#     new_product = create_new_product(name, price)

#     try:
#         add_product_to_cache(new_product)
#         print(("\nThe following product '{}' has been added to the products list\n").format(
#             new_product
#         ))
#     except Exception as e:
#         print(e)


def test_create_new_product_add_product_to_cache():
    mock_inventory = [{"name": "Coke Zero", "price": float(1.2)}]
    new_product = {"name": "Pepsi Max", "price": float(0.5)}

    expected = [{"name": "Coke Zero", "price": float(1.2)}, new_product]

    actual = app.add_product_to_cache(new_product, mock_inventory)

    assert expected == actual

