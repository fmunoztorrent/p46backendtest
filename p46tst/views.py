from django.shortcuts import render
from django.http import HttpResponseNotFound
import itertools

context = {}

# Prints Foo/Bar/Numbers whitin 50 - 150 range
def index(request):

    context["index_foobar_endpoint_results"] = []
    for current_number in range(50, 151):

        # Display Foo if %5 == 0
        if current_number % 5 == 0:
            context["index_foobar_endpoint_results"].append("Foo")
            # Jumps to next loop
            continue

        # Display Foo if %7 == 0
        if current_number % 7 == 0:
            context["index_foobar_endpoint_results"].append("Bar")
            # Jumps to next loop
            continue

        context["index_foobar_endpoint_results"].append(current_number)

    return render(request, 'pages/index.html', context)


def single_digits_ep(request):

    param = request.GET.get("str",None)
    if param:

        """
        For example: if str is "arrb6...4xxbl5...eee5" then your program should return true 
        because there are exactly 3 dots between 6 and 4, and 3 dots between 5 and 5 at the end of the string.

        web_1  | ### all_numbers_list_counter ==>  0
        web_1  | #### sub_list_value ==> 6
        web_1  | ### all_numbers_list_counter ==>  1
        web_1  | #### sub_list_value ==> 4
        web_1  | #### sub_list_value ==> 5
        web_1  | ### all_numbers_list_counter ==>  2
        web_1  | #### sub_list_value ==> 5



        """

        all_numbers_list = []
        str_parts_list = str(param).split('...')
        if str_parts_list:
            for part in str_parts_list:
                numbers_in_str = [int(s) for s in part if s.isdigit()]
                if numbers_in_str:
                    all_numbers_list.append(numbers_in_str)

            all_numbers_list_counter = 0
            successful_results_list = []
            for sub_lis in all_numbers_list:

                print("### all_numbers_list_counter ==> ", all_numbers_list_counter)

                for sub_list_value in sub_lis:

                    print("#### sub_list_value ==>" , sub_list_value)

                    try:
                        next_inmediate_value = all_numbers_list[all_numbers_list_counter+1][0]
                    except IndexError:
                        continue

                    if (sub_list_value + next_inmediate_value) == 10:
                        successful_results_list.append([sub_list_value, next_inmediate_value, (sub_list_value+next_inmediate_value) ])

                    print("### next_inmediate_value ==> ", next_inmediate_value)

                all_numbers_list_counter += 1

            # Permutations
            #print(list(itertools.permutations(all_numbers_list)))

            return render(request, 'pages/str_valid.html', {"successful_results" : successful_results_list})

        else:
            print(str_parts_list)


    else:
        return HttpResponseNotFound("Requested action is not defined")