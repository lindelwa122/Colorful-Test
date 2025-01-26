.. Colorful Test documentation master file, created by
   sphinx-quickstart on Sun Jan 26 09:57:43 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Colorful Test documentation
===========================

**Colorful Test** is a unit testing framework that is similar to and inspired by Python's `unittest <https://docs.python.org/3/library/unittest.html>`_. What makes **Colorful Test** cool and different is that it's uniquely designed for educational settings while also supporting general-purpose use. It displays error messages in *a colorful and more helpful way*, and success messages in a way that makes students proud of their work. 

It also guides students through their projects by *failing fast* *(by default)* and showing them exactly what went wrong. *unittest* doesn't give you much freedom when it comes to the order of test execution, but this is so important for student projects that, with **Colorful Test**, you can just append a number at the end of the test name to determine the order.

We also provide a *grade/score feature* *(optional)* that makes it easy to grade student projects. The run method returns a TestResults object that lets you customize how the output looks, giving you more control.

If you're familiar with *unittest*, it shouldn't be hard to get a grasp of how **Colorful Test** works, and you can skip to :doc:`usage`.


.. toctree::
   :maxdepth: 3
   :caption: Contents:

   usage
   tutorial
   api
