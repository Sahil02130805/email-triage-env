from env.environment import EmailTriageEnv
from env.models import AgentAction

def run():
    env = EmailTriageEnv()
    total = 0

    for _ in range(3):
        obs = env.reset()

        action = AgentAction(
            category="billing",
            priority="medium",
            response="We will fix your issue soon. Sorry for inconvenience.",
            escalate=False
        )

        _, reward, _, _ = env.step(action)
        total += reward

    print("Score:", total / 3)

if __name__ == "__main__":
    run()