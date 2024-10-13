from setuptools import setup, find_packages

setup(
    name='processamento_imagem',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow',  # Dependência para o processamento de imagens
    ],
    entry_points={
        'console_scripts': [
            'processamento-imagem=processamento.main:main',  # Ponto de entrada para o script principal
        ],
    },
    author='Diego',
    author_email='enrico230821@gmail.com',
    description='Um pacote de processamento de imagens.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Dih08/processamento_de_imagem',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
