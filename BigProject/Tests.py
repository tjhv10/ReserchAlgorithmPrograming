import unittest
from algorithm import Project, Doner, update_projects_support,find_project_index, get_project_names, reset_donations, calculate_total_initial_support,calculate_total_initial_support_doners, calculate_excess_support, select_max_excess_project, distribute_excess_support, cstv_budgeting
import random
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
        self.project_A.update_support([5, 10, 0, 0, 15])
        self.assertEqual(self.project_A.support, [5, 10, 0, 0, 15])

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
        self.project_A = Project("A", 27)
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
        self.project_A.update_support([5, 10, 0, 0, 15])
        updated_projects = reset_donations(self.projects, index)
        
        self.assertEqual(updated_projects[index].support, [0, 0, 0, 0, 0])

    def test_calculate_total_initial_support(self):
        i =0
        for project in self.projects:
            don =[]
            for j in range(0,len(self.doners)):
                don.append(self.doners[j].get_donations()[i])
            project.update_support(don)
            i+=1
        self.assertEqual(calculate_total_initial_support(self.projects), 100)

    def test_calculate_excess_support(self):
        i =0
        for project in self.projects:
            don =[]
            for j in range(0,len(self.doners)):
                don.append(self.doners[j].get_donations()[i])
            project.update_support(don)
            i+=1
        self.assertEqual(calculate_excess_support(self.project_A), 3)

    def test_select_max_excess_project(self):
        i =0
        for project in self.projects:
            don =[]
            for j in range(0,len(self.doners)):
                don.append(self.doners[j].get_donations()[i])
            project.update_support(don)
            i+=1
        max_excess_project, excess_support = select_max_excess_project(self.projects)
        self.assertEqual(max_excess_project.name, 'B')
        self.assertEqual(excess_support, 10)

    def test_cstv_budgeting_with_zero_budget(self):
        self.doner1.update_donations([0,0,0])
        self.doner2.update_donations([0,0,0])
        self.doner3.update_donations([0,0,0])
        self.doner4.update_donations([0,0,0])
        self.doner5.update_donations([0,0,0])
        self.projects = update_projects_support(self.projects,self.doners)
        selected_projects = cstv_budgeting(self.projects, self.doners)
        self.assertEqual(selected_projects, [])

    def test_cstv_budgeting_with_budget_less_than_min_project_cost(self):
        self.project_A.update_support([5, 0, 0, 0, 5])
        self.project_B.update_support([0, 0, 5, 0, 5])
        self.project_C.update_support([5, 0, 5,0, 0])
        selected_projects = cstv_budgeting(self.projects, self.doners)
        self.assertEqual(selected_projects, [])

    def test_cstv_budgeting_with_budget_greater_than_max_total_needed_support(self):
        self.project_A.update_support([10, 20, 0, 0, 30])
        self.project_B.update_support([20, 20, 30, 0, 10])
        self.project_C.update_support([10, 0, 10, 40, 0])
        selected_projects = cstv_budgeting(self.projects, self.doners)
        self.assertEqual(len(selected_projects), len(self.projects))
        self.assertEqual([project.name for project in selected_projects], ['B', 'A', 'C'])

    def test_cstv_budgeting_with_budget_between_min_and_max(self):
        self.project_A.update_support([5, 10, 0, 0, 15])
        self.project_B.update_support([10, 10, 15, 0, 5])
        self.project_C.update_support([5, 0, 5, 20, 0])
        selected_projects = cstv_budgeting(self.projects, self.doners)
        self.assertEqual(len(selected_projects), 2)
        self.assertEqual([project.name for project in selected_projects], ['B', 'A'])

    def test_cstv_budgeting_with_budget_exactly_matching_requierd_support(self):
        self.project_A.update_support([10, 20, 0, 0, 7])
        self.project_B.update_support([20, 10, 0, 0, 0])
        self.project_C.update_support([0, 0, 0, 25, 15])
        selected_projects = cstv_budgeting(self.projects, self.doners)
        self.assertEqual(len(selected_projects), 3)
        self.assertEqual([project.name for project in selected_projects], ['A', 'B', 'C'])

class TestCSTVBudgetingNonLegalInput(unittest.TestCase):
    def test_cstv_budgeting_non_legal_input(self):
        # Creating a list of projects with one of them being a string instead of a Project object
        projects = [Project("Project_1", 10), "Project_2"]
        
        # Creating a list of doners
        doners = [Doner([10, 20, 30]), Doner([5, 5, 5])]
        
        # Running the budgeting algorithm with non-legal input
        with self.assertRaises(TypeError):
            cstv_budgeting(projects, doners)

class TestCSTVBudgetingLargeInput(unittest.TestCase):
    def setUp(self):
        # Creating a large number of projects and doners
        num_projects = 100
        num_doners = 100
        self.projects = [Project(f"Project_{i}", 10) for i in range(num_projects)]
        self.doners = [Doner([1] * num_projects) for _ in range(num_doners)]

        # Assigning random support to projects from doners
        for doner in self.doners:
            for project in self.projects:
                project.update_support([1] * num_doners)

    def test_cstv_budgeting_large_input(self):
        # Running the budgeting algorithm with a large input
        selected_projects = cstv_budgeting(self.projects, self.doners)
        self.assertEqual(len(selected_projects), 100)
        self.assertEqual(len(selected_projects), len(self.projects))


class TestCSTVBudgetingLargeRandomInput(unittest.TestCase):
    def setUp(self):
        # Creating 100 projects with random costs between 10 and 100
        self.projects = [Project(f"Project_{i}", random.randint(10, 100)) for i in range(100)]
        # Creating 100 doners with random donations between 0 and 50 for each project
        self.doners = [Doner([random.randint(0, 50) for _ in range(len(self.projects))]) for _ in range(100)]
        
        # Assigning support for each project from the values of the doners
        self.projects = update_projects_support(self.projects,self.doners)
    def test_cstv_budgeting_large_random_input(self):
        cost = calculate_total_initial_support_doners(self.doners)
        # Running the budgeting algorithm with a budget of 10000
        selected_projects = cstv_budgeting(self.projects, self.doners)
        sum = 0
        for project in selected_projects:
            sum+= project.get_cost()

        # cost = calculate_total_initial_support(selected_projects)
        self.assertGreaterEqual(cost,sum)

if __name__ == '__main__':
    unittest.main()
