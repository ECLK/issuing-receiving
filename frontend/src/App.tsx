import React from "react";
import { BrowserRouter, Switch, Redirect, Route } from "react-router-dom";
import { Authentication } from "./helpers/authentication";
import { routes } from "./configs";
import { ProtectedRoute } from "./helpers";
import { RouteInterface } from "./models/routes";
import { HOME } from "./constants";
import { AppLayout } from "./layout";

export const App = (): React.ReactElement => {
	return (
		<BrowserRouter>
			<Authentication>
				<Switch>
					<Redirect exact={true} path="/" to={HOME} />
					{routes?.map((route: RouteInterface, index: number) => {
						if (route.protected) {
							const routedComponent = (
								<ProtectedRoute
									key={index}
									path={route.path}
									exact={route.exact}
									component={route.component}
								/>
							);
							const render = route.appLayout ? (
								<AppLayout key={index}>{routedComponent}</AppLayout>
							) : (
								routedComponent
							);

							return render;
						} else {
							const routedComponent = (
								<Route key={index} path={route.path} exact={route.exact} component={route.component} />
							);
							const render = route.appLayout ? (
								<AppLayout key={index}>{routedComponent}</AppLayout>
							) : (
								routedComponent
							);

							return render;
						}
					})}
				</Switch>
			</Authentication>
		</BrowserRouter>
	);
};
