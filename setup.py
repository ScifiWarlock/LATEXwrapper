from setuptools import setup, find_packages

setup(
    name='texconv',
    version='0.0.4',
    packages=find_packages(),
    install_requires=[  # External dependencies only
        # Add actual external dependencies here, if any
    ],
    author='Omkar Tasgaonkar',
    author_email='rakmot19@gmail.com',
    description='Converting Python scripts to LaTeX',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)