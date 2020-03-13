import React from "react";
import { BrowserRouter, Switch, Redirect, Route } from "react-router-dom";
import { Authentication } from "./helpers/authentication";
import { routes } from "./configs";
import { ProtectedRoute } from "./helpers";
import { RouteInterface } from "./shared/models/routes";
import { HOME } from "./shared/constants";
import { AppLayout } from "./layout";

export const App = (): React.ReactElement => {
	return (
		<BrowserRouter>
			<Authentication>
				<AppLayout>
					<Switch>
						<Redirect exact={true} path="/" to={HOME} />
						{routes?.map((route: RouteInterface, index: number) => {
							if (route.protected) {
								return (
									<ProtectedRoute
										key={index}
										path={route.path}
										exact={route.exact}
										component={route.component}
									/>
								);
							} else {
								return (
									<Route
										key={index}
										path={route.path}
										exact={route.exact}
										component={route.component}
									/>
								);
							}
						})}
					</Switch>
				</AppLayout>
			</Authentication>
		</BrowserRouter>
	);
};
