import React from 'react';
import PropTypes from 'prop-types';

const Avatar = ({ user }) => {
    return (
        <div className="avatar">
            {user.profilePicture ? (
                <img src={user.profilePicture} alt={`${user.name}'s avatar`} className="avatar-image" />
            ) : (
                <div className="avatar-placeholder">
                    {user.name.charAt(0)}
                </div>
            )}
            <style jsx>{`
                .avatar {
                    display: flex;
                    align-items: center;
                }
                .avatar-image {
                    width: 40px;
                    height: 40px;
                    border-radius: 50%;
                    object-fit: cover;
                }
                .avatar-placeholder {
                    width: 40px;
                    height: 40px;
                    border-radius: 50%;
                    background-color: #ccc;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 20px;
                    color: white;
                }
            `}</style>
        </div>
    );
};

Avatar.propTypes = {
    user: PropTypes.shape({
        name: PropTypes.string.isRequired,
        profilePicture: PropTypes.string,
    }).isRequired,
};

export default Avatar;