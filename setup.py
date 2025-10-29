from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="iotpatch",
    version="0.2.0",
    author="Soumyapriya Goswami",
    author_email="soumyapriya.goswami.it2023@kgec.ac.in",
    description="IoT Security Hardening Toolkit for Edge Devices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/soumyapriyagoswami/iotpatch.git",
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    install_requires=[
        "pycryptodome>=3.19.0",
        "paho-mqtt>=1.6.1",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Security",
        "Topic :: System :: Networking",
        
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
