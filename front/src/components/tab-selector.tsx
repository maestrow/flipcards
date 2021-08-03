// ToDo Unused component, delete

import React from "react";
import cn from "classnames";
import css from "./tab-selector.module.css"

interface IProps extends React.ButtonHTMLAttributes<any> {
  isActive: boolean
}

export const TabSelector = (props: IProps) => {
  const { isActive, children, onClick, ...rest } = props;
  const cssRoot = cn(css.root, {[css.active]: isActive});
  return (
    <button {...rest}>
      {children}
    </button>
  )
}