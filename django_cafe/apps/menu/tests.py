from django.test import TestCase as DjangoTest
import unittest
from menu.models import Tea
from menu.forms import TeaSearchForm

class TeaMenagerTest(DjangoTest):
    def setUp(self):
        Tea.objects.bulk_create([
            Tea(name="ダージリン", kind="english"),
            Tea(name="烏龍茶", kind="chinese"),
            Tea(name="普洱茶", kind="chinese"),
        ])

    def test_count_each_kind(self):
        result = Tea.objects.counr_each_kind()
        self.assertEqual(result, dict(english=1, chinese=2))


class TeaSearchFromTest(unittest.TestCase):
    def test_valid(self):
        """正常な入力をしたときにエラーにならないことを検証する"""
        params = dict(name="foo", kind=["english"])
        form = TeaSearchForm(params)
        self.assertEqual(form.is_valid(), True, form.errors.as_text())

    def test_either1(self):
        """名称と種類のどちらも入力しないとエラーになることを検証する"""
        params = dict()
        form = TeaSearchForm(params)
        self.assertEqual(form.is_valid(), False, form.errors.as_text())

    def test_either2(self):
        """名称を入力すればエラーにならないことを検証する"""
        params = dict(name="foo")
        form = TeaSearchForm(params)
        self.assertEqual(form.is_valid(), True, form.errors.as_text())

    def test_either3(self):
        """種類を入力すればエラーにならないことを検証する"""
        params = dict(kind=["english", "chinese"])
        form = TeaSearchForm(params)
        self.assertEqual(form.is_valid(), True, form.errors.as_text())

