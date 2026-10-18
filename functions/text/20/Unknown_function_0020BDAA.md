# sub_0020BDAA

- RVA: `0x0020BDAA`–`0x0020C20E` (길이 `1,124` bytes)
- VA: `0x000000014020BDAA`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D884`
- 디코드: `249`개 명령, `1,124/1,124` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x0020BF08` → [KiPerformWaitDeferredWork](../22/KiPerformWaitDeferredWork_function_00220480.md) (function, `0x00220480`)
- `0x0020BF2D` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0020BFAB` → [KiActivateWaiterQueueWithNoLocks](KiActivateWaiterQueueWithNoLocks_function_0020CEB0.md) (function, `0x0020CEB0`)
- `0x0020BFBF` → [KiAcquireKobjectLockSafe](../25/KiAcquireKobjectLockSafe_function_00251C90.md) (function, `0x00251C90`)
- `0x0020C055` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0020C14E` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0020C16C` → [EtwTraceDequeueWork](../4B/EtwTraceDequeueWork_function_004BDBFC.md) (function, `0x004BDBFC`)
- `0x0020C1F0` → [KiRcuReportQuiescentState](KiRcuReportQuiescentState_function_0020AB8C.md) (function, `0x0020AB8C`)
- `0x0020C204` → [KiRcuFlushCompleted](KiRcuFlushCompleted_function_0020AD38.md) (function, `0x0020AD38`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0020BE9B` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0020BF1D` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0020C044` → RVA `0x00EFAAB8` (`.data`; read)
- `0x0020C157` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x0020C1D1` → RVA `0x00F110C0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **22**
  - `0x0020BDC0` → [sub_0020C2D4 + 0x8A1](Unknown_function_0020C2D4.md) (`tail-transfer`)
  - `0x0020BDCD` → [sub_0020C2D4 + 0xA3E](Unknown_function_0020C2D4.md) (`tail-transfer`)
  - `0x0020BEA1` → [sub_0020C2D4 + 0x43](Unknown_function_0020C2D4.md) (`tail-transfer`)
  - `0x0020BEBB` → [sub_0020C2D4 + 0xED](Unknown_function_0020C2D4.md) (`tail-transfer`)
  - `0x0020BF17` → [sub_0020C2D4 + 0x885](Unknown_function_0020C2D4.md) (`tail-transfer`)
  - `0x0020BF39` → [sub_0020C2D4 + 0x865](Unknown_function_0020C2D4.md) (`tail-transfer`)
  - `0x0020BF4B` → [sub_0020C2D4 + 0x919](Unknown_function_0020C2D4.md) (`tail-transfer`)
  - `0x0020BF93` → [sub_0020C2D4 + 0x225](Unknown_function_0020C2D4.md) (`tail-transfer`)
  - `0x0020BFCF` → [sub_0020C2D4 + 0x20C](Unknown_function_0020C2D4.md) (`tail-transfer`)
  - `0x0020BFF3` → [sub_0020C2D4 + 0x1C](Unknown_function_0020C2D4.md) (`tail-transfer`)
  - `0x0020BFFE` → [sub_0020C2D4 + 0xE0](Unknown_function_0020C2D4.md) (`tail-transfer`)
  - `0x0020C00C` → [sub_0020C2D4 + 0xE0](Unknown_function_0020C2D4.md) (`tail-transfer`)
  - `0x0020C037` → [sub_0020C222](Unknown_function_0020C222.md) (`tail-transfer`)
  - `0x0020C094` → [sub_0020C2D4](Unknown_function_0020C2D4.md) (`tail-transfer`)
  - `0x0020C09D` → [sub_0020C2D4 + 0x1E2](Unknown_function_0020C2D4.md) (`tail-transfer`)
  - `0x0020C0B7` → [sub_0020C2D4 + 0x1BB](Unknown_function_0020C2D4.md) (`tail-transfer`)
  - `0x0020C0D3` → [sub_0020C2D4 + 0x72D](Unknown_function_0020C2D4.md) (`tail-transfer`)
  - `0x0020C0E8` → [sub_0020C2D4 + 0x6A](Unknown_function_0020C2D4.md) (`tail-transfer`)
  - `0x0020C0F5` → [sub_0020C2D4 + 0xA30](Unknown_function_0020C2D4.md) (`tail-transfer`)
  - `0x0020C128` → [sub_0020C2D4 + 0x156](Unknown_function_0020C2D4.md) (`tail-transfer`)
  - `0x0020C131` → [sub_0020C2D4 + 0x8F9](Unknown_function_0020C2D4.md) (`tail-transfer`)
  - `0x0020C19A` → [sub_0020C2D4 + 0x4BF](Unknown_function_0020C2D4.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0020BDAA  4C 89 A4 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], r12
0020BDB2  80 7E 20 01                     cmp byte ptr [rsi + 0x20], 1
0020BDB6  77 2F                           ja 0x14020bde7
0020BDB8  48 83 BE F8 38 00 00 00         cmp qword ptr [rsi + 0x38f8], 0
0020BDC0  0F 85 AF 0D 00 00               jne 0x14020cb75
0020BDC6  80 BE E5 38 00 00 00            cmp byte ptr [rsi + 0x38e5], 0
0020BDCD  0F 85 3F 0F 00 00               jne 0x14020cd12
0020BDD3  48 8B 96 E8 38 00 00            mov rdx, qword ptr [rsi + 0x38e8]
0020BDDA  48 3B 96 F0 38 00 00            cmp rdx, qword ptr [rsi + 0x38f0]
0020BDE1  0F 85 E7 03 00 00               jne 0x14020c1ce
0020BDE7  48 B8 B0 03 00 00 80 F7 FF FF   movabs rax, 0xfffff780000003b0
0020BDF1  48 B9 08 00 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000008
0020BDFB  41 BC 01 00 00 00               mov r12d, 1
0020BE01  4D 85 FF                        test r15, r15
0020BE04  74 1D                           je 0x14020be23
0020BE06  41 83 7F 04 00                  cmp dword ptr [r15 + 4], 0
0020BE0B  0F 8C 4A 02 00 00               jl 0x14020c05b
0020BE11  49 8B 07                        mov rax, qword ptr [r15]
0020BE14  45 33 C9                        xor r9d, r9d
0020BE17  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0020BE1C  44 89 64 24 30                  mov dword ptr [rsp + 0x30], r12d
0020BE21  EB 08                           jmp 0x14020be2b
0020BE23  45 33 C9                        xor r9d, r9d
0020BE26  44 89 4C 24 30                  mov dword ptr [rsp + 0x30], r9d
0020BE2B  48 8B 87 E8 00 00 00            mov rax, qword ptr [rdi + 0xe8]
0020BE32  49 3B C6                        cmp rax, r14
0020BE35  75 14                           jne 0x14020be4b
0020BE37  41 83 7E 04 00                  cmp dword ptr [r14 + 4], 0
0020BE3C  0F 85 9A 01 00 00               jne 0x14020bfdc
0020BE42  4D 85 FF                        test r15, r15
0020BE45  0F 85 3B 02 00 00               jne 0x14020c086
0020BE4B  0F B6 AF 86 01 00 00            movzx ebp, byte ptr [rdi + 0x186]
0020BE52  41 BE 02 00 00 00               mov r14d, 2
0020BE58  44 0F B6 AC 24 A8 00 00 00      movzx r13d, byte ptr [rsp + 0xa8]
0020BE61  44 0F B6 BC 24 B0 00 00 00      movzx r15d, byte ptr [rsp + 0xb0]
0020BE6A  4C 89 4C 24 50                  mov qword ptr [rsp + 0x50], r9
0020BE6F  83 67 74 EF                     and dword ptr [rdi + 0x74], 0xffffffef
0020BE73  C6 47 70 00                     mov byte ptr [rdi + 0x70], 0
0020BE77  44 88 AF 87 01 00 00            mov byte ptr [rdi + 0x187], r13b
0020BE7E  45 84 FF                        test r15b, r15b
0020BE81  74 04                           je 0x14020be87
0020BE83  83 4F 74 10                     or dword ptr [rdi + 0x74], 0x10
0020BE87  41 8B F1                        mov esi, r9d
0020BE8A  66 0F 1F 44 00 00               nop word ptr [rax + rax]
0020BE90  F0 48 0F BA 6F 40 00            lock bts qword ptr [rdi + 0x40], 0
0020BE97  73 1B                           jae 0x14020beb4
0020BE99  FF C6                           inc esi
0020BE9B  85 35 0B 94 DB 00               test dword ptr [rip + 0xdb940b], esi
0020BEA1  0F 84 70 04 00 00               je 0x14020c317
0020BEA7  F3 90                           pause
0020BEA9  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
0020BEAD  48 85 C0                        test rax, rax
0020BEB0  74 DE                           je 0x14020be90
0020BEB2  EB E5                           jmp 0x14020be99
0020BEB4  80 BF C1 00 00 00 00            cmp byte ptr [rdi + 0xc1], 0
0020BEBB  0F 85 00 05 00 00               jne 0x14020c3c1
0020BEC1  4C 8B B4 24 A0 00 00 00         mov r14, qword ptr [rsp + 0xa0]
0020BEC9  44 8B AC 24 C8 00 00 00         mov r13d, dword ptr [rsp + 0xc8]
0020BED1  45 84 FF                        test r15b, r15b
0020BED4  0F 85 B2 02 00 00               jne 0x14020c18c
0020BEDA  45 33 C9                        xor r9d, r9d
0020BEDD  F6 87 C2 00 00 00 02            test byte ptr [rdi + 0xc2], 2
0020BEE4  74 75                           je 0x14020bf5b
0020BEE6  44 38 8C 24 A8 00 00 00         cmp byte ptr [rsp + 0xa8], r9b
0020BEEE  74 6B                           je 0x14020bf5b
0020BEF0  BE C0 00 00 00                  mov esi, 0xc0
0020BEF5  4C 89 4C 24 50                  mov qword ptr [rsp + 0x50], r9
0020BEFA  45 0F B6 C4                     movzx r8d, r12b
0020BEFE  4C 8D 4C 24 50                  lea r9, [rsp + 0x50]
0020BF03  8B D3                           mov edx, ebx
0020BF05  48 8B CF                        mov rcx, rdi
0020BF08  E8 73 45 01 00                  call 0x140220480
0020BF0D  48 C7 47 40 00 00 00 00         mov qword ptr [rdi + 0x40], 0
0020BF15  85 C0                           test eax, eax
0020BF17  0F 85 3C 0C 00 00               jne 0x14020cb59
0020BF1D  39 05 FD AD DB 00               cmp dword ptr [rip + 0xdbadfd], eax
0020BF23  74 0D                           je 0x14020bf32
0020BF25  44 0F 20 C1                     mov rcx, cr8
0020BF29  40 0F B6 D5                     movzx edx, bpl
0020BF2D  E8 66 97 2E 00                  call 0x1404f5698
0020BF32  44 0F 22 C5                     mov cr8, rbp
0020BF36  48 85 F6                        test rsi, rsi
0020BF39  0F 85 FA 0B 00 00               jne 0x14020cb39
0020BF3F  45 33 C9                        xor r9d, r9d
0020BF42  EB 45                           jmp 0x14020bf89
0020BF44  45 33 C9                        xor r9d, r9d
0020BF47  44 38 4F 72                     cmp byte ptr [rdi + 0x72], r9b
0020BF4B  0F 85 9C 0C 00 00               jne 0x14020cbed
0020BF51  41 8B C1                        mov eax, r9d
0020BF54  41 8B F1                        mov esi, r9d
0020BF57  85 C0                           test eax, eax
0020BF59  75 9A                           jne 0x14020bef5
0020BF5B  C6 87 84 01 00 00 05            mov byte ptr [rdi + 0x184], 5
0020BF62  49 BD 20 03 00 00 80 F7 FF FF   movabs r13, 0xfffff78000000320
0020BF6C  C6 87 83 02 00 00 0F            mov byte ptr [rdi + 0x283], 0xf
0020BF73  41 8B 45 00                     mov eax, dword ptr [r13]
0020BF77  44 8B AC 24 C8 00 00 00         mov r13d, dword ptr [rsp + 0xc8]
0020BF7F  89 87 B4 01 00 00               mov dword ptr [rdi + 0x1b4], eax
0020BF85  4C 89 4F 40                     mov qword ptr [rdi + 0x40], r9
0020BF89  48 8B 97 E8 00 00 00            mov rdx, qword ptr [rdi + 0xe8]
0020BF90  4C 3B F2                        cmp r14, rdx
0020BF93  0F 84 60 05 00 00               je 0x14020c4f9
0020BF99  48 8D B7 08 02 00 00            lea rsi, [rdi + 0x208]
0020BFA0  48 85 D2                        test rdx, rdx
0020BFA3  74 0B                           je 0x14020bfb0
0020BFA5  4C 8B C6                        mov r8, rsi
0020BFA8  48 8B CF                        mov rcx, rdi
0020BFAB  E8 00 0F 00 00                  call 0x14020ceb0
0020BFB0  4C 89 B7 E8 00 00 00            mov qword ptr [rdi + 0xe8], r14
0020BFB7  F0 41 FF 46 28                  lock inc dword ptr [r14 + 0x28]
0020BFBC  49 8B CE                        mov rcx, r14
0020BFBF  E8 CC 5C 04 00                  call 0x140251c90
0020BFC4  49 8B 4E 38                     mov rcx, qword ptr [r14 + 0x38]
0020BFC8  49 8D 46 30                     lea rax, [r14 + 0x30]
0020BFCC  48 39 01                        cmp qword ptr [rcx], rax
0020BFCF  0F 84 0B 05 00 00               je 0x14020c4e0
0020BFD5  B9 03 00 00 00                  mov ecx, 3
0020BFDA  CD 29                           int 0x29
0020BFDC  41 8B 46 28                     mov eax, dword ptr [r14 + 0x28]
0020BFE0  41 3B 46 2C                     cmp eax, dword ptr [r14 + 0x2c]
0020BFE4  0F 87 58 FE FF FF               ja 0x14020be42
0020BFEA  F0 41 0F BA 2E 07               lock bts dword ptr [r14], 7
0020BFF0  41 8B F1                        mov esi, r9d
0020BFF3  0F 82 F7 02 00 00               jb 0x14020c2f0
0020BFF9  41 83 7E 04 00                  cmp dword ptr [r14 + 4], 0
0020BFFE  0F 84 B0 03 00 00               je 0x14020c3b4
0020C004  41 8B 46 28                     mov eax, dword ptr [r14 + 0x28]
0020C008  41 3B 46 2C                     cmp eax, dword ptr [r14 + 0x2c]
0020C00C  0F 87 A2 03 00 00               ja 0x14020c3b4
0020C012  49 8B 56 18                     mov rdx, qword ptr [r14 + 0x18]
0020C016  49 8D 4E 18                     lea rcx, [r14 + 0x18]
0020C01A  44 8B AC 24 C8 00 00 00         mov r13d, dword ptr [rsp + 0xc8]
0020C022  41 8B F1                        mov esi, r9d
0020C025  4C 8B BC 24 C0 00 00 00         mov r15, qword ptr [rsp + 0xc0]
0020C02D  41 FF 4E 04                     dec dword ptr [r14 + 4]
0020C031  48 8B 02                        mov rax, qword ptr [rdx]
0020C034  48 85 C0                        test rax, rax
0020C037  0F 85 E5 01 00 00               jne 0x14020c222
0020C03D  48 8B 42 10                     mov rax, qword ptr [rdx + 0x10]
0020C041  4D 8B C6                        mov r8, r14
0020C044  4C 8B 0D 6D EA CE 00            mov r9, qword ptr [rip + 0xceea6d]
0020C04B  B9 96 00 00 00                  mov ecx, 0x96
0020C050  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0020C055  E8 06 16 2F 00                  call 0x1404fd660
0020C05A  CC                              int3
0020C05B  48 8B 00                        mov rax, qword ptr [rax]
0020C05E  48 8B 09                        mov rcx, qword ptr [rcx]
0020C061  48 2B C8                        sub rcx, rax
0020C064  C7 44 24 30 02 00 00 00         mov dword ptr [rsp + 0x30], 2
0020C06C  48 8B 87 F8 00 00 00            mov rax, qword ptr [rdi + 0xf8]
0020C073  49 03 07                        add rax, qword ptr [r15]
0020C076  48 2B C8                        sub rcx, rax
0020C079  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
0020C07E  45 33 C9                        xor r9d, r9d
0020C081  E9 A5 FD FF FF                  jmp 0x14020be2b
0020C086  49 83 3F 00                     cmp qword ptr [r15], 0
0020C08A  0F 85 BB FD FF FF               jne 0x14020be4b
0020C090  45 84 66 01                     test byte ptr [r14 + 1], r12b
0020C094  0F 85 3A 02 00 00               jne 0x14020c2d4
0020C09A  45 84 ED                        test r13b, r13b
0020C09D  0F 84 13 04 00 00               je 0x14020c4b6
0020C0A3  41 8B F1                        mov esi, r9d
0020C0A6  F0 48 0F BA 6F 40 00            lock bts qword ptr [rdi + 0x40], 0
0020C0AD  73 1B                           jae 0x14020c0ca
0020C0AF  FF C6                           inc esi
0020C0B1  85 35 F5 91 DB 00               test dword ptr [rip + 0xdb91f5], esi
0020C0B7  0F 84 D2 03 00 00               je 0x14020c48f
0020C0BD  F3 90                           pause
0020C0BF  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
0020C0C3  48 85 C0                        test rax, rax
0020C0C6  74 DE                           je 0x14020c0a6
0020C0C8  EB E5                           jmp 0x14020c0af
0020C0CA  48 0F BE C5                     movsx rax, bpl
0020C0CE  80 7C 38 72 00                  cmp byte ptr [rax + rdi + 0x72], 0
0020C0D3  0F 85 28 09 00 00               jne 0x14020ca01
0020C0D9  40 84 ED                        test bpl, bpl
0020C0DC  74 10                           je 0x14020c0ee
0020C0DE  48 8D 87 A8 00 00 00            lea rax, [rdi + 0xa8]
0020C0E5  48 39 00                        cmp qword ptr [rax], rax
0020C0E8  0F 85 50 02 00 00               jne 0x14020c33e
0020C0EE  45 33 C9                        xor r9d, r9d
0020C0F1  44 38 4F 72                     cmp byte ptr [rdi + 0x72], r9b
0020C0F5  0F 85 09 0C 00 00               jne 0x14020cd04
0020C0FB  41 8B C1                        mov eax, r9d
0020C0FE  48 85 C0                        test rax, rax
0020C101  75 0E                           jne 0x14020c111
0020C103  48 C7 44 24 58 02 01 00 00      mov qword ptr [rsp + 0x58], 0x102
0020C10C  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0020C111  4C 8B BC 24 C0 00 00 00         mov r15, qword ptr [rsp + 0xc0]
0020C119  49 89 07                        mov qword ptr [r15], rax
0020C11C  45 84 ED                        test r13b, r13b
0020C11F  74 04                           je 0x14020c125
0020C121  4C 89 4F 40                     mov qword ptr [rdi + 0x40], r9
0020C125  83 FB 02                        cmp ebx, 2
0020C128  0F 83 FC 02 00 00               jae 0x14020c42a
0020C12E  41 84 DC                        test r12b, bl
0020C131  0F 85 96 0A 00 00               jne 0x14020cbcd
0020C137  83 3D E2 AB DB 00 00            cmp dword ptr [rip + 0xdbabe2], 0
0020C13E  0F B6 9F 86 01 00 00            movzx ebx, byte ptr [rdi + 0x186]
0020C145  74 0C                           je 0x14020c153
0020C147  44 0F 20 C1                     mov rcx, cr8
0020C14B  0F B6 D3                        movzx edx, bl
0020C14E  E8 45 95 2E 00                  call 0x1404f5698
0020C153  44 0F 22 C3                     mov cr8, rbx
0020C157  F7 05 A3 A9 DB 00 00 00 00 01   test dword ptr [rip + 0xdba9a3], 0x1000000
0020C161  74 0E                           je 0x14020c171
0020C163  45 8B C4                        mov r8d, r12d
0020C166  49 8B D7                        mov rdx, r15
0020C169  48 8B CF                        mov rcx, rdi
0020C16C  E8 8B 1A 2B 00                  call 0x1404bdbfc
0020C171  41 8B C4                        mov eax, r12d
0020C174  4C 8B A4 24 B8 00 00 00         mov r12, qword ptr [rsp + 0xb8]
0020C17C  48 83 C4 60                     add rsp, 0x60
0020C180  41 5F                           pop r15
0020C182  41 5E                           pop r14
0020C184  41 5D                           pop r13
0020C186  5F                              pop rdi
0020C187  5E                              pop rsi
0020C188  5D                              pop rbp
0020C189  5B                              pop rbx
0020C18A  C3                              ret
0020C18B  CC                              int3
0020C18C  48 0F BE 8C 24 A8 00 00 00      movsx rcx, byte ptr [rsp + 0xa8]
0020C195  80 7C 39 72 00                  cmp byte ptr [rcx + rdi + 0x72], 0
0020C19A  0F 85 F3 05 00 00               jne 0x14020c793
0020C1A0  84 C9                           test cl, cl
0020C1A2  0F 84 9C FD FF FF               je 0x14020bf44
0020C1A8  48 8D 87 A8 00 00 00            lea rax, [rdi + 0xa8]
0020C1AF  48 39 00                        cmp qword ptr [rax], rax
0020C1B2  0F 84 8C FD FF FF               je 0x14020bf44
0020C1B8  80 8F C2 00 00 00 02            or byte ptr [rdi + 0xc2], 2
0020C1BF  B8 C0 00 00 00                  mov eax, 0xc0
0020C1C4  8B F0                           mov esi, eax
0020C1C6  45 33 C9                        xor r9d, r9d
0020C1C9  E9 89 FD FF FF                  jmp 0x14020bf57
0020C1CE  8B 4E 24                        mov ecx, dword ptr [rsi + 0x24]
0020C1D1  48 8D 05 E8 4E D0 00            lea rax, [rip + 0xd04ee8]
0020C1D8  48 C1 E1 05                     shl rcx, 5
0020C1DC  48 03 C8                        add rcx, rax
0020C1DF  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0020C1E3  4C 8B 01                        mov r8, qword ptr [rcx]
0020C1E6  4C 85 40 38                     test qword ptr [rax + 0x38], r8
0020C1EA  0F 85 F7 FB FF FF               jne 0x14020bde7
0020C1F0  E8 97 E9 FF FF                  call 0x14020ab8c
0020C1F5  85 C0                           test eax, eax
0020C1F7  0F 84 EA FB FF FF               je 0x14020bde7
0020C1FD  0F B6 8E E6 38 00 00            movzx ecx, byte ptr [rsi + 0x38e6]
0020C204  E8 2F EB FF FF                  call 0x14020ad38
0020C209  E9 D9 FB FF FF                  jmp 0x14020bde7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0020BDAA(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, unsigned __int8 a21, unsigned __int8 a22, __int64 a23, __int64 a24, unsigned int a25)
{
    __int64 result;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_pB8;

    v_stack_pB8 = v_r12;
    if ((*(unsigned __int8 *)(v_rsi + 32)) > 1) goto loc_0020BDE7;
    if ((*(unsigned __int64 *)(v_rsi + 14568)) != (*(unsigned __int64 *)(v_rsi + 14576))) goto loc_0020C1CE;
loc_0020BDE7:
    if (v_r15 == 0) goto loc_0020BE23;
    if ((*(unsigned int *)(v_r15 + 4)) < 0) goto loc_0020C05B;
    a4 = 0;
    v_stack_p58 = *(unsigned __int64 *)(v_r15);
    v_stack_p30 = 1;
    goto loc_0020BE2B;
loc_0020BE23:
    a4 = 0;
    v_stack_p30 = 0;
loc_0020BE2B:
    if ((*(unsigned __int64 *)(v_rdi + 232)) != v_r14) goto loc_0020BE4B;
    if ((*(unsigned int *)(v_r14 + 4)) != 0) goto loc_0020BFDC;
loc_0020BE42:
    if (v_r15 != 0) goto loc_0020C086;
loc_0020BE4B:
    v_stack_p50 = 0;
    *(unsigned __int8 *)(v_rdi + 112) = 0;
    *(unsigned __int8 *)(v_rdi + 391) = a21;
    if (a22 != 0) {
    }
loc_0020BE90:
    if (condition_is_above_or_equal) goto loc_0020BEB4;
loc_0020BE99:
    v_rsi = (unsigned int)((0) + 1);
    if (*(unsigned __int64 *)(v_rdi + 64) == 0) goto loc_0020BE90;
    goto loc_0020BE99;
loc_0020BEB4:
    if (a22 != 0) goto loc_0020C18C;
    a4 = 0;
    if (((*(unsigned __int8 *)(v_rdi + 194)) & (2)) == 0) goto loc_0020BF5B;
    if (a21 == 0) goto loc_0020BF5B;
loc_0020BEF5:
    v_stack_p50 = 0;
    result = KiPerformWaitDeferredWork(v_rdi, (unsigned int)((unsigned int)(v_rbx)), 1, a10);
    *(unsigned __int64 *)(v_rdi + 64) = 0;
    if ((*(unsigned int *)(v_rip + 14396925)) != ((unsigned int)(result))) {
        a1 = v_cr8;
        a2 = (unsigned __int8)(*(unsigned __int8 *)(v_rdi + 390));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, 1, a10);
    }
    a4 = 0;
    goto loc_0020BF89;
loc_0020BF44:
    a4 = 0;
loc_0020BF57:
    if (0 != 0) goto loc_0020BEF5;
loc_0020BF5B:
    *(unsigned __int8 *)(v_rdi + 388) = 5;
    *(unsigned __int8 *)(v_rdi + 643) = 15;
    *(unsigned int *)(v_rdi + 436) = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(a25))));
    *(unsigned __int64 *)(v_rdi + 64) = 0;
loc_0020BF89:
    result = (unsigned int)(*(unsigned int *)((unsigned int)(a25)));
    if (*(unsigned __int64 *)(v_rdi + 232) != 0) {
        a3 = v_rdi + 520;
        a1 = v_rdi;
        result = KiActivateWaiterQueueWithNoLocks(a1, *(unsigned __int64 *)(v_rdi + 232), a3, a4);
    }
    *(unsigned __int64 *)(v_rdi + 232) = a20;
    result = KiAcquireKobjectLockSafe(a20, *(unsigned __int64 *)(v_rdi + 232), a3, a4);
loc_0020BFDC:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a20 + 40)))) > (*(unsigned int *)(a20 + 44))) goto loc_0020BE42;
    v_stack_p20 = *(unsigned __int64 *)(*(unsigned __int64 *)(a20 + 24) + 16);
    result = KeBugCheckEx(150, *(unsigned __int64 *)(a20 + 24), a20, *(unsigned __int64 *)(v_rip + 13560429));
loc_0020C05B:
    a1 = (*(unsigned __int64 *)(150)) - (*(unsigned __int64 *)(result));
    v_stack_p30 = 2;
    result = (*(unsigned __int64 *)(v_rdi + 248)) + (*(unsigned __int64 *)(a24));
    a1 = (a1) - (result);
    v_stack_p58 = a1;
    a4 = 0;
    goto loc_0020BE2B;
loc_0020C086:
    if ((*(unsigned __int64 *)(a24)) != 0) goto loc_0020BE4B;
loc_0020C0A6:
    if (condition_is_above_or_equal) goto loc_0020C0CA;
loc_0020C0AF:
    v_rsi = (unsigned int)((0) + 1);
    if (*(unsigned __int64 *)(v_rdi + 64) == 0) goto loc_0020C0A6;
    goto loc_0020C0AF;
loc_0020C0CA:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rdi + 390)) == 0) goto loc_0020C0EE;
loc_0020C0EE:
    a4 = 0;
    result = 0;
    if (0 == 0) {
        v_stack_p58 = 258;
        result = a11;
    }
    *(unsigned __int64 *)(a24) = result;
    if ((unsigned __int8)((unsigned int)(a25)) != 0) {
        *(unsigned __int64 *)(v_rdi + 64) = 0;
    }
    if ((*(unsigned int *)(v_rip + 14396386)) != 0) {
        a1 = *(unsigned __int8 *)(v_rdi + 390);
        a2 = (unsigned __int8)(*(unsigned __int8 *)(v_rdi + 390));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a20, a4);
    }
    if (((*(unsigned int *)(v_rip + 14395811)) & (0x1000000ULL)) != 0) {
        a3 = 1;
        a2 = a24;
        a1 = v_rdi;
        result = EtwTraceDequeueWork(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (96);
    return 1;
loc_0020C18C:
    if ((unsigned __int8)((__int8)(a21)) == 0) goto loc_0020BF44;
    if ((*(unsigned __int64 *)(v_rdi + 168)) == (v_rdi + 168)) goto loc_0020BF44;
    a4 = 0;
    goto loc_0020BF57;
loc_0020C1CE:
    a1 = ((unsigned int)(*(unsigned int *)(192 + 36))) << (5);
    a1 = (a1) + (v_rip + 13651688);
    if (((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 56)) & (*(unsigned __int64 *)(a1))) != 0) goto loc_0020BDE7;
    result = KiRcuReportQuiescentState(a1, a2, *(unsigned __int64 *)(a1), a4);
    if ((unsigned int)(result) == 0) goto loc_0020BDE7;
    result = KiRcuFlushCompleted(*(unsigned __int8 *)(192 + 14566), a2, *(unsigned __int64 *)(a1), a4);
    goto loc_0020BDE7;
}
```

## 5. (Beta) C Style

```c
int64_t sub_0020BDAA(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, int64_t Arg10, int64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, uint64_t Arg17, uint64_t Arg18, uint64_t Arg19, int64_t Arg20, void *Arg21, uint8_t Arg22, int64_t Arg23, void *Arg24, uint32_t Arg25)
{
    uint8_t *arg21 = (uint8_t *)Arg21;
    uint8_t *arg24 = (uint8_t *)Arg24;

    int64_t result;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p20;
    uint32_t v_stack_p30;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_pB8;

    v_stack_pB8 = local_r12;
    if ((*(uint8_t *)(local_rsi + 0x20)) > 1) goto loc_0020BDE7;
    if ((*(uint64_t *)(local_rsi + 0x38E8)) != (*(uint64_t *)(local_rsi + 0x38F0))) goto loc_0020C1CE;
loc_0020BDE7:
    if (local_r15 == 0) goto loc_0020BE23;
    if ((*(uint32_t *)(local_r15 + 0x4)) < 0) goto loc_0020C05B;
    Arg4 = 0;
    v_stack_p58 = *(uint64_t *)(local_r15);
    v_stack_p30 = 1;
    goto loc_0020BE2B;
loc_0020BE23:
    Arg4 = 0;
    v_stack_p30 = 0;
loc_0020BE2B:
    if ((*(uint64_t *)(local_rdi + 0xE8)) != local_r14) goto loc_0020BE4B;
    if ((*(uint32_t *)(local_r14 + 0x4)) != 0) goto loc_0020BFDC;
loc_0020BE42:
    if (local_r15 != 0) goto loc_0020C086;
loc_0020BE4B:
    v_stack_p50 = 0;
    *(uint8_t *)(local_rdi + 0x70) = 0;
    *(uint8_t *)(local_rdi + 0x187) = Arg21;
    if (Arg22 != 0) {
    }
loc_0020BE90:
    if (condition_is_above_or_equal) goto loc_0020BEB4;
loc_0020BE99:
    local_rsi = (uint32_t)((0) + 1);
    if (*(uint64_t *)(local_rdi + 0x40) == 0) goto loc_0020BE90;
    goto loc_0020BE99;
loc_0020BEB4:
    if (Arg22 != 0) goto loc_0020C18C;
    Arg4 = 0;
    if (((*(uint8_t *)(local_rdi + 0xC2)) & (2)) == 0) goto loc_0020BF5B;
    if (Arg21 == NULL) goto loc_0020BF5B;
loc_0020BEF5:
    v_stack_p50 = 0;
    result = KiPerformWaitDeferredWork(local_rdi, (uint32_t)((uint32_t)(local_rbx)), 1, Arg10);
    *(uint64_t *)(local_rdi + 0x40) = 0;
    if ((*(uint32_t *)(v_rip + 0xDBADFD)) != ((uint32_t)(result))) {
        Arg1 = v_cr8;
        Arg2 = (uint8_t)(*(uint8_t *)(local_rdi + 0x186));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, 1, Arg10);
    }
    Arg4 = 0;
    goto loc_0020BF89;
loc_0020BF44:
    Arg4 = 0;
loc_0020BF57:
    if (0 != 0) goto loc_0020BEF5;
loc_0020BF5B:
    *(uint8_t *)(local_rdi + 0x184) = 5;
    *(uint8_t *)(local_rdi + 0x283) = 15;
    *(uint32_t *)(local_rdi + 0x1B4) = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(Arg25))));
    *(uint64_t *)(local_rdi + 0x40) = 0;
loc_0020BF89:
    result = (uint32_t)(*(uint32_t *)((uint32_t)(Arg25)));
    if (*(uint64_t *)(local_rdi + 0xE8) != 0) {
        Arg3 = local_rdi + 520;
        Arg1 = local_rdi;
        result = KiActivateWaiterQueueWithNoLocks(Arg1, *(uint64_t *)(local_rdi + 0xE8), Arg3, Arg4);
    }
    *(uint64_t *)(local_rdi + 0xE8) = Arg20;
    result = KiAcquireKobjectLockSafe(Arg20, *(uint64_t *)(local_rdi + 0xE8), Arg3, Arg4);
loc_0020BFDC:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg20 + 0x28)))) > (*(uint32_t *)(Arg20 + 0x2C))) goto loc_0020BE42;
    v_stack_p20 = *(uint64_t *)(*(uint64_t *)(Arg20 + 0x18) + 0x10);
    result = KeBugCheckEx(150, *(uint64_t *)(Arg20 + 0x18), Arg20, *(uint64_t *)(v_rip + 0xCEEA6D));
loc_0020C05B:
    Arg1 = (*(uint64_t *)(150)) - (*(uint64_t *)(result));
    v_stack_p30 = 2;
    result = (*(uint64_t *)(local_rdi + 0xF8)) + (*(uint64_t *)(arg24));
    Arg1 = (Arg1) - (result);
    v_stack_p58 = Arg1;
    Arg4 = 0;
    goto loc_0020BE2B;
loc_0020C086:
    if ((*(uint64_t *)(arg24)) != 0) goto loc_0020BE4B;
loc_0020C0A6:
    if (condition_is_above_or_equal) goto loc_0020C0CA;
loc_0020C0AF:
    local_rsi = (uint32_t)((0) + 1);
    if (*(uint64_t *)(local_rdi + 0x40) == 0) goto loc_0020C0A6;
    goto loc_0020C0AF;
loc_0020C0CA:
    if ((uint8_t)(*(uint8_t *)(local_rdi + 0x186)) == 0) goto loc_0020C0EE;
loc_0020C0EE:
    Arg4 = 0;
    result = 0;
    if (0 == 0) {
        v_stack_p58 = 258;
        result = Arg11;
    }
    *(uint64_t *)(arg24) = result;
    if ((uint8_t)((uint32_t)(Arg25)) != 0) {
        *(uint64_t *)(local_rdi + 0x40) = 0;
    }
    if ((*(uint32_t *)(v_rip + 0xDBABE2)) != 0) {
        Arg1 = *(uint8_t *)(local_rdi + 0x186);
        Arg2 = (uint8_t)(*(uint8_t *)(local_rdi + 0x186));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg20, Arg4);
    }
    if (((*(uint32_t *)(v_rip + 0xDBA9A3)) & (0x1000000ULL)) != 0) {
        Arg3 = 1;
        Arg2 = Arg24;
        Arg1 = local_rdi;
        result = EtwTraceDequeueWork(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (96);
    return 1;
loc_0020C18C:
    if ((uint8_t)((int8_t)(Arg21)) == 0) goto loc_0020BF44;
    if ((*(uint64_t *)(local_rdi + 0xA8)) == (local_rdi + 168)) goto loc_0020BF44;
    Arg4 = 0;
    goto loc_0020BF57;
loc_0020C1CE:
    Arg1 = ((uint32_t)(*(uint32_t *)(192 + 0x24))) << (5);
    Arg1 = (Arg1) + (v_rip + 13651688);
    if (((*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x38)) & (*(uint64_t *)(Arg1))) != 0) goto loc_0020BDE7;
    result = KiRcuReportQuiescentState(Arg1, Arg2, *(uint64_t *)(Arg1), Arg4);
    if ((uint32_t)(result) == 0) goto loc_0020BDE7;
    result = KiRcuFlushCompleted(*(uint8_t *)(192 + 0x38E6), Arg2, *(uint64_t *)(Arg1), Arg4);
    goto loc_0020BDE7;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg21` | `+ 0x72 + rdi*1` | `8` | `R` |
| `Arg24` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0020BDAA&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
