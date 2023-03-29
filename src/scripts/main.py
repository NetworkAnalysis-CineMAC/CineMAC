'''

CINEMAC. 

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

project for the course of Network Analysis - 2022/2023
Realized by.
	Andrea D'Arpa
	Maddalena Ghiotto		
	Chloe Papadopoulou

'''
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ast import literal_eval
from listReader import *
# creating the tables with pandas to interact with our datasets
# getting the current working directory
cwd = os.getcwd()


name = cwd+'/src/datasets/name.basics.tsv'
name_table = pd.read_csv(name , sep='\t', header=0)

title = cwd+'/src/datasets/title.principals.tsv'
title_table = pd.read_csv(title , sep='\t', header=0)

countries = cwd+'/src/datasets/countries.list.gz'
countries_table = get_movie_countries(countries)

movies = cwd+'/src/datasets/movie-links.list.gz'
movies_table = get_movie_links(movies)

'''
testing the tables
'''
print(movies_table)