from setuptools import setup

setup(
    name='calculateapp',
    version='0.1',
    author='Oguzhan Mavi',
    author_email='oguzhanmavii98@gmail.com',
    description='bu paket test etmek icin kurulmus bir hesap makinesidird',
    url="https://github.com/oguzhanmavii/my-package-calculate",
    py_modules=['calculate'],
    install_requires=[
        'Click',
    ],
    entry_points='''
    [console_scripts]
    calculate=calculate:Mainloop
    ''',
    packages=['calculate'],
)