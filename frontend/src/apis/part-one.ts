import { http, Methods } from "../configs";
import { apiEndpoints } from "../constants";
import { AxiosRequestConfig } from "axios";
import { errorStatus } from "../utils";
import { ReportToWork } from "../models";

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
                array[index].date = date.toLocaleDateString();
            });
            return Promise.resolve(response.data as ReportToWork<true>);
        })
        .catch((error) => {
            Promise.reject(error);
        });
};
