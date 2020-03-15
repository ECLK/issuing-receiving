import React, { useState } from "react";
import { List, ListItemAvatar, Avatar, ListItem, ListItemText, Typography, IconButton, ListItemSecondaryAction, Divider, Card, CardContent, TextField, CardHeader, Button, CardActions, Grid } from "@material-ui/core";
import { Delete, Edit } from "@material-ui/icons";
import useStyles from "../../../theme";
import { ReportToWork } from "../../../models";
import { Autocomplete } from '@material-ui/lab';
import {
    MuiPickersUtilsProvider,
    KeyboardTimePicker,
    KeyboardDatePicker,
} from '@material-ui/pickers';
import MomentUtils from '@date-io/moment';
import moment, { Moment } from "moment";


export const BeforeElection = (): React.ReactElement => {

    const classes = useStyles();

    const [date, setDate] = useState<Moment | null>(moment());
    const list = [
        {
            name: "Jofra Archer",
            nic: "45678975678V",
            address: "45,Statham Street, Colombo-09",
            type: "Senior Polling Officer",
            time: "9:30 AM",
            date: "25th April 2020"
        },
        {
            name: "Jofra Archer",
            nic: "45678975678V",
            address: "45,Statham Street, Colombo-09",
            type: "Senior Polling Officer",
            time: "9:30 AM",
            date: "25th April 2020"
        },
        {
            name: "Jofra Archer",
            nic: "45678975678V",
            address: "45,Statham Street, Colombo-09",
            type: "Senior Polling Officer",
            time: "9:30 AM",
            date: "25th April 2020"
        },
        {
            name: "Jofra Archer",
            nic: "45678975678V",
            address: "45,Statham Street, Colombo-09",
            type: "Senior Polling Officer",
            time: "9:30 AM",
            date: "25th April 2020"
        },
        {
            name: "Jofra Archer",
            nic: "45678975678V",
            address: "45,Statham Street, Colombo-09",
            type: "Senior Polling Officer",
            time: "9:30 AM",
            date: "25th April 2020"
        },
        {
            name: "Jofra Archer",
            nic: "45678975678V",
            address: "45,Statham Street, Colombo-09",
            type: "Senior Polling Officer",
            time: "9:30 AM",
            date: "25th April 2020"
        }

    ]
    return (
        <>
            <Card variant="outlined">
                <CardHeader title="Report To Work" />
                <CardContent>
                    <Grid container direction="row" spacing={3} justify="space-between" alignItems="flex-end">
                        <Grid item xs={6}>
                            <Autocomplete
                                options={list}
                                getOptionLabel={option => option.name}
                                renderInput={params => <TextField {...params} label="Select a Staff" variant="outlined" />}
                            />
                        </Grid>
                        <Grid item xs={6} justify="flex-end">
                            <MuiPickersUtilsProvider utils={MomentUtils}>
                                <KeyboardDatePicker
                                    margin="normal"
                                    id="date-picker-dialog"
                                    label="Date picker dialog"
                                    value={date}
                                    onChange={(date: Moment | null) => { setDate(date) }}
                                    KeyboardButtonProps={{
                                        'aria-label': 'change date',
                                    }}
                                />
                                <KeyboardTimePicker
                                    margin="normal"
                                    id="time-picker"
                                    label="Time picker"
                                    value={date}
                                    onChange={(date: Moment | null) => { setDate(date) }}
                                    KeyboardButtonProps={{
                                        'aria-label': 'change time',
                                    }}
                                />
                            </MuiPickersUtilsProvider>
                        </Grid>
                    </Grid>
                </CardContent>
                <CardActions >
                    <Grid container justify="flex-end">
                        <Grid item>
                            <Button variant="contained" color="primary">
                                Save
                            </Button>
                        </Grid>
                    </Grid>
                </CardActions>
            </Card>
            <List>
                {
                    list ?.map((item: ReportToWork) => {
                        return (
                            <>
                                <ListItem>
                                    <ListItemAvatar>
                                        <Avatar />
                                    </ListItemAvatar>
                                    <ListItemText
                                        primary={item.name}
                                        secondary={
                                            <span className={classes.listSecondary}>
                                                <Typography
                                                    variant="body2"
                                                    component="span"
                                                    color="textPrimary"
                                                >
                                                    {item.type}
                                                </Typography>
                                                <Typography
                                                    variant="body2"
                                                    component="span"
                                                >
                                                    {item.nic + " | " + item.address}
                                                </Typography>
                                            </span>
                                        }
                                    />
                                    <ListItemText
                                        primary={item.time}
                                        secondary={item.date}
                                    />
                                    <ListItemSecondaryAction>
                                        <IconButton>
                                            <Edit />
                                        </IconButton>
                                        <IconButton className={classes.dangerButton}>
                                            <Delete />
                                        </IconButton>
                                    </ListItemSecondaryAction>
                                </ListItem>
                                <Divider />
                            </>
                        )
                    })
            }
            </List>
        </>
    )
};
