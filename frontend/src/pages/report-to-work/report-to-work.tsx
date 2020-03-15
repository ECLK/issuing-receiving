import React, { useState } from "react";
import { Tabs, Tab, Grid } from "@material-ui/core";
import { BeforeElection, OnElection } from "./components";
import useStyles from "../../theme";

export const ReportToWork = (): React.ReactElement => {

    const [value, setValue] = useState(0);

    const classes = useStyles();

    return (
        <div>
            <Tabs value={value} onChange={(e, newValue) => { setValue(newValue) }}>
                <Tab value={0} label="Day before the election" />
                <Tab value={1} label="On the day of the election" />
            </Tabs>
            <Grid container className={classes.gridGeneric} >
                <Grid item xs={12}>
                    {
                        value === 0
                            ? (
                                <BeforeElection />
                            )
                            : (
                                <OnElection />
                            )
                    }
                </Grid>
            </Grid>
        </div>
    )
};
