import React, { useState, useRef, useEffect } from "react";
import { List, Fab, Divider, DialogTitle, DialogContent, Dialog, DialogActions, Button } from "@material-ui/core";
import { AddEditDialog } from "./add-edit-dialog";
import { Add } from "@material-ui/icons";
import { ListPageItem } from "./list-page-item";
import useStyles from "../../theme";

interface AddDialog {
    addDialogTitle: string;
    addDialogContent: () => React.ReactNode;
    addPrimaryActionText: string;
    addPrimaryAction: () => void;
    addSecondaryAction?: () => void;
    addSecondaryActionText?: string;
}

interface EditDialog {
    editDialogTitle: string;
    editDialogContent: () => React.ReactNode;
    editPrimaryActionText: string;
    editPrimaryAction: () => void;
    editSecondaryAction?: () => void;
    editSecondaryActionText?: string;
}

export interface Column {
    primaryText: string | string[];
    secondaryText: string | string[] | (string | string[])[];
}

interface ListPagePropsInterface<T> extends AddDialog, EditDialog {
    columns: Column[];
    list: T[];
    avatar: React.ReactElement;
    onDelete: (id: number) => void;
    onEdit: (id: number) => void;
    toggleOpen: boolean;
    deleteTitle: string;
    deleteContent: string;
    onDialogClose: () => void;
}
export const ListPage = <T extends { [ key: string ]: any }> (props: ListPagePropsInterface<T>): React.ReactElement => {

    const {
        addDialogContent,
        addDialogTitle,
        addPrimaryAction,
        addPrimaryActionText,
        addSecondaryAction,
        addSecondaryActionText,
        editDialogContent,
        editDialogTitle,
        editPrimaryAction,
        editPrimaryActionText,
        editSecondaryAction,
        editSecondaryActionText,
        columns,
        list,
        avatar,
        onDelete,
        onEdit,
        toggleOpen,
        deleteContent,
        deleteTitle,
        onDialogClose
    } = props;

    const [ openDialog, setOpenDialog ] = useState(false);
    const [ deleteConfirmation, setDeleteConfirmation ] = useState(false);
    const [ deleteIndex, setDeleteIndex ] = useState(-1);
    // edit: false add: true
    const [ selectedDialog, setSelectedDialog ] = useState<boolean>(true);

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
            setSelectedDialog(true);
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
                    <Button color="primary" onClick={ () => {
                        onDelete(deleteIndex);
                        setDeleteConfirmation(false);
                    } }>
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
                    onClose={ () => {
                        setOpenDialog(false);
                        onDialogClose();
                    } }
                    title={ selectedDialog ? addDialogTitle : editDialogTitle }
                    content={ selectedDialog ? addDialogContent : editDialogContent }
                    primaryAction={ selectedDialog ? addPrimaryAction : editPrimaryAction }
                    secondaryAction={ selectedDialog ? addSecondaryAction : editSecondaryAction }
                    primaryActionText={ selectedDialog ? addPrimaryActionText : editPrimaryActionText }
                    secondaryActionText={ selectedDialog ? addSecondaryActionText : editSecondaryActionText }
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
                                        setSelectedDialog(false);
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
