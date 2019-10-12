from django.shortcuts import render
from search.models import Data
# from search.serializers import Data_serializer
from django.http import *
import json
import requests

def search_function(request):
	search_word = request.GET["word"]
	# print(type(search_word))

	exact_word = Data.objects.filter(word = search_word)
	len_exact_word = len(exact_word)
	# print(len_exact_word)
	startwith_word = Data.objects.filter(word__startswith = search_word).order_by('-frequency')[:25]
	len_startwith_word = len(startwith_word)
    


	# if len_exact_word==1:
	# 	return_list = [exact_word[i].word for i in range(len_exact_word)]
	# 	print("1")
	# else:
	# 	startwith_word = Data.objects.filter(word__startswith = search_word).order_by('-frequency')[:25]
	# 	len_startwith_word = len(startwith_word)
	# 	startword_set ={startwith_word[i].word for i in range(len_startwith_word)}
	# 	if len_startwith_word<25:
	# 		extra_word = 25 - len_startwith_word
	# 		contains_word = Data.objects.filter(word__contains= search_word).exclude(word__startswith = search_word).order_by('-frequency')[:extra_word]
	# 		len_contains_word = len(contains_word)
	# 		contains_set = {contains_word[i].word for i in range(len_contains_word)}
	# 		return_list = list(startword_set.union(contains_set))
	# 	else:
	# 		return_list = list(startword_set)
	# print(return_list)
	# return JsonResponse({"key":return_list})	

	startwith_word = Data.objects.filter(word__startswith = search_word).order_by('-frequency')[:25]
	len_startwith_word = len(startwith_word)
	startword_set =[startwith_word[i].word for i in range(len_startwith_word)]
	print(startword_set)
	if len_startwith_word<25:
		extra_word = 25 - len_startwith_word
		contains_word = Data.objects.filter(word__contains= search_word).exclude(word__startswith = search_word).order_by('-frequency')[:extra_word]
		len_contains_word = len(contains_word)
		contains_set = [contains_word[i].word for i in range(len_contains_word)]
		startword_set.extend(contains_set)
		return_list = startword_set
		print(startword_set)
	else:
		return_list = startword_set
	
	return JsonResponse({"key":return_list})		
	

			
		# elif (len_startwith_word==25):
		# 	return_list = [startwith_word[i].word for i in range(len_startwith_word)]
		# 	print ("2")

		# elif (len_startwith_word >0 & len_startwith_word<25):
		# 	return_list=[]
		# 	print("3")
		# 	# return_list = [startwith_word[i].word for i in range(len_startwith_word)]
		# 	# return_list = [startwith_word[i].word for i in range(len_startwith_word)]
		# 	for i in range(len_startwith_word):
		# 		return_list.append(startwith_word[i].word)
		# 	remaining_word = 25 - len_starting_word
		# 	contains_word = Data.objects.filter(word__contains= search_word).order_by('-frequency')
		# 	return_list_2 = [contains_word[i].word for i in range(remaining_word)]
		# 	return_list.extend(return_list_2)
		# # print (return_list)

	return JsonResponse({"key": return_list})
        







	
# Create your views here.
