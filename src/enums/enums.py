from enum import Enum

class MongoDBEnums(Enum):
    # mongo db objects name
    ABOUT = "about"
    EDUCATION = "education"
    EXPERIENCE = "experience"
    TECH_SKILLS = "tech-skills"
    ACHIEVEMENTS = "achievements"
    
    TOPSKILLS = "topSkills"
    WEB_DEVELOPMENT = "Web Development"
    BACKEND_DEVELOPMENT = "Backend"
    MOBILE_DEVELOPMENT = "Mobile Development"
    DEVICE_PROGRAMMING = "Device Programming"
    TOOLS = "Tools"
    DATABASE = "Database"
    
class ServicesEnums(Enum):
    NO_DATA = "No available information about this section."

    SHOW_DATA = (
        "Here is my educational background:\n\n",
        "Here is are some of my experiences:\n\n",
        "Here are some of my technical skills:",
        "Here are some of my achievements:\n\n",
    )