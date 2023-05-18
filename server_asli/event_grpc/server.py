import grpc
from concurrent import futures
import event_pb2
import event_pb2_grpc
from Database.models import Event
from Database.redis_server import CacheRedis
from mongoengine import *
connection=connect("Event")

class EventService(event_pb2_grpc.EventServiceServicer):
    def GetAllRecords(self, request, context):
        print("in the List Event / in the server project ")
        data = Event.objects().to_json()
        print(data)
        print(type(data))
        redis_obj = CacheRedis()
        x = redis_obj.set("EventAll", data)
        if x:
            print("sending")
            return event_pb2.Record(result=data)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor())
    event_pb2_grpc.add_EventServiceServicer_to_server(EventService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started. Listening on port 50051...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()