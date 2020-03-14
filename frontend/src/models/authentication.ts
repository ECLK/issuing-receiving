export interface AuthState {
	authenticated: boolean;
	accessToken: string | null;
}

export interface AuthAction {
	type: "sign_in" | "sign_out";
	payload: string | null;
}

export interface AuthContextInterface {
	authState: AuthState;
	dispatch: React.Dispatch<AuthAction>;
}
