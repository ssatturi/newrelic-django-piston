from piston.handler import BaseHandler

class TestHandler1(BaseHandler):
	allowed_methods = ('GET',)

	def read(self, request):
		return "hello"
	class Meta:
		app_label = 'TestHandler1'

class TestHandler2(BaseHandler):
	allowed_methods=('GET',)

	def read(self, request):
		return "hi"
        class Meta:
                app_label = 'TestHandler2'

class TestHandler3(BaseHandler):
	allowed_methods=('GET',)

	def read(self, request):
		return "ola"
        class Meta:
                app_label = 'TestHandler3'

class TestHandler4(BaseHandler):
	allowed_methods=('GET',)

	def read(self, request):
		return "namaste"
        class Meta:
                app_label = 'TestHandler4'
