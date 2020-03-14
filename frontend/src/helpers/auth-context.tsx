import React from "react";
import { AuthContextInterface, AuthState } from "../models";

const initialState: AuthState = { authenticated: false, accessToken: null };
export const AuthContext = React.createContext<AuthContextInterface>({ authState: initialState, dispatch: () => {} });
