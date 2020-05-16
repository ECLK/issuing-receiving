import React, { ReactElement, useEffect, useState } from "react";
import { Formik } from "formik";
import { Autocomplete } from "@material-ui/lab";
import { Staff } from "../../../models";
import { listStaffs } from "../../../apis";
import { TextField, Grid } from "@material-ui/core";
import useStyles from "../../../theme";
import { KeyboardDatePicker, MuiPickersUtilsProvider, KeyboardTimePicker } from "@material-ui/pickers";
import MomentUtils from "@date-io/moment";
import moment, { Moment } from "moment";

export const BeforeElectionAdd = (): ReactElement => {

    const [ staffs, setStaffs ] = useState<Staff[]>([]);

    const classes = useStyles();

    useEffect(() => {
        listStaffs().then(response => {
            setStaffs(response);
        }).catch(error => {
            //TODO: Notify error
        })
    }, []);

    return (
        <div>
            <Formik
                onSubmit={ (values, { setSubmitting }) => {

                } }
                initialValues={ {
                    name: "",
                    type: "",
                    date: moment.now(),
                    time: moment.now()
                } }
            >
                {
                    (props) => {
                        const {
                            values,
                            touched,
                            errors,
                            dirty,
                            isSubmitting,
                            handleChange,
                            handleBlur,
                            handleSubmit,
                            handleReset,
                        } = props;

                        return (
                            <form noValidate onSubmit={ handleSubmit }>
                                <Grid className={ classes.gridGeneric } container spacing={ 2 }>
                                    <Grid item xs={ 12 }>
                                        <Autocomplete
                                            id="combo-box-demo"
                                            options={ staffs }
                                            getOptionLabel={ (option) => option.name }
                                            style={ { width: 300 } }
                                            renderInput={
                                                (params) =>
                                                    <TextField
                                                        { ...params }
                                                        label="Select Staff"
                                                        name="staffs"
                                                        variant="outlined"
                                                        value={ values.name }
                                                        onChange={ handleChange }
                                                        helperText={ (errors.name && touched.name) && errors.name }
                                                        required
                                                        fullWidth
                                                    />
                                            }
                                        />
                                    </Grid>
                                    <Grid item xs={ 12 }>
                                        <TextField
                                            label="Staff Type"
                                            name="type"
                                            variant="outlined"
                                            value={ values.type }
                                            onChange={ handleChange }
                                            helperText={ (errors.name && touched.name) && errors.name }
                                            required
                                            fullWidth
                                        />
                                    </Grid>
                                    <Grid item>
                                        <MuiPickersUtilsProvider utils={ MomentUtils }>
                                            <Grid container justify="space-around">
                                                <KeyboardDatePicker
                                                    margin="normal"
                                                    id="date-picker-dialog"
                                                    label="Date"
                                                    name="date"
                                                    format="MM/dd/yyyy"
                                                    value={ values.date }
                                                    onChange={ (date: Moment | null) => {
                                                        handleChange({ name:"date",target: { value: date ? date.unix() : null } })
                                                    } }
                                                    KeyboardButtonProps={ {
                                                        'aria-label': 'change date',
                                                    } }
                                                />
                                                <KeyboardTimePicker
                                                    margin="normal"
                                                    id="time-picker"
                                                    label="Time"
                                                    name="time"
                                                    value={ values.time }
                                                    onChange={ handleChange }
                                                    KeyboardButtonProps={ {
                                                        'aria-label': 'change time',
                                                    } }
                                                />
                                            </Grid>
                                        </MuiPickersUtilsProvider>
                                    </Grid>
                                </Grid>
                            </form>
                        )

                    }
                }

            </Formik>
        </div>
    )
}