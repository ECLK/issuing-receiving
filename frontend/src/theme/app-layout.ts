import { Theme } from "@material-ui/core";
import { TOP_BAR_HEIGHT, DRAWER_WIDTH } from "./constants";

export const appBar = (theme: Theme) => ({
	zIndex: theme.zIndex.drawer + 1
});

export const appBarTitle = (theme: Theme) => ({
	flexGrow: 1
});

export const drawerPaper = (theme: Theme) => ({
	top: TOP_BAR_HEIGHT,
	width: DRAWER_WIDTH
});

export const drawer = (theme: Theme) => ({
	width: DRAWER_WIDTH
});
