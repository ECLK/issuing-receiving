import { RouteInterface } from "../shared/models/routes";
import { SignIn } from "../pages/authentication";
import { Dashboard } from "../pages/dashboard";
import { SignOut } from "../pages/authentication/sign-out";
import { LOGOUT, LOGIN, HOME } from "../shared/constants";

export const routes: RouteInterface[] = [
	{
		component: SignIn,
		path: LOGIN,
		showOnMenu: false,
		protected: false,
		exact: true,
		name: "Login"
	},
	{
		component: SignOut,
		path: LOGOUT,
		protected: true,
		exact: true,
		name: "Logout",
		showOnMenu: false
	},
	{
		component: Dashboard,
		path: HOME,
		showOnMenu: true,
		protected: true,
		exact: true,
		name: "Home"
	}
];
