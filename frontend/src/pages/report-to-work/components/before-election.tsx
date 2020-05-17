import React, { useState, useEffect } from 'react';
import { ListPage } from "../../../layout";
import { Avatar } from "@material-ui/core";
import { ReportToWork } from "../../../models";
import { listBeforeElections, deleteBeforeElection } from "../../../apis";
import { BeforeElectionForm } from ".";

export const BeforeElection = (): React.ReactElement => {

    const [ toggleDialog, setToggleDialog ] = useState(false);
    const [ data, setData ] = useState<ReportToWork<true>[]>([]);
    const [ isStaff, setIsStaff ] = useState(false);
    const [ editData, setEditData ] = useState<ReportToWork<true>>(null);

    let submit: () => void;
    let cancel: () => void;

    useEffect(() => {
        callListBeforeElections();
    }, []);

    const callListBeforeElections = () => {
        listBeforeElections().then(response => {
            setData(response);
        }).catch(error => {
            //TODO: Notify error
        });
    }

    useEffect(() => {
        editData && setToggleDialog(!toggleDialog);
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [ editData ])

    return (
        <ListPage<ReportToWork<true>>
            addDialogTitle="Report To Work"
            addDialogContent={ () => (
                <BeforeElectionForm
                    bindSubmit={ (submitForm) => submit = submitForm }
                    callAfterSubmit={ () => {
                        setToggleDialog(!toggleDialog);
                        callListBeforeElections();
                    } }
                    checkIsAddStaff={ (isStaffAdd) => {
                        setIsStaff(isStaffAdd);
                    } }
                    bindCloseStaff={ (cancelStaff) => {
                        cancel = cancelStaff;
                    } }
                />
            ) }
            addPrimaryActionText="Save"
            addPrimaryAction={ () => {
                submit();
            } }
            addSecondaryAction={ () => {
                if (!isStaff) {
                    setToggleDialog(!toggleDialog)
                } else {
                    cancel();
                }
            } }
            addSecondaryActionText="Cancel"

            editDialogTitle="Edit Report To Work"
            editDialogContent={ () => (
                <BeforeElectionForm
                    bindSubmit={ (submitForm) => submit = submitForm }
                    callAfterSubmit={ () => {
                        setToggleDialog(!toggleDialog);
                        callListBeforeElections();
                    } }
                    checkIsAddStaff={ (isStaffAdd) => {
                        setIsStaff(isStaffAdd);
                    } }
                    bindCloseStaff={ (cancelStaff) => {
                        cancel = cancelStaff;
                    } }
                    data={ editData }
                />
            ) }
            editPrimaryActionText="Update"
            editPrimaryAction={ () => {
                submit();
            } }
            editSecondaryAction={ () => {
                if (!isStaff) {
                    setToggleDialog(!toggleDialog);
                } else {
                    cancel();
                }
            } }
            editSecondaryActionText="Cancel"
            list={ data }
            onDelete={ (index: number) => {
                deleteBeforeElection(data[ index ].id).then(response => {
                    //TODO Notify
                    callListBeforeElections();
                }).catch(error => [
                    //TODO Notify
                ])
             } }    
            onEdit={ (index) => {
                setEditData(data[ index ]);
            } }
            avatar={ < Avatar /> }
            columns={
                [
                    {
                        primaryText: [ "staff", "name" ],
                        secondaryText: [ "type", [ "staff", "nic" ], [ "staff", "address" ] ]
                    },
                    {
                        primaryText: "time",
                        secondaryText: "date"
                    }
                ] }
            toggleOpen={ toggleDialog }
            deleteTitle="Delete this entry?"
            deleteContent="Do you really want to delete this entry?"
            onDialogClose={ () => {
                setIsStaff(false);
                setEditData(null);
            } }
        />
    )
}