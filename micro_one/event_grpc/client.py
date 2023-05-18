import grpc
from event_grpc import event_pb2
from event_grpc import event_pb2_grpc

def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = event_pb2_grpc.EventServiceStub(channel)

    response = stub.GetAllRecords(event_pb2.query(query="EventObjectsAll"))
    return str(response)


# if __name__ == "__main__":
#     run()