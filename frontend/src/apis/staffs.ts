import { http, Methods } from "../configs";
import { apiEndpoints } from "../constants";
import { AxiosRequestConfig } from "axios";
import { errorStatus } from "../utils";
import { Staff } from "../models";

export const listStaffs = (): Promise<any> => {
    const config = {
        url: apiEndpoints.staffs.staffs,
        method: Methods.GET
    };

    return http(config).then((response) => {
        if (response.status !== 200) {
            return Promise.reject(errorStatus(response.status));
        }

        return Promise.resolve(response.data);
    }).catch(error => {
        return Promise.reject(error?.response?.data);
    })
};


export const createStaff = (data: Staff): Promise<any> => {
    const config = {
        url: apiEndpoints.staffs.staffs,
        method: Methods.POST,
        data
    }

    return http(config).then((response) => {
        if (response.status !== 201) {
            return Promise.reject(errorStatus(response.status));
        }

        return Promise.resolve(response.data);
    }).catch(error => {
        return Promise.reject(error ?.response ?.data);
    })
}
