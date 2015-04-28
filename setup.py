from setuptools import setup

setup(
    name="fromto-printer",
    version="0.1.0",
    author="Rory McCann",
    author_email="rory@technomancy.org",
    py_modules=['fromto'],
    platforms=['any',],
    requires=[],
    entry_points={
        'console_scripts': [
            'fromto = fromto:main',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
    ],
)
