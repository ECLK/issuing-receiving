import React from "react";
import { AuthContextInterface, AuthState } from "../shared/models";

const initialState: AuthState = { authenticated: false, accessToken: null };
export const AuthContext = React.createContext<AuthContextInterface>({ authState: initialState, dispatch: () => {} });
