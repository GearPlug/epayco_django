import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='epayco-django',
      version='0.0.1',
      include_package_data=True,
      license='MIT',
      description='A django integration for ePayco\'s gateway.',
      long_description=read('README.md'),
      url='https://github.com/gustav0/epayco_django',
      author='gustav0',
      author_email='tavito.286@gmail.com',
      packages=['epayco_django'],
      install_requires=[
          'django>=1.11',
          'pyepayco',
      ],
      classifiers=[
          'Environment :: Web Environment',
          'Framework :: Django',
          'Framework :: Django :: 2.0',
          'Framework :: Django :: 2.1',
          'Framework :: Django :: 2.2',
          'Framework :: Django :: 2.2',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
      ],
      zip_safe=False)