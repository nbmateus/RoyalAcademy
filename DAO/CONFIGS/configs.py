
#modo = 'produccion'
modo = 'desarrollo'


def getConfigDB():
    configDB = {}
    if (modo == 'desarrollo'):
        configDB['host'] = 'localhost'
        configDB['user'] = 'royaladmin'
        configDB['password'] = 'royaladmin'
        configDB['database'] = 'royalacademydb'
        configDB['auth_plugin']='mysql_native_password'
        
    return configDB