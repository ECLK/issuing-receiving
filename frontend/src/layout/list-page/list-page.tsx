import React, { useState, useRef, useEffect } from "react";
import { List, Fab, Divider, DialogTitle, DialogContent, Dialog, DialogActions, Button } from "@material-ui/core";
import { AddEditDialog } from "./add-edit-dialog";
import { Add } from "@material-ui/icons";
import { ListPageItem } from "./list-page-item";
import useStyles from "../../theme";

interface Dialog {
    dialogTitle: string;
    dialogContent: React.ReactNode;
    primaryActionText: string;
    primaryAction: () => void;
    secondaryAction?: () => void;
    secondaryActionText?: string;
}

export interface Column {
    primaryText: string | string[];
    secondaryText: string | string[] | (string | string[])[];
}

interface ListPagePropsInterface<T> {
    editDialog: Dialog;
    addDialog: Dialog;
    columns: Column[];
    list: T[];
    avatar: React.ReactElement;
    onDelete: (id: number) => void;
    onEdit: (id: number) => void;
    toggleOpen: boolean;
    deleteTitle: string;
    deleteContent: string;
}
export const ListPage = <T extends { [ key: string ]: any }> (props: ListPagePropsInterface<T>): React.ReactElement => {

    const { editDialog, addDialog, columns, list, avatar, onDelete, onEdit, toggleOpen, deleteContent, deleteTitle } = props;

    const [ openDialog, setOpenDialog ] = useState(false);
    const [ deleteConfirmation, setDeleteConfirmation ] = useState(false);
    const [ deleteIndex, setDeleteIndex ] = useState(-1);
    const [ selectedDialog, setSelectedDialog ] = useState<Dialog>(addDialog);

    const initRender = useRef(true);

    const classes = useStyles();

    useEffect(() => {
        if (initRender.current) {
            initRender.current = false;
        } else {
            setOpenDialog(!openDialog);
        }
    }, [ toggleOpen ]);

    useEffect(() => {
        if (!openDialog) {
            setSelectedDialog(addDialog);
        }
    }, [ openDialog ]);

    const closeDeleteDialog = () => {
        setDeleteConfirmation(false);
        setDeleteIndex(- 1);
    };

    const deleteDialog = (): React.ReactElement => {
        return (
            <Dialog open={ deleteConfirmation } onClose={ closeDeleteDialog }>
                <DialogTitle>
                    { deleteTitle }
                </DialogTitle>
                <DialogContent>
                    { deleteContent }
                </DialogContent>
                <DialogActions>
                    <Button onClick={ closeDeleteDialog }>
                        Cancel
                    </Button>
                    <Button color="primary" onClick={ () => { onDelete(deleteIndex) } }>
                        Delete
                    </Button>
                </DialogActions>
            </Dialog>
        )
    }

    return (
        <>
            {
                deleteConfirmation &&
                deleteDialog()
            }
            {
                openDialog &&
                <AddEditDialog
                    open={ openDialog }
                    onClose={ () => setOpenDialog(false) }
                    title={ selectedDialog.dialogTitle }
                    content={ selectedDialog.dialogContent }
                    primaryAction={ selectedDialog.primaryAction }
                    secondaryAction={ selectedDialog.secondaryAction }
                    primaryActionText={ selectedDialog.primaryActionText }
                    secondaryActionText={ selectedDialog.secondaryActionText }
                />
            }
            <List>
                {
                    list ?.map((item: T, index: number) => {
                        return (
                            <React.Fragment key={ index }>
                                <ListPageItem<T>
                                    avatar={ avatar }
                                    item={ item }
                                    columns={ columns }
                                    onEdit={ () => {
                                        setSelectedDialog(editDialog)
                                        setOpenDialog(true);
                                        onEdit(index);
                                    } }
                                    onDelete={ () => {
                                        setDeleteIndex(index);
                                        setDeleteConfirmation(true);
                                    } }
                                />
                                { index !== list.length - 1 && <Divider /> }
                            </React.Fragment>
                        )
                    }) 
                }
            </List>
            <Fab className={ classes.fab } color="primary" aria-label="add" onClick={ () => { setOpenDialog(true) } }>
                <Add />
            </Fab>
        </>

    )
};
