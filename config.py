from environs import Env

env = Env()
env.read_env()

DB_USER = env.str("DB_USER")
DB_PASSWORD = env.str("DB_PASSWORD")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")
