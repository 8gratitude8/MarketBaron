import React from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';

class Services extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            content: ''
        };
    }

    componentDidMount() {
        fetch('/api/services')
            .then(response => response.text())
            .then(data => {
                this.setState({
                    content: data.replace(/NFT/g, 'Independent Game')
                });
            });
    }

    render() {
        return (
            <div>
                <Header />
                <div dangerouslySetInnerHTML={{ __html: this.state.content }} />
                <Footer />
            </div>
        );
    }
}

export default Services;