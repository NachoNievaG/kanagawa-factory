from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='kanagawa-factory',
    packages=['factory'],
    version='1.0.0',
    license='MIT',
    author='Ignacio Nieva',
    author_email='jose.ign.nieva@gmail.com',
    url='https://github.com/NachoNievaG/kanagawa-factory',
    description='convert any image to the kanagawa pallete!',
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={'console_scripts': ['kanagawa-factory= factory.__main__:main']},
    include_package_data=True,
    install_requires=['image-go-nord', 'rich'],
    keywords=['kanagawa', 'cli', 'kanagawa-factory', 'wallpaper', 'image', 'image-go-nord', 'palette', 'factory', 'nord'],
)
