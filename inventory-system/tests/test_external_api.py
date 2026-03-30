from unittest.mock import patch
from external_api import fetch_product_by_barcode

def test_fetch_valid_product():
    with patch("external_api.requests.get") as mock_get:
        mock_get.return_value.json.return_value = {
            "status": 1,
            "product": {"product_name": "Almond Milk", "brands": "Silk"}
        }

        result = fetch_product_by_barcode("123")
        assert result["product_name"] == "Almond Milk"

def test_fetch_invalid_product():
    with patch("external_api.requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"status": 0}

        result = fetch_product_by_barcode("000")
        assert result is None