import React from "react";
import { BrowserRouter, Switch, Redirect, Route } from "react-router-dom";
import { Authentication } from "./helpers/authentication";
import { routes, RouteInterface } from "./configs";
import { ProtectedRoute } from "./helpers";

export const App = (): React.ReactElement => {
	return (
		<BrowserRouter>
			<Authentication>
				<Switch>
					<Redirect exact={true} path="/" to="" />
					{routes?.map((route: RouteInterface) => {
						if (route.protected) {
							return <ProtectedRoute path={route.path} exact={route.exact} component={route.component} />;
						} else {
							return <Route path={route.path} exact={route.exact} component={route.component} />;
						}
					})}
				</Switch>
			</Authentication>
		</BrowserRouter>
	);
};
