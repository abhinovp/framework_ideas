###########################################
# Author: AP
# A simple automation framework design with multiple generators
# Use-cases: Micro-service API calls, Async IO, Workloads and Test Automation frameworks.
###########################################


class butterfly_automation:
    '''
    BA Class for simplfying multiple calls and building workflows.
    '''

    def __init__(self):
        pass

    global_tc_count = 0

    def build_iteration_sets(self):
        '''
        # This def will store all data strcutures with constants that are needed,
        # to churn out iterated tuples/sets
        '''

        # Random data init- can simulate any dataset or incoming responses.
        C_test_data = [x for x in range(1,8,2)]
        B_test_data = [x for x in range(75,150,15)]
        A_test_data = [x for x in range(100,1100,100)]

        td_string = butterfly_automation.global_user_choice + "_test_data"
        current_test_data = eval(td_string)

        print("\n ################################################ \n Beginning workflow : ",butterfly_automation.global_user_choice)

        for every_ts in current_test_data:

            print("> BIS: ",every_ts)
            
            yield every_ts

        pass

    def gather_test_data(self):
        '''
        # This def will gather and prepare data sets that will be consumed by,
        # each outgoing payload.
        '''

        current_td = None

        for every_ts in butterfly_automation.build_iteration_sets(self):

            print("> GTD: ",every_ts)

            #transform every_ts accordingly
            current_td = every_ts

            yield current_td

    def prepare_payload(self):
        '''
        # This def will load and insert all test data into a default template
        # and prepare one such template for every transaction/test/API call
        '''

        current_payload = None

        for every_ts in butterfly_automation.gather_test_data(self):

            print("> PP: ",every_ts)

            #transform every_ts accordingly
            current_payload = every_ts

            yield current_payload

    def transact(self):
        '''
        # This def will post requests to API/ Perform SQL query/Module call and
        # get a response respectively.
        '''

        current_response = None

        for every_ts in butterfly_automation.prepare_payload(self):

            print("> TX: ",every_ts)

            #transform every_ts accordingly
            current_response = every_ts

            yield current_response

    def filter_response(self):
        '''
        # This def will hold the logic to filter the incoming response as per business logic
        # in-turn creating a list/tuple format ready to write to output files.
        '''

        current_output_set = None

        for every_ts in butterfly_automation.transact(self):

            print("> FR: ",every_ts)

            #transform every_ts accordingly
            current_output_set = every_ts

            yield current_output_set

    def output_writer(self):
        '''
        # This def will write all incoming lists/tuples onto excel/csv/xml/jsons
        '''
        
        current_payload = None

        for every_ts in butterfly_automation.filter_response(self):

            print("> OP: ",every_ts)

        butterfly_automation.global_tc_count += 1

    
    # Secondary framework preperation defs used to get/set context.
    

    def mapper(self):
        '''
        Utilize this def to create a map, containing all required modules and
        files converted as object references.
        Then use eval() to create just the current referred workflow sets.
        '''

    def get_user_choices(self,user_choice):
        '''
        To gather user inputs
        '''
        print("User selected workflow: ",user_choice)

        #setting current choice to global choice
        butterfly_automation.global_user_choice = user_choice

        #Calling loop starter.
        butterfly_automation.output_writer(self)



##########################################

butterfly = butterfly_automation()

# Enter options among A,B,C( Each option is a new workflow path)

# Async call could be used for all requested workflows.

workflows = ("A","B","C")
for each_wf in workflows:
    butterfly.get_user_choices(each_wf)
