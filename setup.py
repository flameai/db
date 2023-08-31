from setuptools import setup

setup(
    name='common_db',
    description='My pesonal code for creating DB components such as MySQL, Postgres, ClickHouse etc',
    version='v1.0.0',
    author='Alexander Andryukov',
    author_email='andryukov@gmail.com',
    extras_require={
        'ClickHouse': [
            'clickhouse-driver==0.2.6',
        ],
        'MySQL': [
            'asyncmy==0.2.8',
        ],
        'Postgres': [
            'asyncpg==0.28.0'
        ],
    }
)
