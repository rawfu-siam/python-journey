# t1
skills = {"Python", "n8n"}
skills.add("Python")
print(skills)
# t2
active_users = {"user1", "user2", "user3"}
active_users.discard("user4")
print(active_users)
# t3
newsletter_subscribers = {"a@test.com", "b@test.com", "c@test.com"}
buyers = {"b@test.com", "d@test.com"}
only_subscribed = newsletter_subscribers.difference(buyers)
print(only_subscribed)
