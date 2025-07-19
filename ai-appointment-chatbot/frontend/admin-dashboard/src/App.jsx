import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import Analytics from './components/Analytics';
import FlowBuilder from './components/FlowBuilder';
import Settings from './components/Settings';
import Login from './pages/Login';

const App = () => {
    return (
        <Router>
            <Switch>
                <Route path="/" exact component={Dashboard} />
                <Route path="/analytics" component={Analytics} />
                <Route path="/flow-builder" component={FlowBuilder} />
                <Route path="/settings" component={Settings} />
                <Route path="/login" component={Login} />
            </Switch>
        </Router>
    );
};

export default App;