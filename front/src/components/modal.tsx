import React from "react";
import css from "./modal.module.css";

interface IProps {
  onAction: (action: string) => void,
  actions: Array<[string, string | null]>,     // [action, key]
  show: boolean
}

export class Modal extends React.Component<IProps> {
  
  componentDidMount () {
    document.addEventListener('keydown', this.onKeyDown);
  }

  componentWillUnmount () {
    document.removeEventListener('keydown', this.onKeyDown);
  }

  onKeyDown = (event: KeyboardEvent) => {
    const key = event.code.toLowerCase()
    const act = this.props.actions.find(([a, k]) => k && k.toLowerCase() === key);
    if (act && this.props.onAction) {
       this.props.onAction(act[0]);  
    }
  }

  onAction = (e: React.MouseEvent<HTMLButtonElement>) => {
    this.props.onAction && this.props.onAction(e.currentTarget.name);
  };
  
  render() {
    const p = this.props;
    if (!this.props.show) {
      return null;
    }
    return (
      <div className={css.root}>
        <div className={css.container}>
          <h3>Add word?</h3>
          <div className={css.content}>
            {this.props.children}
          </div>
        </div>
        <div className={css.actions}>
          {p.actions.map(([a, _], idx) => 
            <button key={a} className={css.button} name={a} onClick={this.onAction} autoFocus={idx===0}>
              {a}
            </button>
          )}
        </div>
      </div>
    );
  }
}
