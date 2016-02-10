from distutils.core import setup

requires = ['pymp4parse', 'protobuf']

setup(
    name='pywvpssh',
    version='0.1.0',
    packages=[''],
    url='https://github.com/use-sparingly/wvpssh',
    license='The MIT License',
    author='Alastair Mccormack',
    author_email='alastair at alu.media',
    description='Widevine Modular PSSH Decoder',
    requires=requires,
    install_requires=requires,

    entry_points={
        'console_scripts': [
            'pywvpsshdump = pywvpssh:main'
        ]
    }
)
