import time
#import schedule
import threading
from locust import User, task, between,events,SequentialTaskSet
import grpc
import random
from faker import Faker


from protos import vacancy_service_pb2_grpc, vacancy_service_pb2
from protos import rpc_create_vacancy_pb2, rpc_update_vacancy_pb2
from protos import auth_service_pb2,auth_service_pb2_grpc
from protos import rpc_signin_user_pb2
fake = Faker()
last_run_times = {}
#@events.request.add_listener

class VacancyTaskSequence(SequentialTaskSet):
    def on_start(self):
        self.created_vacancy_id = None
        self.start_time = time.time()
        self.fetch_thread = threading.Thread(target=self.fetch_all_vacancies_background)
        self.fetch_thread.start()

    def create_random_vacancy_data(self):
        return rpc_create_vacancy_pb2.CreateVacancyRequest(
            Title=fake.job(),
            Description=fake.text(),
            Division=random.randint(0, 3),
            Country=fake.country_code()
        )
    def fetch_all_vacancies_background(self):
        while True:
            self.fetch_all_vacancies()
            time.sleep(45)  

    
    def fetch_all_vacancies(self):
        current_time = time.time()

        page = 1
        limit = 10       
       
        
        
         # Fetch all vacancies
        try:
            while True:
                get_vacancies_request = vacancy_service_pb2.GetVacanciesRequest()
                vacancies = list(self.user.vacancy_stub.GetVacancies(get_vacancies_request,timeout=1))
                if not vacancies:
                    # Exit the loop if no more vacancies are returned
                    return
                for vacancy in vacancies:
                 
                    print(f"Fetched Vacancy: {vacancy.Title}, {vacancy.Description}")

                page += 1  # Go to the next page
                
                response_time = int((time.time() - current_time) * 1000)  # Convert to milliseconds
                events.request.fire(
                    request_type="grpc",
                    name="fetch_all_vacancies",
                    response_time=response_time,
                    response_length=0
            )                
            #custom_wait_function(self.__class__.__name__, 'fetch_all_vacancies', {'fetch_all_vacancies': 45})    
        except grpc.RpcError as e:
            print(f"Fetch All Vacancies failed: {e}")
            response_time = int((time.time() - current_time) * 1000)  # Convert to milliseconds

            events.request.fire(
                request_type="grpc",
                name="fetch_all_vacancies_fail",
                response_time=response_time,
                response_length=0
           )                            
             
          
    
    @task
    def create_vacancy(self):
        max_retries = 3
        start_time = time.time()

        for attempt in range(max_retries):
            try:
                create_request = self.create_random_vacancy_data()
                response = self.user.vacancy_stub.CreateVacancy(create_request)
                self.created_vacancy_id = response.vacancy.Id
                print(f"Created Vacancy ID: {self.created_vacancy_id}")
                response_time = int((time.time() - start_time) * 1000)
               
                events.request.fire(
                    request_type="grpc",
                    name="create_vacancy",
                    response_time=response_time,
                    response_length=0
                )
                break  
            except grpc.RpcError as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                if attempt == max_retries - 1:
                    response_time = int((time.time() - start_time) * 1000)

                    events.request.fire(
                            request_type="grpc",
                            name="create_vacancy_fail",
                            response_time=response_time,
                            response_length=0
                        )
       

        
         

       # custom_wait_function(self.__class__.__name__, 'create_vacancy', {'create_vacancy': 30})   
        
    @task
    def update_vacancy(self):
        start_time = time.time()

        if self.created_vacancy_id is not None:
            update_request = rpc_update_vacancy_pb2.UpdateVacancyRequest(
                Id=self.created_vacancy_id,
                Title=fake.job(),
                Description=fake.text(),
                Views=random.randint(0, 100),
                Division=random.randint(0, 3),
                Country=fake.country_code()
            )
            try:
                response = self.user.vacancy_stub.UpdateVacancy(update_request)
                print(f"Updated Vacancy: {response.vacancy}")
                response_time = int((time.time() - start_time) * 1000)  # Convert to milliseconds
                events.request.fire(
                    request_type="grpc",
                    name="update_vacancy",
                    response_time=response_time,
                    response_length=0
                )                                  
            except grpc.RpcError as e:
                print(f"Update Vacancy failed: {e}")
                response_time = int((time.time() - start_time) * 1000)  # Convert to milliseconds
                
                events.request.fire(
                    request_type="grpc",
                    name="update_vacancy_fail",
                    response_time=response_time,
                    response_length=0
                )                                    
        
    

    @task
    def fetch_vacancy(self):
        start_time = time.time()
        
        if self.created_vacancy_id is not None:
            fetch_request = vacancy_service_pb2.VacancyRequest(
                Id=self.created_vacancy_id
            )
            try:
                response = self.user.vacancy_stub.GetVacancy(fetch_request)
                response_time = int((time.time() - start_time) * 1000)  # Convert to milliseconds
                events.request.fire(
                    request_type="grpc",
                    name="fetch_vacancy",
                    response_time=response_time,
                    response_length=0
                )                            
                print(f"Fetched Vacancy: {response.vacancy}")
            except grpc.RpcError as e:
                print(f"Fetch Vacancy failed: {e}")
                response_time = int((time.time() - start_time) * 1000)  # Convert to milliseconds

                events.request.fire(
                    request_type="grpc",
                    name="fetch_vacancy_fail",
                    response_time=response_time,
                    response_length=0
                )       
                        
           
      
               
        
    
    @task
    def delete_vacancy(self):
        start_time = time.time()
        
        if self.created_vacancy_id is not None:
            delete_request = vacancy_service_pb2.VacancyRequest(
                Id=self.created_vacancy_id
            )
            try:
                self.user.vacancy_stub.DeleteVacancy(delete_request)
                print(f"Deleted Vacancy ID: {self.created_vacancy_id}")
                self.created_vacancy_id = None
                response_time = int((time.time() - start_time) * 1000)  # Convert to milliseconds
                events.request.fire(
                    request_type="grpc",
                    name="delete_vacancy",
                    response_time=response_time,
                    response_length=0
                )                                       
            except grpc.RpcError as e:
                print(f"Delete Vacancy failed: {e}")
         
            if VacancyUser.completed_user<2:
                VacancyUser.completed_user +=1
            else:
                VacancyUser.completed_user = 0
                       
        time.sleep(30)

    def on_stop(self):
        if self.fetch_thread.is_alive():
            # Signal the thread to stop if necessary
            # ...
            self.fetch_thread.join()

class VacancyUser(User):
    wait_time = between(1, 2) 
    completed_user = 0
    tasks = [VacancyTaskSequence]
    users = [
        {"email": "selimburakozturk@gmail.com", "password": "12"},
        {"email": "selimburakozturk@beykoz.edu.tr", "password": "12"},
        {"email": "sbozturkea@gmail.com", "password": "12"}
    ]

    def on_start(self):
        # Initialize gRPC channel and stub
        self.channel = grpc.insecure_channel('vacancies.cyrextech.net:7823')
        self.vacancy_stub = vacancy_service_pb2_grpc.VacancyServiceStub(self.channel)
        self.auth_stub = auth_service_pb2_grpc.AuthServiceStub(self.channel)
        self.created_vacancy_id = None
        self.user_credential = random.choice(self.users)
        self.users.remove(self.user_credential) 
        self.login()
        #self.background_thread = threading.Thread(target=self.fetch_all_vacancies_background)
        #self.background_thread.start()        

    def login(self):
        login_request = rpc_signin_user_pb2.SignInUserInput(
            email=self.user_credential['email'],
            password=self.user_credential['password']
        )
        try:
            response = self.auth_stub.SignInUser(login_request)
            print(f"{login_request}")
        except grpc.RpcError as e:
            print(f"Login failed: {e}")


    def on_stop(self):
        # Clean up (close the channel)
    
        self.channel.close()

