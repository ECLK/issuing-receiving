import React from "react";
import { ListItemAvatar, ListItem, ListItemText, IconButton, ListItemSecondaryAction, Typography, Grid } from "@material-ui/core";
import { Delete, Edit } from "@material-ui/icons";
import useStyles from "../../theme";
import { Column } from "./list-page";

interface ListPageItemProps<T> {
    columns: Column[];
    avatar: React.ReactElement;
    onEdit: () => void;
    onDelete: () => void;
    item: T;
}
export const ListPageItem = <T extends { [ key: string ]: any },> (props: ListPageItemProps<T>): React.ReactElement => {

    const classes = useStyles();

    const { columns, avatar, onEdit, onDelete, item } = props;

    const accessValue = (object: T, keys: string | string[]): any => {
        if (keys instanceof Array) {
            let tempObj = { ...object };
            let value: string = "";
            keys.forEach((key, index: number) => {
                if (index === keys.length - 1) {
                    value = tempObj[ key ];
                } else {
                    tempObj = tempObj[ key ]
                }
            })

            return value;
        } else {
            return object[ keys ];
        }
    }
    return (
        <ListItem>
            <Grid container>
                { avatar &&
                    <Grid item xs={ 1 }>
                        <ListItemAvatar>
                            { avatar }
                        </ListItemAvatar>
                    </Grid>
                }
                {
                    columns.map((column: Column, index: number) => {
                        return (
                            <Grid key={ index } item xs={ Math.floor(10 / columns.length) as 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 }>
                                <ListItemText
                                    primary={ accessValue(item, column.primaryText) }
                                    secondary={
                                        column.secondaryText instanceof Array
                                            ? <span className={ classes.listSecondary }>
                                                <Typography
                                                    variant="body2"
                                                    component="span"
                                                    color="textPrimary"
                                                >
                                                    { accessValue(item, column.secondaryText[ 0 ]) }
                                                </Typography>
                                                { column.secondaryText.length > 1 &&
                                                    <Typography
                                                        variant="body2"
                                                        component="span"
                                                    >
                                                        { accessValue(item, column.secondaryText[ 1 ]) }
                                                        { column.secondaryText.length === 3 &&
                                                            " | " + accessValue(item, column.secondaryText[ 2 ]) }
                                                    </Typography>

                                                }
                                            </span>

                                            : item[ column.secondaryText ]
                                    }
                                />
                            </Grid>
                        )
                    })
                }
                <Grid item xs={ 1 }>
                    <ListItemSecondaryAction>
                        <IconButton onClick={ () => { onEdit() } }>
                            <Edit />
                        </IconButton>
                        <IconButton onClick={ () => { onDelete() } } className={ classes.dangerButton }>
                            <Delete />
                        </IconButton>
                    </ListItemSecondaryAction>
                </Grid>
            </Grid>
        </ListItem>
    )
};
