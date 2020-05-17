import { http, Methods } from "../configs";
import { apiEndpoints } from "../constants";
import { AxiosRequestConfig } from "axios";
import { errorStatus } from "../utils";
import { ReportToWork, Staff } from "../models";

export const listBeforeElections = (): Promise<any> => {
    const config: AxiosRequestConfig = {
        url: apiEndpoints.partOne.beforeElection,
        method: Methods.GET
    };

    return http(config)
        .then((response) => {
            if (response.status !== 200) {
                return Promise.reject(errorStatus(response.status));
            }
            const reportToWork = response.data as ReportToWork<true>[];

            reportToWork.forEach((value: ReportToWork<true>, index: number, array: ReportToWork<true>[]) => {
                const date = new Date(value.time);
                array[index].time = date.toLocaleTimeString();
                array[ index ].date = date.toLocaleDateString();
                array[ index ].timestamp = date.getTime();
            });
            return Promise.resolve(response.data as ReportToWork<true>);
        })
        .catch((error) => {
            Promise.reject(error);
        });
};

export const createBeforeElection = (data: ReportToWork<false>): Promise<any> => {
    const config: AxiosRequestConfig = {
        url: apiEndpoints.partOne.beforeElection,
        method: Methods.POST,
        data: data
    };

    return http(config)
        .then((response) => {
            if (response.status !== 201) {
                return Promise.reject(errorStatus(response.status));
            }

            return Promise.resolve(response.data);
        })
        .catch((error) => {
            return Promise.reject(error?.response?.data);
        });
};

export const updateBeforeElection = (id:number, data: ReportToWork<false>): Promise<any> => {
    const config: AxiosRequestConfig = {
        url: `${apiEndpoints.partOne.beforeElection}${id}/`,
        method: Methods.PUT,
        data: data
    };

    return http(config)
        .then((response) => {
            if (response.status !== 200) {
                return Promise.reject(errorStatus(response.status));
            }

            return Promise.resolve(response.data);
        })
        .catch((error) => {
            return Promise.reject(error?.response?.data);
        });
};

export const deleteBeforeElection = (id: number):Promise<any> => {
    const config: AxiosRequestConfig = {
        url: `${apiEndpoints.partOne.beforeElection}${id}/`,
        method: Methods.DELETE
    };

    return http(config)
        .then((response) => {
            if (response.status !== 204) {
                return Promise.reject(errorStatus(response.status));
            }

            return Promise.resolve(response.data);
        })
        .catch((error) => {
            return Promise.reject(error?.response?.data);
        });
}
