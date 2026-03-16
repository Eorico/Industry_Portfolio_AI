from repositories.repositories import Repositories
from enums.enums import MongoDBEnums as db_enums, ServicesEnums as serv_enums
from rapidfuzz import fuzz
from pathlib import Path
import json

class ChatBotServices:
    def __init__(self, repository: Repositories):
        self.repo = repository
        self.questions_map = self._chatbot_load_questions()
        self.portfolio_cache = self.repo.get_portfolio()
        
    def _chatbot_load_questions(self):
        try:
            base_path = Path(__file__).resolve().parent
            file_path = base_path.parent / "data" / "ai_question_map.json"
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print("Failed to load AI questions JSON:", e)
            return {}
        
    def _chatbot_get_portfolio(self):
        if not self.portfolio_cache:
            self.portfolio_cache = self.repo.get_portfolio()

        return self.portfolio_cache
        
    def _chatbot_get_about(self) -> str:
        portfolio = self._chatbot_get_portfolio()
        
        about = portfolio.get(db_enums.ABOUT.value) if portfolio else None
        print("Debug about:", about)
        if about:
            return (
                f"""
                    Hello!, my name is {about.get("title")} and I work as a {about.get("role")}.
                    
                    {about.get("description")}
                    
                    You can contact me at:
                        Email: {about.get("email")},
                        Phone: {about.get("phoneNumber")}
                """
            )
        return f"{serv_enums.NO_DATA.value}"

    def _chatbot_get_education(self) -> str:
        portfolio = self._chatbot_get_portfolio()
        
        educ = portfolio.get(db_enums.EDUCATION.value, []) if portfolio else []
        print("Debug education:", educ)
        
        text = []
        
        for e in educ:
            text.append(
            f"""
                {e.get("school")} ({e.get("year")}) - {e.get("course")}        
            """)
        
        if text:
            
            return f"{serv_enums.SHOW_DATA.value[0]}" + "\n".join(text)
            
        return f"{serv_enums.NO_DATA.value}"

    def _chatbot_get_experience(self) -> str:
        portfolio = self._chatbot_get_portfolio()
        
        experience = portfolio.get(db_enums.EXPERIENCE.value, []) if portfolio else []
        print("Debug experience:", experience)
        text = []

        for e in experience:
            text.append(
            f"""
                {e.get("role")} ({e.get("year")}) - {e.get("description")}        
            """)
            
        if text:
            
            return f"{serv_enums.SHOW_DATA.value[1]}" + "\n".join(text)
        
        return f"{serv_enums.NO_DATA.value}"

    def _chatbot_get_skills(self) -> str:
        portfolio = self._chatbot_get_portfolio()
        
        skills = portfolio.get(db_enums.TECH_SKILLS.value) if portfolio else None
        print("Debug skills:", skills)
        
        if not skills:
            return f"{serv_enums.NO_DATA.value}"
        
        overview = ", ".join(skills.get("topSkills", []))
        
        cat_map = {}
        for c in skills.get("categories", []):
            cat_name = c.get("categories")
            cat_skills = ", ".join(c.get(db_enums.TOPSKILLS.value), [])
            cat_map[cat_name] = cat_skills
        
  
        return f"""
                Great question! 👨‍💻

                Great question! 👨‍💻
                {serv_enums.SHOW_DATA.value[2]}

                Languages / Top Skills: {overview}
                Web Development: {cat_map.get(db_enums.WEB_DEVELOPMENT.value, "None")}
                Backend Development: {cat_map.get(db_enums.BACKEND_DEVELOPMENT.value, "None")}
                Mobile Development: {cat_map.get(db_enums.MOBILE_DEVELOPMENT.value, "None")}
                Device Programming: {cat_map.get(db_enums.DEVICE_PROGRAMMING.value, "None")}
                Tools: {cat_map.get(db_enums.TOOLS.value, "None")}
                Database: {cat_map.get(db_enums.DATABASE.value, "None")}
            """

    def _chatbot_get_achievements(self) -> str:
        portfolio = self._chatbot_get_portfolio()
        
        achievements = portfolio.get(db_enums.ACHIEVEMENTS.value, []) if portfolio else []
        print("Debug achievements:", achievements)
        
        text = []
        
        for a in achievements:
            text.append(
            f"""
                {a.get("title")} ({a.get("year")})     
            """)
            
        if text:
            
            return f"{serv_enums.SHOW_DATA.value[3]}" + "\n".join(text)
        
        return f"{serv_enums.NO_DATA.value}"

    def chatbot_ask(self, question: str) -> str:
        try:
            q = question.lower()
            
            best_confidence = 0
            best_category = None
            
            for category, questions in self.questions_map.items():
                for sample in questions:
                    confidence = fuzz.ratio(q, sample)
                    
                    if confidence > best_confidence:
                        best_confidence = confidence
                        best_category = category
                        
            if best_confidence < 35:
                return """
                            I'm not sure about that yet 🤔

                            You can ask me things like:
                            • Who is Eorico?
                            • What are your skills?
                            • What is your education?
                            • Tell me about your experience
                        """
                        
            handlers = {
                "about": self._chatbot_get_about,
                "education": self._chatbot_get_education,
                "experience": self._chatbot_get_experience,
                "skills": self._chatbot_get_skills,
                "achievements": self._chatbot_get_achievements
            }
                        
            handler = handlers.get(best_category)
            
            if handler:
                return handler()
            
            return serv_enums.NO_DATA.value
        except Exception as e:
            print("Chatbot as handler error:", e)
            return serv_enums.NO_DATA.value