# -*- coding: utf-8 -*-

import requests

class Issues(object):
	def __init__(self, cfg):
		super(Issues, self).__init__()
		self.api = 'http://%s/api/v4/issues'
		self.source = cfg['source']
		self.target = cfg['target']
		self.params = { 'per_page': cfg['per_page'], 'scope': 'all' }

	def run(self):
		source = self.get()
		target = self.inserts(source)

		return { 'source': source, 'target': target }

	def get(self):
		resp = requests.get(self.api % self.source['address'], 
			headers = self.source['headers'], params = self.params)

		issues = resp.json()

		print('Total issues: %d' % len(issues))

		return issues

	def inserts(self, issues):
		return []
