# setup.py
from distutils.core import setup

'''
pip install .
pip install git+https://github.com/LSJohnsen/ACIT4420-study-reminders.git
'''

setup(name='studyreminders',
      version='1.0.1',
      author='Lars Johnsen',
      author_email='s359056@oslomet.no',
      url='https://github.com/LSJohnsen/ACIT4420-study-reminders',
      packages=['study_reminders', 'study_reminders.utils'],
      description='Automated study reminder package',
      entry_points={'console_scripts': ['study-reminders = study_reminders.main:main']})