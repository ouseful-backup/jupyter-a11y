import setuptools

setuptools.setup(
    name="nbreader",
    packages=['nbreader'],
    version='0.0.1',
    include_package_data=True,
    install_requires=[
        'notebook', 'jupyter_nbextensions_configurator'
    ],
    data_files=[
        # like `jupyter nbextension install --sys-prefix`
        ("share/jupyter/nbextensions/nbreader", [
            "nbreader/static/index.js",  "nbreader/static/nbreader.yaml",
            "nbreader/static/README.md",
        ]),
        # like `jupyter nbextension enable --sys-prefix`
        ("etc/jupyter/nbconfig/notebook.d", [
            "jupyter-config/nbconfig/notebook.d/nbreader.json"
        ])
    ],
    zip_safe=False
)