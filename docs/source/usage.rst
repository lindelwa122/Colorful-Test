Usage
=====

.. _installation:

Installation
------------

To use Colorful Test, first install it using pip:

.. code-block:: console

    $ pip install colorful-test

.. _basic_example:

Basic Example
-------------

Colorful Test provides a handful of useful tools to help you construct and run tests. Here's a basic example of some of those tools in action:

.. code-block:: python

    from colorful_test import TestCase, show_message
    from solution import add, mul, div

    class TestSolution(TestCase):

        @show_message(
            success='Your add method works as expected',
            fail='''
            Your add method doesn't work as expected. Hints:

            Expected: %s
            Received: %f
            '''
        )
        def test_basic_addition_2(self):
            self.assert_equal(add(1, 1), 2)
            self.assert_equal(add(1, 2), 3)

        @show_message(
            success='Your mul method works as expected',
            fail='''
            Your mul method doesn't work as expected. Hints:

            Expected: %s
            Received: %f
            '''
        )
        def test_basic_multiplication_0(self):
            self.assert_equal(mul(1, 1), 1)
            self.assert_equal(mul(1, 2), 2)

        @show_message(
            success='Your div method works as expected',
            fail='Your div method should raise a ZeroDivisionError if the second argument is 0'
        )
        def test_basic_division_error_1(self):
            self.assert_raises(ZeroDivisionError, div, 3, 0)

    if __name__ == '__main__':
        TestSolution.run_and_output_results()

A TestCase is created by inheriting TestCase. The test runner looks for methods that start with **test_** and considers them as tests. These tests are then ordered based on the number appended to their names.

In each test, **assert_equal** or **assert_raises** can be used—these work similarly to *assertEqual* and *assertRaises* from the `unittest <https://docs.python.org/3/library/unittest.html>`_ framework. **assert_equal** checks if the first and second arguments are equivalent, while **assert_raises** verifies whether the specified callable raises an error with the given arguments. However, you don't have to use these methods—you can simply use **assert**, and the test runner will still accumulate all test results and generate a test report.

One thing to note is that **test_basic_multiplication_0** will be executed first, followed by **test_basic_division_error_1**, and so on. This happens because of how the tests are ordered. Appending a number to test method names is not mandatory—if omitted, test methods will be ordered alphabetically.

.. _command_line_interface:

Command Line Interface
----------------------

The tests are run in the command-line interface. While the framework doesn't yet offer as many commands or as much flexibility as other Python frameworks, you can still run tests easily.

To execute a test file, run one of the following commands:

.. code-block:: console

    $ python <test_file>

or

.. code-block:: console

    $ python -m colorful-test <test_file>/<directory>

If you specify a directory, Colorful Test will find all Python files in that directory that start with **test_** and execute them.

.. _organizing_your_code:

Organizing your code
--------------------

The basic building blocks of unit testing are test cases—single scenarios that must be set up and checked for correctness. **Colorful Test**'s *TestCase* provides functionalities to create test cases and test methods, making it easy to test different scenarios.

You don't always have to use *show_message*, as seen in the :ref:`Basic Example <basic_example>`, when writing test methods. Here's another basic example of a test case:

.. code-block:: python

    from colorful_test import TestCase
    from person import person
    from account import Account

    class TestBankAccount(TestCase):

        def test_account_deposit(self):
            josh = Person('Josh', 'Gilder')
            account = Account(josh)
            account.open()

            account.deposit(500)
            self.assert_equal(account.get_balance(), 500)

    if __name__ == '__main__':
        TestBankAccount.run_and_output_results()

That is a simple test case that checks if money can be deposited into an account. It uses one of our **assert_*** methods to achieve this.

Note that we have to call the **run_and_output_results** method to run our test case. Without calling the runner, nothing will happen. But if we do call it, we'll get a report on how our unit tests ran—even without using *show_message*.

This is how the output will look:

.. code-block:: console

    Ran 1 tests in 0.000078 ms
    1 passed
    0 failed
    0 skipped
    0 error(s)

    ✓ Grade: 100.0%

**Grade** is just another metric that specifies the success rate of our tests. It can be useful in educational environments.

Tests can be numerous, and their setup can be repetitive. That's where **set_up** comes in—it's a method that is called before each test runs, providing a setup that will be used by the test methods.

Here's an example:

.. code-block:: python

    from colorful_test import TestCase
    from person import person
    from account import Account

    class TestBankAccount(TestCase):

        def set_up(self):
            self.josh = Person('Josh', 'Gilder')
            self.account = Account(josh)
            self.account.open()

        def test_account_deposit(self):
            self.account.deposit(500)
            self.assert_equal(account.get_balance(), 500)

    if __name__ == '__main__':
        TestBankAccount.run_and_output_results()

If the **set_up()** method raises an exception while the test is running, the framework will consider the test to have encountered an error, and the test method will not be executed.

Similarly, we can provide a **tear_down()** method to clean up after the test method has run:

.. code-block:: python

    from colorful_test import TestCase
    from person import person
    from account import Account

    class TestBankAccount(TestCase):

        def set_up(self):
            self.josh = Person('Josh', 'Gilder')
            self.account = Account(josh)
            self.account.open()

        def tear_down(self):
            self.account.close()

By default, tests will fail fast, meaning the run will stop immediately after encountering the first error or failure. You can change this by setting **fail_fast** to *False* in **run_and_output_results**.

Here's an example:

.. code-block:: python

    if __name__ == '__main__':
        TestBankAccount.run_and_output_results(fail_fast=False)

Using **run_and_output_results** will run your test case and display the results in the console. However, you can also use the **run** method, which won't print anything to the console but will return a **TestResults** object, allowing you to customize how you handle errors and different scenarios.

Example using the **run** method:

.. code-block:: python

    if __name__ == '__main__':
        TestBankAccount.run(fail_fast=False)

.. _skipping_tests:

Skipping tests
--------------

**Colorful Test** supports skipping test methods. Skipping a test is as simple as raising a **SkipTest** exception—the test runner will recognize this as a skipped test.

Here's an example of how you can skip tests:

.. code-block:: python

    import colorful_test

    class ExampleTestCase(colorful_test.TestCase):

        @colorful_test.skip(reason='showing how skip works')
        def test_one(self):
            # Test will be skipped
            pass

        @colorful_test.skip_if(not feature_enabled("dark_mode"), reason="Dark mode is not enabled")
        def test_two(self):
            # Test will be skipped only if dark_mode is not enabled
            pass

        @colorful_test.skip_unless(sys.platform == "win32", reason="Only supports Windows")
        def test_three(self):
            # Test will be skipped unless platform is Windows
            pass

The following decorators and exception implement test skipping:

.. autofunction:: colorful_test.skip_test.skip_test(reason)

.. autofunction:: colorful_test.skip_test.skip_test_if(reason)

.. autofunction:: colorful_test.skip_test.skip_test_unless(reason)

.. _classes_and_functions:

Classes and functions 
---------------------

.. _classes_and_functions_testcase:

TestCase
~~~~~~~~

.. autoclass:: colorful_test.testcase.TestCase
   :members:
   :undoc-members:
   :inherited-members:
   :show-inheritance:

.. _classes_and_functions_message:

Message 
~~~~~~~

.. autofunction:: colorful_test.message.show_message
