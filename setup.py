from setuptools import setup

ENTRY_POINTS = {
    'console_scripts': [
        'boilerplatepy = boilerplatepy.main:main'
    ]
}

setup(
    name="boilerplatepy",
    install_requires=["Jinja2", "requests", "platter"],
    packages=["boilerplatepy"],
    entry_points=ENTRY_POINTS,
)
