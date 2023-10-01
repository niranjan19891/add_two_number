#Bare bones Example used to demonstrate processing by AppEngine for data sent through the Android app
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util


class MainHandler(webapp.RequestHandler):
    def post(self):
        num1 = self.request.get('num1')
        num2 = self.request.get('num2')
        num3= int(num1)*int(num2)
        self.response.out.write(num3)



def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()