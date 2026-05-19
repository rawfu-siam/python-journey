# t1
class Computer:
    ram = 8
    def upgrade_ram(self):
        self.ram = self.ram + 8
my_comp = Computer()
print(my_comp.ram)
my_comp.upgrade_ram()
print(my_comp.ram)
# t2
class N8nWorkflow:
    name = "AI Agent"
    is_running = False
    def start_workflow(self):
        self.is_running = True
    def get_status(self):
        if self.is_running == True:
            print("The workflow is running")
        else:
            print("The workflow is stopped")
