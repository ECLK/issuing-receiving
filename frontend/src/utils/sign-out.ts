import { AuthAction } from "../shared/models";
import { SIGN_OUT, ACCESS_TOKEN } from "../shared/constants";

export const signOut = (dispatch: React.Dispatch<AuthAction>) => {
	localStorage.removeItem(ACCESS_TOKEN);
	dispatch({ type: SIGN_OUT, payload: null });
};
