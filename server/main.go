package main

import (
	"flag"
	log "log/slog"
	"net"
	"time"

	"google.golang.org/grpc"
	"google.golang.org/grpc/peer"

	pb "github.com/codefever/grpc_mem_leaks/protos"
)

var addr = flag.String("addr", ":50051", "")

type server struct {
	pb.UnimplementedCounterServiceServer
}

func (s *server) Count(request *pb.CounterRequest, stream pb.CounterService_CountServer) error {
	p, _ := peer.FromContext(stream.Context())
	log.Info("start to serve", "request", request, "peer", p)

	for i := uint64(0); i < request.MaxNumber; i++ {
		time.Sleep(time.Second)

		err := stream.Send(&pb.CounterResponse{Number: i})
		if err != nil {
			//log.Error("failed to send response", "error", err)
			return err
		}
	}

	return nil
}

func main() {
	flag.Parse()

	listener, err := net.Listen("tcp", *addr)
	if err != nil {
		panic(err)
	}

	s := grpc.NewServer()
	pb.RegisterCounterServiceServer(s, &server{})

	if err := s.Serve(listener); err != nil {
		panic(err)
	}
}
