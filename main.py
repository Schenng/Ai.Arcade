from environement import Environement
from train import Trainer
from dqn import DQN

env = Envrionement(args)
agent = DQN(env, args)

Trainer(agent).run()

env.gym.monitor.start(args.out, force=True)
agent.play()
env.gym.monitor.close()