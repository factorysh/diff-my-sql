# Diff my SQL

Use sqlalchemy for displaying diff between preprod and prod models.

```
./diff.py mysql://user:pw1D@preprod/projet mysql://user:pw2@prod/projet
```

Here is a respsonse sample :

```
[CHANGED]  articles
***

---

***************

*** 2,9 ****

    `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
    `title` varchar(255) NOT NULL,
    `content` longtext NOT NULL,
-   `published_at` date NOT NULL,
    `category` int(11) DEFAULT NULL,
    `created_at` timestamp NULL DEFAULT current_timestamp(),
    `updated_at` timestamp NULL DEFAULT current_timestamp(),
    PRIMARY KEY (`id`)
--- 2,10 ----

    `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
    `title` varchar(255) NOT NULL,
    `content` longtext NOT NULL,
    `category` int(11) DEFAULT NULL,
+   `created_by` int(11) DEFAULT NULL,
+   `updated_by` int(11) DEFAULT NULL,
    `created_at` timestamp NULL DEFAULT current_timestamp(),
    `updated_at` timestamp NULL DEFAULT current_timestamp(),
    PRIMARY KEY (`id`)

[CHANGED]  users-permissions_permission
***

---

***************

*** 6,10 ****

    `enabled` tinyint(1) NOT NULL,
    `policy` varchar(255) DEFAULT NULL,
    `role` int(11) DEFAULT NULL,
    PRIMARY KEY (`id`)
! ) ENGINE=InnoDB AUTO_INCREMENT=189 DEFAULT CHARSET=utf8
--- 6,12 ----

    `enabled` tinyint(1) NOT NULL,
    `policy` varchar(255) DEFAULT NULL,
    `role` int(11) DEFAULT NULL,
+   `created_by` int(11) DEFAULT NULL,
+   `updated_by` int(11) DEFAULT NULL,
    PRIMARY KEY (`id`)
! ) ENGINE=InnoDB AUTO_INCREMENT=185 DEFAULT CHARSET=utf8
```


