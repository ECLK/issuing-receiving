import { getAccessToken } from "./../utils/sign-in";
import axios, { AxiosRequestConfig } from "axios";

export enum Methods {
    GET = "GET",
    POST = "POST",
    DELETE = "DELETE",
    PATCH = "PATCH",
    PUT = "PUT"
}

const config: AxiosRequestConfig = {
    baseURL: "http://127.0.0.1:8000/"
};

const httpClient = axios.create({
    ...config
});

httpClient.interceptors.request.use(
    (config) => {
        if (getAccessToken()) {
            config.headers = {
                Authorization: `bearer ${getAccessToken()}`
            };
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

export const http = httpClient;
