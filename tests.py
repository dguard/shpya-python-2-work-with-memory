import unittest


class TestMemory(unittest.TestCase):

    def test_number_is_immutable_type(self):
        num = 123
        num_id = id(num)
        num = 1

        self.assertNotEqual(num_id, id(num))

    def test_number_is_not_passed_by_reference_to_function(self):
        num = 123
        num_id = id(num)

        def add_1(n):
            n += 1
        add_1(num)

        self.assertEqual(num_id, id(num))

    def test_string_is_immutable_type(self):
        string = "first"
        string_id = id(string)
        string = "second"

        self.assertNotEqual(string_id, id(string))

    def test_string_is_not_passed_by_reference_to_function(self):
        string = "first"
        string_id = id(string)

        def add_a(s):
            s += "a"
        add_a(string)

        self.assertEqual(string_id, id(string))

    def test_tuple_is_immutable_type(self):
        _typle = (1, 2, 3)
        id_typle = id(_typle)

        _typle = _typle.__add__((1, 2, 3))

        self.assertNotEqual(id_typle, id(_typle))

    def test_tuple_is_not_passed_by_reference_to_function(self):
        _typle = (1, 2, 3)
        id_typle = id(_typle)

        def add_typle(_t):
            _t = _t.__add__((3, 4, 5))
        add_typle(_typle)

        self.assertEqual(id_typle, id(_typle))

    def test_list_is_not_immutable_type(self):
        _list = [1, 2, 3]
        id_list = id(_list)

        _list.append(4)

        self.assertEqual(id_list, id(_list))

    def test_list_is_passed_by_reference_to_function(self):
        _list = [1, 2, 3]
        id_list = id(_list)

        def append_1(l):
            l.append(1)
        append_1(_list)

        self.assertEqual(id_list, id(_list))

    def test_dictionary_is_not_immutable_type(self):
        _dict = {'a': 1, 'b': 2, 'c': 3}
        id_dict = id(_dict)

        _dict['d'] = 4

        self.assertEqual(id_dict, id(_dict))

    def test_dictionary_is_passed_by_reference_to_function(self):
        _dict = {'a': 1, 'b': 2, 'c': 3}
        id_dict = id(_dict)

        def add_d(d):
            d['d'] = 4
        add_d(_dict)

        self.assertEqual(id_dict, id(_dict))

    def test_set_is_not_immutable_type(self):
        _set = set(['1', '2', '3'])  # same as {'1','2','3'}
        id_set = id(_set)
        _set.add('4')
        self.assertEqual(id_set, id(_set))

    def test_set_is_passed_by_reference_to_function(self):
        _set = set(['1', '2', '3'])  # same as {'1','2','3'}
        id_set = id(_set)

        def add_4(s):
            s.add('4')
        add_4(_set)

        self.assertEqual(id_set, id(_set))

    def test_object_is_not_immutable_type(self):
        class TestObj(object):
            field = 1

        obj = TestObj()
        obj_id = id(obj)

        obj.field = 2

        self.assertEqual(obj_id, id(obj))

    def test_object_is_passed_by_reference_to_function(self):
        class TestObj(object):
            field = 1

        obj = TestObj()
        obj_id = id(obj)

        def change_field_to_2(_obj):
            _obj.field = 2
        change_field_to_2(obj)

        self.assertEqual(obj_id, id(obj))

    def test_object_does_not_change_after_passing_to_another_variable_and_changing_field(self):
        class TestObj(object):
            field = 1

        obj = TestObj()
        obj_id = id(obj)

        obj2 = obj
        obj2.field = 2

        self.assertEqual(obj.field, obj2.field)
        self.assertEqual(obj_id, id(obj2))

if __name__ == '__main__':
    unittest.main()