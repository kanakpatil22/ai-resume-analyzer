# List of skills we want to search for in resumes
SKILLS_LIST = [
    "python", "java", "c++", "sql", "javascript", "html", "css",
    "machine learning", "deep learning", "data analysis",
    "excel", "power bi", "tableau", "git", "communication",
    "problem solving", "teamwork", "leadership"
]

# Important resume elements that companies look for
RESUME_ELEMENTS = [
    "internship", "certification", "certified",
    "project", "achievement", "award",
    "volunteer", "extracurricular",
    "objective", "summary",
    "linkedin", "github", "portfolio",
    "reference", "workshop", "training",
    "publication", "research"
]

# Free learning resources for common skills (used for suggestions)
SKILL_RESOURCES = {
    "python": "https://www.w3schools.com/python/",
    "sql": "https://www.w3schools.com/sql/",
    "java": "https://www.w3schools.com/java/",
    "machine learning": "https://www.coursera.org/learn/machine-learning",
    "data analysis": "https://www.kaggle.com/learn/pandas",
    "excel": "https://www.udemy.com/course/microsoft-excel-2013-from-beginner-to-advanced-and-beyond/",
    "power bi": "https://learn.microsoft.com/en-us/power-bi/",
    "git": "https://www.w3schools.com/git/",
    "digital marketing": "https://learndigital.withgoogle.com/digitalgarage",
    "accounting": "https://www.coursera.org/learn/accounting-basics",
    "communication": "https://www.coursera.org/learn/wharton-communication-skills",
    "leadership": "https://www.coursera.org/learn/leadership-skills",
}

# Domain-specific skill sets
DOMAINS = {
    "B.Tech/B.E. - Computer Science/IT": [
        "python", "java", "c++", "c", "sql", "javascript", "html", "css",
        "machine learning", "deep learning", "artificial intelligence",
        "data structures", "algorithms", "dbms", "operating systems",
        "computer networks", "git", "github", "aws", "cloud computing",
        "react", "node.js", "django", "flask", "cybersecurity",
        "communication", "problem solving", "teamwork"
    ],
    "B.Tech/B.E. - Mechanical": [
        "autocad", "solidworks", "catia", "matlab", "ansys",
        "thermodynamics", "cad design", "manufacturing", "robotics",
        "automation", "plc programming", "communication", "teamwork",
        "problem solving", "project management"
    ],
    "B.Tech/B.E. - Electrical/Electronics": [
        "circuit design", "embedded systems", "microcontrollers",
        "vlsi", "pcb design", "power systems", "matlab", "autocad",
        "communication", "problem solving", "teamwork"
    ],
    "B.Tech/B.E. - Civil": [
        "autocad", "revit", "structural analysis", "construction management",
        "building codes", "project management", "communication", "teamwork"
    ],
    "M.Tech": [
        "python", "machine learning", "deep learning", "research",
        "data analysis", "matlab", "publication", "problem solving",
        "communication", "project management"
    ],
    "BCA": [
        "python", "java", "c++", "sql", "html", "css", "javascript",
        "dbms", "data structures", "git", "communication", "problem solving"
    ],
    "MCA": [
        "python", "java", "sql", "machine learning", "data structures",
        "algorithms", "cloud computing", "git", "aws",
        "communication", "problem solving", "leadership"
    ],
    "BBA": [
        "business analysis", "excel", "market research", "communication",
        "teamwork", "leadership", "presentation skills", "sales",
        "customer relationship management", "time management"
    ],
    "BBA - Foreign Trade": [
        "international trade", "export", "import", "logistics",
        "supply chain management", "market research", "negotiation",
        "communication", "excel", "business analysis"
    ],
    "MBA - General/Marketing": [
        "digital marketing", "seo", "social media marketing",
        "market research", "brand management", "content marketing",
        "strategic planning", "communication", "leadership", "negotiation"
    ],
    "MBA - Finance": [
        "financial modeling", "financial analysis", "investment banking",
        "equity research", "accounting", "excel", "risk management",
        "budgeting", "communication", "leadership"
    ],
    "MBA - HR": [
        "recruitment", "talent acquisition", "employee relations",
        "payroll", "performance management", "hr policies",
        "communication", "leadership", "conflict resolution"
    ],
    "B.Com/M.Com": [
        "accounting", "tally", "financial analysis", "taxation",
        "auditing", "gst", "income tax", "bookkeeping", "excel",
        "communication", "budgeting"
    ],
    "Law (LLB/LLM)": [
        "legal research", "contract drafting", "litigation",
        "corporate law", "intellectual property law", "criminal law",
        "legal compliance", "case analysis", "legal writing",
        "communication", "critical thinking"
    ],
    "Architecture (B.Arch)": [
        "autocad", "revit", "sketchup", "3d modeling",
        "structural analysis", "urban planning", "interior design",
        "building codes", "creativity", "communication"
    ],
    "Design (UI/UX, Graphic)": [
        "photoshop", "illustrator", "figma", "ui/ux design", "canva",
        "video editing", "graphic design", "animation", "creativity",
        "communication"
    ],
    "General/Other (All Skills)": SKILLS_LIST
}

# Common AI/cliché phrases often found in AI-generated resumes, with human-sounding alternatives
AI_PHRASES = {
    "results-driven": "Try being specific: mention an actual result/number instead",
    "proven track record": "Replace with a specific achievement (e.g. 'increased sales by 20%')",
    "leverage": "Use a simpler word like 'use'",
    "utilize": "Use 'use' instead — sounds more natural",
    "spearheaded": "Use 'led' or 'started' if it fits better",
    "dynamic professional": "Describe what makes you dynamic with an example",
    "synergy": "Use 'collaboration' or 'teamwork'",
    "cutting-edge": "Use 'latest' or 'modern'",
    "seamless": "Use 'smooth' or be specific about what worked well",
    "robust": "Use 'strong' or 'reliable'",
    "holistic approach": "Explain the approach specifically instead",
    "self-starter": "Give an example of when you worked independently",
    "go-getter": "Show initiative through a specific example instead",
    "empower": "Use 'help' or 'support'",
    "streamline": "Use 'simplify' or 'improve'",
    "innovative solutions": "Describe the actual solution you built",
    "passionate about": "Show your passion through achievements, not this phrase",
    "in today's fast-paced world": "Remove this — it adds no real information",
    "value-added": "Remove or replace with a specific benefit you provided",
    "strategic thinker": "Give an example of strategic thinking instead"
}