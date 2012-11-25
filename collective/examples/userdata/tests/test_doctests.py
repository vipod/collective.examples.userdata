import doctest
from unittest import TestSuite

from Testing.ZopeTestCase import FunctionalDocFileSuite
from Products.PloneTestCase.PloneTestCase import setupPloneSite, installPackage

from plone.app.users.tests import TestCase

installPackage('collective.examples.userdata')
setupPloneSite(products=['collective.examples.userdata'])

OPTIONFLAGS = (doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)

def test_suite():
    tests = ['registration_forms.txt',
             'userdata.txt',
             ]
    suite = TestSuite()
    for test in tests:
        suite.addTest(FunctionalDocFileSuite(test,
            optionflags=OPTIONFLAGS,
            package="collective.examples.userdata.tests",
            test_class=TestCase))
    return suite
