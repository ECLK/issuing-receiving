import { RouteInterface } from "../models";
import { SignIn } from "../pages/authentication";
import { Dashboard } from "../pages/dashboard";
import { SignOut } from "../pages/authentication/sign-out";
import { LOGOUT, LOGIN, HOME, I_R_FROM_TOOLS_SPO, REPORT_TO_WORK } from "../constants";
import { IssueReceiveToolsFromSPO } from "../pages/issue-receive-tools-from-spo";
import { Work } from "@material-ui/icons";
import React from "react";
import { ReportToWork } from "../pages/report-to-work";

export const routes: RouteInterface[] = [
	{
		component: SignIn,
		path: LOGIN,
		showOnMenu: false,
		protected: false,
		exact: true,
		name: "Login",
		appLayout: false
	},
	{
		component: SignOut,
		path: LOGOUT,
		protected: true,
		exact: true,
		name: "Logout",
		showOnMenu: false,
		appLayout: false
	},
	{
		component: Dashboard,
		path: HOME,
		showOnMenu: false,
		protected: true,
		exact: true,
		name: "Home",
		appLayout: true
	},
	{
		component: ReportToWork,
		path: REPORT_TO_WORK,
		showOnMenu: true,
		protected: true,
		exact: true,
		name: "Report to Work",
		appLayout: true,
		icon:<Work/>
	}, {
		component: IssueReceiveToolsFromSPO,
		path: I_R_FROM_TOOLS_SPO,
		showOnMenu: true,
		protected: true,
		exact: true,
		name: "Issue and Receive tools from SPO",
		appLayout: true,
		icon: <Work />
	}
];
