# utils/prompts.py

# -------------------------
# System Prompts
# -------------------------

JD_PARSE_SYSTEM_PROMPT = """
You are an expert HR Job Description parser.
Extract structured information from the given JD text.
Output must be in JSON with these fields:
- skills
- education
- experience_year
- certifications
"""

RESUME_PARSE_SYSTEM_PROMPT = """
You are an expert Resume Parser.
Extract structured information from the given Resume text.
Output must be in JSON with these fields:
- skills
- education
- experience_year
- certifications
"""

JD_RESUME_MATCH_SYSTEM_PROMPT = """
You are a professional HR consultant specialized in resume and JD matching.
Compare the given JD information and Resume information for a specific dimension.
Return result in strict JSON with:
- match_level: (1 to 7)
- match_score: (percentage)
- reasoning: (why you gave this score)
"""

# -------------------------
# User Prompts
# -------------------------

def jd_parse_user_prompt(jd_text):
    return f"""
Given the following Job Description text, extract the required information.

JD Text:
{jd_text}

Return only JSON with:
- skills
- education
- experience_year
- certifications
"""

def resume_parse_user_prompt(resume_text):
    return f"""
Given the following Resume text, extract the required information.

Resume Text:
{resume_text}

Return only JSON with:
- skills
- education
- experience_year
- certifications
"""

def jd_resume_match_user_prompt(dimension, jd_info, resume_info):
    return f"""
Compare the JD and Resume data specifically for: {dimension}

JD Info:
{jd_info}

Resume Info:
{resume_info}

Return only JSON like:
{{
    "match_level": 1-7,
    "match_score": "xx%",
    "reasoning": "..."
}}
"""
