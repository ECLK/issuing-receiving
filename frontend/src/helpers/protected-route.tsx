import React, { useContext } from "react";
import { Route, Redirect } from "react-router-dom";
import { AuthContext } from ".";

interface ProtectedRoutePropsInterface {
	path: string;
	component: React.FunctionComponent | React.ComponentClass;
	exact: boolean;
}
export const ProtectedRoute = (props: ProtectedRoutePropsInterface): React.ReactElement => {
	const { path, component, exact } = props;
	const { authState } = useContext(AuthContext);

	if (authState) {
		return <Route path={path} component={component} exact={exact} />;
	} else {
		return <Redirect to="/login" />;
	}
};
