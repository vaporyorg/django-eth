from django.core.exceptions import ValidationError
from django.test import TestCase

from ..validators import validate_checksumed_address
from .factories import get_eth_address_with_key


class TestValidators(TestCase):
    def test_checksum_address_validator(self):
        eth_address, eth_key = get_eth_address_with_key()

        self.assertIsNone(validate_checksumed_address(eth_address))

        self.assertRaises(ValidationError, validate_checksumed_address, eth_address.lower())