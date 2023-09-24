import requests
import json

class GetPrograms:

    def get_programs(self):
        URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
        response = requests.get(URL)
        return response.content

    def program_school(self):
        programs_list = []
        programs = json.loads(self.get_programs())
        for program in programs:
            programs_list.append(program["agency"])
        return programs_list

# Create an instance of the GetPrograms class
programs_instance = GetPrograms()

# Call the get_programs method on the instance
programs = programs_instance.get_programs()
print(programs)

# Call the program_school method on the instance
programs_schools = programs_instance.program_school()

for school in set(programs_schools):
    print(school)
