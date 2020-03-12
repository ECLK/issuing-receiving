import { AuthAction } from "../shared/models";
import { SIGN_IN } from "../shared/constants";

export const signIn = (dispatch: React.Dispatch<AuthAction>, accessToken: string) => {
	localStorage.setItem("accessToken", accessToken);
	dispatch({ type: SIGN_IN, payload: accessToken });
};

export const getAccessToken = () => {
	return localStorage.getItem("accessToken");
};
