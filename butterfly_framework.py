###########################################
# A simple automation framework design with multiple generators
#
###########################################


class butterfly_automation:

    def __init__(self):
        pass

    global_tc_count = 0

    #####################################################################
    # This def will store all data strcutures with constants that are needed,
    # to churn out iterated tuples/sets
    #####################################################################

    def build_iteration_sets(self):

        current_is = None

        for every_ts in butterfly_automation.build_iteration_sets():

            yield current_is

        pass

    #####################################################################
    # This def will gather and prepare data sets that will be consumed by,
    # each outgoing payload.
    #####################################################################

    def gather_test_data(self):

        current_td = None

        for every_ts in butterfly_automation.build_iteration_sets():

            yield current_td

    #####################################################################
    # This def will load and insert all test data into a default template
    # and prepare one such template for every transaction/test/API call
    #####################################################################

    def prepare_payload(self):

        current_payload = None

        for every_ts in butterfly_automation.build_iteration_sets():

            yield current_payload

    #####################################################################
    # This def will post requests to API/ Perform SQL query/Module call and
    # get a response respectively.
    #####################################################################

    def transact(self):

        current_response = None

        for every_ts in butterfly_automation.prepare_payload():

            yield current_response

    #####################################################################
    # This def will hold the logic to filter the incoming response as per business logic
    # in-turn creating a list/tuple format ready to write to output files.
    #####################################################################

    def filter_response(self):

        current_output_set = None

        for every_ts in butterfly_automation.filter_response():

            yield current_output_set

    #####################################################################
    # This def will write all incoming lists/tuples onto excel/csv/xml/jsons
    #####################################################################

    def output_writer(self):

        current_payload = None

        for every_ts in butterfly_automation.filter_response():

            print("Writing to CSV/Excel/DB")

        butterfly_automation.global_tc_count += 1

    #####################################################################
    # Secondary framework preperation defs used to get/set context.
    #####################################################################

    def mapper(self):

        print("Define sets to map each input from user")
        print("Set global values")

    def get_user_choices(self):
        print("Get user choices")


##########################################

butterfly = butterfly_automation()

butterfly.get_user_choices()

