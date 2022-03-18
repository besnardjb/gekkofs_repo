# SPACK recipes for GekkoFS

## How to test

```
git clone https://github.com/besnardjb/gekkofs_repo.git
spack repo add ./gekkofs_repo
spack install gekkofs
```


## Updated Packages

- rocksdb : add RTTI support flag (needed by gekko)

## New Packages

- agios
- capstone
- syscall-intercept
    - On this one we applied the gekko upstream patch (+gekko)
        (packages/syscall-intercept/syscall_intercept.patch)
    - We also fixed capstone detection (certainly version mismatch) (packages/syscall-intercept/dep-capstone.patch)

## Fixes in GekkoFS

The libtz is now called date-tz in the date package, we added its detection if the former is not detected.
(packages/gekkofs/date.patch)

