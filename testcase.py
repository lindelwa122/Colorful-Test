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
        pass

    def assertFalse(self, expr):
        """
        Test that expr is False.
        """
        pass

    def assertIs(self, first, second):
        """
        Test that first and second evaluate to the same object.
        """
        pass

    def assertIsNot(self, first, second):
        """
        Test that first and second does not evaluate to the same object.
        """
        pass

    def assertIsNone(self, expr):
        """
        Test that expr is None.
        """
        pass

    def assertIsNotNone(self, expr):
        """
        Test that expr is not None.
        """
        pass

    def assertIn(self, first, second):
        """
        Test that first is in second.
        """
        pass

    def assertNotIn(self, first, second):
        """
        Test that first is not in second.
        """
        pass

    def assertIsInstance(self, obj, cls):
        """
        Test that obj is an instance of cls.
        """
        pass

    def assertNotIsInstance(self, obj, cls):
        """
        Test that obj is not an instance of cls.
        """
        pass

    def assertRaises(self, exception, callable, *args, **kwargs):
        """
        Test that an exception (specific) is raised when callable is
        called with any positional or keyword arguments. The test passes
        if exception is raised, is an error if another exception is 
        raised, or fails if no exception is raised.
        """
        pass

    def assertDoesNotRaises(self, exception, callable, *args, **kwargs):
        """
        Test that an exception (specific) is not raised when callable is
        called with any positional or keyword arguments. The test passes
        if exception is not raised, is an error if another exception is 
        raised, or fails if exception is raised.
        """
        pass

    def assertRaisesRegex(self, exception, regex, callable, *args, **kwargs):
        """
        Like assertRaises() but also tests that regex matches on the 
        string representation of the raised exception.
        """
        pass

    def assertAlmostEqual(self, first, second, places=7):
        """
        Test that first and second are approximately equal by computing
        the difference, rounding to the given number of decimal places
        (default 7), and comparing to zero. 
        """
        pass

    def assertNotAlmostEqual(self, first, second, places=7):
        """
        Test that first and second are not approximately equal by
        computing the difference, rounding to the given number of decimal
        places (default 7), and comparing to zero. 
        """
        pass

    def assertGreater(self, first, second):
        """
        Test that first is > than the second. If not, the test will fail.
        """
        pass

    def assertGreaterEqual(self, first, second):
        """
        Test that first is >= than the second. If not, the test will fail.
        """
        pass

    def assertLess(self, first, second):
        """
        Test that first is < than the second. If not, the test will fail.
        """
        pass

    def assertLessEqual(self, first, second):
        """
        Test that first is <= than the second. If not, the test will fail.
        """
        pass

    def assertRegex(self, text, regex):
        """
        Test that a regex search matches the text.
        """
        pass

    def assertNotRegex(self, text, regex):
        """
        Test that a regex search does not math the text.
        """
        pass

    def assertCountEqual(self, first, second):
        """
        Test that sequence first contains the same elements as second,
        regardless of their order. Duplicates are not ignored.
        """
        pass

    def assertSequenceEqual(self, first, second, seq_type=None):
        """
        Test that two sequences are equal. If a seq_type is supplied, 
        both first and second must be instances of seq_type or a failure
        will be raised.
        """
        pass

    def assertListEqual(self, first, second):
        """
        Test that two lists are equal.
        """
        pass

    def assertTupleEqual(self, first, second):
        """
        Test that two tuples are equal.
        """
        pass

    def assertSetEqual(self, first, second):
        """
        Test that two sets are equal.

        Fails if either of first or second does not have a 
        set.difference() method.
        """
        pass

    def assertDictEqual(self, first, second):
        """
        Test that two dictionaries are equal.
        """
        pass

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
    