# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import protos.auth_service_pb2 as auth__service__pb2
import protos.rpc_signin_user_pb2 as rpc__signin__user__pb2
import protos.rpc_signup_user_pb2 as rpc__signup__user__pb2
import protos.user_pb2 as user__pb2


class AuthServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SignUpUser = channel.unary_unary(
                '/pb.AuthService/SignUpUser',
                request_serializer=rpc__signup__user__pb2.SignUpUserInput.SerializeToString,
                response_deserializer=user__pb2.GenericResponse.FromString,
                )
        self.SignInUser = channel.unary_unary(
                '/pb.AuthService/SignInUser',
                request_serializer=rpc__signin__user__pb2.SignInUserInput.SerializeToString,
                response_deserializer=rpc__signin__user__pb2.SignInUserResponse.FromString,
                )
        self.VerifyEmail = channel.unary_unary(
                '/pb.AuthService/VerifyEmail',
                request_serializer=auth__service__pb2.VerifyEmailRequest.SerializeToString,
                response_deserializer=user__pb2.GenericResponse.FromString,
                )


class AuthServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SignUpUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SignInUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VerifyEmail(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SignUpUser': grpc.unary_unary_rpc_method_handler(
                    servicer.SignUpUser,
                    request_deserializer=rpc__signup__user__pb2.SignUpUserInput.FromString,
                    response_serializer=user__pb2.GenericResponse.SerializeToString,
            ),
            'SignInUser': grpc.unary_unary_rpc_method_handler(
                    servicer.SignInUser,
                    request_deserializer=rpc__signin__user__pb2.SignInUserInput.FromString,
                    response_serializer=rpc__signin__user__pb2.SignInUserResponse.SerializeToString,
            ),
            'VerifyEmail': grpc.unary_unary_rpc_method_handler(
                    servicer.VerifyEmail,
                    request_deserializer=auth__service__pb2.VerifyEmailRequest.FromString,
                    response_serializer=user__pb2.GenericResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pb.AuthService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AuthService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SignUpUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.AuthService/SignUpUser',
            rpc__signup__user__pb2.SignUpUserInput.SerializeToString,
            user__pb2.GenericResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SignInUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.AuthService/SignInUser',
            rpc__signin__user__pb2.SignInUserInput.SerializeToString,
            rpc__signin__user__pb2.SignInUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VerifyEmail(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.AuthService/VerifyEmail',
            auth__service__pb2.VerifyEmailRequest.SerializeToString,
            user__pb2.GenericResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
