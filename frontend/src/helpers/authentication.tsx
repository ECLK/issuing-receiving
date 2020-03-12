import React, { useEffect, useReducer } from "react";
import { AuthContext } from "./auth-context";
import { AuthState, AuthAction } from "../shared/models";
import { SIGN_IN, SIGN_OUT } from "../shared/constants";
import { getAccessToken } from "../utils";

const reducer = (state: AuthState, action: AuthAction): AuthState => {
	switch (action.type) {
		case SIGN_IN:
			return { authenticated: true, accessToken: action.payload };
		case SIGN_OUT:
			return { authenticated: false, accessToken: null };
		default:
			return { ...state };
	}
};

const initialState: AuthState = { authenticated: false, accessToken: null };
export const Authentication = (props: React.PropsWithChildren<any>): React.ReactElement => {
	const [authState, dispatch] = useReducer(reducer, initialState);
	const { children } = props;

	useEffect(() => {
		// Check if access token is there in the local storage
		if (getAccessToken()) {
			dispatch({ type: SIGN_IN, payload: getAccessToken() });
		}
	}, []);

	return <AuthContext.Provider value={{ authState, dispatch }}>{children}</AuthContext.Provider>;
};
