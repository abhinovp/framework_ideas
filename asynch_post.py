###########################################
# A Asynchrnous post class defined for butterfly framework
#
###########################################

import asyncio
from aiohttp import ClientSession
from aiohttp.client_exceptions import ClientOSError, ClientConnectorError,\
    ClientConnectionError

class asynch_post_class:
    
    async def fetch(self,post_singular_bite, session):
        ####
        # Prepare all required headers, transaction param, connectors before
        ####

        ## Sample API post def using the same.
        api_url = ""
        api_headers = ""
        async with session.post(api_url,headers=api_headers, data=post_singular_bite) as resp:
            
            return await resp.read()
    
    async def run(self,incoming_request_bites):
        
        ### incoming_request_bites meaning number of requests/queries/transactions etc.
        
        print("\n LEN OF incoming_request_bites: ",len(incoming_request_bites))
        
        tasks = []
        
        num_of_reqs = len(requests_dict)
        
        req_looper = 0
        
        batch_size = 10
        
        
        try: 
            
            #
            # Using a semaphore is optional for a small scale engine. 
            semaphore = asyncio.Semaphore(batch_size)
            
            async with semaphore:
                
                async with ClientSession() as session:
                    for t in incoming_request_bites:
                        
                        task = asyncio.ensure_future(asynch_post_class.fetch(self, t, session))
                        tasks.append(task)
                        
                        req_looper+=1
                        
            
                    responses = await asyncio.gather(*tasks)
                    
                    responses_list = responses_list + responses

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
            # break

        except TimeoutError:
            print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")
            print("\n The Server timed out on request bites. Check responses times manually and restart suite")
            print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")
            # break

        except ClientConnectorError:
            print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")
            print("\n The Server disconnected posting requests. Check responses times manually and restart suite")
            print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")
            # break

        except ClientConnectionError:
            print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")
            print("\n Too many request bites in queue at the Server. Check responses times manually and restart suite")
            print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")
            # break

        except:
            print("\n I found a error in API response")
        pass