import os
from google.colab import files
import io
from crewai import Task
from decouple import config
from crewai import Crew, Process
from textwrap import dedent
from agents import CustomAgents
from tasks import CustomTasks
# Set up environment variables
os.environ["OPENAI_API_KEY"] = "..."

class ProjectCrew:
    def __init__(self):
        self.agents = CustomAgents()
        self.tasks = CustomTasks()
    
    def run(self):
        # Initialize agents
        profile_analyzer=self.agents.profile_analyzer()
        weekly_task_generator=self.agents.weekly_task_generator()
        project_generator=self.agents.project_generator()
        student_matcher=self.agents.student_matcher()

        
  
        # Initialize tasks with respective agents and the user-provided business information
        analyze_profile = self.tasks.analyze_profile(profile_analyzer)
        create_project = self.tasks.create_project(project_generator)
        # Initialize tasks with respective agents and the user-provided business information
        analyze_profile = self.tasks.analyze_profile(profile_analyzer)
        #weekly_tasks = self.tasks.weekly_tasks(weekly_task_generator)
        create_project = self.tasks.create_project(project_generator)
        #assign_student_to_project_role = self.tasks.assign_student_to_project_role(student_matcher)
        weekly_tasks = Task(
            description=dedent("""\
                Generate a personalized weekly task for each student that was analyzed, consisting one of the four developmentally-aligned categories, prioritizing the one that the student has the most room for improvement:
                   1. Emotional Awareness 
                   2. Social/Environmental Awareness 
                   3. Talent-Based 
                   4. Academics-Based
                Each task: 
                   1. Must be suitable for the age group of the students;
                   2. Should consider the possible absence of resources and materials that the students from disadvantaged regions; 
                   3. Should be based on the student’s profile card and their profile analysis, which includes emotional state, communication style, hobbies, academic tendencies, and social-emotional skills;
                   4. Must be short enough for a student of the specified age group to finish within at most 7 days."""),
            agent=weekly_task_generator,
            context=[analyze_profile],
            expected_output=dedent("""\
                The Weekly Task Generator produces a task description from the following four personalized development task categories every week for each student. These tasks are based on the student’s individual profile card, which includes emotional status, communication style, interests, and academic preferences.
                Each week, the student receives one task from the four options below:
                    -Emotional Awareness Task – Encourages reflection on personal feelings and emotional triggers.
                    -Social/Environmental Awareness Task – Promotes critical thinking about the student’s community and surroundings.
                    -Talent-Based Task – Designed to activate the student’s strengths, hobbies, or dominant intelligences (e.g., artistic, verbal, spatial).
                    -Academics-Based Task - Designed to encourage the student to connect the concepts learned in the classroom with their daily life applications, prioritizing the subject at which the student is weakest. 
                Output Format: A structured text also containing:
                    -Task category
                    -Title
                    -Description
                    -Reflective question
                    -Detailed explanation of the expected output from the student
                    -Week identifier and student ID.""")   
        )

        assign_student_to_project_role = Task(
            description=dedent("""\
                Match a student to the most developmentally appropriate team role within a selected social impact project. Use student profile data (personality, academic strengths, emotional/social skills, interests) to determine the best fit."""),
            agent=student_matcher,
            context=[create_project, analyze_profile],
            expected_output=dedent("""\
                The Student Matcher assigns each student to the most appropriate team role according to the results of the analysis of the profile_analyzer agent within a given project that is created by the project_generator agent. It analyzes the student’s complete profile—including social-emotional skills, academic focus, personality traits, and interest areas—and matches them to a best-fit role in the project that will both support and stretch their abilities.

                Each output includes:
                    The student ID

                    The assigned project

                    The description of the role of each student 

                    A rationale based on profile data (e.g., “shows empathy and curiosity, suited to Researcher role”)

                """)
        )

        # Form the crew with defined agents and tasks
        crew = Crew(
            agents=[profile_analyzer, weekly_task_generator, project_generator, student_matcher],
            tasks=[analyze_profile, weekly_tasks, create_project, assign_student_to_project_role],
            delegation=True,
            verbose=True,
        )

        # Execute the crew to carry out the business automation project
        return crew.kickoff()

if __name__ == "__main__":
    print("Welcome to the Personalized Project Creation Crew Setup")
    print("------------------------------------------------")
    #business_info = input("Hello, please tell me about your business and the problems you would like to solve, or if you have questions about CrewAI ask away as well: ").strip()
    
    project_crew = ProjectCrew()
    result = project_crew.run()
    
    with open('project_crew_output.txt', 'w') as file:
        file.write("## Project Generation Results:\n")
        file.write("########################\n\n")
        file.write(result)
        file.write("\n########################\n")
    
    print("\n\n########################")
    print("## Here are the results of your project:")
    print("########################\n")
    print(result)
