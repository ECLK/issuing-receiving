import React from "react";
import {
	AppBar,
	Toolbar,
	IconButton,
	Typography,
	Button,
	Drawer,
	List,
	ListItem,
	ListItemIcon,
	ListItemText
} from "@material-ui/core";
import { Mail } from "@material-ui/icons";
import useStyles from "../theme";

export const AppLayout = (props: React.PropsWithChildren<any>): React.ReactElement => {
	const classes = useStyles();

	return (
		<>
			<AppBar position="static" className={classes.appBar}>
				<Toolbar>
					<IconButton edge="start" color="inherit" aria-label="menu"></IconButton>
					<Typography variant="h6">Issuing and Receiving App</Typography>
					<Button color="inherit">Login</Button>
				</Toolbar>
			</AppBar>
			<Drawer variant="permanent" classes={{ paper: classes.drawer }}>
				<List>
					<ListItem>
						<ListItemIcon>
							<Mail />
						</ListItemIcon>
						<ListItemText primary="Sample" />
					</ListItem>
				</List>
			</Drawer>
			{props.children}
		</>
	);
};
