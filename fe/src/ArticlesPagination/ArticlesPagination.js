import React from "react";
import Pagination from "react-bootstrap/Pagination";

const generate_pages = (active, total, changePage, term) => {
  let items = [
    <Pagination.First key={"first"} onClick={() => changePage(term, active)} />,
    <Pagination.Prev key={"prev"} onClick={() => changePage(term, active - 1)} />,
  ];
  const max = total > 5 ? 5 : total;
  for (let number = 1; number <= max; number++) {
    items.push(
      <Pagination.Item
        key={number}
        active={number === active}
        onClick={() => changePage(term, number)}
      >
        {number}
      </Pagination.Item>
    );
  }

  if (max < total) {
    items.push(<Pagination.Ellipsis key={"ellipsis"} />);
  }

  if (active > max) {
    items.push(
      <Pagination.Item key={active} active={true}>
        {active}
      </Pagination.Item>
    );
  }

  items.push(
    <Pagination.Next key={"next"} onClick={() => changePage(term, active + 1)} />,
    <Pagination.Last key={"last"} onClick={() => changePage(term, total)} />
  );
  return items;
};

const ArticlesPagination = (props) => {
  return (
    <Pagination className="mt-3">
      {generate_pages(props.page, props.total, props.changePage, props.term)}
    </Pagination>
  );
};

export default ArticlesPagination;
