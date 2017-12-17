from pymongo import MongoClient
import traceback


class Mdb:
    def __init__(self):
        conn_str = "mongodb://admin:123@127.0.0.1:27017/admin"
        # conn_str = 'mongodb://pmuser:pmpass@ds161742.mlab.com:61742/projectmanager'
        client = MongoClient(conn_str)
        self.db = client['projectmanager']

    def register(self, name, email, type, password):
        try:
            rce = {
                'name': name,
                'email': email,
                'type': type,
                'password': password
            }
            self.db.registration.insert(rce)
        except Exception as exp:
            print('registration() :: Got exception: %s' % exp)
            print(traceback.format_exc())

    def user_exists(self, company_email, password):
        """
        fucntion check if a employee given email and password
        exists in database
        :return:
        """
        return self.db.company_manager.find({'company_email': company_email,
                                             'password': password}).count() > 0

if __name__ == '__main__':
    mdb = Mdb()
    # testing
    # mdb.register('john', 'john@gmail.con', 'jonny', '123', '123')
    if mdb.user_exists('john@gmail.con', '123'):
        print 'employee exist'
    else:
        print 'employee does not exist'
    print "<<++++++++ Data is saved +++++++>>"
