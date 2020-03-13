import { AuthAction } from "../shared/models";
import { SIGN_IN, ACCESS_TOKEN } from "../shared/constants";

export const signIn = (dispatch: React.Dispatch<AuthAction>, accessToken: string) => {
	localStorage.setItem(ACCESS_TOKEN, accessToken);
	dispatch({ type: SIGN_IN, payload: accessToken });
};

export const getAccessToken = () => {
	return localStorage.getItem(ACCESS_TOKEN);
};
