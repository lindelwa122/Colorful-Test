from re import compile
from time import time

from .exceptions import SkipTest
from .message import output_msg

class TestCase:
    """
    Base class that implements the interface needed by the runner to allow
    it do drive the tests, and methods that the test code can use to check 
    for and report various kinds of failures.    
    """

    class TestResult:
        """
        Class that stores the results of the tests ran by run(). It provides
        functionalities to display output to the screen.
        """
        def __init__(self):
            self.failed = []
            self.errors = []
            self.passed = []
            self.time = 0

        def get_total_tests_ran(self):
            return len(self.failed) + len(self.errors) + len(self.passed)

        def add_test(self, status, order_num, name, errors=None):
            match status:
                case 'error':
                    self.errors.append({ 'order': order_num, 'name': name, 'errors': errors })

                case 'pass':
                    self.passed.append({ 'order': order_num, 'name': name })

                case 'fail':
                    self.failed.append({ 'order': order_num, 'name': name })

    def __init_subclass__(cls, **kwargs):
        cls.clean_ups = []
        super().__init_subclass__(**kwargs)

    def __call_a_callable_safely(self, callable, test, index, results, fail_fast):
        try:
            try:
                callable()
            except (AssertionError, SkipTest) as err:
                results.add_test('fail', index, test.__name__)

                # Do cleanups
                self.do_cleanups()

                if not fail_fast: return results, 'fail_slow'
                else: return results, 'fail_fast'

        except Exception as err:
            results.add_test('error', index, test.__name__, err)
            
            # Do cleanups
            self.do_cleanups()

            if not fail_fast: return results, 'fail_slow'
            else: return results, 'fail_fast'

        return results, 'success'

    def __get_tests(self):
        tests = []

        for method in dir(self):
            if method.startswith('test_'):
                tests.append(getattr(self, method))

        return tests
    
    def __order_tests(self, tests):
        def sort_by(test):
            key = test.__name__.split('_')[-1]
            return int(key) if key.isdigit() else 0
        
        tests.sort(key=sort_by)
        return tests
    
    def set_up(self):
        """
        This method is called immediately before calling a test method;
        other than AssertionError or SkipTest, any exception raised by
        this method will be considered an error rather than a test
        failure. The default implementation does nothing.
        """
        pass

    def tear_down(self):
        """
        This method is called immediately after calling a test method;
        other than AssertionError or SkipTest, any exception raised by
        this method will be considered an error rather than a test
        failure. This method will be executed only if set_up succeeds.
        The default implemantation does nothing.
        """
        pass

    @classmethod
    def set_up_class(cls):
        """
        This method is called before tests in an individual class run. The
        default implementation does nothing.
        """
        pass

    @classmethod
    def tear_down_class(cls):
        """
        This method is called after tests in an individual class run. The
        default implementation does nothing.
        """
        pass

    @classmethod
    def run(cls, fail_fast=True):
        """
        Run the tests, collecting the results into TestResult object. The
        result object is returned to run()'s caller.
        """
        # Start timer
        start = time()
        
        # Create an instance
        instance = cls()
        
        # Create test results
        results = TestCase.TestResult()

        # Set up class
        TestCase.set_up_class()

        # Get and sort tests
        tests = instance.__get_tests()
        tests = instance.__order_tests(tests)
        
        for index, test in enumerate(tests):
            # Set up before running a test
            results, status = instance.__call_a_callable_safely(
                instance.set_up, 
                test, 
                index, 
                results, 
                fail_fast
            )

            match status:
                case 'fail_slow': 
                    continue
                case 'fail_fast':
                    end = time()
                    results.time = f'{(end - start) * 1000:.6f}' 
                    return results
                
            # Run tests
            results, status = instance.__call_a_callable_safely(
                test,
                test,
                index,
                results,
                fail_fast
            )

            match status:
                case 'fail_slow': 
                    continue
                case 'fail_fast': 
                    end = time()
                    results.time = f'{(end - start) * 1000:.6f}'
                    return results

            # Clean up
            results, status = instance.__call_a_callable_safely(
                instance.tear_down,
                test,
                index,
                results,
                fail_fast
            )
            
            match status:
                case 'fail_slow': 
                    continue
                case 'fail_fast': 
                    end = time()
                    results.time = f'{(end - start) * 1000:.6f}'
                    return results
                case 'success': 
                    results.add_test('pass', index, test.__name__)
                    cls.do_cleanups()

        # Clean up class 
        TestCase.tear_down_class()
        
        # End timer
        end = time()
        
        results.time = f'{(end - start) * 1000:.6f}'

        return results

    @classmethod
    def run_and_output_results(cls, fail_fast=True):
        results = cls.run(fail_fast)

        print(
            '========================================================\n',
            f'Ran {results.get_total_tests_ran()} tests in {results.time} ms',
            f'{len(results.passed)} passed',
            f'{len(results.failed)} failed',
            f'{len(results.errors)} error(s)',
            sep='\n',
            end='\n\n',
        )
        
        if results.errors:
            print('Errors: ')
            
            for error in results.errors:
                output_msg(
                    "err",
                    f'''
    Test Number: {error["order"]}
    Test Name: {error["name"]}
    Error: {error["errors"]}
                    '''
                )
                
        if results.failed:
            print('Failures: ')
            
            for failure in results.failed:
                print(
                    f'Test Number: {failure["order"]}',
                    f'Test Name: {failure["name"]}',
                    sep='\n',
                    end='\n\n',
                )
    
    def skip_test(cls, reason):
        """
        Calling this during a test method or setUp() skips the current test.
        """
        raise SkipTest(reason)

    def assert_equal(self, first, second):
        """
        Test that first and second are equal. If the values does not 
        compare, the test will fail.
        """
        if isinstance(first, list) and isinstance(second, list):
            self.assert_list_equal(first, second)
        elif isinstance(first, tuple) and isinstance(second, tuple):
            self.assert_tuple_equal(first, second)
        elif isinstance(first, dict) and isinstance(second, dict):
            self.assert_dict_equal(first, second)
        elif isinstance(first, set) and isinstance(second, set):
            self.assert_set_equal(first, second)
        else:
            assert first == second, { 'first': first, 'second': second }

    def assert_not_equal(self, first, second):
        """
        Test that first and second are not equal. If the values do compare
        equal, the test will fail
        """
        assert first != second, { 'first': first, 'second': second }

    def assert_true(self, expr):
        """
        Test that expr is True.
        """
        assert bool(expr), { 'first': expr, 'second': True }

    def assert_false(self, expr):
        """
        Test that expr is False.
        """
        assert not bool(expr), { 'first': expr, 'second': False }

    def assert_is(self, first, second):
        """
        Test that first and second evaluate to the same object.
        """
        assert first is second, { 'first': first, 'second': second }

    def assert_is_not(self, first, second):
        """
        Test that first and second does not evaluate to the same object.
        """
        assert first is not second, { 'first': first, 'second': second }       

    def assert_is_none(self, expr):
        """
        Test that expr is None.
        """
        assert expr is None, { 'first': expr, 'second': None }

    def assert_is_not_none(self, expr):
        """
        Test that expr is not None.
        """
        assert expr is not None, { 'first': expr, 'second': None }

    def assert_in(self, first, second):
        """
        Test that first is in second.
        """
        assert first in second, { 'first': first, 'second': second }

    def assert_not_in(self, first, second):
        """
        Test that first is not in second.
        """
        assert first not in second, { 'first': first, 'second': second }

    def assert_is_instance(self, obj, cls):
        """
        Test that obj is an instance of cls.
        """
        assert isinstance(obj, cls), { 'first': obj, 'second': cls }

    def assert_not_is_instance(self, obj, cls):
        """
        Test that obj is not an instance of cls.
        """
        assert not isinstance(obj, cls), { 'first': obj, 'second': cls }

    def assert_raises(self, exception, callable, *args, **kwargs):
        """
        Test that an exception (specific) is raised when callable is
        called with any positional or keyword arguments. The test passes
        if exception is raised, is an error if another exception is 
        raised, or fails if no exception is raised.
        """
        try:
            callable(*args, **kwargs)
            assert False, { 'first': exception, 'second': { 'callable': callable, 'args': args, 'kwargs': kwargs } }
        except exception:
            assert True

    def assert_does_not_raises(self, exception, callable, *args, **kwargs):
        """
        Test that an exception (specific) is not raised when callable is
        called with any positional or keyword arguments. The test passes
        if exception is not raised, is an error if another exception is 
        raised, or fails if exception is raised.
        """
        try:
            callable(*args, **kwargs)
            assert True
        except exception:
            assert False, { 'first': exception, 'second': { 'callable': callable, 'args': args, 'kwargs': kwargs } }

    def assert_raises_regex(self, exception, regex, callable, *args, **kwargs):
        """
        Like assertRaises() but also tests that regex matches on the 
        string representation of the raised exception.
        """
        pattern = compile(regex)
        try:
            callable(*args, **kwargs)
            assert False, { 
            'first': exception, 
            'second': { 'callable': callable, 'args': args, 'kwargs': kwargs, 'regex': regex } }
        except exception as exc:
            assert pattern.match(exc), { 'expected': f'error message to match {regex}', 'received': exc } 

    def assert_almost_equal(self, first, second, places=7):
        """
        Test that first and second are approximately equal by computing
        the difference, rounding to the given number of decimal places
        (default 7), and comparing to zero. 
        """
        assert round(first-second, places) == 0, { 'first': first, 'second': second }

    def assert_not_almost_equal(self, first, second, places=7):
        """
        Test that first and second are not approximately equal by
        computing the difference, rounding to the given number of decimal
        places (default 7), and comparing to zero. 
        """
        assert round(first-second, places) != 0, { 'first': first, 'second': second }

    def assert_greater(self, first, second):
        """
        Test that first is > than the second. If not, the test will fail.
        """
        assert first > second, { 'first': first, 'second': second }

    def assert_greater_equal(self, first, second):
        """
        Test that first is >= than the second. If not, the test will fail.
        """
        assert first >= second, { 'first': first, 'second': second }

    def assert_less(self, first, second):
        """
        Test that first is < than the second. If not, the test will fail.
        """
        assert first < second, { 'first': first, 'second': second }

    def assert_less_equal(self, first, second):
        """
        Test that first is <= than the second. If not, the test will fail.
        """
        assert first <= second, { 'first': first, 'second': second }

    def assert_regex(self, text, regex):
        """
        Test that a regex search matches the text.
        """
        pattern = compile(regex)
        assert pattern.match(text), { 'first': text, 'second': regex }

    def assert_not_regex(self, text, regex):
        """
        Test that a regex search does not math the text.
        """
        pattern = compile(regex)
        assert not pattern.match(text), { 'first': text, 'second': regex }

    def assert_count_equal(self, first, second):
        """
        Test that sequence first contains the same elements as second,
        regardless of their order. Duplicates are not ignored.
        """
        diff, first, second = [], list(first), list(second)
        for item in first:
            if item in second: second.remove(item)
            else: diff.append(item)

        if second: diff.extend(second)

        assert not diff, { 'first': first, 'second': second }
        
    def assert_sequence_equal(self, first, second, seq_type=None):
        """
        Test that two sequences are equal. If a seq_type is supplied, 
        both first and second must be instances of seq_type or a failure
        will be raised.
        """
        if seq_type:
            assert first == second and type(first) == type(second) == seq_type, { 'first': first, 'second': second }
        else:
            assert first == second, { 'expected': first, 'received': second }

    def assert_list_equal(self, first, second):
        """
        Test that two lists are equal.
        """
        self.assert_sequence_equal(first, second, list)

    def assert_tuple_equal(self, first, second):
        """
        Test that two tuples are equal.
        """
        self.assert_sequence_equal(first, second, tuple)

    def assert_set_equal(self, first, second):
        """
        Test that two sets are equal.

        Fails if either of first or second does not have a 
        set.difference() method.
        """
        self.assert_sequence_equal(first, second, set)

    def assert_dict_equal(self, first, second):
        """
        Test that two dictionaries are equal.
        """
        self.assert_sequence_equal(first, second, dict)

    @classmethod
    def add_cleanup(cls, function, *args, **kwargs):
        """
        Add a function to be called after tearDown() to clean up resources
        used during the test. Functions will be called in reverse order to
        the order they are added (LIFO). They are called with any 
        arguments and keyword arguments passed into addCleanup when they 
        are added.

        If setUp() fails meaning that tearDown() is not called, then any 
        cleanup functions will still be called.
        """
        cls.clean_ups.append({
            'callable': function,
            'args': args,
            'kwargs': kwargs
        })

    @classmethod
    def do_cleanups(cls):
        """
        The method is called unconditionally after tearDown(), or after 
        setUp() if setUp() raises an exception.
        """
        for clean_up in cls.clean_ups:
            callable = clean_up['callable']
            args = clean_up['args']
            kwargs = clean_up['kwargs']
            
            callable(*args, **kwargs)
   
