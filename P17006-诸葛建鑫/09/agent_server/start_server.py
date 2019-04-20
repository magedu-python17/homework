# from server.model import db
# db.drop_all()
# db.create_all()


from server.server import FtpServer
fs = FtpServer()
fs.serve_forever()
