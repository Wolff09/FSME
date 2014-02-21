# -*- coding: utf-8 -*-

import os
from jinja2 import Environment, FileSystemLoader
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


######################### data functions #########################

addrs = [
	#[id,[tags],Vorname,Nachname,eMail,Telefon]
	[0,[u'Fachschaft'],u'Fachschaft',u'Architektur',u'fachschaft@architektur.uni-kl.de',u'2026'],
	[1,[u'Professor'],u'Jürgen',u'Avenhaus',u'avenhaus@informatik.uni-kl.de',u''],
	[2,[u'Student',u'FSler'],u'Sebastian',u'Bachtler',u's_bachtl@informatik.uni-kl.de',u''],
	[3,[u'Student',u'FSler',u'Fete'],u'Rouven',u'Bauer',u'r_bauer11@cs.uni-kl.de',u'0178 14 30 8 44',
		u'24. August', u'Apfelstr. 4', u'67655 Kaiserslautern', u'ICQ: 341-750-388'],
	[4,[u'Student'],u'Hannah',u'Bayer',u'h_bayer@informatik.uni-kl.de',u'06324-9114293'],
	[5,[u'Student'],u'Martin',u'Birtel',u'm_birtel@informatik.uni-kl.de',u'0631-6263773'],
	[6,[u'Professor'],u'Thomas',u'GanzLangerNameBreuel',u'tmb@informatik.uni-kl.de',u'0631 20575-400 bzw. 3456'],
	[7,[u'Professor'],u'Andreas',u'Dengel',u'andreas.dengel@dfki.de',u'0631 20575-100'],
	[8,[],u'Christian',u'Petry',u'c_petry@web.de',u'6268699, 3547618'],
]
tags = ['Fachschaft','Professor','FSler','Fete','Student']
prots = [
	[0, '13.11.2013', 'Penis Ulrich', 'Penis Ulrich', '-', True],
	[1, '01.10.2013', 'Chris Box', 'Chris Box', '-', False],
	[2, '24.06.2013', 'Franz Krim', 'Franz Krim', '01.07.2013', True],
	[3, '14.06.2013', 'Rex Blazorek', 'Rex Blazorek', '04.07.2013', False],
	[4, '07.06.2013', 'Lor Emipsum', 'Lor Emipsum', '07.07.2013', True],
	[5, '23.02.2013', 'Lorem Ipsum', 'Lorem Ipsum', '27.07.2013', True],
]
fsr = ['Penis Ulrich', 'Chris Box', 'Heinrich Kritz', 'Lorem Ipsum', 'Pakitos Raletor', 'Kejtorla Grotizja',
		'Penis Ulrich', 'Chris Box', 'Heinrich Kritz', 'Lorem Ipsum', 'Pakitos Raletor', 'Kejtorla Grotizja']
guest = ['Penis Ulrich', 'Chris Box', 'Heinrich Kritz', 'Lorem Ipsum', 'Pakitos Raletor']

def addr_list(matchdict):
	return { 'tags': tags, 'addresses': addrs }

def addr_detail(matchdict):
	id = int(matchdict['id'] if matchdict and 'id' in matchdict else 1)
	return {
		'id': addrs[id][0],'tags': addrs[id][1],'firstname': addrs[id][2],
		'lastname': addrs[id][3],'email': addrs[id][4],'tele': addrs[id][5],
		'birthday': addrs[id][6] if len(addrs[id]) > 6 else u'',
		'street': addrs[id][7] if len(addrs[id]) > 7 else u'',
		'town': addrs[id][8] if len(addrs[id]) > 8 else u'',
		'misc': addrs[id][9] if len(addrs[id]) > 9 else u'',
	}

def prot_list(matchdict):
	return {'prots': prots}

#def protokoll_view(matchdict):
#	id = int(matchdict['id'] if matchdict and 'id' in matchdict else 1)
#	return {'prot': prots[id] if id >= 0 and id < len(prots) else prots[0], 'fsr': fsr, 'guest': guest}


######################## configure views #########################

def register(config):
	# add routes and views here
	add(config, '/', 'home')
	add(config, '/addr/', 'address_book', addr_list)
	add(config, '/addr/change', 'address_form')
	add(config, '/addr/{id}', 'address_detail', addr_detail)
	add(config, '/prot/', 'protokoll_home', prot_list)
	add(config, '/prot/{id}', 'protokoll_view/base')
	add(config, '/prot/change/meta', 'protokoll_change/meta')
	add(config, '/prot/change/request', 'protokoll_change/request')
	add(config, '/prot/change/top', 'protokoll_change/top')
	add(config, '/login', 'login')
	add(config, '/profile', 'profile')

	# add(config, '/prot/add/', 'protokoll_add')
	# add(config, '/prot/change/', 'protokoll_change')


######################## configure server ########################

env = Environment(loader=FileSystemLoader('templates'))

def render(template, datadict=None):
	tmp = env.get_template(template)
	res = tmp.render(datadict or {})
	return Response(res)

def add(config, route, template, data_func=None):
	config.add_route(template, route)
	def view(request):
		data = data_func(request.matchdict) if data_func else request.matchdict
		return render(template + '.html', data)
	config.add_view(view, route_name=template)

if __name__ == '__main__':
	config = Configurator()
	register(config)
	config.add_static_view('static', '.', cache_max_age=0)
	app = config.make_wsgi_app()
	server = make_server('127.0.0.1', 8080, app)
	server.serve_forever()
