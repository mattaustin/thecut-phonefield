# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from ..widgets import PhoneInput
from django.test import TestCase


class TestPhoneInput(TestCase):

    """Tests for the PhoneInput widget."""

    def setUp(self):
        self.widget = PhoneInput()

    def test_custom_autocomplete_type(self):
        """Change autocomplete type of base TextInput."""
        self.assertIn('autocomplete', self.widget.attrs.keys())
        self.assertEqual('tel', self.widget.attrs['autocomplete'])

    def test_custom_input_type(self):
        """Change input type of base TextInput."""
        self.assertEqual('tel', self.widget.input_type)
