from colorful_test.testcase import TestCase

class TestTestCase(TestCase):
    def handle_exc(exception, callable, *args, **kwargs):
        try:
            callable(*args, **kwargs)
        except exception:
            pass
    
    def test_assert_raises_pass_0(self):
        # Simple error raised
        def raises_value_error(x):
            if x < 0:
                raise ValueError()
            
        self.assert_raises(ValueError, raises_value_error, -1)
        
        def raises_index_error(*args):
            if len(args) > 4:
                raise IndexError()
            
        self.assert_raises(IndexError, raises_index_error, 1, 2, 3, 4, 5)
        
        # Custom error raised
        class CustomError(Exception): pass
        
        def raises_custom_error():
            raise CustomError()
        
        self.assert_raises(CustomError, raises_custom_error)
        
        # Error raised in a nested function
        def inner_function(x):
            if not isinstance(x, int):
                raise TypeError('i was expecting an int')
            
        def outer_function(x):
            inner_function(x)
            
        self.assert_raises(TypeError, outer_function, '0')
        
    def test_assert_raises_fail_1(self):
        # Does not raise an error
        def does_not_raise_error():
            x = 5
            return x + 1
        
        self.handle_exc(AssertionError, self.assert_raises, ZeroDivisionError, does_not_raise_error)
        
        try:
            self.assert_raises(ZeroDivisionError, does_not_raise_error)
        except AssertionError:
            pass
        
        try:
            self.assert_raises(Exception, does_not_raise_error)
        except AssertionError:
            pass
        
        def raises_an_unexpected_error():
            raise IndexError()
        
        try:
            self.assert_raises(ValueError, raises_an_unexpected_error)
        except IndexError:
            pass
    
    # Test that assert_equal doesn't raise any errors for these cases
    def test_assert_equal_pass_2(self):
        # Simple comparisons
        self.assert_equal(1, 1)
        self.assert_equal(5, 5.0)
        self.assert_equal('hello', 'hello')
        self.assert_equal([1, 2], [1, 2])
        
        # Boolean comparisons
        self.assert_equal(True, True)
        self.assert_equal(False, False)
        self.assert_equal(True, 1)
        self.assert_equal(False, 0)
        self.assert_equal(None, None)
        
        # Complex data structure comparisons
        self.assert_equal({ 'key': 'value'}, { 'key': 'value'})
        self.assert_equal((1, 2, 3), (1, 2, 3))
        self.assert_equal({'a': [1, 2], 'b': (3, 4)}, {'a': [1, 2], 'b': (3, 4)})
        
        # Same values, but different list objects
        a = [1, 2]
        b = a[:]
        self.assert_equal(a, b)
        
        # Empty collections
        self.assert_equal({}, {})
        self.assert_equal([], [])
        self.assert_equal(set(), set())
        
    def test_assert_equal_fail_3(self):
        # Simple comparisons
        try:
            self.assert_equal(1, 2)
        except:
            pass
        
        
        
        

if __name__ == '__main__': 
    TestTestCase.run_and_output_results(fail_fast=False)
        