# -*- coding: UTF-8 -*-

import requests
import json

#insert your host's URL below
host = 'http://localhost:3011'
token = requests.get('{0}/token'.format(host)).content

def author_name(set_author_name):
    def get_author_name(*args, **kwargs):
        params = set_author_name()
        json_params = json.dumps(params, indent=2)
        print json_params
        response = requests.post('{0}/{1}/authorName'.format(host, token),json = params)
        print response
        return set_author_name(*args, **kwargs)
    return get_author_name

def author_email(set_author_email):
    def get_author_email(*args, **kwargs):
        params = set_author_email()
        json_params = json.dumps(params, indent=2)
        print json_params
        response = requests.post('{0}/{1}/authorEmail'.format(host, token),json = params)
        print response
        return set_author_email(*args, **kwargs)
    return get_author_email

def context(set_context):
    def get_context(*args, **kwargs):
        params = set_context()
        json_params = json.dumps(params, indent=2)
        print json_params
        response = requests.post('{0}/{1}/context'.format(host, token),json = params)
        print response
        return set_context(*args, **kwargs)
    return get_context

def organization(set_organization):
    def get_organization(*args, **kwargs):
        params = set_organization()
        json_params = json.dumps(params, indent=2)
        print json_params
        response = requests.post('{0}/{1}/organization'.format(host, token),json = params)
        print response
        return set_organization(*args, **kwargs)
    return get_organization

def experiment_tile(set_experiment_title):
    def get_experiment_title(*args, **kwargs):
        params = set_experiment_title()
        json_params = json.dumps(params, indent=2)
        print json_params
        response = requests.post('{0}/{1}/experimentTitle'.format(host, token),json = params)
        print response
        return set_experiment_title(*args, **kwargs)
    return get_experiment_title

def algorithm(set_algorithm):
    def get_algorithm(*args, **kwargs):
        params = set_algorithm()
        json_params = json.dumps(params, indent=2)
        print json_params
        response = requests.post('{0}/{1}/experimentAlgorithm'.format(host, token),json = params)
        print response
        return set_algorithm(*args, **kwargs)
    return get_algorithm

def dataset_name(set_dataset):
    def get_dataset(*args, **kwargs):
        params = set_dataset()
        json_params = json.dumps(params, indent=2)
        print json_params
        response = requests.post('{0}/{1}/experimentDataset'.format(host, token),json = params)
        print response
        return set_dataset(*args, **kwargs)
    return get_dataset

def hardware(set_hardware_info):
    def get_hardware_info(*args, **kwargs):
        params = set_hardware_info()
        json_params = json.dumps(params, indent=2)
        print json_params
        response = requests.post('{0}/{1}/experimentHardware'.format(host, token),json = params)
        print response
        return set_hardware_info(*args, **kwargs)
    return get_hardware_info

def sampling_method(set_sampling_method):
    def get_sampling_method(*args, **kwargs):
        params = set_sampling_method()
        json_params = json.dumps(params, indent=2)
        print json_params
        response =requests.post('{0}/{1}/experimentSamplingMethod'.format(host, token),json = params)
        print response
        return set_sampling_method(*args, **kwargs)
    return get_sampling_method

def start(argument):
    def get_start(*args, **kwargs):
        params = argument()
        response = requests.post('http://localhost:8080/rest4mex/resources/experiment/start',)
        print response
        return argument(*args, **kwargs)
    return get_start

print token
