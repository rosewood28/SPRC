/*
 * This is sample code generated by rpcgen.
 * These are only templates and you can use them
 * as a guideline for developing your own functions.
 */

#include "sum.h"

int *
get_sum_1_svc(int_pair *argp, struct svc_req *rqstp)
{
	static int  result;

	result = argp->a + argp->b;
    printf("SERVER: %d + %d = %d\n", argp->a, argp->b, result);

	return &result;
}
