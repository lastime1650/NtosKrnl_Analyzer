# _CmUpdateDevicePanel

- RVA: `0x00A0A16C`–`0x00A0AD80` (길이 `3,092` bytes)
- VA: `0x0000000140A0A16C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A8918`
- 디코드: `734`개 명령, `3,092/3,092` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **42**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **20**

### Outgoing calls
- `0x00A0A227` → [CmIsRootDevice](../93/CmIsRootDevice_function_009325E4.md) (function, `0x009325E4`)
- `0x00A0A270` → [CmQueryDevicePanelPldProperty](CmQueryDevicePanelPldProperty_function_00A0AD88.md) (function, `0x00A0AD88`)
- `0x00A0A294` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A0A2E7` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x00A0A300` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A0A409` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x00A0A488` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00A0A4C8` → [CmGetParentDeviceContainerId](CmGetParentDeviceContainerId_function_00A0AF08.md) (function, `0x00A0AF08`)
- `0x00A0A4E2` → [_CmGetDevicePanelGroup](_CmGetDevicePanelGroup_function_00A0B618.md) (function, `0x00A0B618`)
- `0x00A0A514` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A0A533` → [CmBuildDevicePanelId](CmBuildDevicePanelId_function_00A0B008.md) (function, `0x00A0B008`)
- `0x00A0A557` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A0A5F1` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00A0A60B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A0A61A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A0A655` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00A0A68B` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00A0A6C3` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00A0A73A` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00A0A7B6` → [CmGetParentDeviceContainerId](CmGetParentDeviceContainerId_function_00A0AF08.md) (function, `0x00A0AF08`)
- `0x00A0A7F4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A0A874` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00A0A8C0` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00A0A90C` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00A0A97C` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00A0A9D3` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00A0AA4E` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00A0AA84` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00A0AABA` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00A0AADD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A0AB87` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00A0ABD8` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00A0AC41` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00A0AC91` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00A0ACCE` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00A0ACED` → [CmAddPanelDevice](../82/CmAddPanelDevice_function_0082DDEC.md) (function, `0x0082DDEC`)
- `0x00A0AD08` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A0AD3A` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00A0AD49` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A0AD58` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A0AD67` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A0AD76` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [PiUpdateDevicePanel](../8F/PiUpdateDevicePanel_function_008FBD4C.md) at `0x008FBD9F`

### Static image references
- `0x00A0A188` → RVA `0x00E0A740` (`.data`; read)
- `0x00A0A196` → RVA `0x00E66398` (`.data`; read)
- `0x00A0A264` → RVA `0x00014DB0` (`.rdata`; read)
- `0x00A0A2D3` → RVA `0x000115A0` (`.rdata`; read)
- `0x00A0A38E` → RVA `0x00014DE0` (`.rdata`; read)
- `0x00A0A395` → RVA `0x00014DF0` (`.rdata`; read)
- `0x00A0A3A5` → RVA `0x00014DD8` (`.rdata`; read)
- `0x00A0A3B2` → RVA `0x00014DC8` (`.rdata`; read)
- `0x00A0A5D1` → RVA `0x00014DF8` (`.rdata`; read)
- `0x00A0A628` → RVA `0x00014E88` (`.rdata`; read)
- `0x00A0A65C` → RVA `0x00014EA0` (`.rdata`; read)
- `0x00A0A692` → RVA `0x00014EB8` (`.rdata`; read)
- `0x00A0A717` → RVA `0x00014ED0` (`.rdata`; read)
- `0x00A0A8A1` → RVA `0x00014E10` (`.rdata`; read)
- `0x00A0A8ED` → RVA `0x00014E28` (`.rdata`; read)
- `0x00A0A959` → RVA `0x00014E40` (`.rdata`; read)
- `0x00A0A9B7` → RVA `0x00014E58` (`.rdata`; read)
- `0x00A0AA8B` → RVA `0x00014E70` (`.rdata`; read)
- `0x00A0AAEE` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00A0ACA1` → RVA `0x00021C80` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **16**
  - `0x00A0A294` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A0A300` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A0A488` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00A0A514` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A0A557` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A0A60B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A0A61A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A0A7F4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A0AADD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A0AB87` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x00A0AD08` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A0AD3A` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00A0AD49` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A0AD58` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A0AD67` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A0AD76` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **20**
  - `0x00A0A328` → [sub_00B34E9C + 0x27D](../B3/Unknown_function_00B34E9C.md) (`tail-transfer`)
  - `0x00A0A340` → [sub_00B34E9C + 0x46C](../B3/Unknown_function_00B34E9C.md) (`tail-transfer`)
  - `0x00A0A349` → [sub_00B34E9C + 0x6EB](../B3/Unknown_function_00B34E9C.md) (`tail-transfer`)
  - `0x00A0A376` → [sub_00B34E9C + 0x794](../B3/Unknown_function_00B34E9C.md) (`tail-transfer`)
  - `0x00A0A566` → [sub_00B34E9C](../B3/Unknown_function_00B34E9C.md) (`tail-transfer`)
  - `0x00A0A750` → [sub_00B34E9C + 0x794](../B3/Unknown_function_00B34E9C.md) (`tail-transfer`)
  - `0x00A0A7A6` → [sub_00B34E9C + 0x7FE](../B3/Unknown_function_00B34E9C.md) (`tail-transfer`)
  - `0x00A0A7CA` → [sub_00B34E9C + 0x7FE](../B3/Unknown_function_00B34E9C.md) (`tail-transfer`)
  - `0x00A0A81C` → [sub_00B34E9C + 0x1C6](../B3/Unknown_function_00B34E9C.md) (`tail-transfer`)
  - `0x00A0A941` → [sub_00B34E9C + 0xC7](../B3/Unknown_function_00B34E9C.md) (`tail-transfer`)
  - `0x00A0AB23` → [sub_00B34E9C + 0x7A](../B3/Unknown_function_00B34E9C.md) (`tail-transfer`)
  - `0x00A0AB2E` → [sub_00B34E9C + 0x7A](../B3/Unknown_function_00B34E9C.md) (`tail-transfer`)
  - `0x00A0AB40` → [sub_00B34E9C + 0x7A](../B3/Unknown_function_00B34E9C.md) (`tail-transfer`)
  - `0x00A0AB4A` → [sub_00B34E9C + 0xBE](../B3/Unknown_function_00B34E9C.md) (`tail-transfer`)
  - `0x00A0AB53` → [sub_00B34E9C + 0xBE](../B3/Unknown_function_00B34E9C.md) (`tail-transfer`)
  - `0x00A0AB7B` → [sub_00B34E9C + 0x8D](../B3/Unknown_function_00B34E9C.md) (`tail-transfer`)
  - `0x00A0AB90` → [sub_00B34E9C + 0x8D](../B3/Unknown_function_00B34E9C.md) (`tail-transfer`)
  - `0x00A0AB98` → [sub_00B34E9C + 0x8F](../B3/Unknown_function_00B34E9C.md) (`tail-transfer`)
  - `0x00A0ABA2` → [sub_00B34E9C + 0xA4](../B3/Unknown_function_00B34E9C.md) (`tail-transfer`)
  - `0x00A0AC04` → [sub_00B34E9C + 0x27D](../B3/Unknown_function_00B34E9C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00A0A16C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A0A171  55                              push rbp
00A0A172  56                              push rsi
00A0A173  57                              push rdi
00A0A174  41 54                           push r12
00A0A176  41 55                           push r13
00A0A178  41 56                           push r14
00A0A17A  41 57                           push r15
00A0A17C  48 8D 6C 24 E0                  lea rbp, [rsp - 0x20]
00A0A181  48 81 EC 20 01 00 00            sub rsp, 0x120
00A0A188  48 8B 05 B1 05 40 00            mov rax, qword ptr [rip + 0x4005b1]
00A0A18F  48 33 C4                        xor rax, rsp
00A0A192  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
00A0A196  48 8B 3D FB C1 45 00            mov rdi, qword ptr [rip + 0x45c1fb]
00A0A19D  45 33 E4                        xor r12d, r12d
00A0A1A0  33 C0                           xor eax, eax
00A0A1A2  4C 89 65 A8                     mov qword ptr [rbp - 0x58], r12
00A0A1A6  0F 57 C0                        xorps xmm0, xmm0
00A0A1A9  44 89 65 8C                     mov dword ptr [rbp - 0x74], r12d
00A0A1AD  0F 57 C9                        xorps xmm1, xmm1
00A0A1B0  4C 89 65 C0                     mov qword ptr [rbp - 0x40], r12
00A0A1B4  48 8B CA                        mov rcx, rdx
00A0A1B7  44 89 65 94                     mov dword ptr [rbp - 0x6c], r12d
00A0A1BB  8D 58 01                        lea ebx, [rax + 1]
00A0A1BE  4C 89 65 80                     mov qword ptr [rbp - 0x80], r12
00A0A1C2  89 5D 88                        mov dword ptr [rbp - 0x78], ebx
00A0A1C5  4D 8B F8                        mov r15, r8
00A0A1C8  48 8B F2                        mov rsi, rdx
00A0A1CB  44 89 65 A0                     mov dword ptr [rbp - 0x60], r12d
00A0A1CF  4C 89 64 24 70                  mov qword ptr [rsp + 0x70], r12
00A0A1D4  45 8B F4                        mov r14d, r12d
00A0A1D7  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00A0A1DB  44 88 64 24 66                  mov byte ptr [rsp + 0x66], r12b
00A0A1E0  45 8B EC                        mov r13d, r12d
00A0A1E3  44 89 65 98                     mov dword ptr [rbp - 0x68], r12d
00A0A1E7  44 89 65 9C                     mov dword ptr [rbp - 0x64], r12d
00A0A1EB  4C 89 64 24 78                  mov qword ptr [rsp + 0x78], r12
00A0A1F0  4C 89 65 B8                     mov qword ptr [rbp - 0x48], r12
00A0A1F4  44 88 64 24 64                  mov byte ptr [rsp + 0x64], r12b
00A0A1F9  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00A0A1FD  89 45 F0                        mov dword ptr [rbp - 0x10], eax
00A0A200  0F 11 4D F8                     movups xmmword ptr [rbp - 8], xmm1
00A0A204  89 45 08                        mov dword ptr [rbp + 8], eax
00A0A207  4C 89 65 C8                     mov qword ptr [rbp - 0x38], r12
00A0A20B  44 88 64 24 65                  mov byte ptr [rsp + 0x65], r12b
00A0A210  44 89 64 24 60                  mov dword ptr [rsp + 0x60], r12d
00A0A215  44 89 65 B0                     mov dword ptr [rbp - 0x50], r12d
00A0A219  44 89 65 B4                     mov dword ptr [rbp - 0x4c], r12d
00A0A21D  44 88 64 24 6C                  mov byte ptr [rsp + 0x6c], r12b
00A0A222  44 89 64 24 68                  mov dword ptr [rsp + 0x68], r12d
00A0A227  E8 B8 83 F2 FF                  call 0x1409325e4
00A0A22C  84 C0                           test al, al
00A0A22E  0F 85 DB 05 00 00               jne 0x140a0a80f
00A0A234  48 8D 45 94                     lea rax, [rbp - 0x6c]
00A0A238  4D 8B CF                        mov r9, r15
00A0A23B  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00A0A240  44 8B C3                        mov r8d, ebx
00A0A243  48 8D 45 C0                     lea rax, [rbp - 0x40]
00A0A247  48 8B D6                        mov rdx, rsi
00A0A24A  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A0A24F  48 8B CF                        mov rcx, rdi
00A0A252  48 8D 45 8C                     lea rax, [rbp - 0x74]
00A0A256  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A0A25B  48 8D 45 A8                     lea rax, [rbp - 0x58]
00A0A25F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A0A264  48 8D 05 45 AB 60 FF            lea rax, [rip - 0x9f54bb]
00A0A26B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A0A270  E8 13 0B 00 00                  call 0x140a0ad88
00A0A275  8B D8                           mov ebx, eax
00A0A277  3D 25 02 00 C0                  cmp eax, 0xc0000225
00A0A27C  0F 85 27 02 00 00               jne 0x140a0a4a9
00A0A282  BB 72 00 00 00                  mov ebx, 0x72
00A0A287  41 B8 50 4E 50 52               mov r8d, 0x52504e50
00A0A28D  8B D3                           mov edx, ebx
00A0A28F  B9 00 01 00 00                  mov ecx, 0x100
00A0A294  E8 57 7E 17 00                  call 0x140b820f0
00A0A299  33 D2                           xor edx, edx
00A0A29B  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00A0A2A0  48 85 C0                        test rax, rax
00A0A2A3  0F 84 9C 08 00 00               je 0x140a0ab45
00A0A2A9  89 54 24 50                     mov dword ptr [rsp + 0x50], edx
00A0A2AD  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00A0A2B2  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
00A0A2B7  44 8D 43 8F                     lea r8d, [rbx - 0x71]
00A0A2BB  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00A0A2BF  4D 8B CF                        mov r9, r15
00A0A2C2  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A0A2C7  48 8B CF                        mov rcx, rdi
00A0A2CA  48 8D 45 88                     lea rax, [rbp - 0x78]
00A0A2CE  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A0A2D3  48 8D 05 C6 72 60 FF            lea rax, [rip - 0x9f8d3a]
00A0A2DA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A0A2DF  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00A0A2E4  48 8B D6                        mov rdx, rsi
00A0A2E7  E8 94 7E ED FF                  call 0x1408e2180
00A0A2EC  8B D8                           mov ebx, eax
00A0A2EE  3D 25 02 00 C0                  cmp eax, 0xc0000225
00A0A2F3  0F 85 56 08 00 00               jne 0x140a0ab4f
00A0A2F9  33 D2                           xor edx, edx
00A0A2FB  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00A0A300  E8 6B 85 17 00                  call 0x140b82870
00A0A305  33 D2                           xor edx, edx
00A0A307  8B DA                           mov ebx, edx
00A0A309  48 89 54 24 78                  mov qword ptr [rsp + 0x78], rdx
00A0A30E  4D 85 F6                        test r14, r14
00A0A311  0F 85 61 08 00 00               jne 0x140a0ab78
00A0A317  48 85 DB                        test rbx, rbx
00A0A31A  0F 85 7D 08 00 00               jne 0x140a0ab9d
00A0A320  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00A0A325  48 85 C0                        test rax, rax
00A0A328  0F 85 EB AD 12 00               jne 0x140b35119
00A0A32E  48 85 DB                        test rbx, rbx
00A0A331  0F 85 ED 02 00 00               jne 0x140a0a624
00A0A337  41 B8 6D C1 16 6C               mov r8d, 0x6c16c16d
00A0A33D  4D 85 F6                        test r14, r14
00A0A340  0F 85 C2 AF 12 00               jne 0x140b35308
00A0A346  48 85 DB                        test rbx, rbx
00A0A349  0F 85 38 B2 12 00               jne 0x140b35587
00A0A34F  4D 85 F6                        test r14, r14
00A0A352  0F 85 1E 02 00 00               jne 0x140a0a576
00A0A358  48 85 DB                        test rbx, rbx
00A0A35B  0F 85 AF 08 00 00               jne 0x140a0ac10
00A0A361  4D 85 F6                        test r14, r14
00A0A364  0F 85 6F 03 00 00               jne 0x140a0a6d9
00A0A36A  48 85 DB                        test rbx, rbx
00A0A36D  0F 85 ED 08 00 00               jne 0x140a0ac60
00A0A373  4D 85 F6                        test r14, r14
00A0A376  0F 85 B4 B2 12 00               jne 0x140b35630
00A0A37C  48 85 DB                        test rbx, rbx
00A0A37F  0F 85 18 09 00 00               jne 0x140a0ac9d
00A0A385  4D 85 F6                        test r14, r14
00A0A388  0F 85 4C 09 00 00               jne 0x140a0acda
00A0A38E  0F 10 05 4B AA 60 FF            movups xmm0, xmmword ptr [rip - 0x9f55b5]
00A0A395  8B 05 55 AA 60 FF               mov eax, dword ptr [rip - 0x9f55ab]
00A0A39B  49 8B DD                        mov rbx, r13
00A0A39E  4C 8B 65 A8                     mov r12, qword ptr [rbp - 0x58]
00A0A3A2  89 45 F0                        mov dword ptr [rbp - 0x10], eax
00A0A3A5  8B 05 2D AA 60 FF               mov eax, dword ptr [rip - 0x9f55d3]
00A0A3AB  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00A0A3AF  89 45 08                        mov dword ptr [rbp + 8], eax
00A0A3B2  0F 10 05 0F AA 60 FF            movups xmm0, xmmword ptr [rip - 0x9f55f1]
00A0A3B9  8B 45 8C                        mov eax, dword ptr [rbp - 0x74]
00A0A3BC  89 45 90                        mov dword ptr [rbp - 0x70], eax
00A0A3BF  0F 11 45 F8                     movups xmmword ptr [rbp - 8], xmm0
00A0A3C3  48 89 5D A8                     mov qword ptr [rbp - 0x58], rbx
00A0A3C7  89 55 94                        mov dword ptr [rbp - 0x6c], edx
00A0A3CA  89 55 8C                        mov dword ptr [rbp - 0x74], edx
00A0A3CD  89 54 24 50                     mov dword ptr [rsp + 0x50], edx
00A0A3D1  48 8D 4D 8C                     lea rcx, [rbp - 0x74]
00A0A3D5  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
00A0A3DA  4D 8B CF                        mov r9, r15
00A0A3DD  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00A0A3E1  41 B8 01 00 00 00               mov r8d, 1
00A0A3E7  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
00A0A3EC  48 8D 45 94                     lea rax, [rbp - 0x6c]
00A0A3F0  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A0A3F5  48 8B CF                        mov rcx, rdi
00A0A3F8  48 8D 45 E0                     lea rax, [rbp - 0x20]
00A0A3FC  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A0A401  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00A0A406  48 8B D6                        mov rdx, rsi
00A0A409  E8 72 7D ED FF                  call 0x1408e2180
00A0A40E  8B D8                           mov ebx, eax
00A0A410  3D 23 00 00 C0                  cmp eax, 0xc0000023
00A0A415  0F 84 B4 03 00 00               je 0x140a0a7cf
00A0A41B  33 D2                           xor edx, edx
00A0A41D  85 C0                           test eax, eax
00A0A41F  0F 89 30 03 00 00               jns 0x140a0a755
00A0A425  3D 25 02 00 C0                  cmp eax, 0xc0000225
00A0A42A  75 02                           jne 0x140a0a42e
00A0A42C  8B DA                           mov ebx, edx
00A0A42E  4D 85 ED                        test r13, r13
00A0A431  0F 85 00 09 00 00               jne 0x140a0ad37
00A0A437  4D 85 F6                        test r14, r14
00A0A43A  0F 85 C6 01 00 00               jne 0x140a0a606
00A0A440  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00A0A445  48 85 C0                        test rax, rax
00A0A448  0F 85 F6 08 00 00               jne 0x140a0ad44
00A0A44E  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
00A0A452  48 85 C0                        test rax, rax
00A0A455  0F 85 F8 08 00 00               jne 0x140a0ad53
00A0A45B  4D 85 E4                        test r12, r12
00A0A45E  0F 85 B1 01 00 00               jne 0x140a0a615
00A0A464  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00A0A469  48 85 C0                        test rax, rax
00A0A46C  0F 85 F0 08 00 00               jne 0x140a0ad62
00A0A472  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
00A0A476  48 85 C0                        test rax, rax
00A0A479  0F 85 F2 08 00 00               jne 0x140a0ad71
00A0A47F  8B C3                           mov eax, ebx
00A0A481  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
00A0A485  48 33 CC                        xor rcx, rsp
00A0A488  E8 B3 21 CA FF                  call 0x1406ac640
00A0A48D  48 8B 9C 24 60 01 00 00         mov rbx, qword ptr [rsp + 0x160]
00A0A495  48 81 C4 20 01 00 00            add rsp, 0x120
00A0A49C  41 5F                           pop r15
00A0A49E  41 5E                           pop r14
00A0A4A0  41 5D                           pop r13
00A0A4A2  41 5C                           pop r12
00A0A4A4  5F                              pop rdi
00A0A4A5  5E                              pop rsi
00A0A4A6  5D                              pop rbp
00A0A4A7  C3                              ret
00A0A4A8  CC                              int3
00A0A4A9  85 C0                           test eax, eax
00A0A4AB  0F 88 55 06 00 00               js 0x140a0ab06
00A0A4B1  4C 8B 65 C0                     mov r12, qword ptr [rbp - 0x40]
00A0A4B5  4D 85 E4                        test r12, r12
00A0A4B8  0F 84 C4 FD FF FF               je 0x140a0a282
00A0A4BE  4C 8D 45 D0                     lea r8, [rbp - 0x30]
00A0A4C2  48 8B D6                        mov rdx, rsi
00A0A4C5  48 8B CF                        mov rcx, rdi
00A0A4C8  E8 3B 0A 00 00                  call 0x140a0af08
00A0A4CD  45 33 C0                        xor r8d, r8d
00A0A4D0  8B D8                           mov ebx, eax
00A0A4D2  85 C0                           test eax, eax
00A0A4D4  0F 88 2C 06 00 00               js 0x140a0ab06
00A0A4DA  49 8B CC                        mov rcx, r12
00A0A4DD  C6 44 24 66 01                  mov byte ptr [rsp + 0x66], 1
00A0A4E2  E8 31 11 00 00                  call 0x140a0b618
00A0A4E7  89 45 98                        mov dword ptr [rbp - 0x68], eax
00A0A4EA  41 8B C8                        mov ecx, r8d
00A0A4ED  41 8B 44 24 08                  mov eax, dword ptr [r12 + 8]
00A0A4F2  C1 E8 03                        shr eax, 3
00A0A4F5  83 E0 07                        and eax, 7
00A0A4F8  83 F8 07                        cmp eax, 7
00A0A4FB  0F 82 ED 05 00 00               jb 0x140a0aaee
00A0A501  89 4D 9C                        mov dword ptr [rbp - 0x64], ecx
00A0A504  BA 72 00 00 00                  mov edx, 0x72
00A0A509  B9 00 01 00 00                  mov ecx, 0x100
00A0A50E  41 B8 50 4E 50 52               mov r8d, 0x52504e50
00A0A514  E8 D7 7B 17 00                  call 0x140b820f0
00A0A519  4C 8B F0                        mov r14, rax
00A0A51C  48 85 C0                        test rax, rax
00A0A51F  0F 84 DC 05 00 00               je 0x140a0ab01
00A0A525  44 8B 45 9C                     mov r8d, dword ptr [rbp - 0x64]
00A0A529  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00A0A52D  8B 55 98                        mov edx, dword ptr [rbp - 0x68]
00A0A530  4C 8B C8                        mov r9, rax
00A0A533  E8 D0 0A 00 00                  call 0x140a0b008
00A0A538  8B D8                           mov ebx, eax
00A0A53A  85 C0                           test eax, eax
00A0A53C  0F 88 C0 00 00 00               js 0x140a0a602
00A0A542  BB 10 00 00 00                  mov ebx, 0x10
00A0A547  8B D3                           mov edx, ebx
00A0A549  B9 00 01 00 00                  mov ecx, 0x100
00A0A54E  41 B8 50 4E 50 52               mov r8d, 0x52504e50
00A0A554  89 5D 90                        mov dword ptr [rbp - 0x70], ebx
00A0A557  E8 94 7B 17 00                  call 0x140b820f0
00A0A55C  33 D2                           xor edx, edx
00A0A55E  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00A0A563  48 85 C0                        test rax, rax
00A0A566  0F 85 30 A9 12 00               jne 0x140b34e9c
00A0A56C  BB 17 00 00 C0                  mov ebx, 0xc0000017
00A0A571  E9 8C 00 00 00                  jmp 0x140a0a602
00A0A576  4D 85 E4                        test r12, r12
00A0A579  0F 84 D9 FD FF FF               je 0x140a0a358
00A0A57F  41 8B 14 24                     mov edx, dword ptr [r12]
00A0A583  84 D2                           test dl, dl
00A0A585  0F 88 7E 06 00 00               js 0x140a0ac09
00A0A58B  8B C2                           mov eax, edx
00A0A58D  4D 8B CF                        mov r9, r15
00A0A590  C1 E8 10                        shr eax, 0x10
00A0A593  0F B6 C8                        movzx ecx, al
00A0A596  41 0F B6 44 24 03               movzx eax, byte ptr [r12 + 3]
00A0A59C  C1 E0 08                        shl eax, 8
00A0A59F  0B C8                           or ecx, eax
00A0A5A1  C1 EA 08                        shr edx, 8
00A0A5A4  C1 E1 08                        shl ecx, 8
00A0A5A7  0F B6 C2                        movzx eax, dl
00A0A5AA  48 8B D6                        mov rdx, rsi
00A0A5AD  0B C8                           or ecx, eax
00A0A5AF  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00A0A5B4  81 C9 00 00 00 FF               or ecx, 0xff000000
00A0A5BA  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
00A0A5BE  33 C9                           xor ecx, ecx
00A0A5C0  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00A0A5C4  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00A0A5CC  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A0A5D1  48 8D 05 20 A8 60 FF            lea rax, [rip - 0x9f57e0]
00A0A5D8  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00A0A5E0  44 8D 41 01                     lea r8d, [rcx + 1]
00A0A5E4  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A0A5E9  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00A0A5EE  48 8B CF                        mov rcx, rdi
00A0A5F1  E8 F2 C0 EE FF                  call 0x1408f66e8
00A0A5F6  33 D2                           xor edx, edx
00A0A5F8  8B D8                           mov ebx, eax
00A0A5FA  85 C0                           test eax, eax
00A0A5FC  0F 89 D2 00 00 00               jns 0x140a0a6d4
00A0A602  4C 8B 65 A8                     mov r12, qword ptr [rbp - 0x58]
00A0A606  33 D2                           xor edx, edx
00A0A608  49 8B CE                        mov rcx, r14
00A0A60B  E8 60 82 17 00                  call 0x140b82870
00A0A610  E9 2B FE FF FF                  jmp 0x140a0a440
00A0A615  33 D2                           xor edx, edx
00A0A617  49 8B CC                        mov rcx, r12
00A0A61A  E8 51 82 17 00                  call 0x140b82870
00A0A61F  E9 40 FE FF FF                  jmp 0x140a0a464
00A0A624  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00A0A628  48 8D 05 59 A8 60 FF            lea rax, [rip - 0x9f57a7]
00A0A62F  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
00A0A633  4D 8B CF                        mov r9, r15
00A0A636  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
00A0A63B  41 B8 01 00 00 00               mov r8d, 1
00A0A641  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
00A0A645  48 8B CF                        mov rcx, rdi
00A0A648  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A0A64D  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00A0A652  48 8B D6                        mov rdx, rsi
00A0A655  E8 8E C0 EE FF                  call 0x1408f66e8
00A0A65A  33 C9                           xor ecx, ecx
00A0A65C  48 8D 05 3D A8 60 FF            lea rax, [rip - 0x9f57c3]
00A0A663  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00A0A667  4D 8B CF                        mov r9, r15
00A0A66A  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00A0A66E  48 8B D6                        mov rdx, rsi
00A0A671  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00A0A676  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00A0A67A  44 8D 41 01                     lea r8d, [rcx + 1]
00A0A67E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A0A683  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00A0A688  48 8B CF                        mov rcx, rdi
00A0A68B  E8 58 C0 EE FF                  call 0x1408f66e8
00A0A690  33 C9                           xor ecx, ecx
00A0A692  48 8D 05 1F A8 60 FF            lea rax, [rip - 0x9f57e1]
00A0A699  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00A0A69D  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00A0A6A1  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00A0A6A6  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00A0A6AA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A0A6AF  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00A0A6B4  4D 8B CF                        mov r9, r15
00A0A6B7  41 B8 01 00 00 00               mov r8d, 1
00A0A6BD  48 8B D6                        mov rdx, rsi
00A0A6C0  48 8B CF                        mov rcx, rdi
00A0A6C3  E8 20 C0 EE FF                  call 0x1408f66e8
00A0A6C8  33 D2                           xor edx, edx
00A0A6CA  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00A0A6CF  E9 63 FC FF FF                  jmp 0x140a0a337
00A0A6D4  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
00A0A6D9  4D 85 E4                        test r12, r12
00A0A6DC  0F 84 88 FC FF FF               je 0x140a0a36a
00A0A6E2  41 8B 44 24 08                  mov eax, dword ptr [r12 + 8]
00A0A6E7  8B CA                           mov ecx, edx
00A0A6E9  C1 E8 0A                        shr eax, 0xa
00A0A6EC  83 E0 0F                        and eax, 0xf
00A0A6EF  83 F8 09                        cmp eax, 9
00A0A6F2  0F 82 55 05 00 00               jb 0x140a0ac4d
00A0A6F8  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00A0A6FC  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00A0A701  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00A0A709  4D 8B CF                        mov r9, r15
00A0A70C  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A0A711  41 B8 01 00 00 00               mov r8d, 1
00A0A717  48 8D 05 B2 A7 60 FF            lea rax, [rip - 0x9f584e]
00A0A71E  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00A0A726  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A0A72B  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00A0A730  48 8B D6                        mov rdx, rsi
00A0A733  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
00A0A737  48 8B CF                        mov rcx, rdi
00A0A73A  E8 A9 BF EE FF                  call 0x1408f66e8
00A0A73F  33 D2                           xor edx, edx
00A0A741  8B D8                           mov ebx, eax
00A0A743  85 C0                           test eax, eax
00A0A745  0F 88 B7 FE FF FF               js 0x140a0a602
00A0A74B  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
00A0A750  E9 DB AE 12 00                  jmp 0x140b35630
00A0A755  81 7D 94 03 10 00 00            cmp dword ptr [rbp - 0x6c], 0x1003
00A0A75C  0F 85 C1 05 00 00               jne 0x140a0ad23
00A0A762  8B 4D 8C                        mov ecx, dword ptr [rbp - 0x74]
00A0A765  83 F9 01                        cmp ecx, 1
00A0A768  0F 82 B5 05 00 00               jb 0x140a0ad23
00A0A76E  41 8B 04 24                     mov eax, dword ptr [r12]
00A0A772  83 E0 7F                        and eax, 0x7f
00A0A775  83 F8 01                        cmp eax, 1
00A0A778  0F 82 AE FC FF FF               jb 0x140a0a42c
00A0A77E  0F 84 91 05 00 00               je 0x140a0ad15
00A0A784  83 F8 02                        cmp eax, 2
00A0A787  72 09                           jb 0x140a0a792
00A0A789  83 F9 14                        cmp ecx, 0x14
00A0A78C  0F 82 9A FC FF FF               jb 0x140a0a42c
00A0A792  41 8B 44 24 08                  mov eax, dword ptr [r12 + 8]
00A0A797  83 E0 38                        and eax, 0x38
00A0A79A  3C 30                           cmp al, 0x30
00A0A79C  0F 83 8A FC FF FF               jae 0x140a0a42c
00A0A7A2  38 54 24 66                     cmp byte ptr [rsp + 0x66], dl
00A0A7A6  0F 85 EE AE 12 00               jne 0x140b3569a
00A0A7AC  4C 8D 45 D0                     lea r8, [rbp - 0x30]
00A0A7B0  48 8B D6                        mov rdx, rsi
00A0A7B3  48 8B CF                        mov rcx, rdi
00A0A7B6  E8 4D 07 00 00                  call 0x140a0af08
00A0A7BB  8B D8                           mov ebx, eax
00A0A7BD  85 C0                           test eax, eax
00A0A7BF  0F 88 69 FC FF FF               js 0x140a0a42e
00A0A7C5  C6 44 24 66 01                  mov byte ptr [rsp + 0x66], 1
00A0A7CA  E9 CB AE 12 00                  jmp 0x140b3569a
00A0A7CF  8B 45 8C                        mov eax, dword ptr [rbp - 0x74]
00A0A7D2  3B 45 90                        cmp eax, dword ptr [rbp - 0x70]
00A0A7D5  0F 86 48 05 00 00               jbe 0x140a0ad23
00A0A7DB  4D 85 E4                        test r12, r12
00A0A7DE  0F 85 1F 05 00 00               jne 0x140a0ad03
00A0A7E4  8B D0                           mov edx, eax
00A0A7E6  B9 00 01 00 00                  mov ecx, 0x100
00A0A7EB  41 B8 50 4E 50 52               mov r8d, 0x52504e50
00A0A7F1  89 45 90                        mov dword ptr [rbp - 0x70], eax
00A0A7F4  E8 F7 78 17 00                  call 0x140b820f0
00A0A7F9  33 D2                           xor edx, edx
00A0A7FB  4C 8B E0                        mov r12, rax
00A0A7FE  48 85 C0                        test rax, rax
00A0A801  0F 84 26 05 00 00               je 0x140a0ad2d
00A0A807  8B 45 90                        mov eax, dword ptr [rbp - 0x70]
00A0A80A  E9 BE FB FF FF                  jmp 0x140a0a3cd
00A0A80F  BB BB 00 00 C0                  mov ebx, 0xc00000bb
00A0A814  E9 66 FC FF FF                  jmp 0x140a0a47f
00A0A819  4D 85 F6                        test r14, r14
00A0A81C  0F 84 40 A8 12 00               je 0x140b35062
00A0A822  8A 44 24 64                     mov al, byte ptr [rsp + 0x64]
00A0A826  88 44 24 64                     mov byte ptr [rsp + 0x64], al
00A0A82A  48 83 C8 FF                     or rax, 0xffffffffffffffff
00A0A82E  48 FF C0                        inc rax
00A0A831  66 41 39 14 46                  cmp word ptr [r14 + rax*2], dx
00A0A836  75 F6                           jne 0x140a0a82e
00A0A838  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00A0A83C  8D 04 45 02 00 00 00            lea eax, [rax*2 + 2]
00A0A843  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00A0A847  4D 8B CF                        mov r9, r15
00A0A84A  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00A0A84F  48 8D 05 4A 6D 60 FF            lea rax, [rip - 0x9f92b6]
00A0A856  C7 44 24 30 12 00 00 00         mov dword ptr [rsp + 0x30], 0x12
00A0A85E  41 B8 01 00 00 00               mov r8d, 1
00A0A864  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A0A869  48 8B CF                        mov rcx, rdi
00A0A86C  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00A0A871  48 8B D6                        mov rdx, rsi
00A0A874  E8 6F BE EE FF                  call 0x1408f66e8
00A0A879  33 D2                           xor edx, edx
00A0A87B  8B D8                           mov ebx, eax
00A0A87D  85 C0                           test eax, eax
00A0A87F  0F 88 7D FD FF FF               js 0x140a0a602
00A0A885  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00A0A889  48 8D 45 98                     lea rax, [rbp - 0x68]
00A0A88D  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00A0A895  44 8D 42 01                     lea r8d, [rdx + 1]
00A0A899  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A0A89E  4D 8B CF                        mov r9, r15
00A0A8A1  48 8D 05 68 A5 60 FF            lea rax, [rip - 0x9f5a98]
00A0A8A8  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00A0A8B0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A0A8B5  48 8B CF                        mov rcx, rdi
00A0A8B8  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00A0A8BD  48 8B D6                        mov rdx, rsi
00A0A8C0  E8 23 BE EE FF                  call 0x1408f66e8
00A0A8C5  33 D2                           xor edx, edx
00A0A8C7  8B D8                           mov ebx, eax
00A0A8C9  85 C0                           test eax, eax
00A0A8CB  0F 88 31 FD FF FF               js 0x140a0a602
00A0A8D1  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00A0A8D5  48 8D 45 9C                     lea rax, [rbp - 0x64]
00A0A8D9  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00A0A8E1  44 8D 42 01                     lea r8d, [rdx + 1]
00A0A8E5  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A0A8EA  4D 8B CF                        mov r9, r15
00A0A8ED  48 8D 05 34 A5 60 FF            lea rax, [rip - 0x9f5acc]
00A0A8F4  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00A0A8FC  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A0A901  48 8B CF                        mov rcx, rdi
00A0A904  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00A0A909  48 8B D6                        mov rdx, rsi
00A0A90C  E8 D7 BD EE FF                  call 0x1408f66e8
00A0A911  33 D2                           xor edx, edx
00A0A913  8B D8                           mov ebx, eax
00A0A915  85 C0                           test eax, eax
00A0A917  0F 88 E5 FC FF FF               js 0x140a0a602
00A0A91D  4D 85 E4                        test r12, r12
00A0A920  0F 84 BE 02 00 00               je 0x140a0abe4
00A0A926  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00A0A92B  44 8D 42 01                     lea r8d, [rdx + 1]
00A0A92F  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00A0A933  4D 8B CF                        mov r9, r15
00A0A936  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00A0A93E  48 85 C0                        test rax, rax
00A0A941  0F 85 1C A6 12 00               jne 0x140b34f63
00A0A947  41 8B 44 24 04                  mov eax, dword ptr [r12 + 4]
00A0A94C  0F B7 C8                        movzx ecx, ax
00A0A94F  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00A0A954  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A0A959  48 8D 05 E0 A4 60 FF            lea rax, [rip - 0x9f5b20]
00A0A960  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00A0A968  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A0A96D  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00A0A972  48 8B D6                        mov rdx, rsi
00A0A975  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
00A0A979  48 8B CF                        mov rcx, rdi
00A0A97C  E8 67 BD EE FF                  call 0x1408f66e8
00A0A981  33 D2                           xor edx, edx
00A0A983  8B D8                           mov ebx, eax
00A0A985  85 C0                           test eax, eax
00A0A987  0F 88 75 FC FF FF               js 0x140a0a602
00A0A98D  41 0F B7 44 24 06               movzx eax, word ptr [r12 + 6]
00A0A993  44 8D 42 01                     lea r8d, [rdx + 1]
00A0A997  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00A0A99B  4D 8B CF                        mov r9, r15
00A0A99E  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00A0A9A6  48 8B CF                        mov rcx, rdi
00A0A9A9  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00A0A9AD  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00A0A9B2  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A0A9B7  48 8D 05 9A A4 60 FF            lea rax, [rip - 0x9f5b66]
00A0A9BE  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00A0A9C6  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A0A9CB  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00A0A9D0  48 8B D6                        mov rdx, rsi
00A0A9D3  E8 10 BD EE FF                  call 0x1408f66e8
00A0A9D8  33 D2                           xor edx, edx
00A0A9DA  8B D8                           mov ebx, eax
00A0A9DC  85 C0                           test eax, eax
00A0A9DE  0F 88 1E FC FF FF               js 0x140a0a602
00A0A9E4  48 39 54 24 78                  cmp qword ptr [rsp + 0x78], rdx
00A0A9E9  0F 85 B8 01 00 00               jne 0x140a0aba7
00A0A9EF  4D 85 E4                        test r12, r12
00A0A9F2  74 1F                           je 0x140a0aa13
00A0A9F4  41 B8 FF FF 00 00               mov r8d, 0xffff
00A0A9FA  66 45 39 44 24 12               cmp word ptr [r12 + 0x12], r8w
00A0AA00  74 11                           je 0x140a0aa13
00A0AA02  41 8B 44 24 10                  mov eax, dword ptr [r12 + 0x10]
00A0AA07  0F B7 C8                        movzx ecx, ax
00A0AA0A  41 3B C8                        cmp ecx, r8d
00A0AA0D  0F 85 EC 01 00 00               jne 0x140a0abff
00A0AA13  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
00A0AA18  E9 03 F9 FF FF                  jmp 0x140a0a320
00A0AA1D  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00A0AA21  48 8D 05 18 A4 60 FF            lea rax, [rip - 0x9f5be8]
00A0AA28  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
00A0AA2C  4D 8B CF                        mov r9, r15
00A0AA2F  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
00A0AA34  41 B8 01 00 00 00               mov r8d, 1
00A0AA3A  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
00A0AA3E  48 8B CF                        mov rcx, rdi
00A0AA41  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A0AA46  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00A0AA4B  48 8B D6                        mov rdx, rsi
00A0AA4E  E8 95 BC EE FF                  call 0x1408f66e8
00A0AA53  33 C9                           xor ecx, ecx
00A0AA55  48 8D 05 FC A3 60 FF            lea rax, [rip - 0x9f5c04]
00A0AA5C  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00A0AA60  4D 8B CF                        mov r9, r15
00A0AA63  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00A0AA67  48 8B D6                        mov rdx, rsi
00A0AA6A  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00A0AA6F  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00A0AA73  44 8D 41 01                     lea r8d, [rcx + 1]
00A0AA77  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A0AA7C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00A0AA81  48 8B CF                        mov rcx, rdi
00A0AA84  E8 5F BC EE FF                  call 0x1408f66e8
00A0AA89  33 C9                           xor ecx, ecx
00A0AA8B  48 8D 05 DE A3 60 FF            lea rax, [rip - 0x9f5c22]
00A0AA92  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00A0AA96  4D 8B CF                        mov r9, r15
00A0AA99  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00A0AA9D  48 8B D6                        mov rdx, rsi
00A0AAA0  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00A0AAA5  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00A0AAA9  44 8D 41 01                     lea r8d, [rcx + 1]
00A0AAAD  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A0AAB2  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00A0AAB7  48 8B CF                        mov rcx, rdi
00A0AABA  E8 29 BC EE FF                  call 0x1408f66e8
00A0AABF  33 D2                           xor edx, edx
00A0AAC1  4D 85 F6                        test r14, r14
00A0AAC4  0F 85 25 FF FF FF               jne 0x140a0a9ef
00A0AACA  E9 51 F8 FF FF                  jmp 0x140a0a320
00A0AACF  3D 25 02 00 C0                  cmp eax, 0xc0000225
00A0AAD4  75 39                           jne 0x140a0ab0f
00A0AAD6  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00A0AADB  33 D2                           xor edx, edx
00A0AADD  E8 8E 7D 17 00                  call 0x140b82870
00A0AAE2  33 C9                           xor ecx, ecx
00A0AAE4  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
00A0AAE9  E9 94 F7 FF FF                  jmp 0x140a0a282
00A0AAEE  48 8D 0D 0B 55 5F FF            lea rcx, [rip - 0xa0aaf5]
00A0AAF5  8B 8C 81 D0 21 04 00            mov ecx, dword ptr [rcx + rax*4 + 0x421d0]
00A0AAFC  E9 00 FA FF FF                  jmp 0x140a0a501
00A0AB01  BB 17 00 00 C0                  mov ebx, 0xc0000017
00A0AB06  4C 8B 65 A8                     mov r12, qword ptr [rbp - 0x58]
00A0AB0A  E9 4C F9 FF FF                  jmp 0x140a0a45b
00A0AB0F  85 C0                           test eax, eax
00A0AB11  0F 88 EB FA FF FF               js 0x140a0a602
00A0AB17  81 7D 88 03 10 00 00            cmp dword ptr [rbp - 0x78], 0x1003
00A0AB1E  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00A0AB23  0F 85 ED A3 12 00               jne 0x140b34f16
00A0AB29  83 7C 24 68 10                  cmp dword ptr [rsp + 0x68], 0x10
00A0AB2E  0F 82 E2 A3 12 00               jb 0x140b34f16
00A0AB34  8A 01                           mov al, byte ptr [rcx]
00A0AB36  24 1F                           and al, 0x1f
00A0AB38  3C 01                           cmp al, 1
00A0AB3A  0F 83 42 F7 FF FF               jae 0x140a0a282
00A0AB40  E9 D1 A3 12 00                  jmp 0x140b34f16
00A0AB45  BB 17 00 00 C0                  mov ebx, 0xc0000017
00A0AB4A  E9 0B A4 12 00                  jmp 0x140b34f5a
00A0AB4F  33 D2                           xor edx, edx
00A0AB51  85 C0                           test eax, eax
00A0AB53  0F 88 01 A4 12 00               js 0x140b34f5a
00A0AB59  83 7D 88 12                     cmp dword ptr [rbp - 0x78], 0x12
00A0AB5D  0F 85 98 F7 FF FF               jne 0x140a0a2fb
00A0AB63  83 7C 24 68 02                  cmp dword ptr [rsp + 0x68], 2
00A0AB68  0F 82 8D F7 FF FF               jb 0x140a0a2fb
00A0AB6E  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
00A0AB73  E9 96 F7 FF FF                  jmp 0x140a0a30e
00A0AB78  48 85 DB                        test rbx, rbx
00A0AB7B  0F 84 A8 A3 12 00               je 0x140b34f29
00A0AB81  49 8B D6                        mov rdx, r14
00A0AB84  48 8B CB                        mov rcx, rbx
00A0AB87  E8 F4 54 AF FF                  call 0x140500080
00A0AB8C  33 D2                           xor edx, edx
00A0AB8E  85 C0                           test eax, eax
00A0AB90  0F 85 93 A3 12 00               jne 0x140b34f29
00A0AB96  8A C2                           mov al, dl
00A0AB98  E9 8E A3 12 00                  jmp 0x140b34f2b
00A0AB9D  C6 44 24 64 01                  mov byte ptr [rsp + 0x64], 1
00A0ABA2  E9 99 A3 12 00                  jmp 0x140b34f40
00A0ABA7  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00A0ABAB  48 8D 05 BE A2 60 FF            lea rax, [rip - 0x9f5d42]
00A0ABB2  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
00A0ABB6  4D 8B CF                        mov r9, r15
00A0ABB9  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
00A0ABBE  41 B8 01 00 00 00               mov r8d, 1
00A0ABC4  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
00A0ABC8  48 8B CF                        mov rcx, rdi
00A0ABCB  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A0ABD0  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00A0ABD5  48 8B D6                        mov rdx, rsi
00A0ABD8  E8 0B BB EE FF                  call 0x1408f66e8
00A0ABDD  33 D2                           xor edx, edx
00A0ABDF  E9 0B FE FF FF                  jmp 0x140a0a9ef
00A0ABE4  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
00A0ABE9  8A 44 24 64                     mov al, byte ptr [rsp + 0x64]
00A0ABED  88 44 24 64                     mov byte ptr [rsp + 0x64], al
00A0ABF1  48 85 DB                        test rbx, rbx
00A0ABF4  0F 84 F5 FD FF FF               je 0x140a0a9ef
00A0ABFA  E9 1E FE FF FF                  jmp 0x140a0aa1d
00A0ABFF  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00A0AC04  E9 10 A5 12 00                  jmp 0x140b35119
00A0AC09  33 D2                           xor edx, edx
00A0AC0B  E9 48 F7 FF FF                  jmp 0x140a0a358
00A0AC10  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00A0AC14  48 8D 05 DD A1 60 FF            lea rax, [rip - 0x9f5e23]
00A0AC1B  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
00A0AC1F  4D 8B CF                        mov r9, r15
00A0AC22  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
00A0AC27  41 B8 01 00 00 00               mov r8d, 1
00A0AC2D  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
00A0AC31  48 8B CF                        mov rcx, rdi
00A0AC34  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A0AC39  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00A0AC3E  48 8B D6                        mov rdx, rsi
00A0AC41  E8 A2 BA EE FF                  call 0x1408f66e8
00A0AC46  33 D2                           xor edx, edx
00A0AC48  E9 14 F7 FF FF                  jmp 0x140a0a361
00A0AC4D  48 8D 0D AC 53 5F FF            lea rcx, [rip - 0xa0ac54]
00A0AC54  8B 8C 81 A8 21 04 00            mov ecx, dword ptr [rcx + rax*4 + 0x421a8]
00A0AC5B  E9 98 FA FF FF                  jmp 0x140a0a6f8
00A0AC60  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00A0AC64  48 8D 05 65 A2 60 FF            lea rax, [rip - 0x9f5d9b]
00A0AC6B  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
00A0AC6F  4D 8B CF                        mov r9, r15
00A0AC72  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
00A0AC77  41 B8 01 00 00 00               mov r8d, 1
00A0AC7D  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
00A0AC81  48 8B CF                        mov rcx, rdi
00A0AC84  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A0AC89  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00A0AC8E  48 8B D6                        mov rdx, rsi
00A0AC91  E8 52 BA EE FF                  call 0x1408f66e8
00A0AC96  33 D2                           xor edx, edx
00A0AC98  E9 D6 F6 FF FF                  jmp 0x140a0a373
00A0AC9D  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00A0ACA1  48 8D 05 D8 6F 61 FF            lea rax, [rip - 0x9e9028]
00A0ACA8  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
00A0ACAC  4D 8B CF                        mov r9, r15
00A0ACAF  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
00A0ACB4  41 B8 01 00 00 00               mov r8d, 1
00A0ACBA  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
00A0ACBE  48 8B CF                        mov rcx, rdi
00A0ACC1  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A0ACC6  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00A0ACCB  48 8B D6                        mov rdx, rsi
00A0ACCE  E8 15 BA EE FF                  call 0x1408f66e8
00A0ACD3  33 D2                           xor edx, edx
00A0ACD5  E9 AB F6 FF FF                  jmp 0x140a0a385
00A0ACDA  38 54 24 64                     cmp byte ptr [rsp + 0x64], dl
00A0ACDE  0F 84 AA F6 FF FF               je 0x140a0a38e
00A0ACE4  4C 8B C6                        mov r8, rsi
00A0ACE7  49 8B D6                        mov rdx, r14
00A0ACEA  48 8B CF                        mov rcx, rdi
00A0ACED  E8 FA 30 E2 FF                  call 0x14082ddec
00A0ACF2  33 D2                           xor edx, edx
00A0ACF4  8B D8                           mov ebx, eax
00A0ACF6  85 C0                           test eax, eax
00A0ACF8  0F 88 04 F9 FF FF               js 0x140a0a602
00A0ACFE  E9 8B F6 FF FF                  jmp 0x140a0a38e
00A0AD03  33 D2                           xor edx, edx
00A0AD05  49 8B CC                        mov rcx, r12
00A0AD08  E8 63 7B 17 00                  call 0x140b82870
00A0AD0D  8B 45 8C                        mov eax, dword ptr [rbp - 0x74]
00A0AD10  E9 CF FA FF FF                  jmp 0x140a0a7e4
00A0AD15  83 F9 10                        cmp ecx, 0x10
00A0AD18  0F 82 0E F7 FF FF               jb 0x140a0a42c
00A0AD1E  E9 61 FA FF FF                  jmp 0x140a0a784
00A0AD23  BB 01 00 00 C0                  mov ebx, 0xc0000001
00A0AD28  E9 01 F7 FF FF                  jmp 0x140a0a42e
00A0AD2D  BB 17 00 00 C0                  mov ebx, 0xc0000017
00A0AD32  E9 F7 F6 FF FF                  jmp 0x140a0a42e
00A0AD37  49 8B CD                        mov rcx, r13
00A0AD3A  E8 71 25 CA FF                  call 0x1406ad2b0
00A0AD3F  E9 F3 F6 FF FF                  jmp 0x140a0a437
00A0AD44  33 D2                           xor edx, edx
00A0AD46  48 8B C8                        mov rcx, rax
00A0AD49  E8 22 7B 17 00                  call 0x140b82870
00A0AD4E  E9 FB F6 FF FF                  jmp 0x140a0a44e
00A0AD53  33 D2                           xor edx, edx
00A0AD55  48 8B C8                        mov rcx, rax
00A0AD58  E8 13 7B 17 00                  call 0x140b82870
00A0AD5D  E9 F9 F6 FF FF                  jmp 0x140a0a45b
00A0AD62  33 D2                           xor edx, edx
00A0AD64  48 8B C8                        mov rcx, rax
00A0AD67  E8 04 7B 17 00                  call 0x140b82870
00A0AD6C  E9 01 F7 FF FF                  jmp 0x140a0a472
00A0AD71  33 D2                           xor edx, edx
00A0AD73  48 8B C8                        mov rcx, rax
00A0AD76  E8 F5 7A 17 00                  call 0x140b82870
00A0AD7B  E9 FF F6 FF FF                  jmp 0x140a0a47f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall _CmUpdateDevicePanel(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA4;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned int v_stack_mBC;
    unsigned int v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned int v_stack_mC8;
    unsigned int v_stack_mCC;
    unsigned int v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int8 v_stack_mEC;
    unsigned int v_stack_mF0;
    unsigned __int8 v_stack_mF2;
    unsigned __int8 v_stack_mF3;
    unsigned __int8 v_stack_mF4;
    unsigned int v_stack_mF8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned int v_stack_p48;
    unsigned __int64 v_stack_p60;
    unsigned __int8 v_stack_p64;
    unsigned __int8 v_stack_p66;
    unsigned int v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (288);
    result = (*(unsigned __int64 *)(v_rip + 4195761)) ^ (v_rsp);
    v_stack_m48 = result;
    v_r12 = 0;
    result = 0;
    v_stack_mB0 = 0;
    v_stack_mCC = 0;
    v_stack_m98 = 0;
    v_stack_mC4 = 0;
    v_stack_mD8 = 0;
    v_stack_mD0 = (unsigned int)(result + 1);
    v_stack_mB8 = 0;
    v_stack_mE8 = 0;
    v_stack_m88 = v_xmm0;
    v_stack_mF2 = 0;
    v_stack_mC0 = 0;
    v_stack_mBC = 0;
    v_stack_mE0 = 0;
    v_stack_mA0 = 0;
    v_stack_mF4 = 0;
    v_stack_m78 = v_xmm0;
    v_stack_m68 = 0;
    v_stack_m60 = v_xmm1;
    v_stack_m50 = 0;
    v_stack_m90 = 0;
    v_stack_mF3 = 0;
    v_stack_mF8 = 0;
    v_stack_mA8 = 0;
    v_stack_mA4 = 0;
    v_stack_mEC = 0;
    v_stack_mF0 = 0;
    result = CmIsRootDevice(a2, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00A0A80F;
    v_stack_m118 = v_stack_mC4;
    v_stack_m120 = v_stack_m98;
    v_stack_m128 = v_stack_mCC;
    v_stack_m130 = v_stack_mB0;
    v_stack_m138 = v_rip - 10441915;
    result = CmQueryDevicePanelPldProperty(*(unsigned __int64 *)(v_rip + 4571643), a2, (unsigned int)((unsigned int)(result + 1)), a3);
    if (((unsigned int)(result)) != 0xC0000225ULL) goto loc_00A0A4A9;
loc_00A0A282:
    result = ExAllocatePool2(256, 114, (unsigned int)(0x52504E50ULL), a3);
    a2 = 0;
    v_stack_mE0 = result;
    if (result == 0) goto loc_00A0AB45;
    v_stack_m108 = 0;
    v_stack_m110 = v_stack_mF0;
    v_stack_m118 = 114;
    v_stack_m120 = result;
    v_stack_m128 = v_stack_mD0;
    v_stack_m130 = v_rip - 10456378;
    v_stack_m138 = 0;
    result = PnpGetObjectProperty(*(unsigned __int64 *)(v_rip + 4571643), 0, 114 - 113, a3);
    if (((unsigned int)(result)) != 0xC0000225ULL) goto loc_00A0AB4F;
    a2 = 0;
loc_00A0A2FB:
    result = ExFreePoolWithTag(v_stack_mE0, a2, 114 - 113, a3);
    a2 = 0;
    v_stack_mE0 = 0;
loc_00A0A30E:
    if (0 != 0) goto loc_00A0AB78;
    if (0 != 0) goto loc_00A0AB9D;
loc_00A0A320:
    if (0 != 0) goto loc_00A0A624;
loc_00A0A337:
    if (0 != 0) goto loc_00A0A576;
loc_00A0A358:
    if (0 != 0) goto loc_00A0AC10;
loc_00A0A361:
    if (0 != 0) goto loc_00A0A6D9;
loc_00A0A36A:
    if (0 != 0) goto loc_00A0AC60;
loc_00A0A373:
    if (0 != 0) goto loc_00A0AC9D;
loc_00A0A385:
    if (0 != 0) goto loc_00A0ACDA;
loc_00A0A38E:
    v_stack_m68 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 10442155)));
    v_stack_m78 = v_xmm0;
    v_stack_m50 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 10442195)));
    v_stack_mC8 = (unsigned int)((unsigned int)(v_stack_mCC));
    v_stack_m60 = v_xmm0;
    v_stack_mB0 = 0;
    v_stack_mC4 = 0;
    v_stack_mCC = 0;
loc_00A0A3CD:
    v_stack_m108 = 0;
    v_stack_m110 = v_stack_mCC;
    v_stack_m118 = (unsigned int)((unsigned int)(v_stack_mCC));
    v_stack_m120 = v_stack_mB0;
    v_stack_m128 = v_stack_mC4;
    v_stack_m130 = v_stack_m78;
    v_stack_m138 = 0;
    result = PnpGetObjectProperty(*(unsigned __int64 *)(v_rip + 4571643), 0, 1, a3);
    if (((unsigned int)(result)) == 0xC0000023ULL) goto loc_00A0A7CF;
    a2 = 0;
    if (!sign_flag) goto loc_00A0A755;
    v_rbx = (unsigned int)((unsigned int)(result));
    if (((unsigned int)(result)) == 0xC0000225ULL) {
        v_rbx = 0;
    }
    if (0 != 0) goto loc_00A0AD37;
loc_00A0A437:
    if (0 != 0) goto loc_00A0A606;
loc_00A0A440:
    if (v_stack_mE0 != 0) goto loc_00A0AD44;
loc_00A0A44E:
    if (v_stack_mA0 != 0) goto loc_00A0AD53;
loc_00A0A45B:
    if (v_stack_mB0 != 0) goto loc_00A0A615;
loc_00A0A464:
    if (v_stack_mE8 != 0) goto loc_00A0AD62;
loc_00A0A472:
    if (v_stack_mD8 != 0) goto loc_00A0AD71;
loc_00A0A47F:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, 1, a3);
    v_rsp = (v_rsp) + (288);
    return result;
loc_00A0A4A9:
    if (sign_flag) goto loc_00A0AB06;
    if (v_stack_m98 == 0) goto loc_00A0A282;
    result = CmGetParentDeviceContainerId(*(unsigned __int64 *)(v_rip + 4571643), 0, v_stack_m88, a3);
    a3 = 0;
    if (sign_flag) goto loc_00A0AB06;
    v_stack_p66 = 1;
    result = _CmGetDevicePanelGroup(v_stack_m98, 0, a3, a3);
    v_stack_mC0 = (unsigned int)(result);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m98 + 8))) >> (3));
    result = (unsigned int)((result) & (7));
    if (((unsigned int)(result)) < 7) goto loc_00A0AAEE;
loc_00A0A501:
    v_stack_mBC = 0;
    result = ExAllocatePool2(256, 114, (unsigned int)(0x52504E50ULL), a3);
    if (result == 0) goto loc_00A0AB01;
    result = CmBuildDevicePanelId(v_stack_m88, (unsigned int)(v_stack_mC0), (unsigned int)(v_stack_mBC), result);
    if (sign_flag) goto loc_00A0A602;
    v_stack_mC8 = 16;
    result = ExAllocatePool2(256, 16, (unsigned int)(0x52504E50ULL), result);
    a2 = 0;
    v_stack_p70 = result;
    goto loc_00A0A602;
loc_00A0A576:
    if (v_stack_m98 == 0) goto loc_00A0A358;
    if (sign_flag) goto loc_00A0AC09;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m98))))) >> (16));
    result = (unsigned int)((*(unsigned __int8 *)(v_stack_m98 + 3)) << (8));
    a1 = (unsigned int)(((unsigned __int8)(result)) | ((unsigned int)(result)));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m98))) >> (8));
    a1 = (unsigned int)((a1) << (8));
    a1 = (unsigned int)((a1) | ((unsigned int)((unsigned __int8)(a2))));
    a1 = (unsigned int)((a1) | (0xFF000000ULL));
    v_stack_p60 = (unsigned int)(a1);
    a1 = 0;
    v_stack_p48 = 0;
    v_stack_p40 = 4;
    v_stack_p38 = v_stack_p60;
    v_stack_p30 = 7;
    v_stack_p28 = v_rip - 10442720;
    v_stack_p20 = 0;
    result = PnpSetObjectProperty(*(unsigned __int64 *)(v_rip + 4571643), a2, a1 + 1, 0);
    a2 = 0;
    if (!sign_flag) goto loc_00A0A6D4;
loc_00A0A602:
loc_00A0A606:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a1 + 1, 0);
    goto loc_00A0A440;
loc_00A0A615:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_mB0, a2, a1 + 1, 0);
    goto loc_00A0A464;
loc_00A0A624:
    v_stack_p48 = 0;
    v_stack_p40 = 0;
    v_stack_p38 = 0;
    v_stack_p30 = 0;
    v_stack_p28 = v_rip - 10442663;
    v_stack_p20 = 0;
    result = PnpSetObjectProperty(*(unsigned __int64 *)(v_rip + 4571643), 0, 1, 0);
    a1 = 0;
    v_stack_p48 = 0;
    v_stack_p40 = 0;
    v_stack_p38 = 0;
    v_stack_p30 = 0;
    v_stack_p28 = v_rip - 10442691;
    v_stack_p20 = 0;
    result = PnpSetObjectProperty(*(unsigned __int64 *)(v_rip + 4571643), 0, a1 + 1, 0);
    a1 = 0;
    v_stack_p48 = 0;
    v_stack_p40 = 0;
    v_stack_p38 = 0;
    v_stack_p30 = 0;
    v_stack_p28 = v_rip - 10442721;
    v_stack_p20 = 0;
    result = PnpSetObjectProperty(*(unsigned __int64 *)(v_rip + 4571643), 0, 1, 0);
    a2 = 0;
    goto loc_00A0A337;
loc_00A0A6D4:
loc_00A0A6D9:
    if (v_stack_mB0 == 0) goto loc_00A0A36A;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mB0 + 8))) >> (10));
    result = (unsigned int)((result) & (15));
    if (((unsigned int)(result)) < 9) goto loc_00A0AC4D;
loc_00A0A6F8:
    v_stack_p48 = 0;
    v_stack_p40 = 4;
    v_stack_p38 = v_stack_p60;
    v_stack_p30 = 7;
    v_stack_p28 = v_rip - 10442830;
    v_stack_p20 = 0;
    v_stack_p60 = 0;
    result = PnpSetObjectProperty(*(unsigned __int64 *)(v_rip + 4571643), 0, 1, 0);
    a2 = 0;
    if (sign_flag) goto loc_00A0A602;
loc_00A0A755:
    if (v_stack_mC4 != 0x1003ULL) goto loc_00A0AD23;
    if (((unsigned int)((unsigned int)(v_stack_mCC))) < 1) goto loc_00A0AD23;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mB0))) & (127));
    if (((unsigned int)(result)) < 1) goto loc_00A0A42C;
    if (((unsigned int)(result)) == 1) goto loc_00A0AD15;
loc_00A0A784:
    if (((unsigned int)(result)) < 2) goto loc_00A0A792;
    if (((unsigned int)((unsigned int)(v_stack_mCC))) < 20) goto loc_00A0A42C;
loc_00A0A792:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mB0 + 8))) & (56));
    if (((unsigned __int8)(result)) >= 48) goto loc_00A0A42C;
    result = CmGetParentDeviceContainerId(*(unsigned __int64 *)(v_rip + 4571643), 0, v_stack_m88, 0);
    if (sign_flag) goto loc_00A0A42E;
    v_stack_p66 = 1;
loc_00A0A7CF:
    if (((unsigned int)((unsigned int)(v_stack_mCC))) <= v_stack_mC8) goto loc_00A0AD23;
    if (v_stack_mB0 != 0) goto loc_00A0AD03;
loc_00A0A7E4:
    v_stack_mC8 = (unsigned int)((unsigned int)(v_stack_mCC));
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(v_stack_mCC))), (unsigned int)(0x52504E50ULL), 0);
    a2 = 0;
    if (result == 0) goto loc_00A0AD2D;
    goto loc_00A0A3CD;
loc_00A0A80F:
    goto loc_00A0A47F;
loc_00A0AAEE:
    goto loc_00A0A501;
loc_00A0AB01:
loc_00A0AB06:
    goto loc_00A0A45B;
loc_00A0AB45:
loc_00A0AB4F:
    a2 = 0;
    if (v_stack_mD0 != 18) goto loc_00A0A2FB;
    if (v_stack_p68 < 2) goto loc_00A0A2FB;
    goto loc_00A0A30E;
loc_00A0AB78:
    result = wcsicmp(v_stack_p78, result, (unsigned int)(0x52504E50ULL), 0);
    a2 = 0;
loc_00A0AB9D:
    v_stack_p64 = 1;
loc_00A0AC09:
    a2 = 0;
    goto loc_00A0A358;
loc_00A0AC10:
    v_stack_p48 = 0;
    v_stack_p40 = 0;
    v_stack_p38 = 0;
    v_stack_p30 = 0;
    v_stack_p28 = v_rip - 10444323;
    v_stack_p20 = 0;
    result = PnpSetObjectProperty(*(unsigned __int64 *)(v_rip + 4571643), 0, 1, 0);
    a2 = 0;
    goto loc_00A0A361;
loc_00A0AC4D:
    goto loc_00A0A6F8;
loc_00A0AC60:
    v_stack_p48 = 0;
    v_stack_p40 = 0;
    v_stack_p38 = 0;
    v_stack_p30 = 0;
    v_stack_p28 = v_rip - 10444187;
    v_stack_p20 = 0;
    result = PnpSetObjectProperty(*(unsigned __int64 *)(v_rip + 4571643), 0, 1, 0);
    a2 = 0;
    goto loc_00A0A373;
loc_00A0AC9D:
    v_stack_p48 = 0;
    v_stack_p40 = 0;
    v_stack_p38 = 0;
    v_stack_p30 = 0;
    v_stack_p28 = v_rip - 10391592;
    v_stack_p20 = 0;
    result = PnpSetObjectProperty(*(unsigned __int64 *)(v_rip + 4571643), 0, 1, 0);
    a2 = 0;
    goto loc_00A0A385;
loc_00A0ACDA:
    if (v_stack_p64 == 0) goto loc_00A0A38E;
    result = CmAddPanelDevice(*(unsigned __int64 *)(v_rip + 4571643), result, 0, 0);
    a2 = 0;
    if (sign_flag) goto loc_00A0A602;
    goto loc_00A0A38E;
loc_00A0AD03:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_mB0, a2, 0, 0);
    goto loc_00A0A7E4;
loc_00A0AD15:
    if (((unsigned int)(v_stack_mB0)) < 16) goto loc_00A0A42C;
    goto loc_00A0A784;
loc_00A0AD23:
    goto loc_00A0A42E;
loc_00A0AD2D:
    goto loc_00A0A42E;
loc_00A0AD37:
    result = ZwClose(0, a2, 0, 0);
    goto loc_00A0A437;
loc_00A0AD44:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, 0, 0);
    goto loc_00A0A44E;
loc_00A0AD53:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, 0, 0);
    goto loc_00A0A45B;
loc_00A0AD62:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, 0, 0);
    goto loc_00A0A472;
loc_00A0AD71:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, 0, 0);
    goto loc_00A0A47F;
}
```

## 5. (Beta) C Style

```c
int64_t _CmUpdateDevicePanel(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rsp;
    uint32_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m48;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA4;
    uint32_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint32_t v_stack_mBC;
    uint32_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint32_t v_stack_mC8;
    uint32_t v_stack_mCC;
    uint32_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint8_t v_stack_mEC;
    uint32_t v_stack_mF0;
    uint8_t v_stack_mF2;
    uint8_t v_stack_mF3;
    uint8_t v_stack_mF4;
    uint32_t v_stack_mF8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint32_t v_stack_p48;
    uint64_t v_stack_p60;
    uint8_t v_stack_p64;
    uint8_t v_stack_p66;
    uint32_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (288);
    result = (*(uint64_t *)(v_rip + 0x4005B1)) ^ (local_rsp);
    v_stack_m48 = result;
    local_r12 = 0;
    result = 0;
    v_stack_mB0 = 0;
    v_stack_mCC = 0;
    v_stack_m98 = 0;
    v_stack_mC4 = 0;
    v_stack_mD8 = 0;
    v_stack_mD0 = (uint32_t)(result + 1);
    v_stack_mB8 = 0;
    v_stack_mE8 = 0;
    v_stack_m88 = v_xmm0;
    v_stack_mF2 = 0;
    v_stack_mC0 = 0;
    v_stack_mBC = 0;
    v_stack_mE0 = 0;
    v_stack_mA0 = 0;
    v_stack_mF4 = 0;
    v_stack_m78 = v_xmm0;
    v_stack_m68 = 0;
    v_stack_m60 = v_xmm1;
    v_stack_m50 = 0;
    v_stack_m90 = 0;
    v_stack_mF3 = 0;
    v_stack_mF8 = 0;
    v_stack_mA8 = 0;
    v_stack_mA4 = 0;
    v_stack_mEC = 0;
    v_stack_mF0 = 0;
    result = CmIsRootDevice(Arg2, Arg2, Arg3, a4);
    if ((uint8_t)(result) != 0) goto loc_00A0A80F;
    v_stack_m118 = v_stack_mC4;
    v_stack_m120 = v_stack_m98;
    v_stack_m128 = v_stack_mCC;
    v_stack_m130 = v_stack_mB0;
    v_stack_m138 = v_rip - 10441915;
    result = CmQueryDevicePanelPldProperty(*(uint64_t *)(v_rip + 0x45C1FB), Arg2, (uint32_t)((uint32_t)(result + 1)), Arg3);
    if (((uint32_t)(result)) != 0xC0000225ULL) goto loc_00A0A4A9;
loc_00A0A282:
    result = ExAllocatePool2(256, 114, (uint32_t)(0x52504E50ULL), Arg3);
    Arg2 = 0;
    v_stack_mE0 = result;
    if (result == 0) goto loc_00A0AB45;
    v_stack_m108 = 0;
    v_stack_m110 = v_stack_mF0;
    v_stack_m118 = 114;
    v_stack_m120 = result;
    v_stack_m128 = v_stack_mD0;
    v_stack_m130 = v_rip - 10456378;
    v_stack_m138 = 0;
    result = PnpGetObjectProperty(*(uint64_t *)(v_rip + 0x45C1FB), 0, 114 - 113, Arg3);
    if (((uint32_t)(result)) != 0xC0000225ULL) goto loc_00A0AB4F;
    Arg2 = 0;
loc_00A0A2FB:
    result = ExFreePoolWithTag(v_stack_mE0, Arg2, 114 - 113, Arg3);
    Arg2 = 0;
    v_stack_mE0 = 0;
loc_00A0A30E:
    if (0 != 0) goto loc_00A0AB78;
    if (0 != 0) goto loc_00A0AB9D;
loc_00A0A320:
    if (0 != 0) goto loc_00A0A624;
loc_00A0A337:
    if (0 != 0) goto loc_00A0A576;
loc_00A0A358:
    if (0 != 0) goto loc_00A0AC10;
loc_00A0A361:
    if (0 != 0) goto loc_00A0A6D9;
loc_00A0A36A:
    if (0 != 0) goto loc_00A0AC60;
loc_00A0A373:
    if (0 != 0) goto loc_00A0AC9D;
loc_00A0A385:
    if (0 != 0) goto loc_00A0ACDA;
loc_00A0A38E:
    v_stack_m68 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x9F55AB)));
    v_stack_m78 = v_xmm0;
    v_stack_m50 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x9F55D3)));
    v_stack_mC8 = (uint32_t)((uint32_t)(v_stack_mCC));
    v_stack_m60 = v_xmm0;
    v_stack_mB0 = 0;
    v_stack_mC4 = 0;
    v_stack_mCC = 0;
loc_00A0A3CD:
    v_stack_m108 = 0;
    v_stack_m110 = v_stack_mCC;
    v_stack_m118 = (uint32_t)((uint32_t)(v_stack_mCC));
    v_stack_m120 = v_stack_mB0;
    v_stack_m128 = v_stack_mC4;
    v_stack_m130 = v_stack_m78;
    v_stack_m138 = 0;
    result = PnpGetObjectProperty(*(uint64_t *)(v_rip + 0x45C1FB), 0, 1, Arg3);
    if (((uint32_t)(result)) == 0xC0000023ULL) goto loc_00A0A7CF;
    Arg2 = 0;
    if (!sign_flag) goto loc_00A0A755;
    local_rbx = (uint32_t)((uint32_t)(result));
    if (((uint32_t)(result)) == 0xC0000225ULL) {
        local_rbx = 0;
    }
    if (0 != 0) goto loc_00A0AD37;
loc_00A0A437:
    if (0 != 0) goto loc_00A0A606;
loc_00A0A440:
    if (v_stack_mE0 != 0) goto loc_00A0AD44;
loc_00A0A44E:
    if (v_stack_mA0 != 0) goto loc_00A0AD53;
loc_00A0A45B:
    if (v_stack_mB0 != 0) goto loc_00A0A615;
loc_00A0A464:
    if (v_stack_mE8 != 0) goto loc_00A0AD62;
loc_00A0A472:
    if (v_stack_mD8 != 0) goto loc_00A0AD71;
loc_00A0A47F:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, 1, Arg3);
    local_rsp = (local_rsp) + (288);
    return result;
loc_00A0A4A9:
    if (sign_flag) goto loc_00A0AB06;
    if (v_stack_m98 == 0) goto loc_00A0A282;
    result = CmGetParentDeviceContainerId(*(uint64_t *)(v_rip + 0x45C1FB), 0, v_stack_m88, Arg3);
    Arg3 = 0;
    if (sign_flag) goto loc_00A0AB06;
    v_stack_p66 = 1;
    result = _CmGetDevicePanelGroup(v_stack_m98, 0, Arg3, Arg3);
    v_stack_mC0 = (uint32_t)(result);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m98 + 0x8))) >> (3));
    result = (uint32_t)((result) & (7));
    if (((uint32_t)(result)) < 7) goto loc_00A0AAEE;
loc_00A0A501:
    v_stack_mBC = 0;
    result = ExAllocatePool2(256, 114, (uint32_t)(0x52504E50ULL), Arg3);
    if (result == 0) goto loc_00A0AB01;
    result = CmBuildDevicePanelId(v_stack_m88, (uint32_t)(v_stack_mC0), (uint32_t)(v_stack_mBC), result);
    if (sign_flag) goto loc_00A0A602;
    v_stack_mC8 = 16;
    result = ExAllocatePool2(256, 16, (uint32_t)(0x52504E50ULL), result);
    Arg2 = 0;
    v_stack_p70 = result;
    goto loc_00A0A602;
loc_00A0A576:
    if (v_stack_m98 == 0) goto loc_00A0A358;
    if (sign_flag) goto loc_00A0AC09;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m98))))) >> (16));
    result = (uint32_t)((*(uint8_t *)(v_stack_m98 + 0x3)) << (8));
    Arg1 = (uint32_t)(((uint8_t)(result)) | ((uint32_t)(result)));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m98))) >> (8));
    Arg1 = (uint32_t)((Arg1) << (8));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)((uint8_t)(Arg2))));
    Arg1 = (uint32_t)((Arg1) | (0xFF000000ULL));
    v_stack_p60 = (uint32_t)(Arg1);
    Arg1 = 0;
    v_stack_p48 = 0;
    v_stack_p40 = 4;
    v_stack_p38 = v_stack_p60;
    v_stack_p30 = 7;
    v_stack_p28 = v_rip - 10442720;
    v_stack_p20 = 0;
    result = PnpSetObjectProperty(*(uint64_t *)(v_rip + 0x45C1FB), Arg2, Arg1 + 1, 0);
    Arg2 = 0;
    if (!sign_flag) goto loc_00A0A6D4;
loc_00A0A602:
loc_00A0A606:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, Arg1 + 1, 0);
    goto loc_00A0A440;
loc_00A0A615:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_mB0, Arg2, Arg1 + 1, 0);
    goto loc_00A0A464;
loc_00A0A624:
    v_stack_p48 = 0;
    v_stack_p40 = 0;
    v_stack_p38 = 0;
    v_stack_p30 = 0;
    v_stack_p28 = v_rip - 10442663;
    v_stack_p20 = 0;
    result = PnpSetObjectProperty(*(uint64_t *)(v_rip + 0x45C1FB), 0, 1, 0);
    Arg1 = 0;
    v_stack_p48 = 0;
    v_stack_p40 = 0;
    v_stack_p38 = 0;
    v_stack_p30 = 0;
    v_stack_p28 = v_rip - 10442691;
    v_stack_p20 = 0;
    result = PnpSetObjectProperty(*(uint64_t *)(v_rip + 0x45C1FB), 0, Arg1 + 1, 0);
    Arg1 = 0;
    v_stack_p48 = 0;
    v_stack_p40 = 0;
    v_stack_p38 = 0;
    v_stack_p30 = 0;
    v_stack_p28 = v_rip - 10442721;
    v_stack_p20 = 0;
    result = PnpSetObjectProperty(*(uint64_t *)(v_rip + 0x45C1FB), 0, 1, 0);
    Arg2 = 0;
    goto loc_00A0A337;
loc_00A0A6D4:
loc_00A0A6D9:
    if (v_stack_mB0 == 0) goto loc_00A0A36A;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mB0 + 0x8))) >> (10));
    result = (uint32_t)((result) & (15));
    if (((uint32_t)(result)) < 9) goto loc_00A0AC4D;
loc_00A0A6F8:
    v_stack_p48 = 0;
    v_stack_p40 = 4;
    v_stack_p38 = v_stack_p60;
    v_stack_p30 = 7;
    v_stack_p28 = v_rip - 10442830;
    v_stack_p20 = 0;
    v_stack_p60 = 0;
    result = PnpSetObjectProperty(*(uint64_t *)(v_rip + 0x45C1FB), 0, 1, 0);
    Arg2 = 0;
    if (sign_flag) goto loc_00A0A602;
loc_00A0A755:
    if (v_stack_mC4 != 0x1003ULL) goto loc_00A0AD23;
    if (((uint32_t)((uint32_t)(v_stack_mCC))) < 1) goto loc_00A0AD23;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mB0))) & (127));
    if (((uint32_t)(result)) < 1) goto loc_00A0A42C;
    if (((uint32_t)(result)) == 1) goto loc_00A0AD15;
loc_00A0A784:
    if (((uint32_t)(result)) < 2) goto loc_00A0A792;
    if (((uint32_t)((uint32_t)(v_stack_mCC))) < 20) goto loc_00A0A42C;
loc_00A0A792:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mB0 + 0x8))) & (56));
    if (((uint8_t)(result)) >= 48) goto loc_00A0A42C;
    result = CmGetParentDeviceContainerId(*(uint64_t *)(v_rip + 0x45C1FB), 0, v_stack_m88, 0);
    if (sign_flag) goto loc_00A0A42E;
    v_stack_p66 = 1;
loc_00A0A7CF:
    if (((uint32_t)((uint32_t)(v_stack_mCC))) <= v_stack_mC8) goto loc_00A0AD23;
    if (v_stack_mB0 != 0) goto loc_00A0AD03;
loc_00A0A7E4:
    v_stack_mC8 = (uint32_t)((uint32_t)(v_stack_mCC));
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(v_stack_mCC))), (uint32_t)(0x52504E50ULL), 0);
    Arg2 = 0;
    if (result == 0) goto loc_00A0AD2D;
    goto loc_00A0A3CD;
loc_00A0A80F:
    goto loc_00A0A47F;
loc_00A0AAEE:
    goto loc_00A0A501;
loc_00A0AB01:
loc_00A0AB06:
    goto loc_00A0A45B;
loc_00A0AB45:
loc_00A0AB4F:
    Arg2 = 0;
    if (v_stack_mD0 != 18) goto loc_00A0A2FB;
    if (v_stack_p68 < 2) goto loc_00A0A2FB;
    goto loc_00A0A30E;
loc_00A0AB78:
    result = wcsicmp(v_stack_p78, result, (uint32_t)(0x52504E50ULL), 0);
    Arg2 = 0;
loc_00A0AB9D:
    v_stack_p64 = 1;
loc_00A0AC09:
    Arg2 = 0;
    goto loc_00A0A358;
loc_00A0AC10:
    v_stack_p48 = 0;
    v_stack_p40 = 0;
    v_stack_p38 = 0;
    v_stack_p30 = 0;
    v_stack_p28 = v_rip - 10444323;
    v_stack_p20 = 0;
    result = PnpSetObjectProperty(*(uint64_t *)(v_rip + 0x45C1FB), 0, 1, 0);
    Arg2 = 0;
    goto loc_00A0A361;
loc_00A0AC4D:
    goto loc_00A0A6F8;
loc_00A0AC60:
    v_stack_p48 = 0;
    v_stack_p40 = 0;
    v_stack_p38 = 0;
    v_stack_p30 = 0;
    v_stack_p28 = v_rip - 10444187;
    v_stack_p20 = 0;
    result = PnpSetObjectProperty(*(uint64_t *)(v_rip + 0x45C1FB), 0, 1, 0);
    Arg2 = 0;
    goto loc_00A0A373;
loc_00A0AC9D:
    v_stack_p48 = 0;
    v_stack_p40 = 0;
    v_stack_p38 = 0;
    v_stack_p30 = 0;
    v_stack_p28 = v_rip - 10391592;
    v_stack_p20 = 0;
    result = PnpSetObjectProperty(*(uint64_t *)(v_rip + 0x45C1FB), 0, 1, 0);
    Arg2 = 0;
    goto loc_00A0A385;
loc_00A0ACDA:
    if (v_stack_p64 == 0) goto loc_00A0A38E;
    result = CmAddPanelDevice(*(uint64_t *)(v_rip + 0x45C1FB), result, 0, 0);
    Arg2 = 0;
    if (sign_flag) goto loc_00A0A602;
    goto loc_00A0A38E;
loc_00A0AD03:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_mB0, Arg2, 0, 0);
    goto loc_00A0A7E4;
loc_00A0AD15:
    if (((uint32_t)(v_stack_mB0)) < 16) goto loc_00A0A42C;
    goto loc_00A0A784;
loc_00A0AD23:
    goto loc_00A0A42E;
loc_00A0AD2D:
    goto loc_00A0A42E;
loc_00A0AD37:
    result = ZwClose(0, Arg2, 0, 0);
    goto loc_00A0A437;
loc_00A0AD44:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, 0, 0);
    goto loc_00A0A44E;
loc_00A0AD53:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, 0, 0);
    goto loc_00A0A45B;
loc_00A0AD62:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, 0, 0);
    goto loc_00A0A472;
loc_00A0AD71:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, 0, 0);
    goto loc_00A0A47F;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A0A16C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
