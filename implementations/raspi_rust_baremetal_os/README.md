# Baremetal Rust Runs on Raspberry Pi

## Install Requirements and Toolchain
```sh
sudo apt install gcc-aarch64-linux-gnu gdb-multiarch libudev-dev picocom pkg-config qemu-system-arm
rustup update
rustup target add aarch64-unknown-none thumbv7em-none-eabihf
rustup component add llvm-tools-preview
cargo install cargo-binutils cargo-embed
```

## Build

```sh
cargo rustc -- -C link-arg=..script=./linker.ld
arm-none-eabi-objcopy -O binary target/armv7a-none-eabi/debug/my-rusty-pi ./kernel7.img
```

## Reference
 * [BAREMETAL RUST Runs on EVERYTHING, Including the Raspberry Pi (no operating system, just Rust)](https://www.youtube.com/watch?v=jZT8APrzvc4)
