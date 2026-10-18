# IopLiveDumpWriteDumpFileWithExtraPages

- RVA: `0x0059F910`–`0x005A01D4` (길이 `2,244` bytes)
- VA: `0x000000014059F910`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C79FC`
- 디코드: `534`개 명령, `2,244/2,244` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **34**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0059FA25` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0059FA5E` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0059FA88` → [IopLiveDumpGetNtMergePages](IopLiveDumpGetNtMergePages_function_0059C81C.md) (function, `0x0059C81C`)
- `0x0059FAA8` → [IopLiveDumpGetExtraMergePages](IopLiveDumpGetExtraMergePages_function_0059C548.md) (function, `0x0059C548`)
- `0x0059FB03` → [IopLiveDumpCheckTermination](../3F/IopLiveDumpCheckTermination_function_003F6780.md) (function, `0x003F6780`)
- `0x0059FB63` → [IopLiveDumpGetExtraMergePages](IopLiveDumpGetExtraMergePages_function_0059C548.md) (function, `0x0059C548`)
- `0x0059FB8D` → [IopLiveDumpWriteBuffer](../3F/IopLiveDumpWriteBuffer_function_003F6688.md) (function, `0x003F6688`)
- `0x0059FBD6` → [MiFreePagesFromMdl](../3F/MiFreePagesFromMdl_function_003F8300.md) (function, `0x003F8300`)
- `0x0059FBEB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0059FC50` → [IopLiveDumpGetNtMergePages](IopLiveDumpGetNtMergePages_function_0059C81C.md) (function, `0x0059C81C`)
- `0x0059FCD2` → [IopLiveDumpGetNtMergePages](IopLiveDumpGetNtMergePages_function_0059C81C.md) (function, `0x0059C81C`)
- `0x0059FD42` → [MmFreeIndependentPages](../2A/MmFreeIndependentPages_function_002A2510.md) (function, `0x002A2510`)
- `0x0059FD80` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0059FDDE` → [IopLiveDumpWriteBuffer](../3F/IopLiveDumpWriteBuffer_function_003F6688.md) (function, `0x003F6688`)
- `0x0059FE67` → [IopLiveDumpWriteBuffer](../3F/IopLiveDumpWriteBuffer_function_003F6688.md) (function, `0x003F6688`)
- `0x0059FE88` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0059FEB2` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0059FEEB` → [IopLiveDumpWriteBuffer](../3F/IopLiveDumpWriteBuffer_function_003F6688.md) (function, `0x003F6688`)
- `0x0059FF2C` → [IopLiveDumpWriteBuffer](../3F/IopLiveDumpWriteBuffer_function_003F6688.md) (function, `0x003F6688`)
- `0x0059FF76` → [IopLiveDumpWriteBuffer](../3F/IopLiveDumpWriteBuffer_function_003F6688.md) (function, `0x003F6688`)
- `0x0059FFA5` → [IopLiveDumpWriteBuffer](../3F/IopLiveDumpWriteBuffer_function_003F6688.md) (function, `0x003F6688`)
- `0x0059FFEF` → [IopLiveDumpWriteBuffer](../3F/IopLiveDumpWriteBuffer_function_003F6688.md) (function, `0x003F6688`)
- `0x005A001E` → [IopLiveDumpWriteBuffer](../3F/IopLiveDumpWriteBuffer_function_003F6688.md) (function, `0x003F6688`)
- `0x005A004B` → [RtlMergeBitMapsEx](../5E/RtlMergeBitMapsEx_function_005E62F0.md) (function, `0x005E62F0`)
- `0x005A006E` → [RtlMergeBitMapsEx](../5E/RtlMergeBitMapsEx_function_005E62F0.md) (function, `0x005E62F0`)
- `0x005A008E` → [RtlNumberOfSetBitsEx](../41/RtlNumberOfSetBitsEx_function_00418CA0.md) (function, `0x00418CA0`)
- `0x005A00EC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x005A0110` → [SecureDump_Get_SecureDumpHeader](../5A/SecureDump_Get_SecureDumpHeader_function_005A2B60.md) (function, `0x005A2B60`)
- `0x005A0142` → [IopLiveDumpWriteBuffer](../3F/IopLiveDumpWriteBuffer_function_003F6688.md) (function, `0x003F6688`)
- `0x005A0177` → [IopLiveDumpWriteBuffer](../3F/IopLiveDumpWriteBuffer_function_003F6688.md) (function, `0x003F6688`)
- `0x005A0188` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x005A0197` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x005A019F` → [IopLiveDumpFreeDumpBuffers](../3F/IopLiveDumpFreeDumpBuffers_function_003F5FE8.md) (function, `0x003F5FE8`)
- `0x005A01AD` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [IoCaptureLiveDump](../4E/IoCaptureLiveDump_function_004E085C.md) at `0x004E0DCB`

### Static image references
- `0x0059F933` → RVA `0x00E0A740` (`.data`; read)
- `0x0059FD38` → RVA `0x00E0A9D0` (`.data`; read)
- `0x0059FD96` → RVA `0x00E0A74C` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x0059FBEB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x0059FD80` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x005A00EC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x005A0188` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x005A0197` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0059F910  48 8B C4                        mov rax, rsp
0059F913  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0059F917  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0059F91B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0059F91F  55                              push rbp
0059F920  41 54                           push r12
0059F922  41 55                           push r13
0059F924  41 56                           push r14
0059F926  41 57                           push r15
0059F928  48 8D 68 A1                     lea rbp, [rax - 0x5f]
0059F92C  48 81 EC F0 00 00 00            sub rsp, 0xf0
0059F933  48 8B 05 06 AE 86 00            mov rax, qword ptr [rip + 0x86ae06]
0059F93A  48 33 C4                        xor rax, rsp
0059F93D  48 89 45 2F                     mov qword ptr [rbp + 0x2f], rax
0059F941  4C 8B B9 68 04 00 00            mov r15, qword ptr [rcx + 0x468]
0059F948  45 33 E4                        xor r12d, r12d
0059F94B  48 8B B1 30 02 00 00            mov rsi, qword ptr [rcx + 0x230]
0059F952  0F 57 C9                        xorps xmm1, xmm1
0059F955  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
0059F95A  0F 57 C0                        xorps xmm0, xmm0
0059F95D  4C 89 65 97                     mov qword ptr [rbp - 0x69], r12
0059F961  48 8B D9                        mov rbx, rcx
0059F964  4C 89 65 B7                     mov qword ptr [rbp - 0x49], r12
0059F968  45 8B EC                        mov r13d, r12d
0059F96B  44 89 65 8B                     mov dword ptr [rbp - 0x75], r12d
0059F96F  4C 89 65 8F                     mov qword ptr [rbp - 0x71], r12
0059F973  4C 89 65 A7                     mov qword ptr [rbp - 0x59], r12
0059F977  44 89 65 87                     mov dword ptr [rbp - 0x79], r12d
0059F97B  4C 89 65 F7                     mov qword ptr [rbp - 9], r12
0059F97F  4C 89 7D E7                     mov qword ptr [rbp - 0x19], r15
0059F983  0F 11 45 1F                     movups xmmword ptr [rbp + 0x1f], xmm0
0059F987  0F 11 4D FF                     movups xmmword ptr [rbp - 1], xmm1
0059F98B  0F 11 4D 0F                     movups xmmword ptr [rbp + 0xf], xmm1
0059F98F  4D 85 FF                        test r15, r15
0059F992  75 0A                           jne 0x14059f99e
0059F994  BF 9A 00 00 C0                  mov edi, 0xc000009a
0059F999  E9 FE 07 00 00                  jmp 0x1405a019c
0059F99E  48 8B B9 70 04 00 00            mov rdi, qword ptr [rcx + 0x470]
0059F9A5  48 89 7D DF                     mov qword ptr [rbp - 0x21], rdi
0059F9A9  48 85 FF                        test rdi, rdi
0059F9AC  74 E6                           je 0x14059f994
0059F9AE  44 38 A1 D8 03 00 00            cmp byte ptr [rcx + 0x3d8], r12b
0059F9B5  74 0F                           je 0x14059f9c6
0059F9B7  8B 81 E0 03 00 00               mov eax, dword ptr [rcx + 0x3e0]
0059F9BD  48 03 86 20 20 00 00            add rax, qword ptr [rsi + 0x2020]
0059F9C4  EB 07                           jmp 0x14059f9cd
0059F9C6  48 8B 86 20 20 00 00            mov rax, qword ptr [rsi + 0x2020]
0059F9CD  4C 8B 71 40                     mov r14, qword ptr [rcx + 0x40]
0059F9D1  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0059F9D6  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0059F9DF  48 83 4D D7 FF                  or qword ptr [rbp - 0x29], 0xffffffffffffffff
0059F9E4  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
0059F9E8  48 8B 81 70 02 00 00            mov rax, qword ptr [rcx + 0x270]
0059F9EF  4C 89 65 BF                     mov qword ptr [rbp - 0x41], r12
0059F9F3  44 88 64 24 30                  mov byte ptr [rsp + 0x30], r12b
0059F9F8  48 39 81 28 02 00 00            cmp qword ptr [rcx + 0x228], rax
0059F9FF  74 29                           je 0x14059fa2a
0059FA01  48 8B 81 68 02 00 00            mov rax, qword ptr [rcx + 0x268]
0059FA08  4D 8B C4                        mov r8, r12
0059FA0B  48 8B 89 70 02 00 00            mov rcx, qword ptr [rcx + 0x270]
0059FA12  A8 1F                           test al, 0x1f
0059FA14  41 0F 95 C0                     setne r8b
0059FA18  48 C1 E8 05                     shr rax, 5
0059FA1C  4C 03 C0                        add r8, rax
0059FA1F  33 D2                           xor edx, edx
0059FA21  49 C1 E0 02                     shl r8, 2
0059FA25  E8 16 72 12 00                  call 0x1406c6c40
0059FA2A  48 8B 83 80 02 00 00            mov rax, qword ptr [rbx + 0x280]
0059FA31  48 39 83 70 02 00 00            cmp qword ptr [rbx + 0x270], rax
0059FA38  74 29                           je 0x14059fa63
0059FA3A  48 8B 83 78 02 00 00            mov rax, qword ptr [rbx + 0x278]
0059FA41  4D 8B C4                        mov r8, r12
0059FA44  48 8B 8B 80 02 00 00            mov rcx, qword ptr [rbx + 0x280]
0059FA4B  A8 1F                           test al, 0x1f
0059FA4D  41 0F 95 C0                     setne r8b
0059FA51  48 C1 E8 05                     shr rax, 5
0059FA55  4C 03 C0                        add r8, rax
0059FA58  33 D2                           xor edx, edx
0059FA5A  49 C1 E0 02                     shl r8, 2
0059FA5E  E8 DD 71 12 00                  call 0x1406c6c40
0059FA63  48 8D 45 A7                     lea rax, [rbp - 0x59]
0059FA67  4C 89 A3 D8 02 00 00            mov qword ptr [rbx + 0x2d8], r12
0059FA6E  4C 8D 4D 87                     lea r9, [rbp - 0x79]
0059FA72  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0059FA77  4C 8D 45 8F                     lea r8, [rbp - 0x71]
0059FA7B  4C 89 A3 E0 02 00 00            mov qword ptr [rbx + 0x2e0], r12
0059FA82  48 8B D7                        mov rdx, rdi
0059FA85  48 8B CB                        mov rcx, rbx
0059FA88  E8 8F CD FF FF                  call 0x14059c81c
0059FA8D  48 8D 4D B7                     lea rcx, [rbp - 0x49]
0059FA91  48 89 7D AF                     mov qword ptr [rbp - 0x51], rdi
0059FA95  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0059FA9A  4C 8D 4D 8B                     lea r9, [rbp - 0x75]
0059FA9E  48 8B CB                        mov rcx, rbx
0059FAA1  4C 8D 45 97                     lea r8, [rbp - 0x69]
0059FAA5  49 8B D7                        mov rdx, r15
0059FAA8  E8 9B CA FF FF                  call 0x14059c548
0059FAAD  44 8B 65 87                     mov r12d, dword ptr [rbp - 0x79]
0059FAB1  4D 8B C7                        mov r8, r15
0059FAB4  4C 89 7D 9F                     mov qword ptr [rbp - 0x61], r15
0059FAB8  44 8A D0                        mov r10b, al
0059FABB  44 8B 7D 8B                     mov r15d, dword ptr [rbp - 0x75]
0059FABF  88 44 24 31                     mov byte ptr [rsp + 0x31], al
0059FAC3  41 BB 00 10 00 00               mov r11d, 0x1000
0059FAC9  45 85 FF                        test r15d, r15d
0059FACC  75 09                           jne 0x14059fad7
0059FACE  45 85 E4                        test r12d, r12d
0059FAD1  0F 84 8F 02 00 00               je 0x14059fd66
0059FAD7  45 85 E4                        test r12d, r12d
0059FADA  75 0A                           jne 0x14059fae6
0059FADC  4C 8D 4D D7                     lea r9, [rbp - 0x29]
0059FAE0  4C 89 4D AF                     mov qword ptr [rbp - 0x51], r9
0059FAE4  EB 16                           jmp 0x14059fafc
0059FAE6  4C 8B 4D AF                     mov r9, qword ptr [rbp - 0x51]
0059FAEA  48 8D 45 D7                     lea rax, [rbp - 0x29]
0059FAEE  45 85 FF                        test r15d, r15d
0059FAF1  49 0F 45 C0                     cmovne rax, r8
0059FAF5  4C 8B C0                        mov r8, rax
0059FAF8  48 89 45 9F                     mov qword ptr [rbp - 0x61], rax
0059FAFC  48 8B 55 EF                     mov rdx, qword ptr [rbp - 0x11]
0059FB00  48 8B CB                        mov rcx, rbx
0059FB03  E8 78 6C E5 FF                  call 0x1403f6780
0059FB08  8B F8                           mov edi, eax
0059FB0A  85 C0                           test eax, eax
0059FB0C  0F 88 8A 06 00 00               js 0x1405a019c
0059FB12  45 85 FF                        test r15d, r15d
0059FB15  0F 84 EC 00 00 00               je 0x14059fc07
0059FB1B  49 8B 01                        mov rax, qword ptr [r9]
0059FB1E  41 8D 4F FF                     lea ecx, [r15 - 1]
0059FB22  49 39 04 C8                     cmp qword ptr [r8 + rcx*8], rax
0059FB26  0F 83 DB 00 00 00               jae 0x14059fc07
0059FB2C  48 8B 45 97                     mov rax, qword ptr [rbp - 0x69]
0059FB30  41 C1 E7 0C                     shl r15d, 0xc
0059FB34  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
0059FB38  41 8B FF                        mov edi, r15d
0059FB3B  48 8B 45 B7                     mov rax, qword ptr [rbp - 0x49]
0059FB3F  48 8D 4D B7                     lea rcx, [rbp - 0x49]
0059FB43  4C 8B 7D E7                     mov r15, qword ptr [rbp - 0x19]
0059FB47  4C 8D 4D 8B                     lea r9, [rbp - 0x75]
0059FB4B  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0059FB50  4C 8D 45 97                     lea r8, [rbp - 0x69]
0059FB54  48 8B CB                        mov rcx, rbx
0059FB57  44 88 54 24 30                  mov byte ptr [rsp + 0x30], r10b
0059FB5C  49 8B D7                        mov rdx, r15
0059FB5F  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
0059FB63  E8 E0 C9 FF FF                  call 0x14059c548
0059FB68  4C 89 7D 9F                     mov qword ptr [rbp - 0x61], r15
0059FB6C  44 8B 7D 8B                     mov r15d, dword ptr [rbp - 0x75]
0059FB70  88 44 24 31                     mov byte ptr [rsp + 0x31], al
0059FB74  48 8B 55 C7                     mov rdx, qword ptr [rbp - 0x39]
0059FB78  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
0059FB7D  44 88 6C 24 28                  mov byte ptr [rsp + 0x28], r13b
0059FB82  44 8B C7                        mov r8d, edi
0059FB85  49 8B CE                        mov rcx, r14
0059FB88  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0059FB8D  E8 F6 6A E5 FF                  call 0x1403f6688
0059FB92  8B F8                           mov edi, eax
0059FB94  85 C0                           test eax, eax
0059FB96  0F 88 00 06 00 00               js 0x1405a019c
0059FB9C  41 BB 00 10 00 00               mov r11d, 0x1000
0059FBA2  4C 8B 45 9F                     mov r8, qword ptr [rbp - 0x61]
0059FBA6  44 8A 54 24 31                  mov r10b, byte ptr [rsp + 0x31]
0059FBAB  44 38 6C 24 30                  cmp byte ptr [rsp + 0x30], r13b
0059FBB0  0F 84 13 FF FF FF               je 0x14059fac9
0059FBB6  48 8B 83 F8 02 00 00            mov rax, qword ptr [rbx + 0x2f8]
0059FBBD  48 8B 7D BF                     mov rdi, qword ptr [rbp - 0x41]
0059FBC1  48 8B 0C F8                     mov rcx, qword ptr [rax + rdi*8]
0059FBC5  48 85 C9                        test rcx, rcx
0059FBC8  0F 84 51 01 00 00               je 0x14059fd1f
0059FBCE  45 33 C9                        xor r9d, r9d
0059FBD1  45 33 C0                        xor r8d, r8d
0059FBD4  33 D2                           xor edx, edx
0059FBD6  E8 25 87 E5 FF                  call 0x1403f8300
0059FBDB  48 8B 8B F8 02 00 00            mov rcx, qword ptr [rbx + 0x2f8]
0059FBE2  BA 4C 64 6D 70                  mov edx, 0x706d644c
0059FBE7  48 8B 0C F9                     mov rcx, qword ptr [rcx + rdi*8]
0059FBEB  E8 80 2C 5E 00                  call 0x140b82870
0059FBF0  48 8B 83 F0 02 00 00            mov rax, qword ptr [rbx + 0x2f0]
0059FBF7  4C 21 2C F8                     and qword ptr [rax + rdi*8], r13
0059FBFB  48 8B 83 F8 02 00 00            mov rax, qword ptr [rbx + 0x2f8]
0059FC02  E9 47 01 00 00                  jmp 0x14059fd4e
0059FC07  45 85 E4                        test r12d, r12d
0059FC0A  74 56                           je 0x14059fc62
0059FC0C  49 8B 00                        mov rax, qword ptr [r8]
0059FC0F  41 8D 4C 24 FF                  lea ecx, [r12 - 1]
0059FC14  49 39 04 C9                     cmp qword ptr [r9 + rcx*8], rax
0059FC18  73 48                           jae 0x14059fc62
0059FC1A  48 8B 45 8F                     mov rax, qword ptr [rbp - 0x71]
0059FC1E  48 8D 4D A7                     lea rcx, [rbp - 0x59]
0059FC22  41 8B FC                        mov edi, r12d
0059FC25  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
0059FC29  48 8B 45 A7                     mov rax, qword ptr [rbp - 0x59]
0059FC2D  4C 8D 4D 87                     lea r9, [rbp - 0x79]
0059FC31  4C 8B 65 DF                     mov r12, qword ptr [rbp - 0x21]
0059FC35  4C 8D 45 8F                     lea r8, [rbp - 0x71]
0059FC39  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0059FC3E  49 8B D4                        mov rdx, r12
0059FC41  C1 E7 0C                        shl edi, 0xc
0059FC44  48 8B CB                        mov rcx, rbx
0059FC47  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
0059FC4B  C6 44 24 30 01                  mov byte ptr [rsp + 0x30], 1
0059FC50  E8 C7 CB FF FF                  call 0x14059c81c
0059FC55  4C 89 65 AF                     mov qword ptr [rbp - 0x51], r12
0059FC59  44 8B 65 87                     mov r12d, dword ptr [rbp - 0x79]
0059FC5D  E9 12 FF FF FF                  jmp 0x14059fb74
0059FC62  49 8B 01                        mov rax, qword ptr [r9]
0059FC65  41 8B FB                        mov edi, r11d
0059FC68  44 88 6C 24 32                  mov byte ptr [rsp + 0x32], r13b
0059FC6D  49 3B 00                        cmp rax, qword ptr [r8]
0059FC70  73 0A                           jae 0x14059fc7c
0059FC72  48 8B 45 8F                     mov rax, qword ptr [rbp - 0x71]
0059FC76  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
0059FC7A  EB 13                           jmp 0x14059fc8f
0059FC7C  48 8B 55 97                     mov rdx, qword ptr [rbp - 0x69]
0059FC80  48 89 55 C7                     mov qword ptr [rbp - 0x39], rdx
0059FC84  C6 44 24 32 01                  mov byte ptr [rsp + 0x32], 1
0059FC89  75 72                           jne 0x14059fcfd
0059FC8B  48 8B 45 8F                     mov rax, qword ptr [rbp - 0x71]
0059FC8F  41 83 C4 FF                     add r12d, -1
0059FC93  44 89 65 87                     mov dword ptr [rbp - 0x79], r12d
0059FC97  74 11                           je 0x14059fcaa
0059FC99  49 03 C3                        add rax, r11
0059FC9C  49 83 C1 08                     add r9, 8
0059FCA0  48 89 45 8F                     mov qword ptr [rbp - 0x71], rax
0059FCA4  4C 89 4D AF                     mov qword ptr [rbp - 0x51], r9
0059FCA8  EB 44                           jmp 0x14059fcee
0059FCAA  48 8B 45 A7                     mov rax, qword ptr [rbp - 0x59]
0059FCAE  48 8D 4D A7                     lea rcx, [rbp - 0x59]
0059FCB2  4C 8B 65 DF                     mov r12, qword ptr [rbp - 0x21]
0059FCB6  4C 8D 4D 87                     lea r9, [rbp - 0x79]
0059FCBA  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0059FCBF  4C 8D 45 8F                     lea r8, [rbp - 0x71]
0059FCC3  48 8B CB                        mov rcx, rbx
0059FCC6  C6 44 24 30 01                  mov byte ptr [rsp + 0x30], 1
0059FCCB  49 8B D4                        mov rdx, r12
0059FCCE  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
0059FCD2  E8 45 CB FF FF                  call 0x14059c81c
0059FCD7  4C 8B 45 9F                     mov r8, qword ptr [rbp - 0x61]
0059FCDB  41 BB 00 10 00 00               mov r11d, 0x1000
0059FCE1  44 8A 54 24 31                  mov r10b, byte ptr [rsp + 0x31]
0059FCE6  4C 89 65 AF                     mov qword ptr [rbp - 0x51], r12
0059FCEA  44 8B 65 87                     mov r12d, dword ptr [rbp - 0x79]
0059FCEE  44 38 6C 24 32                  cmp byte ptr [rsp + 0x32], r13b
0059FCF3  0F 84 7B FE FF FF               je 0x14059fb74
0059FCF9  48 8B 55 97                     mov rdx, qword ptr [rbp - 0x69]
0059FCFD  41 83 C7 FF                     add r15d, -1
0059FD01  44 89 7D 8B                     mov dword ptr [rbp - 0x75], r15d
0059FD05  0F 84 30 FE FF FF               je 0x14059fb3b
0059FD0B  49 03 D3                        add rdx, r11
0059FD0E  49 83 C0 08                     add r8, 8
0059FD12  48 89 55 97                     mov qword ptr [rbp - 0x69], rdx
0059FD16  4C 89 45 9F                     mov qword ptr [rbp - 0x61], r8
0059FD1A  E9 55 FE FF FF                  jmp 0x14059fb74
0059FD1F  4C 39 AB 30 03 00 00            cmp qword ptr [rbx + 0x330], r13
0059FD26  75 2A                           jne 0x14059fd52
0059FD28  4C 39 AB 58 03 00 00            cmp qword ptr [rbx + 0x358], r13
0059FD2F  75 21                           jne 0x14059fd52
0059FD31  48 8B 8B F0 02 00 00            mov rcx, qword ptr [rbx + 0x2f0]
0059FD38  8B 15 92 AC 86 00               mov edx, dword ptr [rip + 0x86ac92]
0059FD3E  48 8B 0C F9                     mov rcx, qword ptr [rcx + rdi*8]
0059FD42  E8 C9 27 D0 FF                  call 0x1402a2510
0059FD47  48 8B 83 F0 02 00 00            mov rax, qword ptr [rbx + 0x2f0]
0059FD4E  4C 21 2C F8                     and qword ptr [rax + rdi*8], r13
0059FD52  4C 8B 45 9F                     mov r8, qword ptr [rbp - 0x61]
0059FD56  32 C0                           xor al, al
0059FD58  44 8A 54 24 31                  mov r10b, byte ptr [rsp + 0x31]
0059FD5D  88 44 24 30                     mov byte ptr [rsp + 0x30], al
0059FD61  E9 5D FD FF FF                  jmp 0x14059fac3
0059FD66  45 33 E4                        xor r12d, r12d
0059FD69  44 38 A3 D8 03 00 00            cmp byte ptr [rbx + 0x3d8], r12b
0059FD70  74 1F                           je 0x14059fd91
0059FD72  41 B8 4C 64 6D 70               mov r8d, 0x706d644c
0059FD78  41 8D 4C 24 40                  lea ecx, [r12 + 0x40]
0059FD7D  49 8B D3                        mov rdx, r11
0059FD80  E8 6B 23 5E 00                  call 0x140b820f0
0059FD85  4C 8B E8                        mov r13, rax
0059FD88  48 85 C0                        test rax, rax
0059FD8B  0F 84 03 FC FF FF               je 0x14059f994
0059FD91  B9 10 00 00 00                  mov ecx, 0x10
0059FD96  8B 05 B0 A9 86 00               mov eax, dword ptr [rip + 0x86a9b0]
0059FD9C  89 4D 27                        mov dword ptr [rbp + 0x27], ecx
0059FD9F  C7 45 1F 44 75 6D 70            mov dword ptr [rbp + 0x1f], 0x706d7544
0059FDA6  C7 45 23 42 6C 6F 62            mov dword ptr [rbp + 0x23], 0x626f6c42
0059FDAD  89 45 2B                        mov dword ptr [rbp + 0x2b], eax
0059FDB0  44 38 A3 D8 03 00 00            cmp byte ptr [rbx + 0x3d8], r12b
0059FDB7  74 0C                           je 0x14059fdc5
0059FDB9  0F 10 45 1F                     movups xmm0, xmmword ptr [rbp + 0x1f]
0059FDBD  F3 41 0F 7F 45 00               movdqu xmmword ptr [r13], xmm0
0059FDC3  EB 2B                           jmp 0x14059fdf0
0059FDC5  44 8B C1                        mov r8d, ecx
0059FDC8  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
0059FDCD  49 8B CE                        mov rcx, r14
0059FDD0  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0059FDD5  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
0059FDDA  48 8D 55 1F                     lea rdx, [rbp + 0x1f]
0059FDDE  E8 A5 68 E5 FF                  call 0x1403f6688
0059FDE3  8B F8                           mov edi, eax
0059FDE5  85 C0                           test eax, eax
0059FDE7  0F 88 A0 03 00 00               js 0x1405a018d
0059FDED  41 8B CC                        mov ecx, r12d
0059FDF0  41 BF 20 00 00 00               mov r15d, 0x20
0059FDF6  8B 83 B8 00 00 00               mov eax, dword ptr [rbx + 0xb8]
0059FDFC  0F 10 83 A0 00 00 00            movups xmm0, xmmword ptr [rbx + 0xa0]
0059FE03  44 89 7D FF                     mov dword ptr [rbp - 1], r15d
0059FE07  89 45 13                        mov dword ptr [rbp + 0x13], eax
0059FE0A  F3 0F 7F 45 03                  movdqu xmmword ptr [rbp + 3], xmm0
0059FE0F  44 89 65 1B                     mov dword ptr [rbp + 0x1b], r12d
0059FE13  44 38 A3 D8 03 00 00            cmp byte ptr [rbx + 0x3d8], r12b
0059FE1A  0F 84 9C 00 00 00               je 0x14059febc
0059FE20  0F 10 45 FF                     movups xmm0, xmmword ptr [rbp - 1]
0059FE24  B8 E0 0F 00 00                  mov eax, 0xfe0
0059FE29  44 8D 60 20                     lea r12d, [rax + 0x20]
0059FE2D  2B C1                           sub eax, ecx
0059FE2F  89 45 17                        mov dword ptr [rbp + 0x17], eax
0059FE32  8B C1                           mov eax, ecx
0059FE34  42 0F 11 04 28                  movups xmmword ptr [rax + r13], xmm0
0059FE39  0F 10 4D 0F                     movups xmm1, xmmword ptr [rbp + 0xf]
0059FE3D  42 0F 11 4C 28 10               movups xmmword ptr [rax + r13 + 0x10], xmm1
0059FE43  45 85 E4                        test r12d, r12d
0059FE46  0F 84 B8 00 00 00               je 0x14059ff04
0059FE4C  C6 44 24 28 00                  mov byte ptr [rsp + 0x28], 0
0059FE51  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
0059FE56  41 B8 00 10 00 00               mov r8d, 0x1000
0059FE5C  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0059FE61  49 8B D5                        mov rdx, r13
0059FE64  49 8B CE                        mov rcx, r14
0059FE67  E8 1C 68 E5 FF                  call 0x1403f6688
0059FE6C  8B F8                           mov edi, eax
0059FE6E  85 C0                           test eax, eax
0059FE70  0F 88 17 03 00 00               js 0x1405a018d
0059FE76  33 D2                           xor edx, edx
0059FE78  41 B8 00 10 00 00               mov r8d, 0x1000
0059FE7E  49 8B CD                        mov rcx, r13
0059FE81  41 81 C4 00 F0 FF FF            add r12d, 0xfffff000
0059FE88  E8 B3 6D 12 00                  call 0x1406c6c40
0059FE8D  8B 7D FF                        mov edi, dword ptr [rbp - 1]
0059FE90  44 3B FF                        cmp r15d, edi
0059FE93  74 AE                           je 0x14059fe43
0059FE95  B8 00 10 00 00                  mov eax, 0x1000
0059FE9A  48 8D 55 FF                     lea rdx, [rbp - 1]
0059FE9E  41 2B FF                        sub edi, r15d
0059FEA1  49 8B CD                        mov rcx, r13
0059FEA4  3B F8                           cmp edi, eax
0059FEA6  0F 47 F8                        cmova edi, eax
0059FEA9  41 8B C7                        mov eax, r15d
0059FEAC  48 03 D0                        add rdx, rax
0059FEAF  44 8B C7                        mov r8d, edi
0059FEB2  E8 89 69 12 00                  call 0x1406c6840
0059FEB7  44 03 FF                        add r15d, edi
0059FEBA  EB 87                           jmp 0x14059fe43
0059FEBC  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
0059FEC1  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
0059FEC6  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
0059FECB  48 8D 55 FF                     lea rdx, [rbp - 1]
0059FECF  45 8B C7                        mov r8d, r15d
0059FED2  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0059FED7  8D 88 1F 10 00 00               lea ecx, [rax + 0x101f]
0059FEDD  81 E1 00 F0 FF FF               and ecx, 0xfffff000
0059FEE3  2B C8                           sub ecx, eax
0059FEE5  89 4D 17                        mov dword ptr [rbp + 0x17], ecx
0059FEE8  49 8B CE                        mov rcx, r14
0059FEEB  E8 98 67 E5 FF                  call 0x1403f6688
0059FEF0  8B F8                           mov edi, eax
0059FEF2  85 C0                           test eax, eax
0059FEF4  0F 88 93 02 00 00               js 0x1405a018d
0059FEFA  8B 45 17                        mov eax, dword ptr [rbp + 0x17]
0059FEFD  48 01 44 24 38                  add qword ptr [rsp + 0x38], rax
0059FF02  EB 08                           jmp 0x14059ff0c
0059FF04  45 33 E4                        xor r12d, r12d
0059FF07  45 8D 7C 24 20                  lea r15d, [r12 + 0x20]
0059FF0C  44 8B 83 B8 00 00 00            mov r8d, dword ptr [rbx + 0xb8]
0059FF13  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
0059FF18  48 8B 93 B0 00 00 00            mov rdx, qword ptr [rbx + 0xb0]
0059FF1F  49 8B CE                        mov rcx, r14
0059FF22  44 88 64 24 28                  mov byte ptr [rsp + 0x28], r12b
0059FF27  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0059FF2C  E8 57 67 E5 FF                  call 0x1403f6688
0059FF31  8B F8                           mov edi, eax
0059FF33  85 C0                           test eax, eax
0059FF35  0F 88 52 02 00 00               js 0x1405a018d
0059FF3B  8B 83 40 04 00 00               mov eax, dword ptr [rbx + 0x440]
0059FF41  85 C0                           test eax, eax
0059FF43  74 6F                           je 0x14059ffb4
0059FF45  0F 10 83 28 04 00 00            movups xmm0, xmmword ptr [rbx + 0x428]
0059FF4C  48 83 65 17 00                  and qword ptr [rbp + 0x17], 0
0059FF51  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
0059FF56  44 88 64 24 28                  mov byte ptr [rsp + 0x28], r12b
0059FF5B  48 8D 55 FF                     lea rdx, [rbp - 1]
0059FF5F  45 8B C7                        mov r8d, r15d
0059FF62  44 89 7D FF                     mov dword ptr [rbp - 1], r15d
0059FF66  49 8B CE                        mov rcx, r14
0059FF69  89 45 13                        mov dword ptr [rbp + 0x13], eax
0059FF6C  F3 0F 7F 45 03                  movdqu xmmword ptr [rbp + 3], xmm0
0059FF71  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0059FF76  E8 0D 67 E5 FF                  call 0x1403f6688
0059FF7B  8B F8                           mov edi, eax
0059FF7D  85 C0                           test eax, eax
0059FF7F  0F 88 08 02 00 00               js 0x1405a018d
0059FF85  44 8B 83 40 04 00 00            mov r8d, dword ptr [rbx + 0x440]
0059FF8C  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
0059FF91  48 8B 93 38 04 00 00            mov rdx, qword ptr [rbx + 0x438]
0059FF98  49 8B CE                        mov rcx, r14
0059FF9B  44 88 64 24 28                  mov byte ptr [rsp + 0x28], r12b
0059FFA0  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0059FFA5  E8 DE 66 E5 FF                  call 0x1403f6688
0059FFAA  8B F8                           mov edi, eax
0059FFAC  85 C0                           test eax, eax
0059FFAE  0F 88 D9 01 00 00               js 0x1405a018d
0059FFB4  8B 83 10 04 00 00               mov eax, dword ptr [rbx + 0x410]
0059FFBA  85 C0                           test eax, eax
0059FFBC  74 6F                           je 0x1405a002d
0059FFBE  0F 10 83 F8 03 00 00            movups xmm0, xmmword ptr [rbx + 0x3f8]
0059FFC5  48 83 65 17 00                  and qword ptr [rbp + 0x17], 0
0059FFCA  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
0059FFCF  44 88 64 24 28                  mov byte ptr [rsp + 0x28], r12b
0059FFD4  48 8D 55 FF                     lea rdx, [rbp - 1]
0059FFD8  45 8B C7                        mov r8d, r15d
0059FFDB  44 89 7D FF                     mov dword ptr [rbp - 1], r15d
0059FFDF  49 8B CE                        mov rcx, r14
0059FFE2  89 45 13                        mov dword ptr [rbp + 0x13], eax
0059FFE5  F3 0F 7F 45 03                  movdqu xmmword ptr [rbp + 3], xmm0
0059FFEA  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0059FFEF  E8 94 66 E5 FF                  call 0x1403f6688
0059FFF4  8B F8                           mov edi, eax
0059FFF6  85 C0                           test eax, eax
0059FFF8  0F 88 8F 01 00 00               js 0x1405a018d
0059FFFE  44 8B 83 10 04 00 00            mov r8d, dword ptr [rbx + 0x410]
005A0005  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
005A000A  48 8B 93 08 04 00 00            mov rdx, qword ptr [rbx + 0x408]
005A0011  49 8B CE                        mov rcx, r14
005A0014  44 88 64 24 28                  mov byte ptr [rsp + 0x28], r12b
005A0019  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
005A001E  E8 65 66 E5 FF                  call 0x1403f6688
005A0023  8B F8                           mov edi, eax
005A0025  85 C0                           test eax, eax
005A0027  0F 88 60 01 00 00               js 0x1405a018d
005A002D  48 8B 83 70 02 00 00            mov rax, qword ptr [rbx + 0x270]
005A0034  48 39 83 28 02 00 00            cmp qword ptr [rbx + 0x228], rax
005A003B  74 13                           je 0x1405a0050
005A003D  48 8D 93 68 02 00 00            lea rdx, [rbx + 0x268]
005A0044  48 8D 8B 20 02 00 00            lea rcx, [rbx + 0x220]
005A004B  E8 A0 62 04 00                  call 0x1405e62f0
005A0050  48 8B 83 80 02 00 00            mov rax, qword ptr [rbx + 0x280]
005A0057  48 39 83 70 02 00 00            cmp qword ptr [rbx + 0x270], rax
005A005E  74 13                           je 0x1405a0073
005A0060  48 8D 93 78 02 00 00            lea rdx, [rbx + 0x278]
005A0067  48 8D 8B 20 02 00 00            lea rcx, [rbx + 0x220]
005A006E  E8 7D 62 04 00                  call 0x1405e62f0
005A0073  48 8D 8B 20 02 00 00            lea rcx, [rbx + 0x220]
005A007A  C7 86 00 20 00 00 53 44 4D 50   mov dword ptr [rsi + 0x2000], 0x504d4453
005A0084  C7 86 04 20 00 00 44 55 4D 50   mov dword ptr [rsi + 0x2004], 0x504d5544
005A008E  E8 0D 8C E7 FF                  call 0x140418ca0
005A0093  48 89 86 28 20 00 00            mov qword ptr [rsi + 0x2028], rax
005A009A  44 38 A3 D8 03 00 00            cmp byte ptr [rbx + 0x3d8], r12b
005A00A1  74 17                           je 0x1405a00ba
005A00A3  8B 83 E0 03 00 00               mov eax, dword ptr [rbx + 0x3e0]
005A00A9  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
005A00AE  48 2B C8                        sub rcx, rax
005A00B1  48 89 8E A0 0F 00 00            mov qword ptr [rsi + 0xfa0], rcx
005A00B8  EB 0C                           jmp 0x1405a00c6
005A00BA  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
005A00BF  48 89 86 A0 0F 00 00            mov qword ptr [rsi + 0xfa0], rax
005A00C6  83 8E 50 10 00 00 10            or dword ptr [rsi + 0x1050], 0x10
005A00CD  44 38 A3 D8 03 00 00            cmp byte ptr [rbx + 0x3d8], r12b
005A00D4  74 47                           je 0x1405a011d
005A00D6  8B 93 E0 03 00 00               mov edx, dword ptr [rbx + 0x3e0]
005A00DC  B9 40 00 00 00                  mov ecx, 0x40
005A00E1  41 B8 4C 64 6D 70               mov r8d, 0x706d644c
005A00E7  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
005A00EC  E8 FF 1F 5E 00                  call 0x140b820f0
005A00F1  4C 8B F8                        mov r15, rax
005A00F4  48 85 C0                        test rax, rax
005A00F7  75 0A                           jne 0x1405a0103
005A00F9  BF 9A 00 00 C0                  mov edi, 0xc000009a
005A00FE  E9 8A 00 00 00                  jmp 0x1405a018d
005A0103  44 8B 83 E0 03 00 00            mov r8d, dword ptr [rbx + 0x3e0]
005A010A  48 8B D0                        mov rdx, rax
005A010D  48 8B CE                        mov rcx, rsi
005A0110  E8 4B 2A 00 00                  call 0x1405a2b60
005A0115  8B F8                           mov edi, eax
005A0117  85 C0                           test eax, eax
005A0119  78 68                           js 0x1405a0183
005A011B  EB 09                           jmp 0x1405a0126
005A011D  4C 8B 7D F7                     mov r15, qword ptr [rbp - 9]
005A0121  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
005A0126  44 8B 86 20 20 00 00            mov r8d, dword ptr [rsi + 0x2020]
005A012D  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
005A0132  44 88 64 24 28                  mov byte ptr [rsp + 0x28], r12b
005A0137  48 8B D6                        mov rdx, rsi
005A013A  49 8B CE                        mov rcx, r14
005A013D  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
005A0142  E8 41 65 E5 FF                  call 0x1403f6688
005A0147  8B F8                           mov edi, eax
005A0149  85 C0                           test eax, eax
005A014B  78 31                           js 0x1405a017e
005A014D  44 38 A3 D8 03 00 00            cmp byte ptr [rbx + 0x3d8], r12b
005A0154  74 28                           je 0x1405a017e
005A0156  44 8B 83 E0 03 00 00            mov r8d, dword ptr [rbx + 0x3e0]
005A015D  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
005A0162  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
005A0167  49 8B D7                        mov rdx, r15
005A016A  49 8B CE                        mov rcx, r14
005A016D  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
005A0172  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
005A0177  E8 0C 65 E5 FF                  call 0x1403f6688
005A017C  8B F8                           mov edi, eax
005A017E  4D 85 FF                        test r15, r15
005A0181  74 0A                           je 0x1405a018d
005A0183  33 D2                           xor edx, edx
005A0185  49 8B CF                        mov rcx, r15
005A0188  E8 E3 26 5E 00                  call 0x140b82870
005A018D  4D 85 ED                        test r13, r13
005A0190  74 0A                           je 0x1405a019c
005A0192  33 D2                           xor edx, edx
005A0194  49 8B CD                        mov rcx, r13
005A0197  E8 D4 26 5E 00                  call 0x140b82870
005A019C  48 8B CB                        mov rcx, rbx
005A019F  E8 44 5E E5 FF                  call 0x1403f5fe8
005A01A4  8B C7                           mov eax, edi
005A01A6  48 8B 4D 2F                     mov rcx, qword ptr [rbp + 0x2f]
005A01AA  48 33 CC                        xor rcx, rsp
005A01AD  E8 8E C4 10 00                  call 0x1406ac640
005A01B2  4C 8D 9C 24 F0 00 00 00         lea r11, [rsp + 0xf0]
005A01BA  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
005A01BE  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
005A01C2  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
005A01C6  49 8B E3                        mov rsp, r11
005A01C9  41 5F                           pop r15
005A01CB  41 5E                           pop r14
005A01CD  41 5D                           pop r13
005A01CF  41 5C                           pop r12
005A01D1  5D                              pop rbp
005A01D2  C3                              ret
005A01D3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopLiveDumpWriteDumpFileWithExtraPages(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_mE0;
    unsigned __int8 v_stack_mE6;
    unsigned __int8 v_stack_mE7;
    unsigned __int8 v_stack_mE8;
    unsigned __int8 v_stack_mF0;
    unsigned __int64 v_stack_mF8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (240);
    result = (*(unsigned __int64 *)(v_rip + 8826374)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 47) = result;
    v_r12 = 0;
    v_stack_mE0 = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 105) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 73) = 0;
    *(unsigned int *)(v_rsp - 95 - 117) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 113) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 89) = 0;
    *(unsigned int *)(v_rsp - 95 - 121) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 9) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 25) = *(unsigned __int64 *)(a1 + 1128);
    *(unsigned __int64 *)(v_rsp - 95 + 31) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 95 - 1) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 95 + 15) = v_xmm1;
    if (*(unsigned __int64 *)(a1 + 1128) != 0) goto loc_0059F99E;
loc_0059F994:
    goto loc_005A019C;
loc_0059F99E:
    *(unsigned __int64 *)(v_rsp - 95 - 33) = *(unsigned __int64 *)(a1 + 1136);
    if (*(unsigned __int64 *)(a1 + 1136) == 0) goto loc_0059F994;
    if ((*(unsigned __int8 *)(a1 + 984)) == 0) goto loc_0059F9C6;
    result = ((unsigned int)(*(unsigned int *)(a1 + 992))) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 560) + 8224));
    goto loc_0059F9CD;
loc_0059F9C6:
loc_0059F9CD:
    v_stack_mE0 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 560) + 8224);
    *(unsigned __int64 *)(v_rsp - 95 - 17) = *(unsigned __int64 *)(gs_base + (0 + 392));
    *(unsigned __int64 *)(v_rsp - 95 - 65) = 0;
    v_stack_mE8 = 0;
    result = *(unsigned __int64 *)(a1 + 624);
    if ((*(unsigned __int64 *)(a1 + 552)) != (*(unsigned __int64 *)(a1 + 624))) {
        result = *(unsigned __int64 *)(a1 + 616);
        a3 = 0;
        a1 = *(unsigned __int64 *)(a1 + 624);
        a3 = ((((unsigned __int8)(result)) & (31)) != 0) ? 1 : 0;
        result = (result) >> (5);
        a3 = (a3) + (result);
        a2 = 0;
        a3 = (a3) << (2);
        result = memset(a1, a2, a3, a4);
    }
    result = *(unsigned __int64 *)(a1 + 640);
    if ((*(unsigned __int64 *)(a1 + 624)) != (*(unsigned __int64 *)(a1 + 640))) {
        result = *(unsigned __int64 *)(a1 + 632);
        a3 = 0;
        a1 = *(unsigned __int64 *)(a1 + 640);
        a3 = ((((unsigned __int8)(result)) & (31)) != 0) ? 1 : 0;
        result = (result) >> (5);
        a3 = (a3) + (result);
        a2 = 0;
        a3 = (a3) << (2);
        result = memset(a1, a2, a3, a4);
    }
    *(unsigned __int64 *)(a1 + 728) = 0;
    v_stack_mF8 = v_rsp - 95 - 89;
    *(unsigned __int64 *)(a1 + 736) = 0;
    result = IopLiveDumpGetNtMergePages(a1, *(unsigned __int64 *)(a1 + 1136), v_rsp - 95 - 113, v_rsp - 95 - 121);
    *(unsigned __int64 *)(v_rsp - 95 - 81) = *(unsigned __int64 *)(a1 + 1136);
    v_stack_mF8 = v_rsp - 95 - 73;
    result = IopLiveDumpGetExtraMergePages(a1, *(unsigned __int64 *)(a1 + 1128), v_rsp - 95 - 105, v_rsp - 95 - 117);
    *(unsigned __int64 *)(v_rsp - 95 - 97) = *(unsigned __int64 *)(a1 + 1128);
    v_stack_mE7 = (unsigned __int8)(result);
loc_0059FAC3:
loc_0059FAC9:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 117))) != 0) goto loc_0059FAD7;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 121))) == 0) goto loc_0059FD66;
loc_0059FAD7:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 121))) != 0) goto loc_0059FAE6;
    *(unsigned __int64 *)(v_rsp - 95 - 81) = v_rsp - 95 - 41;
    goto loc_0059FAFC;
loc_0059FAE6:
    result = v_rsp - 95 - 41;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 117))) != 0) { result = *(unsigned __int64 *)(a1 + 1128); }
    *(unsigned __int64 *)(v_rsp - 95 - 97) = result;
loc_0059FAFC:
    result = IopLiveDumpCheckTermination(a1, *(unsigned __int64 *)(v_rsp - 95 - 17), result, *(unsigned __int64 *)(v_rsp - 95 - 81));
    if (sign_flag) goto loc_005A019C;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 117))) == 0) goto loc_0059FC07;
    if ((*(unsigned __int64 *)(result + (unsigned int)(*(unsigned int *)(v_rsp - 95 - 117)) - 1 * 8)) >= (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 81)))) goto loc_0059FC07;
    v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 117))) << (12));
    *(unsigned __int64 *)(v_rsp - 95 - 57) = *(unsigned __int64 *)(v_rsp - 95 - 105);
loc_0059FB3B:
    v_stack_mF8 = v_rsp - 95 - 73;
    v_stack_mE8 = (unsigned __int8)((unsigned __int8)(result));
    *(unsigned __int64 *)(v_rsp - 95 - 65) = *(unsigned __int64 *)(v_rsp - 95 - 73);
    result = IopLiveDumpGetExtraMergePages(a1, *(unsigned __int64 *)(v_rsp - 95 - 25), v_rsp - 95 - 105, v_rsp - 95 - 117);
    *(unsigned __int64 *)(v_rsp - 95 - 97) = *(unsigned __int64 *)(v_rsp - 95 - 25);
    v_stack_mE7 = (unsigned __int8)(result);
loc_0059FB74:
    v_stack_mF0 = 0;
    v_stack_mF8 = a1;
    result = IopLiveDumpWriteBuffer(*(unsigned __int64 *)(a1 + 64), *(unsigned __int64 *)(v_rsp - 95 - 57), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r15)))), v_stack_mE0);
    if (sign_flag) goto loc_005A019C;
    if (v_stack_mE8 == 0) goto loc_0059FAC9;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 760) + *(unsigned __int64 *)(v_rsp - 95 - 65) * 8) == 0) goto loc_0059FD1F;
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = MiFreePagesFromMdl(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 760) + *(unsigned __int64 *)(v_rsp - 95 - 65) * 8), a2, a3, a4);
    result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 760) + *(unsigned __int64 *)(v_rsp - 95 - 65) * 8), (unsigned int)(0x706D644CULL), a3, a4);
    goto loc_0059FD4E;
loc_0059FC07:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 121))) == 0) goto loc_0059FC62;
    if ((*(unsigned __int64 *)(a4 + (unsigned int)(*(unsigned int *)(v_rsp - 95 - 121)) - 1 * 8)) >= (*(unsigned __int64 *)(a3))) goto loc_0059FC62;
    *(unsigned __int64 *)(v_rsp - 95 - 57) = *(unsigned __int64 *)(v_rsp - 95 - 113);
    v_stack_mF8 = v_rsp - 95 - 89;
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 121))))) << (12));
    *(unsigned __int64 *)(v_rsp - 95 - 65) = *(unsigned __int64 *)(v_rsp - 95 - 89);
    v_stack_mE8 = 1;
    result = IopLiveDumpGetNtMergePages(a1, *(unsigned __int64 *)(v_rsp - 95 - 33), v_rsp - 95 - 113, v_rsp - 95 - 121);
    *(unsigned __int64 *)(v_rsp - 95 - 81) = *(unsigned __int64 *)(v_rsp - 95 - 33);
    goto loc_0059FB74;
loc_0059FC62:
    v_stack_mE6 = 0;
    if ((*(unsigned __int64 *)(v_rsp - 95 - 121)) >= (*(unsigned __int64 *)(v_rsp - 95 - 113))) goto loc_0059FC7C;
    *(unsigned __int64 *)(v_rsp - 95 - 57) = *(unsigned __int64 *)(v_rsp - 95 - 113);
    goto loc_0059FC8F;
loc_0059FC7C:
    *(unsigned __int64 *)(v_rsp - 95 - 57) = *(unsigned __int64 *)(v_rsp - 95 - 105);
    v_stack_mE6 = 1;
    if ((*(unsigned __int64 *)(v_rsp - 95 - 121)) != (*(unsigned __int64 *)(v_rsp - 95 - 113))) goto loc_0059FCFD;
loc_0059FC8F:
    v_r12 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 121))) + (-1));
    *(unsigned int *)(v_rsp - 95 - 121) = (unsigned int)(v_r12);
    if (condition_is_equal) goto loc_0059FCAA;
    result = (*(unsigned __int64 *)(v_rsp - 95 - 113)) + ((unsigned int)(0x1000ULL));
    a4 = (v_rsp - 95 - 121) + (8);
    *(unsigned __int64 *)(v_rsp - 95 - 113) = result;
    *(unsigned __int64 *)(v_rsp - 95 - 81) = a4;
    goto loc_0059FCEE;
loc_0059FCAA:
    v_stack_mF8 = v_rsp - 95 - 89;
    v_stack_mE8 = 1;
    *(unsigned __int64 *)(v_rsp - 95 - 65) = *(unsigned __int64 *)(v_rsp - 95 - 89);
    result = IopLiveDumpGetNtMergePages(a1, *(unsigned __int64 *)(v_rsp - 95 - 33), v_rsp - 95 - 113, v_rsp - 95 - 121);
    *(unsigned __int64 *)(v_rsp - 95 - 81) = *(unsigned __int64 *)(v_rsp - 95 - 33);
loc_0059FCEE:
    if (v_stack_mE6 == 0) goto loc_0059FB74;
loc_0059FCFD:
    v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 117))) + (-1));
    *(unsigned int *)(v_rsp - 95 - 117) = (unsigned int)(v_r15);
    if (condition_is_equal) goto loc_0059FB3B;
    a2 = (*(unsigned __int64 *)(v_rsp - 95 - 105)) + ((unsigned int)(0x1000ULL));
    a3 = (*(unsigned __int64 *)(v_rsp - 95 - 97)) + (8);
    *(unsigned __int64 *)(v_rsp - 95 - 105) = a2;
    *(unsigned __int64 *)(v_rsp - 95 - 97) = a3;
    goto loc_0059FB74;
loc_0059FD1F:
    if ((*(unsigned __int64 *)(a1 + 816)) != 0) goto loc_0059FD52;
    if ((*(unsigned __int64 *)(a1 + 856)) != 0) goto loc_0059FD52;
    result = MmFreeIndependentPages(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 752) + (unsigned int)((unsigned int)((unsigned int)(0x1000ULL))) * 8), (unsigned int)(*(unsigned int *)(v_rip + 8826002)), a3, v_rsp - 95 - 121);
loc_0059FD4E:
loc_0059FD52:
    result = 0;
    v_stack_mE8 = 0;
    goto loc_0059FAC3;
loc_0059FD66:
    v_r12 = 0;
    if ((*(unsigned __int8 *)(a1 + 984)) == 0) goto loc_0059FD91;
    result = ExAllocatePool2(v_r12 + 64, (unsigned int)(0x1000ULL), (unsigned int)(0x706D644CULL), v_rsp - 95 - 121);
    if (result == 0) goto loc_0059F994;
loc_0059FD91:
    *(unsigned int *)(v_rsp - 95 + 39) = 16;
    *(unsigned int *)(v_rsp - 95 + 31) = 0x706D7544ULL;
    *(unsigned int *)(v_rsp - 95 + 35) = 0x626F6C42ULL;
    *(unsigned int *)(v_rsp - 95 + 43) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8825264)));
    if ((*(unsigned __int8 *)(a1 + 984)) == 0) goto loc_0059FDC5;
    *(unsigned __int64 *)(result) = v_xmm0;
    goto loc_0059FDF0;
loc_0059FDC5:
    v_stack_mF0 = 1;
    v_stack_mF8 = a1;
    result = IopLiveDumpWriteBuffer(*(unsigned __int64 *)(a1 + 64), v_rsp - 95 + 31, 16, v_stack_mE0);
    if (sign_flag) goto loc_005A018D;
loc_0059FDF0:
    *(unsigned int *)(v_rsp - 95 - 1) = 32;
    *(unsigned int *)(v_rsp - 95 + 19) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 184)));
    *(unsigned __int64 *)(v_rsp - 95 + 3) = v_xmm0;
    *(unsigned int *)(v_rsp - 95 + 27) = 0;
    if ((*(unsigned __int8 *)(a1 + 984)) == 0) goto loc_0059FEBC;
    result = (unsigned int)(((unsigned int)(0xFE0ULL)) - (0));
    *(unsigned int *)(v_rsp - 95 + 23) = (unsigned int)(result);
    *(unsigned __int64 *)(0 + result * 1) = v_xmm0;
    *(unsigned __int64 *)(0 + result * 1 + 16) = v_xmm1;
loc_0059FE43:
    if ((unsigned int)((unsigned int)(0xFE0ULL) + 32) == 0) goto loc_0059FF04;
    v_stack_mF0 = 0;
    v_stack_mF8 = a1;
    result = IopLiveDumpWriteBuffer(*(unsigned __int64 *)(a1 + 64), result, (unsigned int)(0x1000ULL), v_stack_mE0);
    if (sign_flag) goto loc_005A018D;
    a2 = 0;
    v_r12 = (unsigned int)(((unsigned int)(0xFE0ULL) + 32) + (0xFFFFF000ULL));
    result = memset(result, a2, (unsigned int)(0x1000ULL), v_stack_mE0);
    if (32 == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 1))))) goto loc_0059FE43;
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 1))) - (32));
    if (((unsigned int)(v_rdi)) > ((unsigned int)((unsigned int)(0x1000ULL)))) { v_rdi = (unsigned int)((unsigned int)(0x1000ULL)); }
    a2 = (v_rsp - 95 - 1) + (32);
    result = memcpy(result, a2, (unsigned int)((unsigned int)(v_rdi)), v_stack_mE0);
    v_r15 = (unsigned int)((32) + ((unsigned int)(v_rdi)));
    goto loc_0059FE43;
loc_0059FEBC:
    v_stack_mF0 = 1;
    v_stack_mF8 = a1;
    a1 = (unsigned int)((v_stack_mE0 + 4127) & (0xFFFFF000ULL));
    a1 = (unsigned int)((a1) - ((unsigned int)(v_stack_mE0)));
    *(unsigned int *)(v_rsp - 95 + 23) = (unsigned int)(a1);
    result = IopLiveDumpWriteBuffer(*(unsigned __int64 *)(a1 + 64), v_rsp - 95 - 1, (unsigned int)((unsigned int)(v_r15)), v_stack_mE0);
    if (sign_flag) goto loc_005A018D;
    goto loc_0059FF0C;
loc_0059FF04:
    v_r12 = 0;
loc_0059FF0C:
    v_stack_mF0 = 0;
    v_stack_mF8 = a1;
    result = IopLiveDumpWriteBuffer(*(unsigned __int64 *)(a1 + 64), *(unsigned __int64 *)(a1 + 176), (unsigned int)(*(unsigned int *)(a1 + 184)), v_stack_mE0);
    if (sign_flag) goto loc_005A018D;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1088))) == 0) goto loc_0059FFB4;
    v_stack_mF0 = 0;
    *(unsigned int *)(v_rsp - 95 - 1) = (unsigned int)(v_r12 + 32);
    *(unsigned int *)(v_rsp - 95 + 19) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1088)));
    *(unsigned __int64 *)(v_rsp - 95 + 3) = v_xmm0;
    v_stack_mF8 = a1;
    result = IopLiveDumpWriteBuffer(*(unsigned __int64 *)(a1 + 64), v_rsp - 95 - 1, (unsigned int)((unsigned int)(v_r12 + 32)), v_stack_mE0);
    if (sign_flag) goto loc_005A018D;
    v_stack_mF0 = 0;
    v_stack_mF8 = a1;
    result = IopLiveDumpWriteBuffer(*(unsigned __int64 *)(a1 + 64), *(unsigned __int64 *)(a1 + 1080), (unsigned int)(*(unsigned int *)(a1 + 1088)), v_stack_mE0);
    if (sign_flag) goto loc_005A018D;
loc_0059FFB4:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1040))) == 0) goto loc_005A002D;
    v_stack_mF0 = 0;
    *(unsigned int *)(v_rsp - 95 - 1) = (unsigned int)(v_r12 + 32);
    *(unsigned int *)(v_rsp - 95 + 19) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1040)));
    *(unsigned __int64 *)(v_rsp - 95 + 3) = v_xmm0;
    v_stack_mF8 = a1;
    result = IopLiveDumpWriteBuffer(*(unsigned __int64 *)(a1 + 64), v_rsp - 95 - 1, (unsigned int)((unsigned int)(v_r12 + 32)), v_stack_mE0);
    if (sign_flag) goto loc_005A018D;
    v_stack_mF0 = 0;
    v_stack_mF8 = a1;
    result = IopLiveDumpWriteBuffer(*(unsigned __int64 *)(a1 + 64), *(unsigned __int64 *)(a1 + 1032), (unsigned int)(*(unsigned int *)(a1 + 1040)), v_stack_mE0);
    if (sign_flag) goto loc_005A018D;
loc_005A002D:
    result = *(unsigned __int64 *)(a1 + 624);
    if ((*(unsigned __int64 *)(a1 + 552)) != (*(unsigned __int64 *)(a1 + 624))) {
        a2 = a1 + 616;
        a1 = a1 + 544;
        result = RtlMergeBitMapsEx(a1, a2, (unsigned int)(*(unsigned int *)(a1 + 1040)), v_stack_mE0);
    }
    result = *(unsigned __int64 *)(a1 + 640);
    if ((*(unsigned __int64 *)(a1 + 624)) != (*(unsigned __int64 *)(a1 + 640))) {
        a2 = a1 + 632;
        a1 = a1 + 544;
        result = RtlMergeBitMapsEx(a1, a2, (unsigned int)(*(unsigned int *)(a1 + 1040)), v_stack_mE0);
    }
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 560) + 8192) = 0x504D4453ULL;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 560) + 8196) = 0x504D5544ULL;
    result = RtlNumberOfSetBitsEx(a1 + 544, a2, (unsigned int)(*(unsigned int *)(a1 + 1040)), v_stack_mE0);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 560) + 8232) = result;
    if ((*(unsigned __int8 *)(a1 + 984)) == 0) goto loc_005A00BA;
    a1 = (v_stack_mE0) - ((unsigned int)(*(unsigned int *)(a1 + 992)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 560) + 4000) = a1;
    goto loc_005A00C6;
loc_005A00BA:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 560) + 4000) = v_stack_mE0;
loc_005A00C6:
    if ((*(unsigned __int8 *)(a1 + 984)) == 0) goto loc_005A011D;
    v_stack_mE0 = (unsigned int)(*(unsigned int *)(a1 + 992));
    result = ExAllocatePool2(64, (unsigned int)(*(unsigned int *)(a1 + 992)), (unsigned int)(0x706D644CULL), v_stack_mE0);
    if (result != 0) goto loc_005A0103;
    goto loc_005A018D;
loc_005A0103:
    result = SecureDump_Get_SecureDumpHeader(*(unsigned __int64 *)(a1 + 560), result, (unsigned int)(*(unsigned int *)(a1 + 992)), v_stack_mE0);
    if (sign_flag) goto loc_005A0183;
    goto loc_005A0126;
loc_005A011D:
    v_stack_mE0 = 0;
loc_005A0126:
    v_stack_mF0 = 0;
    v_stack_mF8 = a1;
    result = IopLiveDumpWriteBuffer(*(unsigned __int64 *)(a1 + 64), *(unsigned __int64 *)(a1 + 560), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 560) + 8224)), v_stack_mE0);
    if (sign_flag) goto loc_005A017E;
    v_rdi = (unsigned int)((unsigned int)(result));
    if ((*(unsigned __int8 *)(a1 + 984)) != 0) {
        a3 = *(unsigned int *)(a1 + 992);
        a4 = v_stack_mE0;
        v_stack_mF0 = 1;
        a2 = *(unsigned __int64 *)(v_rsp - 95 - 9);
        a1 = *(unsigned __int64 *)(a1 + 64);
        v_stack_mF8 = a1;
        v_stack_mE0 = 0;
        result = IopLiveDumpWriteBuffer(a1, a2, a3, a4);
        v_rdi = (unsigned int)(result);
    }
    if (*(unsigned __int64 *)(v_rsp - 95 - 9) != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_rsp - 95 - 9);
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    result = IopLiveDumpFreeDumpBuffers(a1, a2, a3, a4);
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 47)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopLiveDumpWriteDumpFileWithExtraPages(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_mE0;
    uint8_t v_stack_mE6;
    uint8_t v_stack_mE7;
    uint8_t v_stack_mE8;
    uint8_t v_stack_mF0;
    uint64_t v_stack_mF8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (240);
    result = (*(uint64_t *)(v_rip + 0x86AE06)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x2F) = result;
    local_r12 = 0;
    v_stack_mE0 = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x69) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x49) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x75) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x71) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x59) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x79) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x9) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x19) = *(uint64_t *)(arg1 + 0x468);
    *(uint64_t *)(local_rsp - 0x5F + 0x1F) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x5F - 0x1) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x5F + 0xF) = v_xmm1;
    if (*(uint64_t *)(arg1 + 0x468) != 0) goto loc_0059F99E;
loc_0059F994:
    goto loc_005A019C;
loc_0059F99E:
    *(uint64_t *)(local_rsp - 0x5F - 0x21) = *(uint64_t *)(arg1 + 0x470);
    if (*(uint64_t *)(arg1 + 0x470) == 0) goto loc_0059F994;
    if ((*(uint8_t *)(arg1 + 0x3D8)) == 0) goto loc_0059F9C6;
    result = ((uint32_t)(*(uint32_t *)(arg1 + 0x3E0))) + (*(uint64_t *)(*(uint64_t *)(arg1 + 0x230) + 0x2020));
    goto loc_0059F9CD;
loc_0059F9C6:
loc_0059F9CD:
    v_stack_mE0 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x230) + 0x2020);
    *(uint64_t *)(local_rsp - 0x5F - 0x11) = *(uint64_t *)(gs_base + (0 + 0x188));
    *(uint64_t *)(local_rsp - 0x5F - 0x41) = 0;
    v_stack_mE8 = 0;
    result = *(uint64_t *)(arg1 + 0x270);
    if ((*(uint64_t *)(arg1 + 0x228)) != (*(uint64_t *)(arg1 + 0x270))) {
        result = *(uint64_t *)(arg1 + 0x268);
        a3 = 0;
        Arg1 = *(uint64_t *)(arg1 + 0x270);
        a3 = ((((uint8_t)(result)) & (31)) != 0) ? 1 : 0;
        result = (result) >> (5);
        a3 = (a3) + (result);
        Arg2 = 0;
        a3 = (a3) << (2);
        result = memset(Arg1, Arg2, a3, a4);
    }
    result = *(uint64_t *)(arg1 + 0x280);
    if ((*(uint64_t *)(arg1 + 0x270)) != (*(uint64_t *)(arg1 + 0x280))) {
        result = *(uint64_t *)(arg1 + 0x278);
        a3 = 0;
        Arg1 = *(uint64_t *)(arg1 + 0x280);
        a3 = ((((uint8_t)(result)) & (31)) != 0) ? 1 : 0;
        result = (result) >> (5);
        a3 = (a3) + (result);
        Arg2 = 0;
        a3 = (a3) << (2);
        result = memset(Arg1, Arg2, a3, a4);
    }
    *(uint64_t *)(arg1 + 0x2D8) = 0;
    v_stack_mF8 = local_rsp - 95 - 89;
    *(uint64_t *)(arg1 + 0x2E0) = 0;
    result = IopLiveDumpGetNtMergePages(Arg1, *(uint64_t *)(arg1 + 0x470), local_rsp - 95 - 113, local_rsp - 95 - 121);
    *(uint64_t *)(local_rsp - 0x5F - 0x51) = *(uint64_t *)(arg1 + 0x470);
    v_stack_mF8 = local_rsp - 95 - 73;
    result = IopLiveDumpGetExtraMergePages(Arg1, *(uint64_t *)(arg1 + 0x468), local_rsp - 95 - 105, local_rsp - 95 - 117);
    *(uint64_t *)(local_rsp - 0x5F - 0x61) = *(uint64_t *)(arg1 + 0x468);
    v_stack_mE7 = (uint8_t)(result);
loc_0059FAC3:
loc_0059FAC9:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x75))) != 0) goto loc_0059FAD7;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x79))) == 0) goto loc_0059FD66;
loc_0059FAD7:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x79))) != 0) goto loc_0059FAE6;
    *(uint64_t *)(local_rsp - 0x5F - 0x51) = local_rsp - 95 - 41;
    goto loc_0059FAFC;
loc_0059FAE6:
    result = local_rsp - 95 - 41;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x75))) != 0) { result = *(uint64_t *)(arg1 + 0x468); }
    *(uint64_t *)(local_rsp - 0x5F - 0x61) = result;
loc_0059FAFC:
    result = IopLiveDumpCheckTermination(Arg1, *(uint64_t *)(local_rsp - 0x5F - 0x11), result, *(uint64_t *)(local_rsp - 0x5F - 0x51));
    if (sign_flag) goto loc_005A019C;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x75))) == 0) goto loc_0059FC07;
    if ((*(uint64_t *)(result + (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x75)) - 0x1 * 8)) >= (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x51)))) goto loc_0059FC07;
    local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x75))) << (12));
    *(uint64_t *)(local_rsp - 0x5F - 0x39) = *(uint64_t *)(local_rsp - 0x5F - 0x69);
loc_0059FB3B:
    v_stack_mF8 = local_rsp - 95 - 73;
    v_stack_mE8 = (uint8_t)((uint8_t)(result));
    *(uint64_t *)(local_rsp - 0x5F - 0x41) = *(uint64_t *)(local_rsp - 0x5F - 0x49);
    result = IopLiveDumpGetExtraMergePages(Arg1, *(uint64_t *)(local_rsp - 0x5F - 0x19), local_rsp - 95 - 105, local_rsp - 95 - 117);
    *(uint64_t *)(local_rsp - 0x5F - 0x61) = *(uint64_t *)(local_rsp - 0x5F - 0x19);
    v_stack_mE7 = (uint8_t)(result);
loc_0059FB74:
    v_stack_mF0 = 0;
    v_stack_mF8 = Arg1;
    result = IopLiveDumpWriteBuffer(*(uint64_t *)(arg1 + 0x40), *(uint64_t *)(local_rsp - 0x5F - 0x39), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r15)))), v_stack_mE0);
    if (sign_flag) goto loc_005A019C;
    if (v_stack_mE8 == 0) goto loc_0059FAC9;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x2F8) + *(uint64_t *)(local_rsp - 0x5F - 0x41) * 8) == 0) goto loc_0059FD1F;
    a4 = 0;
    a3 = 0;
    Arg2 = 0;
    result = MiFreePagesFromMdl(*(uint64_t *)(*(uint64_t *)(arg1 + 0x2F8) + *(uint64_t *)(local_rsp - 0x5F - 0x41) * 8), Arg2, a3, a4);
    result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(arg1 + 0x2F8) + *(uint64_t *)(local_rsp - 0x5F - 0x41) * 8), (uint32_t)(0x706D644CULL), a3, a4);
    goto loc_0059FD4E;
loc_0059FC07:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x79))) == 0) goto loc_0059FC62;
    if ((*(uint64_t *)(a4 + (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x79)) - 0x1 * 8)) >= (*(uint64_t *)(a3))) goto loc_0059FC62;
    *(uint64_t *)(local_rsp - 0x5F - 0x39) = *(uint64_t *)(local_rsp - 0x5F - 0x71);
    v_stack_mF8 = local_rsp - 95 - 89;
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x79))))) << (12));
    *(uint64_t *)(local_rsp - 0x5F - 0x41) = *(uint64_t *)(local_rsp - 0x5F - 0x59);
    v_stack_mE8 = 1;
    result = IopLiveDumpGetNtMergePages(Arg1, *(uint64_t *)(local_rsp - 0x5F - 0x21), local_rsp - 95 - 113, local_rsp - 95 - 121);
    *(uint64_t *)(local_rsp - 0x5F - 0x51) = *(uint64_t *)(local_rsp - 0x5F - 0x21);
    goto loc_0059FB74;
loc_0059FC62:
    v_stack_mE6 = 0;
    if ((*(uint64_t *)(local_rsp - 0x5F - 0x79)) >= (*(uint64_t *)(local_rsp - 0x5F - 0x71))) goto loc_0059FC7C;
    *(uint64_t *)(local_rsp - 0x5F - 0x39) = *(uint64_t *)(local_rsp - 0x5F - 0x71);
    goto loc_0059FC8F;
loc_0059FC7C:
    *(uint64_t *)(local_rsp - 0x5F - 0x39) = *(uint64_t *)(local_rsp - 0x5F - 0x69);
    v_stack_mE6 = 1;
    if ((*(uint64_t *)(local_rsp - 0x5F - 0x79)) != (*(uint64_t *)(local_rsp - 0x5F - 0x71))) goto loc_0059FCFD;
loc_0059FC8F:
    local_r12 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x79))) + (-1));
    *(uint32_t *)(local_rsp - 0x5F - 0x79) = (uint32_t)(local_r12);
    if (condition_is_equal) goto loc_0059FCAA;
    result = (*(uint64_t *)(local_rsp - 0x5F - 0x71)) + ((uint32_t)(0x1000ULL));
    a4 = (local_rsp - 95 - 121) + (8);
    *(uint64_t *)(local_rsp - 0x5F - 0x71) = result;
    *(uint64_t *)(local_rsp - 0x5F - 0x51) = a4;
    goto loc_0059FCEE;
loc_0059FCAA:
    v_stack_mF8 = local_rsp - 95 - 89;
    v_stack_mE8 = 1;
    *(uint64_t *)(local_rsp - 0x5F - 0x41) = *(uint64_t *)(local_rsp - 0x5F - 0x59);
    result = IopLiveDumpGetNtMergePages(Arg1, *(uint64_t *)(local_rsp - 0x5F - 0x21), local_rsp - 95 - 113, local_rsp - 95 - 121);
    *(uint64_t *)(local_rsp - 0x5F - 0x51) = *(uint64_t *)(local_rsp - 0x5F - 0x21);
loc_0059FCEE:
    if (v_stack_mE6 == 0) goto loc_0059FB74;
loc_0059FCFD:
    local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x75))) + (-1));
    *(uint32_t *)(local_rsp - 0x5F - 0x75) = (uint32_t)(local_r15);
    if (condition_is_equal) goto loc_0059FB3B;
    Arg2 = (*(uint64_t *)(local_rsp - 0x5F - 0x69)) + ((uint32_t)(0x1000ULL));
    a3 = (*(uint64_t *)(local_rsp - 0x5F - 0x61)) + (8);
    *(uint64_t *)(local_rsp - 0x5F - 0x69) = Arg2;
    *(uint64_t *)(local_rsp - 0x5F - 0x61) = a3;
    goto loc_0059FB74;
loc_0059FD1F:
    if ((*(uint64_t *)(arg1 + 0x330)) != 0) goto loc_0059FD52;
    if ((*(uint64_t *)(arg1 + 0x358)) != 0) goto loc_0059FD52;
    result = MmFreeIndependentPages(*(uint64_t *)(*(uint64_t *)(arg1 + 0x2F0) + (uint32_t)((uint32_t)((uint32_t)(0x1000ULL))) * 8), (uint32_t)(*(uint32_t *)(v_rip + 0x86AC92)), a3, local_rsp - 95 - 121);
loc_0059FD4E:
loc_0059FD52:
    result = 0;
    v_stack_mE8 = 0;
    goto loc_0059FAC3;
loc_0059FD66:
    local_r12 = 0;
    if ((*(uint8_t *)(arg1 + 0x3D8)) == 0) goto loc_0059FD91;
    result = ExAllocatePool2(local_r12 + 64, (uint32_t)(0x1000ULL), (uint32_t)(0x706D644CULL), local_rsp - 95 - 121);
    if (result == 0) goto loc_0059F994;
loc_0059FD91:
    *(uint32_t *)(local_rsp - 0x5F + 0x27) = 16;
    *(uint32_t *)(local_rsp - 0x5F + 0x1F) = 0x706D7544ULL;
    *(uint32_t *)(local_rsp - 0x5F + 0x23) = 0x626F6C42ULL;
    *(uint32_t *)(local_rsp - 0x5F + 0x2B) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x86A9B0)));
    if ((*(uint8_t *)(arg1 + 0x3D8)) == 0) goto loc_0059FDC5;
    *(uint64_t *)(result) = v_xmm0;
    goto loc_0059FDF0;
loc_0059FDC5:
    v_stack_mF0 = 1;
    v_stack_mF8 = Arg1;
    result = IopLiveDumpWriteBuffer(*(uint64_t *)(arg1 + 0x40), local_rsp - 95 + 31, 16, v_stack_mE0);
    if (sign_flag) goto loc_005A018D;
loc_0059FDF0:
    *(uint32_t *)(local_rsp - 0x5F - 0x1) = 32;
    *(uint32_t *)(local_rsp - 0x5F + 0x13) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB8)));
    *(uint64_t *)(local_rsp - 0x5F + 0x3) = v_xmm0;
    *(uint32_t *)(local_rsp - 0x5F + 0x1B) = 0;
    if ((*(uint8_t *)(arg1 + 0x3D8)) == 0) goto loc_0059FEBC;
    result = (uint32_t)(((uint32_t)(0xFE0ULL)) - (0));
    *(uint32_t *)(local_rsp - 0x5F + 0x17) = (uint32_t)(result);
    *(uint64_t *)(0 + result * 1) = v_xmm0;
    *(uint64_t *)(0 + result * 1 + 0x10) = v_xmm1;
loc_0059FE43:
    if ((uint32_t)((uint32_t)(0xFE0ULL) + 32) == 0) goto loc_0059FF04;
    v_stack_mF0 = 0;
    v_stack_mF8 = Arg1;
    result = IopLiveDumpWriteBuffer(*(uint64_t *)(arg1 + 0x40), result, (uint32_t)(0x1000ULL), v_stack_mE0);
    if (sign_flag) goto loc_005A018D;
    Arg2 = 0;
    local_r12 = (uint32_t)(((uint32_t)(0xFE0ULL) + 32) + (0xFFFFF000ULL));
    result = memset(result, Arg2, (uint32_t)(0x1000ULL), v_stack_mE0);
    if (32 == ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x1))))) goto loc_0059FE43;
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x1))) - (32));
    if (((uint32_t)(local_rdi)) > ((uint32_t)((uint32_t)(0x1000ULL)))) { local_rdi = (uint32_t)((uint32_t)(0x1000ULL)); }
    Arg2 = (local_rsp - 95 - 1) + (32);
    result = memcpy(result, Arg2, (uint32_t)((uint32_t)(local_rdi)), v_stack_mE0);
    local_r15 = (uint32_t)((32) + ((uint32_t)(local_rdi)));
    goto loc_0059FE43;
loc_0059FEBC:
    v_stack_mF0 = 1;
    v_stack_mF8 = Arg1;
    Arg1 = (uint32_t)((v_stack_mE0 + 4127) & (0xFFFFF000ULL));
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(v_stack_mE0)));
    *(uint32_t *)(local_rsp - 0x5F + 0x17) = (uint32_t)(Arg1);
    result = IopLiveDumpWriteBuffer(*(uint64_t *)(arg1 + 0x40), local_rsp - 95 - 1, (uint32_t)((uint32_t)(local_r15)), v_stack_mE0);
    if (sign_flag) goto loc_005A018D;
    goto loc_0059FF0C;
loc_0059FF04:
    local_r12 = 0;
loc_0059FF0C:
    v_stack_mF0 = 0;
    v_stack_mF8 = Arg1;
    result = IopLiveDumpWriteBuffer(*(uint64_t *)(arg1 + 0x40), *(uint64_t *)(arg1 + 0xB0), (uint32_t)(*(uint32_t *)(arg1 + 0xB8)), v_stack_mE0);
    if (sign_flag) goto loc_005A018D;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x440))) == 0) goto loc_0059FFB4;
    v_stack_mF0 = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x1) = (uint32_t)(local_r12 + 32);
    *(uint32_t *)(local_rsp - 0x5F + 0x13) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x440)));
    *(uint64_t *)(local_rsp - 0x5F + 0x3) = v_xmm0;
    v_stack_mF8 = Arg1;
    result = IopLiveDumpWriteBuffer(*(uint64_t *)(arg1 + 0x40), local_rsp - 95 - 1, (uint32_t)((uint32_t)(local_r12 + 32)), v_stack_mE0);
    if (sign_flag) goto loc_005A018D;
    v_stack_mF0 = 0;
    v_stack_mF8 = Arg1;
    result = IopLiveDumpWriteBuffer(*(uint64_t *)(arg1 + 0x40), *(uint64_t *)(arg1 + 0x438), (uint32_t)(*(uint32_t *)(arg1 + 0x440)), v_stack_mE0);
    if (sign_flag) goto loc_005A018D;
loc_0059FFB4:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x410))) == 0) goto loc_005A002D;
    v_stack_mF0 = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x1) = (uint32_t)(local_r12 + 32);
    *(uint32_t *)(local_rsp - 0x5F + 0x13) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x410)));
    *(uint64_t *)(local_rsp - 0x5F + 0x3) = v_xmm0;
    v_stack_mF8 = Arg1;
    result = IopLiveDumpWriteBuffer(*(uint64_t *)(arg1 + 0x40), local_rsp - 95 - 1, (uint32_t)((uint32_t)(local_r12 + 32)), v_stack_mE0);
    if (sign_flag) goto loc_005A018D;
    v_stack_mF0 = 0;
    v_stack_mF8 = Arg1;
    result = IopLiveDumpWriteBuffer(*(uint64_t *)(arg1 + 0x40), *(uint64_t *)(arg1 + 0x408), (uint32_t)(*(uint32_t *)(arg1 + 0x410)), v_stack_mE0);
    if (sign_flag) goto loc_005A018D;
loc_005A002D:
    result = *(uint64_t *)(arg1 + 0x270);
    if ((*(uint64_t *)(arg1 + 0x228)) != (*(uint64_t *)(arg1 + 0x270))) {
        Arg2 = Arg1 + 616;
        Arg1 = Arg1 + 544;
        result = RtlMergeBitMapsEx(Arg1, Arg2, (uint32_t)(*(uint32_t *)(arg1 + 0x410)), v_stack_mE0);
    }
    result = *(uint64_t *)(arg1 + 0x280);
    if ((*(uint64_t *)(arg1 + 0x270)) != (*(uint64_t *)(arg1 + 0x280))) {
        Arg2 = Arg1 + 632;
        Arg1 = Arg1 + 544;
        result = RtlMergeBitMapsEx(Arg1, Arg2, (uint32_t)(*(uint32_t *)(arg1 + 0x410)), v_stack_mE0);
    }
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x230) + 0x2000) = 0x504D4453ULL;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x230) + 0x2004) = 0x504D5544ULL;
    result = RtlNumberOfSetBitsEx(Arg1 + 544, Arg2, (uint32_t)(*(uint32_t *)(arg1 + 0x410)), v_stack_mE0);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x230) + 0x2028) = result;
    if ((*(uint8_t *)(arg1 + 0x3D8)) == 0) goto loc_005A00BA;
    Arg1 = (v_stack_mE0) - ((uint32_t)(*(uint32_t *)(arg1 + 0x3E0)));
    *(void **)(*(uint64_t *)(arg1 + 0x230) + 0xFA0) = Arg1;
    goto loc_005A00C6;
loc_005A00BA:
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x230) + 0xFA0) = v_stack_mE0;
loc_005A00C6:
    if ((*(uint8_t *)(arg1 + 0x3D8)) == 0) goto loc_005A011D;
    v_stack_mE0 = (uint32_t)(*(uint32_t *)(arg1 + 0x3E0));
    result = ExAllocatePool2(64, (uint32_t)(*(uint32_t *)(arg1 + 0x3E0)), (uint32_t)(0x706D644CULL), v_stack_mE0);
    if (result != 0) goto loc_005A0103;
    goto loc_005A018D;
loc_005A0103:
    result = SecureDump_Get_SecureDumpHeader(*(uint64_t *)(arg1 + 0x230), result, (uint32_t)(*(uint32_t *)(arg1 + 0x3E0)), v_stack_mE0);
    if (sign_flag) goto loc_005A0183;
    goto loc_005A0126;
loc_005A011D:
    v_stack_mE0 = 0;
loc_005A0126:
    v_stack_mF0 = 0;
    v_stack_mF8 = Arg1;
    result = IopLiveDumpWriteBuffer(*(uint64_t *)(arg1 + 0x40), *(uint64_t *)(arg1 + 0x230), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x230) + 0x2020)), v_stack_mE0);
    if (sign_flag) goto loc_005A017E;
    local_rdi = (uint32_t)((uint32_t)(result));
    if ((*(uint8_t *)(arg1 + 0x3D8)) != 0) {
        a3 = *(uint32_t *)(arg1 + 0x3E0);
        a4 = v_stack_mE0;
        v_stack_mF0 = 1;
        Arg2 = *(uint64_t *)(local_rsp - 0x5F - 0x9);
        Arg1 = *(uint64_t *)(arg1 + 0x40);
        v_stack_mF8 = Arg1;
        v_stack_mE0 = 0;
        result = IopLiveDumpWriteBuffer(Arg1, Arg2, a3, a4);
        local_rdi = (uint32_t)(result);
    }
    if (*(uint64_t *)(local_rsp - 0x5F - 0x9) != 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(local_rsp - 0x5F - 0x9);
        result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
    }
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
    }
    result = IopLiveDumpFreeDumpBuffers(Arg1, Arg2, a3, a4);
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x2F)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, a4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0xA0` | `128` | `R` |
| `Arg1` | `+ 0xB0` | `64` | `R` |
| `Arg1` | `+ 0xB8` | `32` | `R` |
| `Arg1` | `+ 0x220` | `64` | `R` |
| `Arg1` | `+ 0x228` | `64` | `R` |
| `Arg1` | `+ 0x230` | `64` | `R` |
| `Arg1` | `+ 0x268` | `64` | `R` |
| `Arg1` | `+ 0x270` | `64` | `R` |
| `Arg1` | `+ 0x278` | `64` | `R` |
| `Arg1` | `+ 0x280` | `64` | `R` |
| `Arg1` | `+ 0x2D8` | `64` | `W` |
| `Arg1` | `+ 0x2E0` | `64` | `W` |
| `Arg1` | `+ 0x2F0` | `64` | `R` |
| `Arg1` | `+ 0x2F8` | `64` | `R` |
| `Arg1` | `+ 0x330` | `64` | `R` |
| `Arg1` | `+ 0x358` | `64` | `R` |
| `Arg1` | `+ 0x3D8` | `8` | `R` |
| `Arg1` | `+ 0x3E0` | `32` | `R` |
| `Arg1` | `+ 0x3F8` | `128` | `R` |
| `Arg1` | `+ 0x408` | `64` | `R` |
| `Arg1` | `+ 0x410` | `32` | `R` |
| `Arg1` | `+ 0x428` | `128` | `R` |
| `Arg1` | `+ 0x438` | `64` | `R` |
| `Arg1` | `+ 0x440` | `32` | `R` |
| `Arg1` | `+ 0x468` | `64` | `R` |
| `Arg1` | `+ 0x470` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0059F910&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
