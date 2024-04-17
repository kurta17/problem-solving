#include <arpa/inet.h>
#include <netdb.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>

#define MAX 80
#define PORT 8080
#define SA struct sockaddr

void handle_client(int connfd1, int connfd2) {
    char buff[MAX];
    int n;

    for (;;) {
        bzero(buff, sizeof(buff));

        n = read(connfd1, buff, sizeof(buff));
        if (n == 0 || strncmp(buff, "exit", 4) == 0) {
            printf("Client 1 disconnected.\n");
            break;
        }
        printf("From Client 1: %s\n", buff);
        write(connfd2, buff, n);

        bzero(buff, sizeof(buff));

        n = read(connfd2, buff, sizeof(buff));
        if (n == 0 || strncmp(buff, "exit", 4) == 0) {
            printf("Client 2 disconnected.\n");
            break;
        }
        printf("From Client 2: %s\n", buff);
        write(connfd1, buff, n);
    }

    close(connfd1);
    close(connfd2);
}

int main() {
    int sockfd, connfd1, connfd2, len;
    struct sockaddr_in servaddr, cli;

    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd == -1) {
        printf("Socket creation failed...\n");
        exit(0);
    } else {
        printf("Socket successfully created..\n");
    }

    bzero(&servaddr, sizeof(servaddr));

    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY);  
    servaddr.sin_port = htons(PORT);

    if (bind(sockfd, (SA*)&servaddr, sizeof(servaddr)) != 0) {
        printf("Socket bind failed...\n");
        exit(0);
    } else {
        printf("Socket successfully bound..\n");
    }

    if (listen(sockfd, 5) != 0) {
        printf("Listen failed...\n");
        exit(0);
    } else {
        printf("Server listening..\n");
    }

    len = sizeof(cli);

    printf("Waiting for two clients...\n");

    connfd1 = accept(sockfd, (SA*)&cli, &len);
    if (connfd1 < 0) {
        printf("Server accept failed for client 1...\n");
        exit(0);
    }
    printf("Client 1 connected.\n");

    connfd2 = accept(sockfd, (SA*)&cli, &len);
    if (connfd2 < 0) {
        printf("Server accept failed for client 2...\n");
        exit(0);
    }
    printf("Client 2 connected.\n");

    handle_client(connfd1, connfd2);

    close(sockfd);

    return 0;
}