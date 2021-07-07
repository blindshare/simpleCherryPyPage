#!/usr/bin/python3

import cherrypy

class SimpleTest(object):
    r = ""

    @cherrypy.expose
    def index(self):
        host = cherrypy.request.headers['User-Agent']
        a = []
        x = ""
        a.append("<!DOCTYPE html> \n")
        a.append("<HTML><TITLE>A simple Test</TITLE>\n")
        a.append("<BODY>\n")
        a.append("<H1>A simple Test</H1>\n")
        a.append("<HR>\n")
        a.append("<H2>Hallo " + host + "</H2>\n")
        a.append("<BR>\n")
        a.append("<form action=\"setReply\" method=\"POST\" >Enter some String: <input id=\"in\" type=\"text\" name=\"rep\"><input type=\"submit\"></form>")
        x = self.getReply()
        print("this is X: " + x)
        if (x != ""):
          a.append("<BR>\n")
          a.append("<B>" + x + "</B>\n")
        a.append("</BODY></HTML>\n")

        return a
          
    @cherrypy.expose
    def getReply(self):
        return SimpleTest.r

    @cherrypy.expose
    def setReply(self, rep):
        SimpleTest.r = rep
        return self.index()



    @cherrypy.expose
    def default(self):
      raise cherrypy.HTTPRedirect('index')
    default.exposed = True

if __name__ == '__main__':
    cherrypy.server.socket_host = '0.0.0.0'
    cherrypy.quickstart(SimpleTest())
