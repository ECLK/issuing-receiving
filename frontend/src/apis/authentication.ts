import { errorStatus } from "../utils";
import { Methods, http } from "../configs";
import { apiEndpoints } from "../constants";
import { AxiosRequestConfig } from "axios";


export const authenticate = (username: string, password: string): Promise<any> => {
    const config: AxiosRequestConfig = {
        url: apiEndpoints.auth,
        method: Methods.POST,
        data: {
            username,
            password
        }
    };

    return http(config)
        .then((response) => {
            if (response.status !== 200) {
                return Promise.reject(errorStatus(response.status));
            }

            return Promise.resolve(response.data);
        })
        .catch((error) => {
            return Promise.reject(error);
        });
};

export const getStaffDetails = (): Promise<any> => {
    const config: AxiosRequestConfig = {
        url: apiEndpoints.staffs.getMyDetails,
        method: Methods.GET
    };

    return http(config)
        .then((response) => {
            if (response.status !== 200) {
                return Promise.reject(errorStatus(response.status));
            }

            return Promise.resolve(response.data);
        })
        .catch((error) => {
            return Promise.reject(error);
        });
};
