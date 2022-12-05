#!#!/usr/bin/env python3
import requests
url = 'https://docs.google.com/forms/u/1/d/e/1FAIpQLSeHU1XJzgUtdIxMC-7CIpq2fg2zL_2zHYGPpOm-JHOrKoBi9w/formResponse'
form_data = {'entry.839337160':'this is a test'}
r = requests.post(url, data=form_data)
