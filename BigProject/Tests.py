import unittest
from algorithm import Project, Doner, find_project_index, get_project_names, reset_donations, calculate_total_initial_support, calculate_excess_support, select_max_excess_project, distribute_excess_support, cstv_budgeting

class TestProject(unittest.TestCase):
    def setUp(self):
        self.project_A = Project("A", 37)
        self.project_B = Project("B", 30)
        self.project_C = Project("C", 40)
        self.doner1 = Doner([5, 10, 5])
        self.doner2 = Doner([10, 10, 0])
        self.doner3 = Doner([0, 15, 5])
        self.doner4 = Doner([0, 0, 20])
        self.doner5 = Doner([15, 5, 0])
        
    def test_add_support(self):
        self.project_A.add_support([5, 10, 0, 0, 15])
        self.assertEqual(self.project_A.supporters, [[5, 10, 0, 0, 15]])

    def test_get_name(self):
        self.assertEqual(self.project_A.get_name(), "A")

    def test_get_cost(self):
        self.assertEqual(self.project_A.get_cost(), 37)

    def test_find_project_index(self):
        projects = [self.project_A, self.project_B, self.project_C]
        self.assertEqual(find_project_index(projects, "B"), 1)
        self.assertEqual(find_project_index(projects, "D"), -1)

    def test_get_project_names(self):
        projects = [self.project_A, self.project_B, self.project_C]
        self.assertEqual(get_project_names(projects), ['A', 'B', 'C'])

class TestDoner(unittest.TestCase):
    def setUp(self):
        self.doner1 = Doner([5, 10, 5])
        self.doner2 = Doner([10, 10, 0])
        self.doner3 = Doner([0, 15, 5])
        self.doner4 = Doner([0, 0, 20])
        self.doner5 = Doner([15, 5, 0])

    def test_get_donations(self):
        self.assertEqual(self.doner1.get_donations(), [5, 10, 5])


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.project_A = Project("A", 37)
        self.project_B = Project("B", 30)
        self.project_C = Project("C", 40)
        self.doner1 = Doner([5, 10, 5])
        self.doner2 = Doner([10, 10, 0])
        self.doner3 = Doner([0, 15, 5])
        self.doner4 = Doner([0, 0, 20])
        self.doner5 = Doner([15, 5, 0])
        self.projects = [self.project_A, self.project_B, self.project_C]
        self.doners = [self.doner1, self.doner2, self.doner3, self.doner4, self.doner5]

    def test_reset_donations(self):
        index = 0
        self.project_A.add_support([5, 10, 0, 0, 15])
        updated_projects = reset_donations(self.projects, index)
        
        self.assertEqual(updated_projects[index].supporters, [[0, 0, 0, 0, 0]])

    def test_calculate_total_initial_support(self):
        self.project_A.add_support([5, 10, 0, 0, 15])
        self.project_B.add_support([10, 10, 15, 0, 5])
        self.project_C.add_support([5, 0, 5, 20, 0])
        self.assertEqual(calculate_total_initial_support(self.projects), 100)

    def test_calculate_excess_support(self):
        self.project_A.add_support([5, 10, 0, 0, 15])
        self.assertEqual(calculate_excess_support(self.project_A), -7)

    def test_select_max_excess_project(self):
        max_excess_project, excess_support = select_max_excess_project(self.projects)
        self.assertEqual(max_excess_project.name, 'B')
        self.assertEqual(excess_support, 10)
if __name__ == '__main__':
    unittest.main()
