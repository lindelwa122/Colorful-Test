from sys import path as sys_path
from os import path as os_path

sys_path.append(os_path.abspath(os_path.join(os_path.dirname(__file__), '..')))

from colorful_test.testcase import TestCase

class TestTestCase(TestCase):
    def handle_exc(self, exception, callable, *args, **kwargs):
        try:
            callable(*args, **kwargs)
        except exception:
            return 

        raise AssertionError
    
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
        self.handle_exc(AssertionError, self.assert_raises, ValueError, does_not_raise_error)
        
        def raises_an_unexpected_error():
            raise IndexError()
        
        self.handle_exc(IndexError, self.assert_raises, ValueError, raises_an_unexpected_error)
    
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
        self.handle_exc(AssertionError, self.assert_equal, 1, 2)
        self.handle_exc(AssertionError, self.assert_equal, [1, 2], [2, 1])
        self.handle_exc(AssertionError, self.assert_equal, { 'key': 1 }, { 'key': 2 })
        self.handle_exc(AssertionError, self.assert_equal, False, -1)
        self.handle_exc(AssertionError, self.assert_equal, None, False)
        self.handle_exc(AssertionError, self.assert_equal, None, 0)

    def test_assert_not_equal_pass_4(self):
        # Simple comparisons
        self.assert_not_equal(1, 2)
        self.assert_not_equal('hello', 'Hello')
        self.assert_not_equal([1, 2, 3], [3, 2, 1])
        self.assert_not_equal((1, 2), (2, 1))
        self.assert_not_equal({ 'key': 'value' }, { 'key': 'same value' })

        # Boolean comparisons
        self.assert_not_equal(False, True)
        self.assert_not_equal(True, False)
        self.assert_not_equal(True, 0)
        self.assert_not_equal(False, 1)

        # Complex data structures
        self.assert_not_equal({ 'a': [1, 2] }, { 'a': [1, 3] })
        self.assert_not_equal([], [1])
        self.assert_not_equal({}, { 'key': '' })
        self.assert_not_equal(set(), {'not empty'})
        self.assert_not_equal(tuple(), (1,))
        
    def test_assert_not_equal_fail_5(self):
        self.handle_exc(AssertionError, self.assert_not_equal, 1, 1)
        self.handle_exc(AssertionError, self.assert_not_equal, [1, 2], [1, 2])
        self.handle_exc(AssertionError, self.assert_not_equal, { 'key': 1 }, { 'key': 1 })
        
    def test_assert_true_pass_6(self):
        self.assert_true(True)
        self.assert_true(1)
        self.assert_true(-5)
        self.assert_true('hello')
        self.assert_true([1, 2])
        self.assert_true((0,))
        self.assert_true({ 'key': 'value' })

    def test_assert_true_fail_7(self):
        self.handle_exc(AssertionError, self.assert_true, False)
        self.handle_exc(AssertionError, self.assert_true, 0)
        self.handle_exc(AssertionError, self.assert_true, '')
        self.handle_exc(AssertionError, self.assert_true, [])
        self.handle_exc(AssertionError, self.assert_true, {})
        self.handle_exc(AssertionError, self.assert_true, set())

    def test_assert_false_pass_8(self):
        self.assert_false(False)
        self.assert_false(0),
        self.assert_false('')
        self.assert_false([])
        self.assert_false({})
        self.assert_false(tuple())
        self.assert_false(set())

    def test_assert_false_fail_9(self):
        self.handle_exc(AssertionError, self.assert_false, True)
        self.handle_exc(AssertionError, self.assert_false, 1)
        self.handle_exc(AssertionError, self.assert_false, -5)
        self.handle_exc(AssertionError, self.assert_false, 'hello')
        self.handle_exc(AssertionError, self.assert_false, [1, 2])
        self.handle_exc(AssertionError, self.assert_false, (0,))
        self.handle_exc(AssertionError, self.assert_false, { 'key': 'value' })

    def test_assert_is_pass_10(self):
        a = [1, 2, 3]
        b = a
        self.assert_is(a, b)

        x = 'hello'
        y = x
        self.assert_is(x, y)

        obj = object()
        self.assert_is(obj, obj)

    def test_assert_is_fail_11(self):
        self.handle_exc(AssertionError, self.assert_is, [1, 2, 3], [1, 2, 3])
        self.handle_exc(AssertionError, self.assert_is, 'hello', 'world')
        self.handle_exc(AssertionError, self.assert_is, 42, 43)
        self.handle_exc(AssertionError, self.assert_is, None, 0)
        self.handle_exc(AssertionError, self.assert_is, {}, {})
        self.handle_exc(AssertionError, self.assert_is, set(), set())

    def test_assert_is_not_pass_12(self):
        self.assert_is_not([1, 2, 3], [1, 2, 3])
        self.assert_is_not('hello', 'world')
        self.assert_is_not(42, 43)
        self.assert_is_not(None, 0)
        self.assert_is_not({}, {})
        self.assert_is_not(set(), set())

    def test_assert_is_not_fail_13(self):
        a = [1, 2, 3]
        b = a
        self.handle_exc(AssertionError, self.assert_is_not, a, b)

        x = 'hello'
        y = x
        self.handle_exc(AssertionError, self.assert_is_not, x, y)

        obj = object()
        self.handle_exc(AssertionError, self.assert_is_not, obj, obj)

    def test_assert_is_none_pass_14(self):
        self.assert_is_none(None)

        a = None
        self.assert_is_none(a)

        def fun():
            x = 5
        self.assert_is_none(fun())

    def test_assert_is_none_fail_15(self):
        self.handle_exc(AssertionError, self.assert_is_none, 0)
        self.handle_exc(AssertionError, self.assert_is_none, '')
        self.handle_exc(AssertionError, self.assert_is_none, [])
        self.handle_exc(AssertionError, self.assert_is_none, {})
        self.handle_exc(AssertionError, self.assert_is_none, False)
        self.handle_exc(AssertionError, self.assert_is_none, 'None')
        self.handle_exc(AssertionError, self.assert_is_none, object())

    def test_assert_is_not_none_pass_16(self):
        self.assert_is_not_none(0)
        self.assert_is_not_none('')
        self.assert_is_not_none([])
        self.assert_is_not_none({})
        self.assert_is_not_none('None')
        self.assert_is_not_none(object())

    def test_assert_is_not_none_fail_17(self):
        self.handle_exc(AssertionError, self.assert_is_not_none, None)

        a = None
        self.handle_exc(AssertionError, self.assert_is_not_none, a)

        def fun():
            x = 5
        self.handle_exc(AssertionError, self.assert_is_not_none, fun())

    def test_assert_in_pass_18(self):
        self.assert_in(1, [1, 2, 3])
        self.assert_in('a', 'apple')
        self.assert_in('key', { 'key': 'value' })
        self.assert_in(6, {5, 6, 7})
        self.assert_in(5, (3, 4, 5))

    def test_assert_in_fail_19(self):
        self.handle_exc(AssertionError, self.assert_in, 4, [1, 2, 3])
        self.handle_exc(AssertionError, self.assert_in, 'z', 'apple')
        self.handle_exc(AssertionError, self.assert_in, 'value', { 'key': 'value' })
        self.handle_exc(AssertionError, self.assert_in, 8, {5, 6, 7})
        self.handle_exc(AssertionError, self.assert_in, 9, (3, 4, 5))
        self.handle_exc(AssertionError, self.assert_in, None, [])
        
    def test_assert_not_in_pass_20(self):
        self.assert_not_in(4, [1, 2, 3])
        self.assert_not_in('z', 'apple')
        self.assert_not_in('value', { 'key': 'value' })
        self.assert_not_in(8, {5, 6, 7})
        self.assert_not_in(9, (3, 4, 5))
        self.assert_not_in(None, [])

    def test_assert_not_in_fail_21(self):
        self.handle_exc(AssertionError, self.assert_not_in, 1, [1, 2, 3])
        self.handle_exc(AssertionError, self.assert_not_in, 'a', 'apple')
        self.handle_exc(AssertionError, self.assert_not_in, 'key', { 'key': 'value' })
        self.handle_exc(AssertionError, self.assert_not_in, 6, {5, 6, 7})
        self.handle_exc(AssertionError, self.assert_not_in, 5, (3, 4, 5))

    def test_assert_is_instance_pass_22(self):
        self.assert_is_instance(42, int)
        self.assert_is_instance(3.14, float)
        self.assert_is_instance('hello', str)
        self.assert_is_instance([1, 2, 3], list)
        self.assert_is_instance((1, 2, 3), tuple)
        self.assert_is_instance({1, 2, 3}, set)
        self.assert_is_instance({ 'k': 'v' }, dict)
        self.assert_is_instance(None, type(None))
        self.assert_is_instance(True, bool)
        self.assert_is_instance(ValueError(), Exception)

        class Example:
            pass

        example = Example()
        self.assert_is_instance(example, Example)

    def test_assert_is_instance_fail_23(self):
        self.handle_exc(AssertionError, self.assert_is_instance, 42, str)
        self.handle_exc(AssertionError, self.assert_is_instance, 3.14, int)
        self.handle_exc(AssertionError, self.assert_is_instance, 'hello', list)
        self.handle_exc(AssertionError, self.assert_is_instance, [1, 2, 3], dict)
        self.handle_exc(AssertionError, self.assert_is_instance, { 'k': 'v' }, list)
        self.handle_exc(AssertionError, self.assert_is_instance, None, int)
        self.handle_exc(AssertionError, self.assert_is_instance, True, Exception)
        self.handle_exc(AssertionError, self.assert_is_instance, ZeroDivisionError(), bool)

    def test_assert_not_is_instance_pass_24(self):
        self.assert_not_is_instance(42, str)
        self.assert_not_is_instance(3.14, int)
        self.assert_not_is_instance('hello', list)
        self.assert_not_is_instance([1, 2, 3], dict)
        self.assert_not_is_instance({ 'k': 'v' }, list)
        self.assert_not_is_instance(None, int)
        self.assert_not_is_instance(True, Exception)
        self.assert_not_is_instance(ZeroDivisionError(), bool)

    def test_assert_not_is_instance_fail_25(self):
        self.handle_exc(AssertionError, self.assert_not_is_instance, 42, int)
        self.handle_exc(AssertionError, self.assert_not_is_instance, 3.14, float)
        self.handle_exc(AssertionError, self.assert_not_is_instance, 'hello', str)
        self.handle_exc(AssertionError, self.assert_not_is_instance, [1, 2, 3], list)
        self.handle_exc(AssertionError, self.assert_not_is_instance, (1, 2, 3), tuple)
        self.handle_exc(AssertionError, self.assert_not_is_instance, {1, 2, 3}, set)
        self.handle_exc(AssertionError, self.assert_not_is_instance, { 'k': 'v' }, dict)
        self.handle_exc(AssertionError, self.assert_not_is_instance, None, type(None))
        self.handle_exc(AssertionError, self.assert_not_is_instance, True, bool)
        self.handle_exc(AssertionError, self.assert_not_is_instance, ValueError(), Exception)

        class Example:
            pass

        example = Example()
        self.handle_exc(AssertionError, self.assert_not_is_instance, example, Example)

    def test_assert_does_not_raises_fail_28(self):
        # Simple error raised
        def raises_value_error(x):
            if x < 0:
                raise ValueError()

        self.handle_exc(AssertionError, self.assert_does_not_raises, ValueError, raises_value_error, -1)   
        
        def raises_index_error(*args):
            if len(args) > 4:
                raise IndexError()
            
        self.handle_exc(AssertionError, self.assert_does_not_raises, IndexError, raises_index_error, 1, 2, 3, 4, 5)   
        
        # Custom error raised
        class CustomError(Exception): pass
        
        def raises_custom_error():
            raise CustomError()
        
        self.handle_exc(AssertionError, self.assert_does_not_raises, CustomError, raises_custom_error)   
        
        # Error raised in a nested function
        def inner_function(x):
            if not isinstance(x, int):
                raise TypeError('i was expecting an int')
            
        def outer_function(x):
            inner_function(x)
            
        self.handle_exc(AssertionError, self.assert_does_not_raises, TypeError, outer_function, '0')   
        
    def test_assert_does_not_raises_pass_27(self):
        # Does not raise an error
        def does_not_raise_error():
            x = 5
            return x + 1
        
        self.assert_does_not_raises(ZeroDivisionError, does_not_raise_error)
        self.assert_does_not_raises(Exception, does_not_raise_error)
        self.assert_does_not_raises(ValueError, does_not_raise_error)

    def test_assert_almost_equal_pass_28(self):
        self.assert_almost_equal(3.14159, 3.1416, places=4)
        self.assert_almost_equal(1.000001, 1.000002, places=5)
        self.assert_almost_equal(-5.4321, -5.43210001)
        self.assert_almost_equal(0.0, 0.0000001, places=6)
        self.assert_almost_equal(100, 100.001, places=0)
        
    def test_assert_almost_equal_fail_29(self):
        self.handle_exc(AssertionError, self.assert_almost_equal, 3.14159, 3.1415, places=5)
        self.handle_exc(AssertionError, self.assert_almost_equal, 1.0001, 1.0002, places=4)
        self.handle_exc(AssertionError, self.assert_almost_equal, -5.0, -5.01)
        self.handle_exc(AssertionError, self.assert_almost_equal, 0.0, 0.001, places=3)
        self.handle_exc(AssertionError, self.assert_almost_equal, 42, 43)
        
    def test_assert_not_almost_equal_pass_30(self):
        self.assert_not_almost_equal(3.14159, 3.1415, places=5)
        self.assert_not_almost_equal(1.0001, 1.0002, places=4)
        self.assert_not_almost_equal(-5.0, -5.01)
        self.assert_not_almost_equal(0.0, 0.001, places=3)
        self.assert_not_almost_equal(42, 43)
        
    def test_assert_not_almost_equal_fail_31(self):
        self.handle_exc(AssertionError, self.assert_not_almost_equal, 3.14159, 3.1416, places=4)
        self.handle_exc(AssertionError, self.assert_not_almost_equal, 1.000001, 1.000002, places=5)
        self.handle_exc(AssertionError, self.assert_not_almost_equal, -5.4321, -5.43210001)
        self.handle_exc(AssertionError, self.assert_not_almost_equal, 0.0, 0.0000001, places=6)
        self.handle_exc(AssertionError, self.assert_not_almost_equal, 100, 100.001, places=0)
        
    def test_assert_greater_pass_32(self):
        self.assert_greater(5, 3)
        self.assert_greater(10.5, 7.2)
        self.assert_greater(3.1456, 3.1453)
        self.assert_greater(0, -1)
        self.assert_greater('b', 'a')
        self.assert_greater([2, 1], [1, 2])
        self.assert_greater([1, 2, 3], [1, 2])
        
    def test_assert_greater_fail_33(self):
        self.handle_exc(AssertionError, self.assert_greater, 3, 5)
        self.handle_exc(AssertionError, self.assert_greater, 7.2, 10.5)
        self.handle_exc(AssertionError, self.assert_greater, -5, -1)
        self.handle_exc(AssertionError, self.assert_greater, -1, 0)
        self.handle_exc(AssertionError, self.assert_greater, 'a', 'b')
        self.handle_exc(AssertionError, self.assert_greater, [1, 2], [1, 2, 3])
        
    def test_assert_less_pass_34(self):
        self.assert_less(3, 5)
        self.assert_less(7.2, 10.5)
        self.assert_less(-5, -1)
        self.assert_less(-1, 0)
        self.assert_less('a', 'b')
        self.assert_less([1, 2], [1, 2, 3])
        
    def test_assert_less_fail_35(self):
        self.handle_exc(AssertionError, self.assert_less, 5, 3)
        self.handle_exc(AssertionError, self.assert_less, 10.5, 7.2)
        self.handle_exc(AssertionError, self.assert_less, 3.1456, 3.1453)
        self.handle_exc(AssertionError, self.assert_less, 0, -1)
        self.handle_exc(AssertionError, self.assert_less, 'b', 'a')
        self.handle_exc(AssertionError, self.assert_less, [2, 1], [1, 2])
        self.handle_exc(AssertionError, self.assert_less, [1, 2, 3], [1, 2])
        
    def test_assert_greater_equal_pass_36(self):
        self.assert_greater_equal(5, 3)
        self.assert_greater_equal(5, 5)
        self.assert_greater_equal(10.5, 7.2)
        self.assert_greater_equal(10, 10.0)
        self.assert_greater_equal(-1, -5)
        self.assert_greater_equal(-5, -5)
        self.assert_greater_equal(0, -1)
        self.assert_greater_equal('b', 'a')
        self.assert_greater_equal('b', 'b')
        self.assert_greater_equal([1, 2, 3], [1, 2])
        self.assert_greater_equal([1, 2, 3], [1, 2, 3])
        
    def test_assert_greater_equal_fail_37(self):
        self.handle_exc(AssertionError, self.assert_greater_equal, 3, 5)
        self.handle_exc(AssertionError, self.assert_greater_equal, 7.2, 10.5)
        self.handle_exc(AssertionError, self.assert_greater_equal, -5, -1)
        self.handle_exc(AssertionError, self.assert_greater_equal, -2, -1)
        self.handle_exc(AssertionError, self.assert_greater_equal, 'a', 'b')
        self.handle_exc(AssertionError, self.assert_greater_equal, [1, 2], [1, 2, 3])
        
    def test_assert_less_equal_pass_38(self):
        self.assert_less_equal(3, 5)
        self.assert_less_equal(5, 5)
        self.assert_less_equal(7.2, 10.5)
        self.assert_less_equal(10.0, 10)
        self.assert_less_equal(-5, -1)
        self.assert_less_equal(-5, -5)
        self.assert_less_equal(-2, -1)
        self.assert_less_equal('a', 'b')
        self.assert_less_equal('a', 'a')
        self.assert_less_equal([1, 2], [1, 2, 3])
        self.assert_less_equal([1, 2, 3], [1, 2, 3])
        
    def test_assert_less_equal_fail_39(self):
        self.handle_exc(AssertionError, self.assert_less_equal, 5, 3)
        self.handle_exc(AssertionError, self.assert_less_equal, 10.5, 7.2)
        self.handle_exc(AssertionError, self.assert_less_equal, -1, -5)
        self.handle_exc(AssertionError, self.assert_less_equal, 0, -1)
        self.handle_exc(AssertionError, self.assert_less_equal, 'b', 'a')
        self.handle_exc(AssertionError, self.assert_less_equal, [1, 2, 3], [1, 2])
        
    def test_assert_regex_pass_40(self):
        self.assert_regex('hello', r'hello')
        self.assert_regex('12345', r'\d+')
        self.assert_regex('abc_def', r'abc_\w+')
        self.assert_regex('hello123', r'hello\d+')
        self.assert_regex('aBc', r'[a-zA-Z]+')
        self.assert_regex('2023-01-10', r'\d{4}-\d{2}-\d{2}')
        
    def test_assert_regex_fail_41(self):
        self.handle_exc(AssertionError, self.assert_regex, 'goodbye world', r'hello')
        self.handle_exc(AssertionError, self.assert_regex, 'abc123', r'^\d+$')
        self.handle_exc(AssertionError, self.assert_regex, '2003/01/10', r'\d{4}-\d{2}-\d{2}')
        self.handle_exc(AssertionError, self.assert_regex, 'HELLO', r'^hello$')
        self.handle_exc(AssertionError, self.assert_regex, '', r'.+')
        
    def test_assert_not_regex_pass_42(self):
        self.assert_not_regex('goodbye world', r'hello')
        self.assert_not_regex('abc123', r'^\d+$')
        self.assert_not_regex('2003/01/10', r'\d{4}-\d{2}-\d{2}')
        self.assert_not_regex('HELLO', r'^hello$')
        self.assert_not_regex('', r'.+')
        
    def test_assert_not_regex_fail_43(self):
        self.handle_exc(AssertionError, self.assert_not_regex, 'hello', r'hello')
        self.handle_exc(AssertionError, self.assert_not_regex, '12345', r'\d+')
        self.handle_exc(AssertionError, self.assert_not_regex, 'abc_def', r'abc_\w+')
        self.handle_exc(AssertionError, self.assert_not_regex, 'hello123', r'hello\d+')
        self.handle_exc(AssertionError, self.assert_not_regex, 'aBc', r'[a-zA-Z]+')
        self.handle_exc(AssertionError, self.assert_not_regex, '2023-01-10', r'\d{4}-\d{2}-\d{2}')
        
    def test_assert_count_equal_pass_44(self):
        self.assert_count_equal([1, 2, 3], [1, 2, 3])
        self.assert_count_equal([1, 2, 2], [2, 1, 2])
        self.assert_count_equal([], [])
        self.assert_count_equal('abc', 'cab')
        self.assert_count_equal((1, 2, 3), (3, 2, 1))
        self.assert_count_equal({1: 'a', 2: 'b', 3: 'c'}, {3: 'c', 1: 'a', 2: 'b'})
        self.assert_count_equal([True, False, True], [False, True, True])
        self.assert_count_equal([1, 'a', 2.1], ['a', 2.1, 1])
        self.assert_count_equal([1, 2, 3], (1, 2, 3))
        
    def test_assert_count_equal_fail_45(self):
        self.handle_exc(AssertionError, self.assert_count_equal, [1, 2, 3], [1, 2])
        self.handle_exc(AssertionError, self.assert_count_equal, [1, 2, 2], [1, 2, 3])
        self.handle_exc(AssertionError, self.assert_count_equal, 'abc', 'abcd')
        self.handle_exc(AssertionError, self.assert_count_equal, ['a', 'b', 'c', 'd'], ['a', 'c', 'b'])
        self.handle_exc(AssertionError, self.assert_count_equal, [1, 2, 3], [1, 2, 3, 2])
        
    def test_assert_sequence_equal_pass_46(self):
        self.assert_sequence_equal([1, 2, 3], (1, 2, 3))
        self.assert_sequence_equal([1, 2, 3], [1, 2, 3])
        self.assert_sequence_equal('hello', 'hello')
        self.assert_sequence_equal((1, 2, 3), (1, 2, 3))
        self.assert_sequence_equal([], [])
        self.assert_sequence_equal([True, False], [True, False])
        self.assert_sequence_equal(['a', 1, 2.0], ['a', 1, 2.0])
        
    def test_assert_sequence_equal_fail_47(self):
        self.handle_exc(AssertionError, self.assert_sequence_equal, [1, 2, 3], [3, 2, 1])
        self.handle_exc(AssertionError, self.assert_sequence_equal, [1, 2, 3], [1, 2])
        self.handle_exc(AssertionError, self.assert_sequence_equal, 'hello', 'helo')
        self.handle_exc(AssertionError, self.assert_sequence_equal, (1, 2, 3), (1, 2, 4))
        self.handle_exc(AssertionError, self.assert_sequence_equal, ['a', 1, 2.0], ('a', 1, 3.0))
        self.handle_exc(AssertionError, self.assert_sequence_equal, 'abc', 'ab')
        
    def test_assert_raises_regex_pass_48(self):
        def raise_value_error():
            raise ValueError('This is an example error message')
        
        def raise_type_error():
            raise TypeError('Invalid type provided: expected int, got str')
        
        def raise_custom_error():
            raise RuntimeError('Critical system failure: Code 500')
        
        self.assert_raises_regex(ValueError, r'.*example error.*', raise_value_error)
        self.assert_raises_regex(TypeError, r'.*expected int.*', raise_type_error)
        self.assert_raises_regex(RuntimeError, r'.*Code \d+.*', raise_custom_error)
        
    def test_assert_raises_regex_fail_49(self):
        def raise_value_error():
            raise ValueError('This is an example error message boohoo')
        
        self.handle_exc(AssertionError, self.assert_raises_regex, KeyError, r'.*some key error.*', raise_value_error)
        self.handle_exc(AssertionError, self.assert_raises_regex, ValueError, r'.*wrong message.*', raise_value_error)
        self.handle_exc(AssertionError, self.assert_raises_regex, ValueError, r'.*example error.*', lambda: None)
        self.handle_exc(AssertionError, self.assert_raises_regex, ValueError, r'example error', raise_value_error)
        
        
    @classmethod
    def set_up_class(cls):
        cls.variable = 'setting up class'
        return super().set_up_class()
        
    def test_set_up_class_50(self):
        print(self.variable)
        
if __name__ == '__main__': 
    TestTestCase.run_and_output_results(fail_fast=False)
        