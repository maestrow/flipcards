import React, { useCallback, useState } from 'react';
import ReactDOM from "react-dom";
import css from './side-panel.module.css';
import cn from 'classnames';
import { ITerm } from '../models';
import { TabSelector } from './tab-selector';
import ReactJson from 'react-json-view';

interface IProps {
  list: ITerm[]
  onClear: () => void
  onSync: () => void
}

interface IState {
  visible: boolean
  activeTab: string
}

export class SidePanel extends React.Component<IProps, IState> {

  state: IState = {
    visible: true,
    activeTab: "tab-main"
  }

  switchVisibility = () => {
    this.setState({ visible: !this.state.visible })
  }

  onTabSelect = (event: React.MouseEvent<HTMLButtonElement>) => {
    this.setState({ activeTab: event.currentTarget.name })
  }

  onJsonEdit = (edit: any) => {
    // todo: should use setState
    (this.props.list[edit.namespace[0]] as any)[edit.name] = edit.new_value
    return true
  }

  onJsonDelete = (edit: any) => {
    // todo: should use setState
    this.props.list.splice(edit.name, 1)
    return true
  }

  onClear = () => {
    if (confirm('Clear list? Are you sure?')) {
      this.props.onClear()
    }
  }

  onSync = () => {
    this.props.onSync()
  }

  render() {
    const p = this.props
    const st = this.state;
    const cssVis = st.visible ? css.visible : css.hidden;

    return (
      <div className={cn(css.root, {[css.rootCollapsed]: !st.visible})}>
        <button className={css.buttonHide} onClick={this.switchVisibility}>Show/Hide</button>
        <div className={cn(css.panel, cssVis)}>
          <h2>Vocabulary</h2>
          <div>
            <button className={cn(css.tab, {[css.tabActive]: st.activeTab === "tab-main"})} name="tab-main" onClick={this.onTabSelect}>
              main
            </button>
            <button className={cn(css.tab, {[css.tabActive]: st.activeTab === "tab-json"})} name="tab-json" onClick={this.onTabSelect}>
              json
            </button>

            <button className={css.action} onClick={this.onClear}>
              clear
            </button>
            <button className={css.action} onClick={this.onSync}>
              sync
            </button>
          </div>
          
          <div>
            <div className={cn(css.tabPanel, {[css.hidden]: st.activeTab !== "tab-main"})}>
              
              <table className={css.list}>
                <tbody>
                  {p.list.map((i, idx) =>
                    <React.Fragment key={`item_${idx}`}>
                      <tr className={css.item} key={`item_${idx}_1`}>
                        <td className={css.itemForeign}>{i.foreign}</td>
                        <td className={css.itemMeaning}>{i.meaning}</td>
                      </tr>
                      <tr key={`item_${idx}_2`}>
                        <td colSpan={2} className={css.itemContext}>{i.context}</td>
                      </tr>
                    </React.Fragment>
                  )}
                </tbody>
              </table>
            </div>
            <div className={cn(css.tabPanel, {[css.hidden]: st.activeTab !== "tab-json"})}>
              <ReactJson 
                src={p.list} 
                enableClipboard={true}
                onEdit={this.onJsonEdit}
                onDelete={this.onJsonDelete}
                displayObjectSize={false}
                displayDataTypes={false}
              />
            </div>
          </div>
        </div>
      </div>
    );

  }

}
