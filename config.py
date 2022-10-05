from environs import Env

env = Env()
env.read_env()

DAO_CLASS = env.str("DAO_CLASS")
DB_USER = env.str("DB_USER")
DB_PASSWORD = env.str("DB_PASSWORD")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")
