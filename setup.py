from setuptools import setup

setup(name='life-map',
      version='1.0',
      description='blog for pengfei xue',
      author='Pengfei Xue',
      author_email='pengphy@gmail.com',
      url='https://facebook.com/pengfei.xue',
      install_requires=['flask==0.9', 
        'mongoengine==0.7.6',
        'flask-mongoengine==0.6',
        'Flask-Script==0.5.1',
        'Flask-WTF==0.8',
        'WTForms==1.0.2',
        'pymongo==2.3',
        'Jinja2==2.6',
        'WTForms==1.0.2',
        'Werkzeug==0.8.3',
        'argparse==1.2.1',
        'feedparser==5.1.3',
      ],
     )
