# Colorful Test

**Colorful Test** is a unit testing framework that is similar to and inspired by Python's [unittest](https://docs.python.org/3/library/unittest.html). What makes **Colorful Test** cool and different is that it's uniquely designed for educational settings while also supporting general-purpose use. It displays error messages in *a colorful and more helpful way*, and success messages in a way that makes students proud of their work. 

It also guides students through their projects by *failing fast* *(by default)* and showing them exactly what went wrong. *unittest* doesn't give you much freedom when it comes to the order of test execution, but this is so important for student projects that, with **Colorful Test**, you can just append a number at the end of the test name to determine the order.

We also provide a *grade/score feature* *(optional)* that makes it easy to grade student projects. The run method returns a TestResults object that lets you customize how the output looks, giving you more control.

If you're familiar with *unittest*, it shouldn't be hard to get a grasp of how **Colorful Test** works, and you can skip to the official docs.

## Installation

To use Colorful Test, first install it using pip:

```console
$ pip install colorful-test
```

## Documentation

Read the full documentation [here]().

## Basic Example

Colorful Test provides a handful of useful tools to help you construct and run tests. Here's a basic example of some of those tools in action:

```python
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
```

A TestCase is created by inheriting `TestCase`. The test runner looks for methods that start with **test_** and considers them as tests. These tests are then ordered based on the number appended to their names.

In each test, **assert_equal** or **assert_raises** can be used—these work similarly to [`assertEqual`](https://docs.python.org/3/library/unittest.html) and [`assertRaises`](https://docs.python.org/3/library/unittest.html) from the `unittest` framework.  

- **assert_equal** checks if the first and second arguments are equivalent.  
- **assert_raises** verifies whether the specified callable raises an error with the given arguments.  
- Alternatively, you can simply use **assert**, and the test runner will still accumulate all test results and generate a test report.

One thing to note is that **test_basic_multiplication_0** will be executed first, followed by **test_basic_division_error_1**, and so on. This happens because of how the tests are ordered.  

Appending a number to test method names is not mandatory—if omitted, test methods will be ordered alphabetically.

## Tutorial

[This tutorial]() will guide you on how to write unit tests using **Colorful Test**.

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. [Fork](https://github.com/lindelwa122/Colorful-Test/fork) this repository.

2. Clone the repository to your own machine by running one of the following commands:

   - HTTPS

   ```
   git clone https://github.com/<your-username>/Colorful-Test.git
   ```

   OR

   - SSH

   ```
   git clone git@github.com:<your-username>/Colorful-Test.git
   ```

   OR

   - Github CLI:

   ```
   gh repo clone <your-username>/Colorful-Test
   ```

3. Create a new branch. The name of the branch must reflect the change you are about to make.

   ```
   git checkout -b <branch-name>
   ```

4. Make your changes or add your new feature. Remember to commit early and commit often. Read our commit rules [here](/COMMIT_RULES.md).

   - Short commit messages:
     ```
     git add <changed-files>
     git commit -m "<commit-message>"
     ```
   - Long commit messages:
     ```
     git add <changed-files>
     git commit
     ```

5. Push your changes to Github by running this command:

   ```
   git push origin <branch-name>
   ```

6. Go over to GitHub and create a pull request. Make sure to include a comment explaining the additions. Please include the issue number being addressed in your comment. For instance, if you were resolving issue 6, add `Issue: #6` at the end of your comment. For more information, please refer to our contributing rules [here](/CONTRIBUTING.md).

## More ways to contribute

You can contribute not only by writing code but also by assisting us in enhancing this README, drafting documentation, creating tutorials, and more.

- Fix spelling and grammatical errors across our documentation.
- Enhance this README and other docs.
- Create more tutorials on our website.
- Produce video tutorials.
- Write tests.
- Design a logo for us.
- Report bugs.
- Suggest additional features.

## Licence

Distributed under the Apache License 2.0. See `LICENSE` for more information.

## Contact

Email - [nqabenhlemlaba22@gmail.com](mailto:nqabenhlemlaba22@gmail.com)

Instagram - [instagram.com/asanda.que](https://instagram.com/asanda.que)

GitHub - [github.com/lindelwa122](https://github.com/lindelwa122)

LinkedIn - [linkedin/nqabenhle](https://linkedin.com/in/nqabenhle)
