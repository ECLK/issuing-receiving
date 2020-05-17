import React, { useState } from 'react';
import { ListPage } from "../../../layout";
import { Avatar } from "@material-ui/core";
import { IssueStationeries } from "../../../models";

export const Stationeries = (): React.ReactElement => {

    const [ toggleDialog, setToggleDialog ] = useState(false);

    let submit: () => void;

    return (
        <ListPage<IssueStationeries>
            addDialogTitle="Issue to SPO"
            addDialogContent={ () => {
                return<div></div>
            }}
            addPrimaryActionText="Save"
            addPrimaryAction={ () => {
                submit();
            } }
            addSecondaryAction={ () => {

            } }
            addSecondaryActionText="Cancel"

            editDialogTitle="Edit Issued to SPO"
            editDialogContent={ () => (
                <div></div>
            ) }
            editPrimaryActionText="Update"
            editPrimaryAction={ () => {
                submit();
            } }
            editSecondaryAction={ () => {
     
            } }
            editSecondaryActionText="Cancel"
            list={ [] }
            onDelete={ (index: number) => {
                
            } }
            onEdit={ (index) => {
                setToggleDialog(!toggleDialog);
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

            } }
        />
    )
}