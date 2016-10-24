from piston.handler import BaseHandler

class TestHandler1(BaseHandler):
	allowed_methods = ('GET',)

	def read(self, request):
		return "hello"

class TestHandler2(BaseHandler):
	allowed_methods=('GET',)

	def read(self, request):
		return "hi"
