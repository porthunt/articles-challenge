import React from "react";

const SearchArea = (props) => {
  return (
    <>
      <form onSubmit={(e) => props.searchSubmit(e)}>
        <input
          className="form-control"
          type="text"
          placeholder="Search term"
          aria-label="Search term"
        />
        <button className="d-none" type="submit"></button>
      </form>
      <span>Records found: {props.totalRecords}</span>
    </>
  );
};

export default SearchArea;
