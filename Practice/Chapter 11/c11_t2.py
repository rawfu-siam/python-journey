# t1
class CloudServer:
    operating_system = "Ubuntu"
print(CloudServer.operating_system)
# t2
class AiAgentConfig:
    engine = "running"
    temperature = 1.0
    max_tokens = 25
if AiAgentConfig.temperature > 0.7:
    print("Warning! temperature exceeds 0.7!")
else:
    print("All good!")
