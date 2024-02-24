from setuptools import setup, find_packages
import os
import stat
import shutil

def make_executable(path):
    mode = os.stat(path).st_mode
    mode |= (mode & 0o444) >> 2    # copy R bits to X
    os.chmod(path, mode)

def setup_pasgen():
    # Copy the pasgen script
    pasgen_src = 'pasgen.py'
    pasgen_dst = '/usr/local/bin/pasgen.py'
    shutil.copy(pasgen_src, pasgen_dst)
    make_executable(pasgen_dst)

    # Copy the generate_entries.py script
    generate_entries_src = 'generate_entries.py'
    generate_entries_dst = '/usr/local/bin/generate_entries.py'
    shutil.copy(generate_entries_src, generate_entries_dst)
    make_executable(generate_entries_dst)

# Read the contents of the requirements.txt file
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='pasgen',
    version='1.0',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'pasgen=pasgen:main',
        ],
    },
)

setup_pasgen()
