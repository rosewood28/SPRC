struct request_data {
    string user_id<15>; /*request_auth and request_access*/
    string request_token<15>; /*request_access*/

    string op_type<15>; /*validate_action*/
    string resource<50>; /*validate_action*/
    string access_token<15>; /*validate_action*/
};

struct response_data {
    string request_token<15>; /*request_auth (ori token ori usernotfound)*/
    string access_token<15>; /*request_access*/
    string refresh_token<15>; /*request_access*/
    string permision_response<50>; /*validate_action*/
};

program REQUEST_AUTH_PROG {
    version REQUEST_AUTH_VERS {
        response_data request_auth(struct request_data) = 1;
        response_data request_access(struct request_data) = 2;
        response_data validate_action(struct request_data) = 3;
        response_data approve_request(struct request_data) = 4;
    } = 1;
} = 1;