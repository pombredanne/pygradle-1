import os
import unittest
import sys

from src.pygradle import gradlew


try:
    THIS_FILE_NAME = __file__
except NameError:
    THIS_FILE_NAME = sys.argv[0]

TEST_APP_DIR = os.path.abspath(os.path.join(os.path.dirname(THIS_FILE_NAME),
                                            './testapp/'))
GRADLE_PATH = os.path.join(TEST_APP_DIR, 'gradlew')


class TestInteg(unittest.TestCase):

    def setUp(self):
        self.save_path = os.getcwd()
        os.chdir(TEST_APP_DIR)

    def tearDown(self):
        os.chdir(self.save_path)

    def test_should_gradle_clean_ends_with_success_status(self):
        gradle = gradlew.GradleFactory.create(gradle_cmd=GRADLE_PATH)
        self.assertIn('BUILD SUCCESSFUL', gradle.clean())
