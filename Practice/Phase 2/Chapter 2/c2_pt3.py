'''
Chapter2, topic - super() method
'''
'''
Task 1 (Easy) — The Specialized Client RegisterGoal: Build a parent class Client with 
an __init__ that sets name. Create a child class VIPClient that uses super() to save 
name, but adds a unique instance attribute variable discount_rate = 0.20.Action: 
Instantiate a VIPClient object named "Alpha Corp", and print out its name and 
discount rate.
'''
class Client:
    def __init__(self, name):
        self.name = name
class VIPClient(Client):
    def __init__(self, name, discount_rate=0.20):
        super().__init__(name)
        self.discount_rate = discount_rate
client1 = VIPClient("Alpha Corp")
print(client1.name)
print(client1.discount_rate)
'''
Task 2 (Medium) — Automated Agent API Keys FrameworkGoal: Build a constructor pairing 
pipeline:Parent Class: APIService → __init__ sets an instance attribute endpoint string.
Child Class: OpenAIConnector (inherits from APIService) → its __init__ takes both 
endpoint and api_key. It must pass endpoint to the parent using super(), and save 
api_key locally.Action: Instantiate an OpenAIConnector passing "https://openai.com" 
and "sk-12345". Print both attributes from the child object.
'''
class APIService:
    def __init__(self, endpoint):
        self.endpoint = endpoint
class OpenAIConnector(APIService):
    def __init__(self, endpoint, api_key):
        super().__init__(endpoint)
        self.api_key = api_key
connectorA = OpenAIConnector("https://openai.com", "sk-12345")
print(connectorA.api_key)
print(connectorA.endpoint)
'''
Task 3 (Bit Harder) — The Scaled Notification Relay OverriderGoal: Construct an expanded 
log method system using function extension: Parent Class: TextNotifier → contains a method 
.send_alert(msg) that returns the string f"Alert: {msg}". Child Class: SlackNotifier → 
overrides the .send_alert(msg) method. Inside it, use super() to extract the parent's 
base string alert, and return it wrapped with custom Slack tags: f"[SLACK_CHANNEL] -> 
{parent_output_string}".Action: Instantiate a SlackNotifier and print out the result 
of calling .send_alert("Database Offline!").
'''
class TextNotifier:
    def send_alert(self, msg):
        return f"Alert: {msg}"
class SlackNotifier(TextNotifier):
    def send_alert(self, msg):
        message = super().send_alert(msg)
        return f"[SLACK_CHANNEL] -> {message}"
notifier1 = SlackNotifier()
print(notifier1.send_alert("Database Offline!"))
