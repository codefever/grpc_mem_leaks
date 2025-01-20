package main

import (
	"fmt"
	log "log/slog"
	"net"
	"time"

	"google.golang.org/grpc"

	pb "github.com/codefever/grpc_mem_leaks/protos"
)

type server struct {
	pb.UnimplementedCounterServiceServer
}

func (s *server) Count(request *pb.CounterRequest, stream pb.CounterService_CountServer) error {
	log.Info("start to serve", "request", request)

	for i := uint64(0); i < request.MaxNumber; i++ {
		time.Sleep(time.Second)

		err := stream.Send(&pb.CounterResponse{Number: i})
		if err != nil {
			log.Error("failed to send response", "error", err)
			return err
		}
	}

	return nil
}

func main() {
	listener, err := net.Listen("tcp", fmt.Sprintf(":%d", 50051))
	if err != nil {
		panic(err)
	}

	s := grpc.NewServer()
	pb.RegisterCounterServiceServer(s, &server{})

	if err := s.Serve(listener); err != nil {
		panic(err)
	}
}
