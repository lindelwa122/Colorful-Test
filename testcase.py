from re import compile

class TestCase:
    """
    Base class that implements the interface needed by the runner to allow
    it do drive the tests, and methods that the test code can use to check 
    for and report various kinds of failures.    
    """

    def __init_subclass__(cls, **kwargs):
        cls.clean_ups = []
        super().__init_subclass__(**kwargs)

    def setUp(self):
        """
        This method is called immediately before calling a test method;
        other than AssertionError or SkipTest, any exception raised by
        this method will be considered an error rather than a test
        failure. The default implementation does nothing.
        """
        pass

    def tearDown(self):
        """
        This method is called immediately after calling a test method;
        other than AssertionError or SkipTest, any exception raised by
        this method will be considered an error rather than a test
        failure. This method will be executed only if setUp succeeds.
        The default implemantation does nothing.
        """
        pass

    @classmethod
    def setUpClass(cls):
        """
        This method is called before tests in an individual class run. The
        default implementation does nothing.
        """
        pass

    @classmethod
    def tearDownClass(cls):
        """
        This method is called after tests in an individual class run. The
        default implementation does nothing.
        """
        pass

    def run(self):
        """
        Run the tests, collecting the results into TestResult object. The
        result object is returned to run()'s caller.
        """
        pass

    def skipTest(self, reason):
        """
        Calling this during a test method or setUp() skips the current test.
        """
        pass

    def assertEqual(self, first, second):
        """
        Test that first and second are equal. If the values does not 
        compare, the test will fail.
        """
        pass

    def assertNotEqual(self, first, second):
        """
        Test that first and second are not equal. If the values do compare
        equal, the test will fail
        """
        pass

    def assertTrue(self, expr):
        """
        Test that expr is True.
        """
        assert bool(expr), { 'expected': True, 'received': bool(expr) }

    def assertFalse(self, expr):
        """
        Test that expr is False.
        """
        assert not bool(expr), { 'expected': False, 'received': bool(expr) }

    def assertIs(self, first, second):
        """
        Test that first and second evaluate to the same object.
        """
        assert first is second, { 'expected': f'{first} to be {second}', 'received': f'{first} is {type(first)}' }

    def assertIsNot(self, first, second):
        """
        Test that first and second does not evaluate to the same object.
        """
        assert first is not second, { 'expected': f'{first} to not be {second}', 'received': f'{first} is {second}' }       

    def assertIsNone(self, expr):
        """
        Test that expr is None.
        """
        assert expr is None, { 'expected': None, 'received': expr }

    def assertIsNotNone(self, expr):
        """
        Test that expr is not None.
        """
        assert expr is not None, { 'expected': 'anything other than None', 'received': None }

    def assertIn(self, first, second):
        """
        Test that first is in second.
        """
        assert first in second, { 'expected': f'{first} to be in {second}', 'received': f'{first} not in {second}' }

    def assertNotIn(self, first, second):
        """
        Test that first is not in second.
        """
        assert first not in second, { 'expected': f'{first} to be not in {second}', 'received': f'{first} in {second}' }

    def assertIsInstance(self, obj, cls):
        """
        Test that obj is an instance of cls.
        """
        assert isinstance(obj, cls), { 'expected': f'{obj} is an instance of {cls}', 'received': f'{obj} is not an instance of {cls}' }

    def assertNotIsInstance(self, obj, cls):
        """
        Test that obj is not an instance of cls.
        """
        assert not isinstance(obj, cls), { 'expected': f'{obj} is not an instance of {cls}', 'received': f'{obj} is an instance of {cls}' }

    def assertRaises(self, exception, callable, *args, **kwargs):
        """
        Test that an exception (specific) is raised when callable is
        called with any positional or keyword arguments. The test passes
        if exception is raised, is an error if another exception is 
        raised, or fails if no exception is raised.
        """
        try:
          callable(*args, **kwargs)
          assert False, { 'expected': f'{callable} to raise a/an {exception}', 'received': f'{exception} was not raised' }
        except exception:
          assert True

    def assertDoesNotRaises(self, exception, callable, *args, **kwargs):
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
          assert False, { 'expected': f'{callable} to not raise a/an {exception}', 'received': f'{exception} was raised' }

    def assertRaisesRegex(self, exception, regex, callable, *args, **kwargs):
        """
        Like assertRaises() but also tests that regex matches on the 
        string representation of the raised exception.
        """
        pattern = compile(regex)
        try:
          callable(*args, **kwargs)
          assert False, { 'expected': f'{callable} to raise a/an {exception}', 'received': f'{exception} was not raised' }
        except exception as exc:
          assert pattern.match(exc), { 'expected': f'error message to match {regex}', 'received': exc } 

    def assertAlmostEqual(self, first, second, places=7):
        """
        Test that first and second are approximately equal by computing
        the difference, rounding to the given number of decimal places
        (default 7), and comparing to zero. 
        """
        assert round(first-second, places) == 0, { 'expected': f'a diff of 0', 'received': f'a diff of {round(first-second, places)}' }

    def assertNotAlmostEqual(self, first, second, places=7):
        """
        Test that first and second are not approximately equal by
        computing the difference, rounding to the given number of decimal
        places (default 7), and comparing to zero. 
        """
        expected, received = 'a diff of not 0', 'a diff of 0' 
        assert round(first-second, places) != 0, { 'expected': expected, 'received': received }

    def assertGreater(self, first, second):
        """
        Test that first is > than the second. If not, the test will fail.
        """
        expected = f'{first} is greater than {second}' 
        received = f'{first} is not bigger than {second}'
        assert first > second, { 'expected': expected, 'received': received }

    def assertGreaterEqual(self, first, second):
        """
        Test that first is >= than the second. If not, the test will fail.
        """
        expected = f'{first} is greater or equal to {second}'
        received = f'{first} is not greater or equal to {second}'
        assert first >= second, { 'expected': expected, 'received': received }

    def assertLess(self, first, second):
        """
        Test that first is < than the second. If not, the test will fail.
        """
        expected = f'{first} is less than {second}'
        received = f'{first} is not less than {second}'
        assert first < second, { 'expected': expected, 'received': received }

    def assertLessEqual(self, first, second):
        """
        Test that first is <= than the second. If not, the test will fail.
        """
        expected = f'{first} is less than or equal to {second}'
        received = f'{first} is not less than or equal to {second}'
        assert first <= second, { 'expected': expected, 'received': received }

    def assertRegex(self, text, regex):
        """
        Test that a regex search matches the text.
        """
        pattern = compile(regex)
        expected = f'{text} to match {regex}'
        received = f'{text} does not match {regex}'
        assert pattern.match(text), { 'expected': expected, 'received': received }

    def assertNotRegex(self, text, regex):
        """
        Test that a regex search does not math the text.
        """
        pattern = compile(regex)
        expected = f'{text} to not match {regex}'
        received = f'{text} does match {regex}'
        assert not pattern.match(text), { 'expected': expected, 'received': received }

    def assertCountEqual(self, first, second):
        """
        Test that sequence first contains the same elements as second,
        regardless of their order. Duplicates are not ignored.
        """
        diff = []
        for item in first:
          if item in second: second.remove(item)
          elif: diff.append(item)

        if second: diff.extend(second)

        expected: f'{first} to contain the same elements as {second}'
        received: f'diff: {diff}'

        assert not diff, { 'expected': expected, 'received': received }

    def assertSequenceEqual(self, first, second, seq_type=None):
        """
        Test that two sequences are equal. If a seq_type is supplied, 
        both first and second must be instances of seq_type or a failure
        will be raised.
        """
        if seq_type:
          expected = f'{first} to be equal to {second}, and both types to be {seq_type}'
          received = f'{first}, {second} | types: {type(first)}, {type(second)}'
          assert first == second and type(first) == type(second) == seq_type, { 'expected': expected, 'received': received }
        else:
          assert first == second, { 'expected': first, 'received': second }

    def assertListEqual(self, first, second):
        """
        Test that two lists are equal.
        """
        self.assertSequenceEqual(first, second, list)

    def assertTupleEqual(self, first, second):
        """
        Test that two tuples are equal.
        """
        self.assertSequenceEqual(first, second, tuple)

    def assertSetEqual(self, first, second):
        """
        Test that two sets are equal.

        Fails if either of first or second does not have a 
        set.difference() method.
        """
        self.assertSequenceEqual(first, second, set)

    def assertDictEqual(self, first, second):
        """
        Test that two dictionaries are equal.
        """
        self.assertSequenceEqual(first, second, dict)

    @classmethod
    def addCleanup(cls, function, *args, **kwargs):
        """
        Add a function to be called after tearDown() to clean up resources
        used during the test. Functions will be called in reverse order to
        the order they are added (LIFO). They are called with any 
        arguments and keyword arguments passed into addCleanup when they 
        are added.

        If setUp() fails meaning that tearDown() is not called, then any 
        cleanup functions will still be called.
        """
        pass

    @classmethod
    def doCleanups(cls):
        """
        The method is called unconditionally after tearDown(), or after 
        setUp() if setUp() raises an exception.
        """
        pass
   
