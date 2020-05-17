import React from "react";
import { Dialog, DialogTitle, DialogActions, DialogContent, Button } from "@material-ui/core";

interface AddReportToWorkPropInterface {
    /**
     * Opens the dialog
     */
    open: boolean;
    /**
     * Called when the dialog is closed
     */
    onClose: () => void;
    title: string;
    content: () => React.ReactNode;
    primaryActionText: string;
    secondaryActionText?: string;
    primaryAction: () => void;
    secondaryAction?: () => void;
}
export const AddEditDialog = (props: AddReportToWorkPropInterface): React.ReactElement => {

    const { open, onClose, title, content, primaryAction, primaryActionText, secondaryAction, secondaryActionText } = props;

    return (
        <Dialog open={ open } onClose={ onClose }>
            <DialogTitle>
                { title }
            </DialogTitle>
            <DialogContent>
                { content() }
            </DialogContent>
            <DialogActions>
                { (secondaryAction && secondaryActionText) &&
                    <Button variant="contained" onClick={ secondaryAction }>
                        { secondaryActionText }
                    </Button>
                }
                <Button variant="contained" color="primary" onClick={ primaryAction }>
                    { primaryActionText }
                </Button>

            </DialogActions>
        </Dialog>
    )
}