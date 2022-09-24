from setuptools import setup, find_packages


setup(
    name="mkdocs-section-index",
    version="0.3.4",
    description="MkDocs plugin to allow clickable sections that lead to an index page",
    authors=["Oleh Prypin <oleh@pryp.in>"],
    license="MIT",
    repository="https://github.com/oprypin/mkdocs-section-index",
    keywords=["mkdocs", "mkdocs-plugin"],
    readme="README.md",
    python_requires='>=3.0',
    packages=find_packages(),
    install_requires=[
        'mkdocs>=1.0.4',
    ],
    entry_points={
        'mkdocs.plugins': [
            'section-index = mkdocs_section_index.plugin:SectionIndexPlugin'
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
    ],
)
