import sublime, sublime_plugin

class HexDecCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			if not region.empty():
				s = self.view.substr(region)
				x = int(s,16)
				self.view.replace(edit,region,str(x))

class DecHexCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			if not region.empty():
				s = self.view.substr(region)
				x = hex(int(s))
				self.view.replace(edit,region,str(x))


