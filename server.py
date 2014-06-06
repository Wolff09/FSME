# -*- coding: utf-8 -*-

import os
from jinja2 import Environment, FileSystemLoader
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


######################### data functions #########################



#def protokoll_view(matchdict):
#	id = int(matchdict['id'] if matchdict and 'id' in matchdict else 1)
#	return {'prot': prots[id] if id >= 0 and id < len(prots) else prots[0], 'fsr': fsr, 'guest': guest}


######################## configure views #########################

def register(config):
	# add routes and views here
	add(config, '/', 'views')
	add(config, '/login', 'login')
	add(config, '/landingpage', 'landingpage')
	add(config, '/profile', 'profile')

	add(config, '/addr/list', 'addresses/list')
	add(config, '/addr/details', 'addresses/details')
	# add(config, '/addr/edit', 'addresses/edit')
	# add(config, '/addr/new', 'addresses/new')

	add(config, '/bev/edit_item', 'beverages/edit_item')
	add(config, '/bev/details_item', 'beverages/details_item')
	add(config, '/bev/own_bills', 'beverages/own_bills')
	add(config, '/bev/own_bills_ref', 'beverages/own_bills_ref')
	add(config, '/bev/all_bills', 'beverages/all_bills')
	add(config, '/bev/all_current_bills', 'beverages/all_current_bills')
	add(config, '/bev/item_list', 'beverages/item_list')
	add(config, '/bev/bill_details_item', 'beverages/bill_details_item')
	add(config, '/bev/bill_details_time', 'beverages/bill_details_time')
	add(config, '/bev/edit_bill', 'beverages/edit_bill')
	# add(config, '/bev/add_item', 'addresses/details')

	add(config, '/min/edit_meta', 'minutes/edit_meta')
	add(config, '/min/edit_vv_meta', 'minutes/edit_vv_meta')
	add(config, '/min/edit_request', 'minutes/edit_request')
	add(config, '/min/list_v1', 'minutes/list_v1')
	add(config, '/min/list_v2', 'minutes/list_v2')
	add(config, '/min/view', 'minutes/view/base')
	add(config, '/min/edit_top', 'minutes/edit_top')

	add(config, '/selecttest/single', 'select/single')
	add(config, '/selecttest/multiple', 'select/multiple')
	add(config, '/selecttest/tags', 'select/tags')
	add(config, '/selecttest/live', 'select/live')


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
	server = make_server('127.0.0.1', 8077, app)
	server.serve_forever()
