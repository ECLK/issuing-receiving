import React, { ReactElement, useEffect, useState, useContext } from "react";
import { Formik } from "formik";
import { Autocomplete, Alert } from "@material-ui/lab";
import { Staff, ReportToWork } from "../../../models";
import { listStaffs, createBeforeElection, updateBeforeElection } from "../../../apis";
import { TextField, Grid, Button } from "@material-ui/core";
import useStyles from "../../../theme";
import { KeyboardDatePicker, MuiPickersUtilsProvider, KeyboardTimePicker } from "@material-ui/pickers";
import MomentUtils from "@date-io/moment";
import moment, { Moment } from "moment";
import { AuthContext } from "../../../helpers";
import { AddStaff } from "../../shared";

interface BeforeElectionFormProps {
    bindSubmit: (submit: () => void) => void;
    callAfterSubmit: () => void;
    checkIsAddStaff: (isStaff: boolean) => void;
    bindCloseStaff: (cancel: () => void) => void;
    data?: ReportToWork<true>;
}
export const BeforeElectionForm = (props: BeforeElectionFormProps): ReactElement => {

    const { bindSubmit, callAfterSubmit, checkIsAddStaff, bindCloseStaff, data } = props;

    const [ staffs, setStaffs ] = useState<Staff[]>([]);
    const [ formError, setFormError ] = useState("");
    const [ addNewStaff, setAddNewStaff ] = useState(false);

    const { authState } = useContext(AuthContext);

    const classes = useStyles();

    useEffect(() => {
        callListStaffs();
    }, []);

    const callListStaffs = () => {
        listStaffs().then(response => {
            setStaffs(response);
        }).catch(error => {
            //TODO: Notify error
        })
    }

    const closeAddStaff = () => {
        setAddNewStaff(false);
        checkIsAddStaff(false);
    };

    bindCloseStaff(closeAddStaff);

    return (
        addNewStaff ? (
            <AddStaff
                bindSubmit={ (submit) => {
                    bindSubmit(submit);
                } }
                callAfterSubmit={ () => {
                    callListStaffs();
                    closeAddStaff();
                } }
            />
        )
            : (
                <div>
                    <Formik
                        onSubmit={ (values, { setSubmitting }) => {
                            if (
                                values.staff
                                && values.type
                                && values.time
                                && values.date
                                && authState
                                && authState.staffDetails
                                && authState.staffDetails.profile.id
                            ) {
                                if (data) {
                                    const updateData = {
                                        staff: values.staff,
                                        type: values.type,
                                        time: new Date(values.date).toISOString().split("T")[ 0 ]
                                            + "T" + new Date(values.time).toISOString().split("T")[ 1 ],
                                        i_r_aro: authState && authState.staffDetails
                                            && authState.staffDetails.profile.id,
                                    };

                                    updateBeforeElection(data.id, updateData).then(response => {
                                        //TODO Notify
                                        callAfterSubmit();
                                    }).catch((error: { [ key: string ]: string[] }) => {
                                        if (!error) {
                                            setFormError("Something went wrong!");
                                            return;
                                        }
                                        else if (typeof error === "string") {
                                            setFormError(error);
                                        } else {
                                            const errors: string[] = [];
                                            Object.entries(error).forEach(([ key, values ]) => {
                                                values.forEach((value: string) => {
                                                    errors.push(value)
                                                });
                                            })
                                            setFormError(errors.join("\n"));
                                        }
                                    }).finally(() => {
                                        setSubmitting(false);
                                    });

                                } else {
                                    const data = {
                                        staff: values.staff,
                                        type: values.type,
                                        time: new Date(values.date).toISOString().split("T")[ 0 ]
                                            + "T" + new Date(values.time).toISOString().split("T")[ 1 ],
                                        i_r_aro: authState && authState.staffDetails
                                            && authState.staffDetails.profile.id
                                    };
                                    createBeforeElection(data).then(response => {
                                        callAfterSubmit();
                                        //TODO: Notify
                                    }).catch((error: { [ key: string ]: string[] }) => {
                                        if (!error) {
                                            setFormError("Something went wrong!");
                                            return;
                                        }
                                        else if (typeof error === "string") {
                                            setFormError(error);
                                        } else {
                                            const errors: string[] = [];
                                            Object.entries(error).forEach(([ key, values ]) => {
                                                values.forEach((value: string) => {
                                                    errors.push(value)
                                                });
                                            })
                                            setFormError(errors.join("\n"));
                                        }
                                    }).finally(() => {
                                        setSubmitting(false);
                                    })
                                }
                            }
                        }
                        }
                        initialValues={ {
                            staff: !data ? null as number : data.staff.id,
                            staffName: !data ? "" : data.staff.name,
                            type: !data ? "" : data.type,
                            date: !data ? moment.now() : data.timestamp,
                            time: !data ? moment.now() : data.timestamp
                        }
                        }
                        validate={ (values) => {
                            const errors: { [ key: string ]: string } = {}
                            if (!values.staff) {
                                errors.staff = "Staff is required";
                            }
                            if (!values.type) {
                                errors.type = "Type is required"
                            }
                            if (!values.time) {
                                errors.time = 'Time is required'
                            }
                            if (!values.date) {
                                errors.date = "Date is required"
                            }

                            return errors;
                        } }
                    >
                        {
                            (props) => {
                                const {
                                    values,
                                    touched,
                                    errors,
                                    handleChange,
                                    handleSubmit,
                                    submitForm
                                } = props;

                                bindSubmit(submitForm);

                                return (
                                    <form noValidate onSubmit={ handleSubmit }>
                                        <Grid className={ classes.gridGeneric } container spacing={ 2 }>
                                            <Grid item xs={ 8 }>
                                                <Autocomplete
                                                    options={ staffs }
                                                    getOptionLabel={ (option) => option.name }
                                                    style={ { width: 300 } }
                                                    value={ staffs.find(staff => staff.id === values.staff) ?? null }
                                                    onChange={ (event: any, value: Staff) => {
                                                        handleChange({ target: { value: value ?.id, id: "staff" } });
                                                    } }
                                                    id="staff"
                                                    renderInput={
                                                        (params) =>
                                                            <TextField
                                                                { ...params }
                                                                label="Select Staff"
                                                                variant="outlined"
                                                                helperText={ (errors.staff && touched.staff)
                                                                    && errors.staff }
                                                                required
                                                                fullWidth
                                                            />
                                                    }
                                                />
                                            </Grid>
                                            <Grid item xs={ 4 }>
                                                <Button onClick={ () => {
                                                    setAddNewStaff(true);
                                                    checkIsAddStaff(true);
                                                } }>
                                                    Add New Staff
                                        </Button>
                                            </Grid>
                                            <Grid item xs={ 12 }>
                                                <TextField
                                                    label="Staff Type"
                                                    name="type"
                                                    variant="outlined"
                                                    value={ values.type }
                                                    onChange={ handleChange }
                                                    helperText={ (errors.type && touched.type) && errors.type }
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
                                                            required
                                                            format="D/MM/YYYY"
                                                            value={ values.date }
                                                            onChange={ (date: Moment | null) => {
                                                                handleChange({
                                                                    target: {
                                                                        name: "date",
                                                                        value: date ? date.toDate() : null
                                                                    }
                                                                })
                                                            } }
                                                            KeyboardButtonProps={ {
                                                                'aria-label': 'change date',
                                                            } }
                                                            helperText={ (errors.date && touched.date) && errors.date }
                                                        />
                                                        <KeyboardTimePicker
                                                            margin="normal"
                                                            id="time-picker"
                                                            label="Time"
                                                            required
                                                            name="time"
                                                            value={ values.time }
                                                            onChange={ (date: Moment | null) => {
                                                                handleChange({
                                                                    target: {
                                                                        name: "time",
                                                                        value: date ? date.toDate() : null
                                                                    }
                                                                })
                                                            } }
                                                            KeyboardButtonProps={ {
                                                                'aria-label': 'change time',
                                                            } }
                                                            helperText={ (errors.time && touched.time) && errors.time }
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
                    {
                        formError && (
                            <Alert severity="error">
                                { formError }
                            </Alert>
                        )
                    }
                </div >
            )
    )
}