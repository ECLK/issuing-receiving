import React, { useEffect, ReducerAction, useReducer } from "react";
import { AuthContext } from "./auth-context";

const SIGN_IN = "sign_in";
const SIGN_OUT = "sign_out";

interface AuthState {
	authenticated: boolean;
	accessToken: string | null;
}

interface AuthAction {
	type: "sign_in" | "sign_out";
	payload: string | null;
}

export const initialState: AuthState = { authenticated: false, accessToken: null };

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
export interface AuthContextInterface {
	authState: AuthState;
	dispatch: React.Dispatch<AuthAction>;
}
export const Authentication = (props: React.PropsWithChildren<any>): React.ReactElement => {
	const [authState, dispatch] = useReducer(reducer, initialState);
	const { children } = props;

	useEffect(() => {
		// Check if access token is there in the local storage
		if (true) {
			dispatch({ type: SIGN_IN, payload: "access_token_mock" });
		}
	}, []);

	return <AuthContext.Provider value={{ authState, dispatch }}>{children}</AuthContext.Provider>;
};
