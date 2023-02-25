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

import os                        # for reading directories
import urllib.request            # for downloading files
import gzip                      # for dealing with gzip files
import re                        # for parsing original files
import pandas as pd              # for csv
import multiprocessing as mp     # for multithread version




# get the year of a movie from its title
def get_year_single_movie(title):
    return int(title[-5:-1])

# get dataframe of movie links from gzip file
def get_movie_links(filename):
    regex_movie = re.compile(r'^([^\"][^\(]+ \(\d+\))$')
    regex_links = re.compile(r"\((features|references|follows|spoofs|remake of|spin off from) ([^\"][^\(]+ \(\d+\))\)") #version of??
    result = {"movie": [], "cites": []}
    state = 0 # read movie or reference
    movie = ""
    with gzip.open(filename) as f:
        for line in f:
            line = line.decode("ISO-8859-1")
            if state == 0:  # read movie
                res = re.findall(regex_movie, line)
                if res != []:
                    movie = res[0]
                    state = 1
            elif state == 1: # read reference
                if line == "\n":
                    state = 0
                else:
                    res = re.findall(regex_links, line)
                    if res != []:
                        cites = res[0][1]
                        if(get_year_single_movie(movie) >= get_year_single_movie(cites)):
                            result["movie"] += [movie]
                            result["cites"] += [cites]
    return pd.DataFrame(result, columns = ["movie", "cites"])

# get dataframe of movie countries from gzip file
def get_movie_countries(filename):
    regex_movie_country = re.compile(r'^([^\"][^\(]+ \(\d+\))\t+(.+)$')
    result = {"movie": [], "country": []}
    with gzip.open(filename) as f:
        for line in f:
            line = line.decode("ISO-8859-1")
            res = re.findall(regex_movie_country, line)
            if res != []:
                result["movie"] += [res[0][0]]
                result["country"] += [res[0][1]]
    return pd.DataFrame(result, columns = ["movie", "country"])

