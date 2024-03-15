.. _project_info-contributing:

============
Contributing
============

Contributions are welcome and greatly appreciated!


----------------------
Types of Contributions
----------------------
~~~~~~~~~~~~
Report a bug
~~~~~~~~~~~~
If you have found a bug, please report it on `our issues page <https://github.com/gymrek-lab/core/issues>`_ rather than emailing us directly. Others may have the same issue and this helps us get that information to them.

Before you submit a bug, please search through our issues to ensure it hasn't already been reported. If you encounter an issue that has already been reported, please upvote it by reacting with a thumbs-up emoji. This helps us prioritize the issue.

The most helpful Github issues include
    - the version of core you are using, although it's best to use the latest version
    - detailed steps to help us reproduce your error, ideally with the example datasets in the :code:`tests/data` directory

~~~~~~~~~
Fix a bug
~~~~~~~~~
Look through our issues page for bugs. We especially need help with bugs labeled "help wanted". If you want to start working on a bug then please write a message within the thread for that issue on our issues page, so that no one is duplicating work.

Please add a test reproducing the bug in our `tests/ directory <https://github.com/gymrek-lab/core/tree/main/tests>`_.

~~~~~~~~~~~~~~~~~~~~~~~
Implement a new feature
~~~~~~~~~~~~~~~~~~~~~~~
Our issues page will almost always have features on our wishlist. Once again, if you want to start working on a feature then please write a message within the thread for that feature on our issues page, so that no one is duplicating work.

Have an idea for a new feature that isn't on our wishlist? We'd love to hear about it! Before getting to work, please create a Github issue for it, so that you can make sure we're in agreement about what it should do. After you finish the feature, please add tests and documentation for it, as well.

-------------------------------------------
How to fix a bug or implement a new feature
-------------------------------------------
Please create a pull request! A PR is a collection of changes that you have made to the code that we can review and potentially integrate into core.

To create a pull request you need to do these steps:
    1. Create a Github account
    2. `Fork the repository <https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository>`_
        - Click the "Fork" button in the top, right corner
        - Or, if you had already forked the repository a while ago, `sync your fork <https://docs.github.com/en/github/collaborating-with-pull-requests/working-with-forks/syncing-a-fork>`_ to make sure you're working with the latest version of core
    3. `Clone your fork locally <https://docs.github.com/en/get-started/quickstart/fork-a-repo#cloning-your-forked-repository>`_
    4. :code:`cd core` into the new directory
    5. Create a new branch off of the :code:`main` branch with :code:`git checkout -b <descriptive_branch_name>`. Please follow `best practices <https://www.conventionalcommits.org/>`_ when naming your branch
    6. Setup our development environment by following the instructions in :ref:`dev-setup-instructions` below
    7. Make your changes to the code
    8. Add additional tests to the :code:`tests/` directory and add comments to the documentation to explain how to use your new code. We use pytest for testing and sphinx/numpydoc for documentation.
    9. Run the automated code-checking steps detailed in :ref:`code-check-instructions` below
    10. Commit your changes. Please use informative commit messages and do your best to ensure the commit history is clean and easy to interpret
    11. Now you can push your changes to your Github copy of core by running :code:`git push origin <descriptive_branch_name>`
    12. Go to your Github copy of core in your browser and create a pull request titled according to the `conventional commits spec <https://www.conventionalcommits.org/>`_. Be sure to change the pull request target branch to :code:`main` on this original repository.
    13. Please write an informative pull request detailing the changes you have made and why you made them. Tag any related issues by referring to them by a hashtag followed by their ID


.. _dev-setup-instructions:

------------
Dev Setup
------------

Follow these steps to set up a development environment.

1. Create a conda environment with ``poetry``

    .. code-block:: bash

        conda env create -n core -f dev-env.yml
2. Install core and its dependencies into a separate environment managed by ``poetry``

    .. code-block:: bash

        conda run -n core poetry install

3. Now, whenever you'd like to run/import ``core`` or ``pytest``, you will first need to activate both environments

    .. code-block:: bash

        conda activate core
        poetry shell

---------------------
Managing Dependencies
---------------------
Run ``poetry help`` to read about the suite of commands it offers for managing dependencies.

For example, to add a pypi dependency to our list and install it, just run

    .. code-block:: bash

        poetry add <dependency>

You should specify a `version constraint <https://python-poetry.org/docs/master/dependency-specification>`_ when adding a dependency. Use the oldest version compatible with your code. Don't worry if you're not sure at first -- you can (and should!) always update it later. For example, to specify a version of ``click`` >= 8.0.4:

    .. code-block:: bash

        poetry add 'click>=8.0.4'

-----------------------------
Modifying the ``.hap`` format
-----------------------------
If you modify the :doc:`.hap file format </formats/haplotypes>`, you should bump the version number, which is listed at the top of the `core/data/haplotypes.py <https://github.com/gymrek-lab/core/blob/main/core/data/haplotypes.py>`_ module and follows `semantic versioning <https://semver.org/>`_.

Please describe any modifications or new features in :doc:`the .hap docs </formats/haplotypes>` and in the :ref:`Changelog at the bottom of that page <formats-haplotypes-changelog>`.

After bumping the version number, you should also update all ``.hap`` and ``.hap.gz`` files in the `tests/data/ directory <https://github.com/gymrek-lab/core/tree/main/tests/data>`_ to use the new version number.

.. _code-check-instructions:

-----------
Code Checks
-----------
Before creating your pull request, please run each of our code checks.

1. Format the code correctly

    .. code-block:: bash

        black .

2. If you made changes to the docs, check that they appear correctly.

    .. code-block:: bash

        sphinx-build docs docs/_build
        open docs/_build/index.html

3. Run all of the tests

    .. code-block:: bash

        pytest tests/

    You can also build the package and run the tests from the built version using ``nox``. This will fully simulate installing the package from PyPI.

    .. code-block:: bash

        nox --session=tests

---------------------
Publish a new version
---------------------
To publish a new version of core:

1. First, locate `the most recent core PR <https://github.com/gymrek-lab/core/pulls>`_ prefixed "chore(main)" created by our Github actions bot
2. List an admin on our repository (currently: ``@aryarm``) as a reviewer of the PR and ask them to merge it
3. The bot will automatically create a new version on PyPI and tag a release on Github
4. A few hours later, bioconda will automatically detect the new release on PyPI and create a PR in `their repository <https://github.com/bioconda/bioconda-recipes/pulls>`_
5. Check that all of the dependencies in the recipe have been updated properly. If they are, you should comment on the bioconda PR with "@BiocondaBot please add label"
6. After 1-2 days, someone from the bioconda team will merge our PR and the version will get updated on bioconda. Otherwise, ping them a reminder on `Gitter <https://gitter.im/bioconda/Lobby>`_

-----
Style
-----
~~~~
Code
~~~~

    1. Please type-hint all function parameters
    2. Please adhere to PEP8 whenever possible. :code:`black` will help you with this.
    3. Please use relative imports whenever importing modules from the code base
    4. For readability, please separate imports into three paragraph blocks:
        i. from the python standard library
        ii. from external, third party packages
        iii. from our own internal code

.. _contributing-style-errors:

~~~~~~
Errors
~~~~~~
We use the `Python logging module <https://coralogix.com/blog/python-logging-best-practices-tips/>`_ for all messages, including warnings, debugging info, and otherwise. For example, all classes have a ``log`` property that stores a logger object.

.. code-block:: python

    from logging import getLogger

    # create a new logger object if one hasn't been provided by the user
    log = getLogger(self.__class__.__name__)

    # log a warning message to the logger
    log.warning("This is a warning")

This way, the user can choose their level of verbosity among *CRITICAL*, *ERROR*, *WARNING*, *INFO*, *DEBUG*, and *NOTSET*. However, for critical errors, our convention is to raise exceptions, usually with a custom ``ValueError``.

~~~~~~~~~~~~~~~~~~~
Git commit messages
~~~~~~~~~~~~~~~~~~~

    1. Use the present tense ("Add feature" not "Added feature")
    2. Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
    3. Reference issues and pull requests liberally after the first line
