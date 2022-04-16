from database import *

EMPTY_STRING = ""
mainDB = "default_db"

def printOutput(result):
    print("> ", result)

def setKeyValueHandler(conn, key, value):
    inertInToTable(conn, mainDB, key, value)
    printOutput(EMPTY_STRING)

def getKeyHandler(conn, key):
    result = selectWithKey(conn, mainDB, key)
    printOutput(result)

def delKeyHandler(conn, key):
    deleteWithKey(conn, mainDB, key)
    printOutput(EMPTY_STRING)

def KeysHandler(conn, key):
    matchs = findMatchkeys(conn, mainDB, key)
    printOutput(matchs)

def useHandler(conn, dbName):
    mainDB = dbName
    createTable(conn, mainDB)
    printOutput(EMPTY_STRING)

def listHandler(conn):
    tables = findTables(conn)
    printOutput(tables)

def dumpHandler(conn, dbName, path):
    dumpDB(conn, dbName, path)
    printOutput(EMPTY_STRING)

def loadHandler(conn, path, dbName):
    loadDB(conn, path, dbName)
    printOutput(EMPTY_STRING)

def exitHandler(conn):
    conn.close()
    printOutput(EMPTY_STRING)
    exit(0)

def processInput(conn, cmd):
    cmd_parts = cmd.split()
    if (cmd_parts[0] == "set"):
        value = cmd[len(cmd_parts[1])+5:]
        setKeyValueHandler(conn, cmd_parts[1], value)
    elif (cmd_parts[0] == "get"):
        getKeyHandler(conn, cmd_parts[1])
    elif (cmd_parts[0] == "del"):
        delKeyHandler(conn, cmd_parts[1])
    elif (cmd_parts[0] == "keys"):
        KeysHandler(conn, cmd_parts[1])
    elif (cmd_parts[0] == "use"):
        useHandler(conn, cmd_parts[1])
    elif (cmd_parts[0] == "list"):
        listHandler(conn)
    elif (cmd_parts[0] == "dump"):
        dumpHandler(conn, cmd_parts[1], cmd_parts[2])
    elif (cmd_parts[0] == "load"):
        loadHandler(conn, cmd_parts[1], cmd_parts[2])
    elif (cmd_parts[0] == "exit"):
        exitHandler(conn)

def initialDB():
    connection = createConnection("database.sqlite")
    createTable(connection, mainDB)
    return connection

def main():
    connection = initialDB()
    while(True):
        cmd = input()
        processInput(connection, cmd)

if __name__ == '__main__':
    main()