import React from 'react';
import css from './app.module.css';
import cn from 'classnames';
import { Modal } from './modal';
import { SidePanel } from "./side-panel";
import { DataForm } from './data-form';
import { translate } from "../translator";
import { ICancelablePromise, makeCancelable } from '../cancelable-promise';
import { ITerm } from '../models';
import { fakeData } from '../fake-data';
import { getText, getParagraph, getSentence } from 'get-selection-more'
import { sync } from '../sync';

interface IState {
  modalVisible: boolean,
  selection?: string,
  sentence?: string,
  translation?: any
  translationLoading: boolean,
  list: ITerm[]
}


const modalActions: Array<[string, string|null]> = [
  ['Add', null],
  ['Close', 'escape'],
];

export class App extends React.Component<{}, IState> {

  componentDidMount () {
    document.addEventListener('mouseup', this.onMouseEvent);
    document.addEventListener('dblclick', this.onMouseEvent);
  }

  componentWillUnmount () {
    document.removeEventListener('mouseup', this.onMouseEvent);
    document.removeEventListener('dblclick', this.onMouseEvent);
  }

  state: IState = {
    modalVisible: false,
    translationLoading: false,
    list: fakeData
  }

  job?: ICancelablePromise<any>

  onMouseEvent = (event: MouseEvent) => {
    if (event.ctrlKey) {
      const selection = document.getSelection()
      const sentence = getSentence()
      if (selection?.toString()) {
        this.job?.cancel()
        
        const text = selection.toString().replace(/\r|\n/ig, ' ')
        this.setState({
          modalVisible: true,
          selection: text,
          translation: undefined,
          translationLoading: true,
          sentence,
        });
        
        this.job = makeCancelable(translate(text))
        
        this.job?.promise.then(res => {
          this.setState({
            translation: res,
            translationLoading: false,
          });
        }).catch(err => {
          if (!err || !err.isCanceled) {
            throw err;
          }
        });
      }
    }
  }

  switchModalVisibility = () => {
    this.setState({ modalVisible: !this.state.modalVisible })
  }

  onModalAction = (action: string) => {
    switch (action.toLowerCase()) {
      case 'add':
        const newList = this.state.list.concat({
          foreign: this.state.translation.sentences[0].orig,
          meaning: this.state.translation.sentences[0].trans,
          context: this.state.sentence || '',
        });
        this.setState({ list: newList })
        break;
    }
    this.setState({ 
      modalVisible: false,
      translationLoading: false,
    })
  }

  onListClear = () => {
    this.setState({list: []})
  }

  onSync = () => {
    sync(this.state.list)
  }

  render() {
    const st = this.state;
    return (
      <div>
        {/* <div className={css.left}>
          <button onClick={this.switchModalVisibility}>Modal</button>
        </div> */}
        <SidePanel 
          list={st.list} 
          onClear={this.onListClear}
          onSync={this.onSync}
        />
        <Modal onAction={this.onModalAction} show={st.modalVisible} actions={modalActions}>
          <DataForm text={st.selection} loading={st.translationLoading} result={st.translation} />
        </Modal>
      </div>
    );
  }

}

