# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 11:23:50 2024

@author: Camila
"""

import requests
import random
from collections import Counter

def fetch_mega_sena_results():
    url = "https://loteriascaixa-api.herokuapp.com/api/megasena"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception("Failed to fetch data from the API.")
    
    data = response.json()
    return [draw ['dezenas'] for  draw in data if 'dezenas' in draw]

def get_high_probability_numbers(n):
    results = fetch_mega_sena_results()
    
    # Flatten the list of results and count frequencies
    all_numbers = [int(num) for draw in results for num in draw]
    number_counts = Counter(all_numbers)
    
    # Sort by most common numbers
    most_common_numbers = [num for num, count in number_counts.most_common()]
    
    # Escolhe os 'n' numeros aleatorios dentro do top 15 numeros mais repetidos
    return random.sample(most_common_numbers[:100], n)

    print ("Top 10 numeros mais frequentes:", most_common_numbers[:100])

# Example usage:
n = 6  # Quantidade de numero que você quer
try:
    suggested_numbers = get_high_probability_numbers(n)
    print("Numeros sugeridos para a Mega Sena:", suggested_numbers)

except Exception as e:
   print ("Error:",e)