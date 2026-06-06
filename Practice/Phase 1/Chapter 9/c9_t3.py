# t1
with open("skills.txt", "r") as skillset:
    skills = skillset.readlines()
print(skills)
# t2
second_skill = skills[1]
clean = second_skill.strip()
print(clean)
# t3
current_user = "bot_agent_99"
with open("banned.txt", "r") as banned_user:
    banned_user_rows = banned_user.readlines()
    for user in banned_user_rows:
        clean_version = user.strip()
        if clean_version == current_user:
            print("[CRITICAL SYSTEM WARNING]: Security breach blocked for user: bot_agent_99!")

