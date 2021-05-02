###########################################
# A scheduler class defined for butterfly framework
# Work in tandem with asynch_post_class
###########################################
# IMPORTs BELOW

import json,asyncio
##
from aiohttp.client_exceptions import ClientOSError, ClientConnectorError,\
    ClientConnectionError

############################
# Skel BELOW
# Idea is to build a scheduler to slice incoming input queries/calls into sets of 100/200/10/20 depending on target servers handling capabilites.
# For current implementation, i've set limit to 50 per set.

class slice_and_transact:
    
    
    def __init__(self):
        pass

    tx_list = {}
    
    
    def gather_input_sets(self):
            
        ## Step 1: Collect all DB Queries/ JSONs / Docs from prepare_payload def.
        slice_and_transact.collect_inp_sets(self)
        
        ## Step 2: Call parallel tx class.
        slice_and_transact.deploy_inp_sets(self)
        
        ## Step 3: Write results to excel.
        slice_and_transact.output_writer(self)
        
        pass
    
    def collect_inp_sets(self):

        every_incoming_tx = ""
        every_input_tx_list = None
                
        tx_counter = 1
        temp_all_reqs = []
        
        start = 0
        batch = 20

        for (every_incoming_json,every_input_tx_list) in prepare_payload(self):


            final_in_bite = json.dumps(every_incoming_json)
            
            ##### Appending all JSONs onto a temp list.
            temp_all_reqs.append(final_in_bite)
            
            ##### Appending all test inputs onto a global list.
            input_tuples.append(every_input_tx_list)

        
        #### Splitting all Reqs jsons into chuncks of 50 and attaching to global requests list.
        
        total_reqs_count = len(temp_all_reqs)
        
        while start<=total_reqs_count:
            
            fifty_reqs = temp_all_reqs[start:start+batch]
            requests_dict.append(fifty_reqs)
            start+=batch
        
        print("\n\n Number of bites collected to post :", tx_counter-1)
        pass
    
    

    def deploy_inp_sets(self):
        
        req_looper= 0

        ###
        ### Deploy all sets by iterating all sets in a dict.
        ###

        for each_50set in requests_dict:


            req_looper+=1
            try:   
                loop = asyncio.get_event_loop()
                future = asyncio.ensure_future(slice_and_transact.run(self,each_50set))
                loop.run_until_complete(future)

                #### Async sleep may not be on use. Hence blocking sleep.
                sleep(2)
                
            except KeyboardInterrupt:
                print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")
                print("\n Run interrupted by user, Halting now.")
                print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")
                ##break   
            
            except KeyError:
                
                print("\n I found no keys in API response")
                
            except ValueError:
                print("\n I found no values in API response")
                
            except AttributeError:
                print("\n I found no API response")
            
            
            except ClientOSError:
                print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")
                print("\n Too many request bites in queue at the Server. Check responses times manually and restart suite")
                print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")
                #break
                
            except TimeoutError:
                print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")
                print("\n The Server timed out on request bites. Check responses times manually and restart suite")
                print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")
                #break
             
            except ClientConnectorError:
                print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")
                print("\n The Server disconnected posting requests. Check responses times manually and restart suite")
                print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")
                #break
            
            except ClientConnectionError:
                print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")
                print("\n Too many request bites in queue at the Server. Check responses times manually and restart suite")
                print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")
                #break
                
            except:
                print("\n I found a error in API response")
                
        
        print("\n Number of RESPONSE Bites :", len(responses_list))

    def call_excel_writer(self):
        ###
        ### Writing out to excel / csv instead of default output_writer.
        ### Evaluate a dynamic writing def formatter.

        excel_writer_def = eval(excel_file_writer)
        excel_writer_def(self)
        
        print("\n Number of RESPONSE Bites to output :", len(responses_list))
            
        
        pass
