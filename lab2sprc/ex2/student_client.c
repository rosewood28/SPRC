#include <stdio.h>
#include <rpc/rpc.h>

#include "student.h"
#include "string.h"

#define PROTOCOL "tcp"

int main(int argc, char const *argv[])
{
	CLIENT *handle;
	char *server_response = calloc(200, sizeof(char));
	struct student stud_struct;

	if (argc != 2) {
		fprintf(stderr, "Usage:\n\t%s <SERVER_ADDRESS>\n",
			argv[0]);
		return -1;
	}

	handle = clnt_create(argv[1], CHECKPROG, CHECKVERS, PROTOCOL);
	if (!handle) {
		perror("Failed to create client handle");
		clnt_pcreateerror(argv[0]);
		return -2;
	}

	stud_struct.name = calloc(200, sizeof(char));
	stud_struct.grupa = calloc(200, sizeof(char));

	strcpy(stud_struct.name, "Stan Sabina");
	strcpy(stud_struct.grupa, "341C3");

	strcpy(server_response, *(grade_1(&stud_struct, handle)));
	if (!server_response) {
		perror("RPC failed");
		return -3;
	}
	printf("%s\n", server_response);

	clnt_destroy(handle);
	xdr_free((xdrproc_t)xdr_int, server_response);
	xdr_free((xdrproc_t)xdr_int, stud_struct.name);
	xdr_free((xdrproc_t)xdr_int, stud_struct.grupa);

	return 0;
}