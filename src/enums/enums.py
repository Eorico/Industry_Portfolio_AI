from enum import Enum

class MongoDBEnums(Enum):
    # mongo db objects name
    ABOUT = "about"
    EDUCATION = "education"
    EXPERIENCE = "experience"
    TECH_SKILLS = "tech-skills"
    ACHIEVEMENTS = "achievements"
    
    OVERVIEW = "overviewlanguages"
    WEB_DEVELOPMENT = "webdevelopment"
    BACKEND_DEVELOPMENT = "backenddevelopment"
    MOBILE_DEVELOPMENT = "mobiledevelopment"
    TOOLS = "tools"
    DATABASE = "database"
    
class ServicesEnums(Enum):
    NO_DATA = "No available information about this section."

    SHOW_DATA = (
        "Here is my educational background:\n\n",
        "Here is are some of my experiences:\n\n",
        "Here are some of my technical skills:",
        "Here are some of my achievements:\n\n",
    )