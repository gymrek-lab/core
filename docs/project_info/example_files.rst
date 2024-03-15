.. _project_info-example_files:

=============
Example files
=============

Locating the files
------------------

The examples throughout our documentation make use of two sets of files: test files and example files.

Test files can be found in the `tests/data/ directory <https://github.com/gymrek-lab/core/tree/main/tests/data>`_ of our Github repository. These are short, simplified files used exclusively by our automated test suite.

.. _running-an-example-command:

Running an example command
--------------------------
To run any of the example code in our documentation, follow these steps.

1. :doc:`Install core </project_info/installation>`
2. Clone our Github repository

    .. code-block:: bash

    	git clone -b v$(core --version) https://github.com/gymrek-lab/core.git

3. Change to the cloned directory

    .. code-block:: bash

    	cd core

4. Execute the example code

Running all examples
--------------------
All of our examples are included within our test suite, which is executed regularly by our continuous integration system. To check that all of the examples work on your system, you can just have ``pytest`` automatically run all of our tests.

1. Follow the :ref:`first three steps above <running-an-example-command>`
2. Install ``pytest``

    .. code-block:: bash

    	pip install 'pytest>=6.2.5'

3. Run our tests

    .. code-block:: bash

    	pytest tests/
