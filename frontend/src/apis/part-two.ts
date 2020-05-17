import { IssueStationeries, IssueBallotBoxes, ReceiveBallotBoxes, ReceiveStationeries } from "./../models";
import { http, Methods } from "../configs";
import { apiEndpoints } from "../constants";
import { AxiosRequestConfig } from "axios";
import { errorStatus } from "../utils";

export const listIssuedStationeries = (): Promise<any> => {
    const config: AxiosRequestConfig = {
        url: apiEndpoints.partTwo.issuedToSpo,
        method: Methods.GET
    };

    return http(config)
        .then((response) => {
            if (response?.status !== 200) {
                return Promise.reject(errorStatus(response?.status));
            }

            return Promise.resolve(response?.data);
        })
        .catch((error) => {
            return Promise.reject(error?.response?.data);
        });
};

export const listReceivedStationeries = (): Promise<any> => {
    const config: AxiosRequestConfig = {
        url: apiEndpoints.partTwo.receivedFromSpo,
        method: Methods.GET
    };

    return http(config)
        .then((response) => {
            if (response?.status !== 200) {
                return Promise.reject(errorStatus(response?.status));
            }

            return Promise.resolve(response?.data);
        })
        .catch((error) => {
            return Promise.reject(error?.response?.data);
        });
};

export const listIssuedBallotBoxed = (): Promise<any> => {
    const config: AxiosRequestConfig = {
        url: apiEndpoints.partTwo.issuedBallotBoxes,
        method: Methods.GET
    };

    return http(config)
        .then((response) => {
            if (response?.status !== 200) {
                return Promise.reject(errorStatus(response?.status));
            }

            return Promise.resolve(response?.data);
        })
        .catch((error) => {
            return Promise.reject(error?.response?.data);
        });
};

export const listReceivedBallotBoxed = (): Promise<any> => {
    const config: AxiosRequestConfig = {
        url: apiEndpoints.partTwo.issuedBallotBoxes,
        method: Methods.GET
    };

    return http(config)
        .then((response) => {
            if (response?.status !== 200) {
                return Promise.reject(errorStatus(response?.status));
            }

            return Promise.resolve(response?.data);
        })
        .catch((error) => {
            return Promise.reject(error?.response?.data);
        });
};

export const createIssuedStationeries = (data: IssueStationeries): Promise<any> => {
    const config: AxiosRequestConfig = {
        url: apiEndpoints.partTwo.issuedToSpo,
        method: Methods.POST,
        data: data
    };

    return http(config)
        .then((response) => {
            if (response?.status !== 201) {
                return Promise.reject(errorStatus(response?.status));
            }

            return Promise.resolve(response?.data);
        })
        .catch((error) => {
            return Promise.reject(error?.response?.data);
        });
};

export const createIssuedBallotBoxes = (data: IssueBallotBoxes): Promise<any> => {
    const config: AxiosRequestConfig = {
        url: apiEndpoints.partTwo.issuedBallotBoxes,
        method: Methods.POST,
        data: data
    };

    return http(config)
        .then((response) => {
            if (response?.status !== 201) {
                return Promise.reject(errorStatus(response?.status));
            }

            return Promise.resolve(response?.data);
        })
        .catch((error) => {
            return Promise.reject(error?.response?.data);
        });
};

export const createReceivedBallotBoxes = (data: ReceiveBallotBoxes): Promise<any> => {
    const config: AxiosRequestConfig = {
        url: apiEndpoints.partTwo.receivedBallotBoxes,
        method: Methods.POST,
        data: data
    };

    return http(config)
        .then((response) => {
            if (response?.status !== 201) {
                return Promise.reject(errorStatus(response?.status));
            }

            return Promise.resolve(response?.data);
        })
        .catch((error) => {
            return Promise.reject(error?.response?.data);
        });
};

export const createReceivedStationeries = (data: ReceiveStationeries): Promise<any> => {
    const config: AxiosRequestConfig = {
        url: apiEndpoints.partTwo.receivedFromSpo,
        method: Methods.POST,
        data: data
    };

    return http(config)
        .then((response) => {
            if (response?.status !== 201) {
                return Promise.reject(errorStatus(response?.status));
            }

            return Promise.resolve(response?.data);
        })
        .catch((error) => {
            return Promise.reject(error?.response?.data);
        });
};

export const updateIssuedStationeries = (id: number, data: IssueStationeries): Promise<any> => {
    const config: AxiosRequestConfig = {
        url: `${apiEndpoints.partTwo.issuedToSpo}${id}/`,
        method: Methods.PUT,
        data: data
    };

    return http(config)
        .then((response) => {
            if (response?.status !== 201) {
                return Promise.reject(errorStatus(response?.status));
            }

            return Promise.resolve(response?.data);
        })
        .catch((error) => {
            return Promise.reject(error?.response?.data);
        });
};

export const updateIssuedBallotBoxes = (id: number, data: IssueBallotBoxes): Promise<any> => {
    const config: AxiosRequestConfig = {
        url: `${apiEndpoints.partTwo.issuedBallotBoxes}${id}/`,
        method: Methods.PUT,
        data: data
    };

    return http(config)
        .then((response) => {
            if (response?.status !== 201) {
                return Promise.reject(errorStatus(response?.status));
            }

            return Promise.resolve(response?.data);
        })
        .catch((error) => {
            return Promise.reject(error?.response?.data);
        });
};

export const updateReceivedBallotBoxes = (id: number, data: ReceiveBallotBoxes): Promise<any> => {
    const config: AxiosRequestConfig = {
        url: `${apiEndpoints.partTwo.receivedBallotBoxes}${id}/`,
        method: Methods.PUT,
        data: data
    };

    return http(config)
        .then((response) => {
            if (response?.status !== 201) {
                return Promise.reject(errorStatus(response?.status));
            }

            return Promise.resolve(response?.data);
        })
        .catch((error) => {
            return Promise.reject(error?.response?.data);
        });
};

export const updateReceivedStationeries = (id: number, data: ReceiveStationeries): Promise<any> => {
    const config: AxiosRequestConfig = {
        url: `${apiEndpoints.partTwo.receivedFromSpo}${id}/`,
        method: Methods.PUT,
        data: data
    };

    return http(config)
        .then((response) => {
            if (response?.status !== 201) {
                return Promise.reject(errorStatus(response?.status));
            }

            return Promise.resolve(response?.data);
        })
        .catch((error) => {
            return Promise.reject(error?.response?.data);
        });
};

export const deleteIssuedStationeries = (id: number): Promise<any> => {
    const config: AxiosRequestConfig = {
        url: `${apiEndpoints.partTwo.issuedToSpo}${id}/`,
        method: Methods.DELETE
    };

    return http(config)
        .then((response) => {
            if (response?.status !== 204) {
                return Promise.reject(errorStatus(response?.status));
            }

            return Promise.resolve(response?.data);
        })
        .catch((error) => {
            return Promise.reject(error?.response?.data);
        });
};

export const deleteIssuedBallotBoxes = (id: number): Promise<any> => {
    const config: AxiosRequestConfig = {
        url: `${apiEndpoints.partTwo.issuedBallotBoxes}${id}/`,
        method: Methods.DELETE
    };

    return http(config)
        .then((response) => {
            if (response?.status !== 204) {
                return Promise.reject(errorStatus(response?.status));
            }

            return Promise.resolve(response?.data);
        })
        .catch((error) => {
            return Promise.reject(error?.response?.data);
        });
};

export const deleteReceivedBallotBoxes = (id: number): Promise<any> => {
    const config: AxiosRequestConfig = {
        url: `${apiEndpoints.partTwo.receivedBallotBoxes}${id}/`,
        method: Methods.DELETE
    };

    return http(config)
        .then((response) => {
            if (response?.status !== 204) {
                return Promise.reject(errorStatus(response?.status));
            }

            return Promise.resolve(response?.data);
        })
        .catch((error) => {
            return Promise.reject(error?.response?.data);
        });
};

export const deleteReceivedStationeries = (id: number): Promise<any> => {
    const config: AxiosRequestConfig = {
        url: `${apiEndpoints.partTwo.receivedFromSpo}${id}/`,
        method: Methods.DELETE
    };

    return http(config)
        .then((response) => {
            if (response?.status !== 204) {
                return Promise.reject(errorStatus(response?.status));
            }

            return Promise.resolve(response?.data);
        })
        .catch((error) => {
            return Promise.reject(error?.response?.data);
        });
};
