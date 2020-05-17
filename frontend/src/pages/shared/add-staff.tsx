import React, { ReactElement } from "react";
import { Formik } from "formik";
import { Grid, TextField } from "@material-ui/core";
import useStyles from "../../theme";
import { createStaff } from "../../apis";

interface AddStaffProps {
    bindSubmit: (submit: () => void) => void;
    callAfterSubmit: () => void;
}
export const AddStaff = (props: AddStaffProps): ReactElement => {

    const { bindSubmit, callAfterSubmit } = props;

    const classes = useStyles();

    return (
        <Formik
            onSubmit={
                (values, { setSubmitting }) => {
                    createStaff(values).then(response => {
                        //TODO Notify
                        callAfterSubmit();
                    }).catch(error => {
                        //TODO Notify
                    }).finally(() => {
                        setSubmitting(false);
                    })
                }
            }
            initialValues={ {
                name: "",
                nic: "",
                address: ""
            } }
            validate={ (values) => {
                const errors: { [ key: string ]: string } = {};
                if (!values.address) {
                    errors.address = "Address is required"
                }
                if (!values.name) {
                    errors.name = "Name is required"
                }
                if (!values.nic) {
                    errors.nic = "NIC is required"
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
                                <Grid item xs={ 12 }>
                                    <TextField
                                        label="Staff Name"
                                        name="name"
                                        variant="outlined"
                                        value={ values.name }
                                        onChange={ handleChange }
                                        required
                                        fullWidth
                                        helperText={ (errors.name && touched.name) && errors.name }
                                    />
                                </Grid>
                                <Grid item xs={ 12 }>
                                    <TextField
                                        label="NIC Number"
                                        name="nic"
                                        variant="outlined"
                                        value={ values.nic }
                                        onChange={ handleChange }
                                        required
                                        fullWidth
                                        helperText={ (errors.nic && touched.nic) && errors.nic }
                                    />
                                </Grid>
                                <Grid item xs={ 12 }>
                                    <TextField
                                        label="Staff Address"
                                        name="address"
                                        variant="outlined"
                                        value={ values.address }
                                        onChange={ handleChange }
                                        required
                                        fullWidth
                                        helperText={ (errors.address && touched.address) && errors.address }
                                    />
                                </Grid>
                            </Grid>
                        </form>
                    )
                }
            }
        </Formik>
    )
};
