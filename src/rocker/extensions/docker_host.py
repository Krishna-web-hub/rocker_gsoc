import os
from .rocker_extension import RockerExtension
class DockerHost(RockerExtension):
    @staticmethod
    def get_name():
        return 'docker_host'
    def get_packages(self,clif_args):
        return ['docker-ce-cli']

    def get_docker_args(self, cliargs):
        args = '--volume /var/run/docker.sock:/var/run/docker.sock'
        try:
            docker_socket_gid = os.stat('/var/run/docker.sock').st_gid
            args += f' --group-add {docker_socket_gid}'
        except FileNotFoundError:
            print("Warning: /var/run/docker.sock not found, Docker is not added")

        return args
    @staticmethod
    def get_cli_opts(cli_parser):
        cli_parser.add_argument(
            '--docker-host',
            action='store_true',
            help='Mount the docker socket to control the host docker daemon from inside the container'
        )