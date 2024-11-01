/*
 * Please do not edit this file.
 * It was generated using rpcgen.
 */

#include "rpcinterface.h"

bool_t
xdr_request_data (XDR *xdrs, request_data *objp)
{
	register int32_t *buf;

	 if (!xdr_string (xdrs, &objp->user_id, 15))
		 return FALSE;
	 if (!xdr_string (xdrs, &objp->request_token, 15))
		 return FALSE;
	 if (!xdr_string (xdrs, &objp->op_type, 15))
		 return FALSE;
	 if (!xdr_string (xdrs, &objp->resource, 50))
		 return FALSE;
	 if (!xdr_string (xdrs, &objp->access_token, 15))
		 return FALSE;
	return TRUE;
}

bool_t
xdr_response_data (XDR *xdrs, response_data *objp)
{
	register int32_t *buf;

	 if (!xdr_string (xdrs, &objp->request_token, 15))
		 return FALSE;
	 if (!xdr_string (xdrs, &objp->access_token, 15))
		 return FALSE;
	 if (!xdr_string (xdrs, &objp->refresh_token, 15))
		 return FALSE;
	 if (!xdr_string (xdrs, &objp->permision_response, 50))
		 return FALSE;
	return TRUE;
}
