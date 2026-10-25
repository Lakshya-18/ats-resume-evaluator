resumes_dataset = [
    """
    Name: Priya Sharma
    Email: priya.sharma@email.com | Phone: +91 98765 43210
    Socials: ://linkedin.com
    Education: B.Tech in Computer Science (AI & ML Specialization, 2025), MUJ.
    Skills: Python, Groq API, OpenAI SDK, Vector Databases (Qdrant, Pinecone), Pydantic, Git, GitHub.
    Experience: Built an automated document extraction pipeline utilizing LLMs during a college lab layout. Deeply familiar with API routing frameworks. Spent 3 months building a RAG application.
    Gap: No gap year. Value = 0.
    """,
    """
    Name: Rohan Das
    Email: rohan.das@email.com | Phone: +91 88888 77777
    Socials: ://linkedin.com
    Education: BCA Graduate (2024).
    Skills: Python scripting, HTML/CSS, basic SQL data querying, Linux terminal commands, Git.
    Experience: 1 year working as a junior tech support specialist handling server logs and fundamental debugging workflows. Built a basic web scraper using BeautifulSoup.
    Gap: 0
    """,
    """
    Name: Amit Kumar
    Email: amit.kumar@email.com | Phone: +91 99999 88888
    Socials: null
    Education: B.Tech in Civil Engineering (Graduated 2024).
    Skills: Basic Python syntax, Microsoft Excel, AutoCAD, MATLAB.
    Experience: 6 months as a site management intern overseeing concrete structural layout checks. Looking to transition into technology tracks.
    Gap: 0
    """,
    """
    Name: Arshad Khan
    Email: arshad.khan@email.com | Phone: +91 91111 22222
    Socials: ://linkedin.com
    Education: B.Tech in Computer Science (2023).
    Skills: Python, Django, FastAPI, PostgreSQL, AWS (S3/EC2), Docker, Git.
    Experience: 2 years as a Backend Developer at a tech startup. Optimized API response times by 40% using Redis caching layers. Actively looking for AI engineering exposure.
    Gap: Took 6 months off in 2024 to care for a sick family member.
    """,
    """
    Name: Sneha Reddy
    Email: sneha.reddy@email.com | Phone: +91 92222 33333
    Socials: ://linkedin.com
    Education: M.Tech in Data Science (2025).
    Skills: Python, R, NumPy, Pandas, Scikit-Learn, PyTorch, SQL, Tableau.
    Experience: Interned as a Data Analyst. Developed a predictive machine learning model for customer churn analysis. Familiar with tokenization but no direct LLM API execution experience.
    Gap: 0
    """,
    """
    Name: Vikram Singh
    Email: vikram.singh@email.com | Phone: +91 93333 44444
    Socials: null
    Education: Graduate in Commerce (B.Com, 2023).
    Skills: Tally ERP, Financial Accounting, Advanced Excel, Tax filing.
    Experience: 1.5 years working as an accountant at a local retail corporation. No programming or software engineering background.
    Gap: 1 year gap after graduation to prepare for banking exams.
    """,
    """
    Name: Divya Joshi
    Email: divya.joshi@email.com | Phone: +91 94444 55555
    Socials: ://linkedin.com
    Education: B.Tech in Electronics & Communication (2024).
    Skills: Python, C++, Embedded Systems, LangChain, Groq SDK, Hugging Face Transformers, Git.
    Experience: Developed a voice-controlled smart home automation prototype using LLM functional calls and Raspberry Pi. High interest in AI agentic frameworks.
    Gap: 0
    """,
    """
    Name: Rahul Malhotra
    Email: rahul.m@email.com | Phone: +91 95555 66666
    Socials: ://linkedin.com
    Education: B.Tech in Information Technology (2022).
    Skills: Python, Selenium WebDriver, PyTest, Postman, Jira, Jenkins.
    Experience: 3 years as a QA Automation Engineer. Built robust end-to-end automation testing scripts for e-commerce platforms. Wants to shift toward core AI automation.
    Gap: 0
    """,
    """
    Name: Ishita Verma
    Email: ishita.v@email.com | Phone: +91 96666 77777
    Socials: null
    Education: B.Sc in Mathematics (2024).
    Skills: Statistical Analysis, Linear Algebra, Python basics, SQL.
    Experience: Fresher. Completed a 3-month online certification in Python for Data Analytics. Worked on basic array manipulation challenges.
    Gap: 0
    """,
    """
    Name: Kshitij Anand
    Email: kshitij.a@email.com | Phone: +91 97777 88888
    Socials: ://linkedin.com
    Education: B.Tech in Computer Science (2025).
    Skills: Python, C++, Data Structures & Algorithms (DSA), Object-Oriented Programming (OOP).
    Experience: Academic projects only. Solved 300+ problems on LeetCode using Python. Looking for an entry-level coding profile.
    Gap: 0
    """,
    """
    Name: Meera Nair
    Email: meera.nair@email.com | Phone: +91 98888 99999
    Socials: ://linkedin.com
    Education: B.Tech in Artificial Intelligence (2024).
    Skills: Python, NLP (Natural Language Processing), NLTK, SpaCy, Qdrant Vector Search, Ollama, LangChain.
    Experience: 8 months as an AI Research Intern. Built a semantic search engine for internal corporate text files and knowledge bases.
    Gap: 0
    """,
    """
    Name: Gaurav Saxena
    Email: gaurav.s@email.com | Phone: +91 99999 00000
    Socials: null
    Education: Diploma in Mechanical Engineering (2023).
    Skills: SolidWorks, CNC Programming, Machine Maintenance.
    Experience: 2 years working as a junior technician in an automotive assembly warehouse plant line.
    Gap: 2 years gap due to dynamic career pivots and health recovery.
    """,
    """
    Name: Ananya Hegde
    Email: ananya.h@email.com | Phone: +91 90000 11111
    Socials: ://linkedin.com
    Education: M.Sc in Computer Science (2023).
    Skills: Python, JavaScript, React.js, Node.js, MongoDB, Git, REST APIs.
    Experience: 1.5 years as a Full Stack Web Developer. Integrated external third-party payment gateways and user login wrappers. No direct AI pipeline experience.
    Gap: 0
    """,
    """
    Name: Utkarsh Mishra
    Email: utkarsh.m@email.com | Phone: +91 91111 33333
    Socials: ://linkedin.com
    Education: B.Tech in CS (AIML, 2025), MUJ.
    Skills: Python, OpenAI API, Groq pipeline, Pydantic data modeling, FastAPI, GitHub, Linux bash.
    Experience: Built an automated resume evaluation system using Llama-3 models and structured JSON schemas to match corporate profiles. 
    Gap: 0
    """,
    """
    Name: Pooja Choudhary
    Email: pooja.c@email.com | Phone: +91 92222 44444
    Socials: null
    Education: MCA Graduate (2022).
    Skills: Java, Spring Boot, MySQL, Hibernate.
    Experience: 2.5 years as an enterprise Java engineer building corporate banking backend architectures. Zero experience with Python or AI endpoints.
    Gap: 0
    """,
    """
    Name: Kunal Kapoor
    Email: kunal.k@email.com | Phone: +91 93333 55555
    Socials: ://linkedin.com
    Education: B.Tech in Information Technology (2024).
    Skills: Python, Playwright, BeautifulSoup, LangChain, CrewAI, Git.
    Experience: Built autonomous AI web-scraping agents that monitor e-commerce price layouts and output structured reports automatically.
    Gap: 0
    """,
    """
    Name: Shruti Iyer
    Email: shruti.iyer@email.com | Phone: +91 94444 66666
    Socials: ://linkedin.com
    Education: B.Tech in Computer Science (2023).
    Skills: Python basics, C, HTML, CSS.
    Experience: Worked in non-technical recruitment operations for 1 year. Now self-learning Python pipelines to secure an entry-level automation tech role.
    Gap: Took a 1-year gap in 2025 to transition skills.
    """,
    """
    Name: Tushar Goel
    Email: tushar.goel@email.com | Phone: +91 95555 77777
    Socials: null
    Education: B.Tech in Electrical Engineering (2024).
    Skills: Python scripting, Power Systems, MATLAB, Git basics.
    Experience: Academic project simulating power grid load balances using Python analytics scripts. Looking for corporate software job paths.
    Gap: 0
    """,
    """
    Name: Riya Sen
    Email: riya.sen@email.com | Phone: +91 96666 88888
    Socials: ://linkedin.com
    Education: B.Tech in Computer Science (AI Specialization, 2025).
    Skills: Python, Groq client, Vector DB indexing (Qdrant), Pydantic validation, Streamlit UI, Docker.
    Experience: Designed and deployed a functional RAG web-app layout that allows users to ask questions about lengthy legal PDF documents.
    Gap: 0
    """,
    """
    Name: Abhinav Raj
    Email: abhinav.raj@email.com | Phone: +91 97777 99999
    Socials: ://linkedin.com
    Education: BCA Graduate (2023).
    Skills: Python scripting, PHP, MySQL, JavaScript, Git.
    Experience: 1 year working as a freelance web developer updating legacy local business websites and setting up server database links.
    Gap: 0
    """
]
