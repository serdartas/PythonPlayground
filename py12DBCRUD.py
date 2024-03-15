import json
import mysql.connector

def getDBConfig(env):
    with open('config.json') as configFile:
        configData = json.load(configFile)
    
    for config in configData:
        if config["env"] == env:
            dbConfig = config["config"]
            return dbConfig
    
    raise ValueError(f"Can't find the '{env}' environment in configuration")
    
def getConnection(env, buffered=False):
    environment = getDBConfig(env)
    con = mysql.connector.connect(
        host=environment['server'],
        port=environment['port'],
        user=environment['user'],
        password=environment['password'],
        buffered=buffered
    )
    return con

def getCommands(SQLFilePath):
    with open(SQLFilePath) as SQLFile:
        sql = SQLFile.read()
        commands = sql.split(';')
        commands = [command.strip() for command in commands if command.strip()]
        return commands

if __name__ == "__main__":
    con = getConnection("tascloud")
    cmd = con.cursor()
    commands = getCommands("createDB.sql")
    for command in commands:
        try:
            cmd.execute(command)
            output = cmd.fetchall()
            output = "Command executed successfully" if output == [] else output
        except mysql.connector.Error as e:
            output = "An error occurred running query:\n"
            output += command
            output += "\n" + str(e.errno) + ", " + e.msg

        print(output)