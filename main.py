import os
from crewai_components.crews import crew
from dotenv import load_dotenv
load_dotenv(override=True)

# Starting the task execution process with enhanced feedback
event_criteria = {
    'location': 'Brampton, Ontario',
    'check_in': '23rd August, 2024',
    'check_out': '25th August, 2024',
    'number_of_people': 2,
    'budget': 600
}
result = crew.kickoff(inputs=event_criteria)

#write as a notion page
