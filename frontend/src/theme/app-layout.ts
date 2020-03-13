import { Theme } from "@material-ui/core";

export const appBar = (theme: Theme) => ({
	zIndex: theme.zIndex.drawer + 1
});

export const drawer = (theme: Theme) => ({
	top: "64px"
});
