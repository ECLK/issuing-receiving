import { AuthAction } from "../models";
import { SIGN_IN, ACCESS_TOKEN } from "../constants";

export const signIn = (dispatch: React.Dispatch<AuthAction>, accessToken: string) => {
	localStorage.setItem(ACCESS_TOKEN, accessToken);
	dispatch({ type: SIGN_IN, payload: accessToken });
};

export const getAccessToken = () => {
	return localStorage.getItem(ACCESS_TOKEN);
};
