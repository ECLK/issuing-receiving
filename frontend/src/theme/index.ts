import { makeStyles, Theme } from "@material-ui/core/styles";
import { signInGrid, signInPaper } from "./sign-in";

const useStyles = makeStyles((theme: Theme) => ({
	signInGrid: signInGrid(theme),
	signInPaper: signInPaper(theme)
}));

export default useStyles;
