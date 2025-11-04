import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('HRDataset.csv')
ManagerName = data['name']
print(f"Manager Names:\n ManagerName")
ManagerID= data['employee_id']
print(f"Manager IDs:\n ManagerID")
PerformanceScore= data['performance_score']

print(f"Performance Scores:\n PerformanceScore")
RecruitmentSource= data['recruitment_source']
print(f"Recruitment Sources:\n RecrruitmentSource")
JobSeniority = data['job seniority']
print(f"Job seniority :\n JobSeniority")
MaritalDesc = data['marital_desc']
print(f"Marital Descriptions:\n MaritalDesc")
EmpSatisfaction = data['empsatisfaction']
plt.figure(figsize=(8,6))
plt.scatter("Zależność między bezpośrednim przełożonym pracownika a jego oceną wydajności pracy")
plt.scatter(ManagerName,ManagerID,PerformanceScore, color = 'red')
plt.xlabel("ManagerName and ManagerID")
plt.ylabel("PerformanceScore")
plt.title("Zależność między bezpośrednim przełożonym a jego oceną wydajności pracy z pracy")
plt.grid()
plt.show()
plt.figure(figsize=(8,6))
plt.scatter("Zależność między żródłem rekrutacji a najdłuższym stażem pracowników")
plt.scatter(RecruitmentSource, JobSeniority, color = green)
plt.xlabel("RecruitmentScore")
plt.ylabel("JobSeniority")
plt.tittle("Zależnośc między żródłem rekrutacji a najdłuższym stażem pracowników")
plt.grid()
plt.show()
plt.figure(figsize=(8,6))
plt.scatter("Zależność między stanem cywilnym pracowników a ich zadowoleniem z pracy")
plt.scatter(MaritalDesc,EmpSatisfaction, color = 'orange')
plt.xlabel("MaritalDesc")
plt.ylabel("EmpSatisfaction")
plt.title("Zależność między stanem cywilnym a ich zadowoeleniem z pracy")
plt.grid()
plt.show()
           



WorkersAge = data['age']
print(f"Workers Ages:\In WorkersAge")
plt.hist(WorkersAge, bins = 10, color = 'blue', edgecolor = 'black')
plt.xlabel("Age_of_workers")
plt.ylabel("Number_of_workers")
plt.title("Wiek pracowników w firmie")
plt.grid()
plt.show()
ProjectsCount = data['projects_count']
print(f"Projects Count:\n ProjectsCount")
plt.hist(ProjectsCount, bins =10, color = 'purple', edgecolor = 'black')
plt.xlabel("ProjectsCount")
plt.ylabel("Number_of_projects")
plt.title("Liczba projektów realizowanych przez pracowników")
plt.grid()
plt.show()




