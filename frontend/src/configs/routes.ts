import { RouteInterface } from "../shared/models/routes";
import { SignIn } from "../pages/authentication";
import { Dashboard } from "../pages/dashboard";

export const routes: RouteInterface[] = [
	{
		component: SignIn,
		path: "/login",
		showOnMenu: false,
		protected: false,
		exact: true,
		name: "Login"
	},
	{
		component: Dashboard,
		path: "/dashboard",
		showOnMenu: true,
		protected: true,
		exact: true,
		name: "Home"
	}
];
