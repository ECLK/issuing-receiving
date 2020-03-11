import React from "react";
import { AuthContextInterface, initialState } from "./authentication";

export const AuthContext = React.createContext<AuthContextInterface>({ authState: initialState, dispatch: () => {} });
