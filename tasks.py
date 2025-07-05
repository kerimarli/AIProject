from crewai import Task
from textwrap import dedent
from agents import CustomAgents
agents = CustomAgents()

class CustomTasks:
    def __init__(self):
        # This method initializes any necessary variables or configurations if needed
        pass

    
    def analyze_profile(self, agent):
        """Task for generating a detailed and personal analysis of each student in a classroom and to identify their potential contributions ina group project."""
        return Task(
            description=dedent("""\
                You are assigned to analyze each student in detail and determine the potentially most appropriate project role for each student based on their profile data.

                Analyze the following characteristics for each student:
                - Personality and behavioral traits (communication style, etc.)
                - Social-emotional skills (empathy, cooperation, confidence)
                - Interests and curiosity (hobbies, creative tendencies, question frequency)
                - Academic tendencies (dominant intelligence type, favorite subjects, grades)
                - Teacher observations and self-reflection notes

                Suggest potential contributions of each student in a group project, appropriate to their age group.

                Provide a brief explanation for why the role(s) were chosen based on specific profile traits.
                               
                The students that you will analyze and their information are as follows, their scores on each category are OUT OF 5:
                               
                        1.     Name: Defne Aslan
                               Class: 4/B

                               Age: 10

                               Empathy: 3
                               Teamwork and Collaboration: 5
                               Confidence: 5
                               Inquisitiveness and curiosity: 4
                               Initiative: 5
                               Emotional Stability: 4
                               Responsibleness: 4
                               Decision-making: 4
                               Resilience Under Challenge: 4
                               Detail Orientation: 4
                               Creativity and Openness to New Ideas: 5
                               Discipline: 4
                               Strong Features: Academic Intelligence
                               Talent(s): Football
                               Hobby(s): Music
                               Favourite subject: Mathematics
                               Weakest subject: Turkish
                               Intelligence Type: Logical-Mathematical Intelligence
                               Open for Improvement: Diligence
                               Weekly Teacher Evaluation: Defne was well-performing in her classes. However, she needs to work on developing her empathy skills and emotional intelligence.
                               
                        2.     Name: İnci
                               Class: 4/B
                               StudentID: 21
                               Age: 9
  
                               Empathy: 4.5
                               Teamwork and Collaboration: 4
                               Confidence: 4
                               Inquisitiveness and Curiosity: 4
                               Initiative: 4
                               Determination and Perseverance: 3.5
                               Responsibleness: 4
                               Decision-making: 4
                               Resilience Under Challenge: 3.5
                               Detail Orientation: 3
                               Creativity and Openness to New Ideas: 4
                               Discipline: 4.5
                               Strong Features: Communication
                               Talent(s): Writing
                               Hobby(s): Reading Books
                               Favourite subject: Turkish
                               Weakest subject: Mathematics
                               Intelligence Type: Social Intelligence
                               Open for Improvement: Attention to detail
                               Weekly Teacher Evaluation: İnci is a good reader and writer, and she cares for her friends. But she must pay more attention to classes and should 

                        3.     Name: Aslı
                               Class: 4/A
                               StudentID: 14
                               Age: 10
  
                               Empathy: 3
                               Teamwork and Collaboration: 4.5
                               Confidence: 4
                               Inquisitiveness and Curiosity: 4
                               Initiative: 4
                               Determination and Perseverance: 4.5
                               Responsibleness: 4.5
                               Decision-making: 4
                               Resilience Under Challenge: 3.5
                               Detail Orientation: 4
                               Creativity and Openness to New Ideas: 5
                               Discipline: 4.5
                               Strong Features: Visual and artistic intelligence
                               Talent(s): Drawing
                               Hobby(s): Arts
                               Favourite subject: Visual Arts
                               Weakest subject: Natural Sciences
                               Intelligence Type: Visual spatial intelligence
                               Open for Improvement: Friendship Relationships
                               Weekly Teacher Evaluation: Aslı demonstrated strong creativity and perseverance this week, especially in visual arts activities and group work. She is encouraged to strengthen her friendship skills by engaging more openly with classmates during collaborative tasks.
                        
                        4.     Name: Selim
                               Class: 4/B
                               StudentID: 17
                               Age: 9
  
                               Empathy: 3.5
                               Teamwork and Collaboration: 4.5
                               Confidence: 5
                               Inquisitiveness and Curiosity: 4
                               Initiative: 3.5
                               Determination and Perseverance: 4.5
                               Responsibleness: 3.5
                               Decision-making: 4.5
                               Resilience Under Challenge: 4
                               Detail Orientation: 3.5
                               Creativity and Openness to New Ideas: 4
                               Discipline: 4
                               Strong Features: Writing
                               Talent(s): Tenis
                               Hobby(s): Sports
                               Favourite subject: Turkish
                               Weakest subject: Music
                               Intelligence Type: Verbal Linguistic Intelligence
                               Open for Improvement: Analytical Thinking
                               Weekly Teacher Evaluation: Selim showed strong confidence and perseverance this week, especially during language-based tasks and team activities. To support his development, he is encouraged to engage in activities that strengthen his analytical thinking and attention to detail.
                       
                        5.     Name: Ali
                               Class: 4/B
                               StudentID: 16
                               Age: 9
  
                               Empathy: 3.5
                               Teamwork and Collaboration: 5
                               Confidence: 4
                               Inquisitiveness and Curiosity: 4
                               Initiative: 3
                               Determination and Perseverance: 3.5
                               Responsibleness: 3.5
                               Decision-making: 3.5
                               Resilience Under Challenge: 3
                               Detail Orientation: 3
                               Creativity and Openness to New Ideas: 3
                               Discipline: 4
                               Strong Features: Agile
                               Talent(s): Playing Guitar
                               Hobby(s): Music
                               Favourite subject: Music
                               Weakest subject: Social Sciences
                               Intelligence Type: Rhythmic Intelligence
                               Open for Improvement: Writing
                               Weekly Teacher Evaluation: Ali collaborated very well with his peers this week, showing strong teamwork skills and enthusiasm during music-related activities. To support his growth, he is encouraged to focus more on developing his writing skills through creative expression
                       
                        6.     Name: Ege
                               Class: 4/B
                               StudentID: 29
                               Age: 10
  
                               Empathy: 2
                               Teamwork and Collaboration: 4.
                               Confidence: 4
                               Inquisitiveness and Curiosity: 4.5
                               Initiative: 2.5
                               Determination and Perseverance: 5
                               Responsibleness: 3.5
                               Decision-making: 4
                               Resilience Under Challenge: 4
                               Detail Orientation: 4
                               Creativity and Openness to New Ideas: 5
                               Discipline: 4
                               Strong Features: Disciplined 
                               Talent(s): Sports
                               Hobby(s): Basketball
                               Favourite subject: Natural Sciences
                               Weakest subject: English
                               Intelligence Type: Linguistic Intelligence
                               Open for Improvement: Communication
                               Weekly Teacher Evaluation: Ege is a very determined and confident student. To improve himself, he should be more open to communicating with others. 

                        7.     Name: Zarem
                               Class: 4/B
                               StudentID: 23
                               Age: 10
  
                               Empathy: 4.5
                               Teamwork and Collaboration: 4.5
                               Confidence: 4
                               Inquisitiveness and Curiosity: 4
                               Initiative: 5
                               Determination and Perseverance: 4
                               Responsibleness: 4
                               Decision-making: 4.5
                               Resilience Under Challenge: 5
                               Detail Orientation: 5
                               Creativity and Openness to New Ideas: 4.5
                               Discipline: 4.5
                               Strong Features: Sportive
                               Talent(s): Swimming
                               Hobby(s): Music
                               Favourite subject: Physical Education
                               Weakest subject: Visual Arts
                               Intelligence Type: Logical-Mathematical Intelligence
                               Open for Improvement: Reading Habit 
                               Weekly Teacher Evaluation: Zarem is performing well in her classes. However, she needs to work on developing her confidence and emotional intelligence skills."""),
            agent=agent,
            expected_output=dedent("""\
            By analyzing the student profiles from the student_profiles file, create the following file for each student name:
            "student_name": "Student Name",
            "potential_contributions_in_a_group_project": [],
            "reasoning": {},
            "profile_summary": 
              "communication_style": [],
              "empathy_score": [],
              "cooperation_score": [],
              "confidence_level": [],
              "dominant_intelligence": [],
              "favorite_subjects": [],
              "creative_output": [],
              "curiosity_level": [],
              "peer_interaction": [],
              "general_analysis": [].
               """)      
        )
    def weekly_tasks(self, agent, student_profiles):
        """Task for generating a personalized weekly task set for each student"""
        return Task(
            description=dedent("""\
                Generate a personalized weekly task for each student that was analyzed, consisting one of the four developmentally-aligned categories, prioritizing the one that the student has the most room for improvement:
                   1. Emotional Awareness 
                   2. Social/Environmental Awareness 
                   3. Talent-Based 
                   4. Academics-Based
                Each task: 
                   1. Must be suitable for the age group of 9-10;
                   2. Should consider the possible absence of resources and materials that the students from disadvantaged regions; 
                   3. Should be based on the student’s profile card and their profile analysis, which includes emotional state, communication style, hobbies, academic tendencies, and social-emotional skills;
                   4. Must be short enough for a student of the specified age group to finish within at most 7 days."""),
            agent=agent,
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
    def create_project(self, agent):
        """Task for creating a social impact project for students of different roles and strenghts"""
        return Task(
            description=dedent("""\
                Design a new team-based, socially relevant project suitable for the age group of 9-10. The project must:

                
                    -Address a real-world or community issue,

                
                    -Be inclusive across varied student profiles,


                    -Be applicable and repeatable even in disadvantaged settings, 

                
                    -Offer room for creativity, research, collaboration, and reflection,
                    

                    -Take into account the age group of the analyzed students and be fit to their level."""),
            agent=agent,
            expected_output=dedent("""\
                The Project Generator creates fully structured, socially-driven project blueprints. These projects are built around real-world issues that connect with students’ lives and local communities (e.g., empathy, sustainability, inclusion, gratitude).
                Each project output includes:

                    -A compelling title and real-world theme

                    -A concise description

                    -A 4 week duration

                    -A potential model for the distribution of responsibilities within the project

                    -A clear reflection prompt or deliverable goal

                    -A clear objective

                Output Format: A structured text with:

                    -Project ID and metadata
                
                    -Description of which are the potential tasks or missions within the project and how can students distribute this workload with different roles 

                    -Role-based task assignments

                    -Social focus area (e.g., community, school culture, environment)

                    -Materials needed and expected deliverables""")      
        )
    def assign_student_to_project_role(self, agent):
        """Assigning students roles according to their personal profile, based on the results of the profile_analyzer agent, to the projects created by project_generator agent"""
        return Task(
            description=dedent("""\
                Match a student to the most developmentally appropriate team role within a selected social impact project. Use student profile data (personality, academic strengths, emotional/social skills, interests) to determine the best fit."""),
            agent=agent,
            expected_output=dedent("""\
                The Student Matcher assigns each student to the most appropriate team role according to the results of the analysis of the profile_analyzer agent within a given project that is created by the project_generator agent. It analyzes the student’s complete profile—including social-emotional skills, academic focus, personality traits, and interest areas—and matches them to a best-fit role in the project that will both support and stretch their abilities.

                Each output includes:
                    The student ID

                    The assigned project

                    The description of the role of each student 

                    A rationale based on profile data (e.g., “shows empathy and curiosity, suited to Researcher role”)

                """)      
        )
