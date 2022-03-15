from gym.envs.registration import register

register(
    id='inv-v0',
    entry_point='inv_env.envs:InvEnv',
)

register(
    id='inv-v1',
    entry_point='inv_env.envs:InvEnv1',
)