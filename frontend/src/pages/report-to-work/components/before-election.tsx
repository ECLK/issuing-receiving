import React, { useState, useEffect } from 'react';
import { ListPage } from "../../../layout";
import { Avatar } from "@material-ui/core";
import { ReportToWork } from "../../../models";
import { listBeforeElections } from "../../../apis";
import { BeforeElectionAdd } from ".";

export const BeforeElection = (): React.ReactElement => {

    const [ toggleDialog, setToggleDialog ] = useState(false);
    const [ data, setData ] = useState<ReportToWork<true>[]>([]);

    useEffect(() => {
        listBeforeElections().then(response => {
            setData(response);
        }).catch(error => {
            //TODO: Notify error
        });
    }, []);

    return (
        <ListPage<ReportToWork<true>>
            addDialog={ {
                dialogTitle: "Report To Work",
                dialogContent: <BeforeElectionAdd/>,
                primaryActionText: "Save",
                primaryAction: () => {
                    setToggleDialog(!toggleDialog);
                },
                secondaryAction: () => {
                    setToggleDialog(!toggleDialog);
                },
                secondaryActionText: "Cancel",
            } }
            editDialog={ {
                dialogTitle: "Edit Report To Work",
                dialogContent: "string",
                primaryActionText: "Update",
                primaryAction: () => {

                },
                secondaryAction: () => {

                },
                secondaryActionText: "Cancel",
            } }
            list={ data }
            onDelete={ () => { } }
            onEdit={ () => { } }
            avatar={ <Avatar /> }
            columns={ [
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
        />
    )
}