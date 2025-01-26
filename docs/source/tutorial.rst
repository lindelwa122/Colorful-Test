Tutorial: A simple Calculator program
=====================================

In this tutorial, you'll write unit tests for a simple calculator program. This will help you get started with Colorful Test's features and understand how to make the most of the framework.

For a more detailed explanation, see Usage.

.. _tutorial_getting_started:

Getting started
---------------

To get started, install **Colorful Test** using pip by running this command:

.. code-block:: console

    $ pip install colorful-test

To install **Colorful Test** inside a virtual environment, first create a virtual environment using Python.

.. code-block:: console

    $ python -m venv .env

Activate the virtual environment by running this command:

.. code-block:: console

    $ source .env/bin/activate

.. _tutorial_tutorial:

Calculator program
------------------

Create a folder called **colorful-test-tutorial**, and inside it, create a file named calculator.py. Then, paste the following code inside it:

.. code-block:: python

    # calculator.py

    def add(first, second):
        return first + second

    def multiply(first, second):
        return first * second

    def divide(first, second):
        if second == 0: 
            raise ZeroDivisionError('you cannot divide by 0')

        return first / second

    def subtract(first, second):
        return first - second

That's our basic calculator program! It's simple but enough to showcase some of the powerful features of **Colorful Test**.  

Now, create a **test_calculator.py** file, and let's start writing our tests!

.. code-block:: python

    from colorful_test import TestCase
    import calculator

    class TestCalculator(TestCase):
        def test_add(self):
            assert calculator.add(1, 1) == 2
            assert calculator.add(1, 2) == 3

For now, we have a simple test method that asserts the **add** method of the calculator returns the expected values for given arguments.

.. _tutorial_test_runner:

The test runner
~~~~~~~~~~~~~~~

If you run the tests, you won't see anything on the console. That's because **Colorful Test** doesn't automatically call the test runner—you have to do it yourself.  

To run our tests, modify **test_calculator.py** so that it contains the following code:

.. code-block:: python

    ...

    if __name__ == '__main__':
        TestCalculator.run_and_output_results()

You should see something like this in your console:

.. code-block:: console

    ========================================================

    Ran 1 tests in 1.104116 ms
    1 passed
    0 failed
    0 skipped
    0 error(s)

    ✓ Grade: 100.0%

.. _tutorial_testcase:

TestCase assert_* methods
~~~~~~~~~~~~~~~~~~~~~~~~~

Even though **assert** works fine, for more complex test cases, you'll need to use some of the built-in methods that **TestCase** provides.  

Let's switch to **assert_equal** and add more tests for the calculator program.  

Replace your existing tests with the following code:

.. code-block:: python

    from colorful_test import TestCase
    import calculator

    class TestCalculator(TestCase):
        def test_add(self):
            self.assert_equal(calculator.add(1, 1), 2)
            self.assert_equal(calculator.add(1, 2), 3)

        def test_subtract(self):
            self.assert_equal(calculator.subtract(1, 1), 0)
            self.assert_equal(calculator.subtract(1, 2), -1)

        def test_multiply(self):
            self.assert_equal(calculator.multiply(1, 1), 1)
            self.assert_equal(calculator.multiply(1, 2), 2)

        def test_divide(self):
            self.assert_raises(ZeroDivisionError, calculator.divide, 1, 0)
            self.assert_equal(calculator.divide(1, 2), 0.5)

    if __name__ == '__main__':
        TestCalculator.run_and_output_results()

Things to note about the code above:  

- We now use **TestCase** methods to check if two values are equivalent instead of just using **assert**.  
- We use **assert_raises** to verify that **divide** raises a **ZeroDivisionError** when the second argument is zero.  

After running the code, all tests should pass!

.. _tutorial_colorful_message:

Colorful messages
~~~~~~~~~~~~~~~~~

One of the coolest features of **Colorful Test** is its ability to display elegant and helpful error messages, along with success messages that make users feel excited about their progress.  

Adding these messages is super simple! Just import **show_message** from **colorful_test** and use it as a decorator to wrap your test methods.  

Here's an example of how **show_message** is used:

.. code-block:: python

    @show_message(fail='This test failed', success='This test passed')
    def test_func(self):
        pass

Obviously, you'll want to write more helpful messages than just "Test failed" or "Test passed," but you get the idea!

If the test fails, the failure message will be printed; otherwise, the success message will be displayed. You don't need to specify both arguments.

Now, go ahead and add **show_message** with helpful messages to all your test methods!

.. code-block:: python

    from colorful_test import TestCase, show_message
    import calculator

    class TestCalculator(TestCase):
        @show_message(
            success='Calculator can add two numbers as expected.',
            fail='''
            Calculator failed to add two numbers as expected.

            Hints:
            Expected: %s
            Received: %f
            '''
        )
        def test_add(self):
            self.assert_equal(calculator.add(1, 1), 2)
            self.assert_equal(calculator.add(1, 2), 3)

        @show_message(
            success='Calculator can subtract two numbers as expected.',
            fail='''
            Calculator failed to subtract two numbers as expected.

            Hints:
            Expected: %s
            Received: %f
            '''
        )
        def test_subtract(self):
            self.assert_equal(calculator.subtract(1, 1), 0)
            self.assert_equal(calculator.subtract(1, 2), -1)

        @show_message(
            success='Calculator can multiply two numbers as expected.',
            fail='''
            Calculator failed to multiply two numbers as expected.

            Hints:
            Expected: %s
            Received: %f
            '''
        )
        def test_multiply(self):
            self.assert_equal(calculator.multiply(1, 1), 1)
            self.assert_equal(calculator.multiply(1, 2), 2)

        @show_message(
            success='Calculator can divide two numbers as expected.',
            fail='''
            Calculator failed to divide two numbers as expected.

            Hints:
            Expected: %s
            Received: %f
            '''
        )
        def test_divide(self):
            self.assert_raises(ZeroDivisionError, calculator.divide, 1, 0)
            self.assert_equal(calculator.divide(1, 2), 0.5)

    if __name__ == '__main__':
        TestCalculator.run_and_output_results()

In the **fail messages**, you can use **%f** to refer to the first argument that was passed to the method that failed, and **%s** to refer to the second argument. This can make your test messages much more informative and helpful.

After running the tests, you should now see four new success messages in the console that look something like this:  

.. code-block:: console

    ✓ Calculator can add two numbers as expected.
    ✓ Calculator can divide two numbers as expected.
    ✓ Calculator can multiply two numbers as expected.
    ✓ Calculator can subtract two numbers as expected.
    ========================================================

    Ran 4 tests in 3.145218 ms
    4 passed
    0 failed
    0 skipped
    0 error(s)

    ✓ Grade: 100.0%

Let's intentionally make one test fail to see how the failure message appears:

.. code-block:: python

    ...

    def test_divide(self):
        ...
        self.assert_equal(calculator.divide(1, 3), 0.5)

    ...

Change the two to a three and run the tests.

.. _tutorial_fail_fast:

Fail fast
~~~~~~~~~

By default, tests fail fast, meaning the runner stops execution immediately after encountering an error or failure. That's exactly what happened when we intentionally caused a test to fail.

We can change this behavior by setting the **fail_fast** argument to *False* in the runner:

.. code-block:: python
    
    ...
    if __name__ == '__main__':
        TestCalculator.run_and_output_results(fail_fast=False)

Now, it should say 3 test passed instead of 1.

.. _tutorial_order:

Ordering test methods
~~~~~~~~~~~~~~~~~~~~~

By default, the order in which test methods are executed is based on their alphabetical order. This might not always be ideal. For example, when creating a project for students, it may make more sense to test certain features before others. **Colorful Test** provides the flexibility to order tests according to our needs.

To order our tests, we simply need to add an underscore followed by a number at the end of the test method name. Modify your code to look like this:

.. code-block:: python

    ...

    class TestCalculator(TestCase):
        ...
        def test_add_0(self):
            self.assert_equal(calculator.add(1, 1), 2)
            self.assert_equal(calculator.add(1, 2), 3)

        ...
        def test_subtract_1(self):
            self.assert_equal(calculator.subtract(1, 1), 0)
            self.assert_equal(calculator.subtract(1, 2), -1)

        ...
        def test_multiply_2(self):
            self.assert_equal(calculator.multiply(1, 1), 1)
            self.assert_equal(calculator.multiply(1, 2), 2)

        ...
        def test_divide_3(self):
            self.assert_raises(ZeroDivisionError, calculator.divide, 1, 0)
            self.assert_equal(calculator.divide(1, 3), 0.5)

    ...

Now, your tests should execute in the order we've specified, from test method number 0 to test method number 3.

.. _tutorial_conclusion:

Conclusion
----------

This tutorial covers all the basics you need to get started with **Colorful Test**. For more functions and methods, refer to the :doc:`usage` documentation.
