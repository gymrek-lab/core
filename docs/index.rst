.. _manual-main:

core
====

This is the documentation for the Gymrek Lab's core python library. It is a dependency of many of our other tools.

A highlight of the core library is the :doc:`.hap file </formats/haplotypes>`, our new file format for haplotypes designed for speed, extensibility, and ease-of-use.


Logging
~~~~~~~

All commands output log messages to standard error. The universal ``--verbosity`` flag controls the level of detail in our logging messages. By default, this is set to ``INFO``, which will yield errors, warnings, and info messages. To get more detailed messages, set it to ``DEBUG``. To get only error messages, set it to ``ERROR``. To get errors *and* warnings, set it to ``WARNING``. Refer to `the Python documentation on logging levels <https://docs.python.org/3/library/logging.html#levels>`_ for more information.

Contributing
~~~~~~~~~~~~

We gladly welcome any contributions to ``core``!

Please read our :doc:`contribution guidelines </project_info/contributing>` and then submit a `Github issue <https://github.com/gymrek-lab/core/issues>`_.


.. toctree::
   :caption: Overview
   :name: overview
   :hidden:
   :maxdepth: 1

   project_info/installation
   project_info/contributing

.. toctree::
   :caption: File Formats
   :name: formats
   :hidden:
   :maxdepth: 1

   formats/genotypes.rst
   formats/haplotypes.rst
   formats/phenotypes.rst
   formats/linear.rst
   formats/breakpoints.rst

.. toctree::
   :caption: API
   :name: api
   :hidden:
   :maxdepth: 1

   api/data
   api/examples