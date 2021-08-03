import React from "react";
import css from "./data-form.module.css";
import cn from 'classnames'
import ReactJson from 'react-json-view'
import { simplify } from "../models";

interface IProps {
  text?: string
  loading: boolean
  result?: any
}

const getVisCssClass = (visible: boolean) => visible ? css.visible : css.hidden;

export class DataForm extends React.Component<IProps> {
  
  render () {

    const loaderVis = getVisCssClass(this.props.loading)
    const resultVis = getVisCssClass(!this.props.loading)

    const simple = simplify(this.props.result)

    return (
      <div className={css.root}>
        <div className={css.header}>
          {this.props.text}
        </div>
        <div className={cn(css.loader, loaderVis)}>
          Loading...
        </div>
        {simple ? 
        <div className={cn(css.result, resultVis)}>
          <ReactJson 
            src={simple} 
            enableClipboard={false}
            displayObjectSize={false}
            displayDataTypes={false}
          />
        </div> : undefined}
      </div>
    );
  }
}