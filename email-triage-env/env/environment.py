import random
from env.tasks import TASKS
from env.grader import grade_action
from env.models import EmailObservation

class EmailTriageEnv:

    def __init__(self):
        self.task = None

    def reset(self):
        self.task = random.choice(TASKS)
        return EmailObservation(**self.task["input"])

    def step(self, action):
        score, feedback = grade_action(self.task, action)

        return (
            EmailObservation(**self.task["input"]),
            score,
            True,
            {"feedback": feedback}
        )

    def state(self):
        return {"task": self.task}