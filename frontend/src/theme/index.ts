import { makeStyles, Theme } from "@material-ui/core/styles";
import { signInGrid, signInPaper } from "./sign-in";
import { appBar, drawer } from "./app-layout";

const useStyles = makeStyles((theme: Theme) => ({
	signInGrid: signInGrid(theme),
	signInPaper: signInPaper(theme),
	appBar: appBar(theme),
	drawer: drawer(theme)
}));

export default useStyles;
