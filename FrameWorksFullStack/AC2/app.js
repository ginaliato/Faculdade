import React from 'react';
import {Switch, Route, Link} from 'react-router-dom';
import Usuario from './Usuario';

export default function App() {
    return (
        <>
      <header>
       <Link to='/usuario'>Usuario</Link>
      </header>
      <main>
          <Switch>
            <Route path='/usuario' component= {Usuario}/>
          </Switch>
        </main></>
    );
  }
  