import { Theme } from "@material-ui/core";

export const gridGeneric = (theme: Theme) => ({
    padding: theme.spacing(3)
});

export const listSecondary = (theme: Theme) => ({
    display: "flex",
    flexDirection: "column" as const
});

export const dangerButton = (theme: Theme) => ({
    color: "red"
});

