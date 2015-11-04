import os
import sys

from pygradle import gradlew


try:
    THIS_FILE_NAME = __file__
except NameError:
    THIS_FILE_NAME = sys.argv[0]

TEST_APP_DIR = os.path.abspath(os.path.join(os.path.dirname(THIS_FILE_NAME),
                                            './testapp/'))
GRADLE_PATH = os.path.join(TEST_APP_DIR, 'gradlew')

save_path = os.getcwd()
os.chdir(TEST_APP_DIR)
gradle = gradlew.GradleFactory.create(gradle_cmd=GRADLE_PATH)
assert 'BUILD SUCCESSFUL' in gradle.clean()
os.chdir(save_path)