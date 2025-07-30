from setuptools import find_packages, setup

setup(
    name="quickstart_etl",
    packages=find_packages(exclude=["quickstart_etl_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "boto3",
        "pandas",
        "matplotlib",
        # "dagster-gcp"
        # "google-cloud-bigquery",
        # "pyarrow"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
