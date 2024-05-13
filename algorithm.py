class Project:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.supporters = []

    def add_support(self, supporter):
        self.supporters.append(supporter)
    def get_name(self):
        return self.name
    def get_cost(self):
        return self.cost
    def __str__(self):
        supporter_strings = ", ".join(str(s) for s in self.supporters)
        return f"Project: {self.name}, Cost: {self.cost}, Initial Supporters: [{supporter_strings}]"
    
    
class Doner:
    def __init__(self, donations):
        self.donations = donations
    def get_donations(self):
        return self.donations
    


def find_project_index(projects, project_name):
        i =0
        for project in projects:
            if project == project_name:
                return i
            i+=1
        return -1

def get_project_names(projects):
    return [project.name for project in projects]

def reset_donations(projects, index):
    for project in projects:
        if project == projects[index]:
            for i in range(len(project.supporters)):
                project.supporters[i] = [0] * len(project.supporters[i])
    return projects


def cstv_budgeting(projects,doners, budget):
    selected_projects = []
    projectsnames =  get_project_names(projects)
    while True:
        excess_support = {}  # Stores excess support for each project
        total_initial_support = 0
        for project in projects:
            total_initial_support += sum(project.supporters[0])
        # Step 2: Choosing a project for funding
        for project in projects:
            excess = sum(project.supporters[0]) - project.cost
            excess_support[project] = excess
        if not any(excess_support.values()):
            break  # No project is eligible for funding
        max_excess_project = max(excess_support, key=excess_support.get)
        excess = excess_support.get(max_excess_project)
        if excess<0:
            break
        for project in projects:
            print(project.get_name(),project.supporters[0])
        selected_projects.append(max_excess_project)
        gama = max_excess_project.get_cost()/(excess+max_excess_project.get_cost())
        print("gama:",gama)  
        # Step 3: Distributing excess support
        for project, excess in excess_support.items():
            if project.get_name() != max_excess_project.get_name():
                for j,stam in enumerate(project.supporters[0]):
                    k = find_project_index(projectsnames,max_excess_project.get_name())
                    if doners[j].get_donations()[k]!=0:
                        project.supporters[0][j] = project.supporters[0][j]+project.supporters[0][j]*(1-gama)
        # Step 4: Adding selected project to funded projects list
        k = find_project_index(projectsnames,max_excess_project.get_name())
        projects = reset_donations(projects,k)
        for project in projects:
            print(project.get_name(),project.supporters[0])
        print("---------------")
        budget -= max_excess_project.cost
        # Step 6: Checking eligibility of remaining projects
        projects = [project for project in projects if project.cost <= budget]
        
        if not projects:
            break
    
    return selected_projects


# Example usage
project_A = Project("A", 1)
project_B = Project("B", 30)
project_C = Project("C", 42.7)
doner1 = Doner([5,10,5])
doner2 = Doner([10,10,0])
doner3 = Doner([0,15,5])
doner4 = Doner([0,0,20])
doner5 = Doner([15,5,0])
project_A.add_support([5, 10, 0 , 0, 15])
project_B.add_support([10, 10, 15, 0, 5])
project_C.add_support([5, 0, 5, 20, 0])

projects = [project_A, project_B, project_C]
doners = [doner1,doner2,doner3,doner4,doner5]


selected_projects = cstv_budgeting(projects,doners, 100)

for project in selected_projects:
    print(f"Selected Project: {project.name}, Cost: {project.cost}")

