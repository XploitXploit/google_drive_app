import pugsql
import sqlalchemy as sa
from typing import List


class FastInsertStatement(pugsql.statement.Statement):
    def __init__(self, name: str, table_name: str, column_names: List[str]):
        columns_str = ",".join(column_names)
        params_str = ",".join([f":{c}" for c in column_names])
        sql = f"INSERT INTO {table_name} ({columns_str}) VALUES ({params_str})"
        insert_stmt = sa.table(
            table_name, *[sa.column(c) for c in column_names]
        ).insert()
        super().__init__(
            name, sql, "this is a fast insert statement", pugsql.parser._insert, None
        )
        self._table_name = table_name
        self._column_names = column_names
        self._slow_text = self._text
        self._text = insert_stmt

    def _param_names(self):
        def kfn(p):
            return self.sql.index(":" + p)

        return sorted(self._slow_text._bindparams.keys(), key=kfn)


def add_fast_insert_statement(
    module: pugsql.compiler.Module,
    statement_name: str,
    table_name: str,
    column_names: List[str],
) -> None:
    stmt = FastInsertStatement(statement_name, table_name, column_names)

    if hasattr(module, statement_name):
        if statement_name not in module._statements:
            raise ValueError(
                f'Error adding FastInsertStatement - the function name "{statement_name}"'
                " is reserved. Please choose another name."
            )
        raise ValueError(
            "Error adding FastInsertStatement - there already exists a Statement with "
            f"the name {statement_name} in {getattr(module, statement_name).filename}"
        )

    stmt.set_module(module)

    setattr(module, statement_name, stmt)
    module._statements[statement_name] = stmt
