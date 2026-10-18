# ObGetObjectInformation

- RVA: `0x009DADE0`–`0x009DB45C` (길이 `1,660` bytes)
- VA: `0x00000001409DADE0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A33EC`
- 디코드: `419`개 명령, `1,660/1,660` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x009DAE2C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009DAE73` → [ObpCreateTypeArray](ObpCreateTypeArray_function_009DB4B4.md) (function, `0x009DB4B4`)
- `0x009DAE90` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009DAED5` → [ObpCreateTypeArray](ObpCreateTypeArray_function_009DB4B4.md) (function, `0x009DB4B4`)
- `0x009DAF82` → [ObpDestroyTypeArray](ObpDestroyTypeArray_function_009DB464.md) (function, `0x009DB464`)
- `0x009DB00C` → [ObQueryTypeName](../92/ObQueryTypeName_function_009204B8.md) (function, `0x009204B8`)
- `0x009DB10B` → [OBJECT_HEADER_TO_QUOTA_INFO](../../text/40/OBJECT_HEADER_TO_QUOTA_INFO_function_0040EA80.md) (function, `0x0040EA80`)
- `0x009DB133` → [OBJECT_HEADER_TO_PROCESS_INFO](../../text/4B/OBJECT_HEADER_TO_PROCESS_INFO_function_004B1364.md) (function, `0x004B1364`)
- `0x009DB1D3` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009DB23E` → [ObQueryNameStringMode](../8A/ObQueryNameStringMode_function_008A7ED0.md) (function, `0x008A7ED0`)
- `0x009DB287` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009DB2AB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009DB2EA` → [ObQueryNameStringMode](../8A/ObQueryNameStringMode_function_008A7ED0.md) (function, `0x008A7ED0`)
- `0x009DB35A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009DB3C0` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x009DB3F4` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x009DB42C` → [ObpDestroyTypeArray](ObpDestroyTypeArray_function_009DB464.md) (function, `0x009DB464`)
- `0x009DB436` → [ObpDestroyTypeArray](ObpDestroyTypeArray_function_009DB464.md) (function, `0x009DB464`)
- `0x009DB443` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [ExpGetObjectInformation](../7C/ExpGetObjectInformation_function_007C3B74.md) at `0x007C3BE7`

### Static image references
- `0x009DAE6C` → RVA `0x00F0F660` (`.data`; read)
- `0x009DB172` → RVA `0x00FC6AE0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **11**
  - `0x009DAE2C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009DAE90` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009DB10B` → [OBJECT_HEADER_TO_QUOTA_INFO](../../text/40/OBJECT_HEADER_TO_QUOTA_INFO_function_0040EA80.md) (`PAGE` → `.text`)
  - `0x009DB133` → [OBJECT_HEADER_TO_PROCESS_INFO](../../text/4B/OBJECT_HEADER_TO_PROCESS_INFO_function_004B1364.md) (`PAGE` → `.text`)
  - `0x009DB1D3` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009DB287` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009DB2AB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009DB35A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009DB3C0` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x009DB3F4` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x009DB443` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009DADE0  48 8B C4                        mov rax, rsp
009DADE3  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
009DADE7  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
009DADEB  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
009DADEF  89 48 08                        mov dword ptr [rax + 8], ecx
009DADF2  53                              push rbx
009DADF3  56                              push rsi
009DADF4  57                              push rdi
009DADF5  41 54                           push r12
009DADF7  41 55                           push r13
009DADF9  41 56                           push r14
009DADFB  41 57                           push r15
009DADFD  48 81 EC C0 00 00 00            sub rsp, 0xc0
009DAE04  33 FF                           xor edi, edi
009DAE06  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
009DAE0A  44 8B FF                        mov r15d, edi
009DAE0D  44 8B EF                        mov r13d, edi
009DAE10  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
009DAE15  B8 18 02 00 00                  mov eax, 0x218
009DAE1A  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
009DAE1F  41 B8 4F 62 41 72               mov r8d, 0x7241624f
009DAE25  8B D0                           mov edx, eax
009DAE27  B9 00 01 00 00                  mov ecx, 0x100
009DAE2C  E8 BF 72 1A 00                  call 0x140b820f0
009DAE31  4C 8B E0                        mov r12, rax
009DAE34  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
009DAE3C  48 85 C0                        test rax, rax
009DAE3F  75 19                           jne 0x1409dae5a
009DAE41  B8 9A 00 00 C0                  mov eax, 0xc000009a
009DAE46  48 81 C4 C0 00 00 00            add rsp, 0xc0
009DAE4D  41 5F                           pop r15
009DAE4F  41 5E                           pop r14
009DAE51  41 5D                           pop r13
009DAE53  41 5C                           pop r12
009DAE55  5F                              pop rdi
009DAE56  5E                              pop rsi
009DAE57  5B                              pop rbx
009DAE58  C3                              ret
009DAE59  CC                              int3
009DAE5A  49 8B DC                        mov rbx, r12
009DAE5D  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
009DAE62  44 8B F7                        mov r14d, edi
009DAE65  8B F7                           mov esi, edi
009DAE67  48 89 7C 24 68                  mov qword ptr [rsp + 0x68], rdi
009DAE6C  48 8B 0D ED 47 53 00            mov rcx, qword ptr [rip + 0x5347ed]
009DAE73  E8 3C 06 00 00                  call 0x1409db4b4
009DAE78  48 8B C8                        mov rcx, rax
009DAE7B  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
009DAE80  45 33 C0                        xor r8d, r8d
009DAE83  48 85 C0                        test rax, rax
009DAE86  75 14                           jne 0x1409dae9c
009DAE88  BA 4F 62 41 72                  mov edx, 0x7241624f
009DAE8D  49 8B CC                        mov rcx, r12
009DAE90  E8 DB 79 1A 00                  call 0x140b82870
009DAE95  B8 01 00 00 C0                  mov eax, 0xc0000001
009DAE9A  EB AA                           jmp 0x1409dae46
009DAE9C  41 8B D0                        mov edx, r8d
009DAE9F  89 54 24 44                     mov dword ptr [rsp + 0x44], edx
009DAEA3  3B 11                           cmp edx, dword ptr [rcx]
009DAEA5  0F 83 6A 05 00 00               jae 0x1409db415
009DAEAB  8B C2                           mov eax, edx
009DAEAD  48 8B 4C C1 08                  mov rcx, qword ptr [rcx + rax*8 + 8]
009DAEB2  48 85 C9                        test rcx, rcx
009DAEB5  75 05                           jne 0x1409daebc
009DAEB7  E9 DF 00 00 00                  jmp 0x1409daf9b
009DAEBC  48 83 C1 50                     add rcx, 0x50
009DAEC0  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
009DAEC5  48 8B 05 94 47 53 00            mov rax, qword ptr [rip + 0x534794]
009DAECC  48 3B C8                        cmp rcx, rax
009DAECF  0F 84 C6 00 00 00               je 0x1409daf9b
009DAED5  E8 DA 05 00 00                  call 0x1409db4b4
009DAEDA  4C 8B E8                        mov r13, rax
009DAEDD  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
009DAEE2  45 33 C0                        xor r8d, r8d
009DAEE5  48 85 C0                        test rax, rax
009DAEE8  0F 84 A9 00 00 00               je 0x1409daf97
009DAEEE  B2 01                           mov dl, 1
009DAEF0  88 54 24 38                     mov byte ptr [rsp + 0x38], dl
009DAEF4  41 8B C0                        mov eax, r8d
009DAEF7  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
009DAEFB  41 3B 45 00                     cmp eax, dword ptr [r13]
009DAEFF  73 7E                           jae 0x1409daf7f
009DAF01  8B C8                           mov ecx, eax
009DAF03  49 8B 4C CD 08                  mov rcx, qword ptr [r13 + rcx*8 + 8]
009DAF08  48 89 8C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rcx
009DAF10  48 85 C9                        test rcx, rcx
009DAF13  75 05                           jne 0x1409daf1a
009DAF15  E9 F4 04 00 00                  jmp 0x1409db40e
009DAF1A  4C 8D 49 20                     lea r9, [rcx + 0x20]
009DAF1E  4C 89 8C 24 98 00 00 00         mov qword ptr [rsp + 0x98], r9
009DAF26  4D 8D 59 30                     lea r11, [r9 + 0x30]
009DAF2A  4C 89 9C 24 88 00 00 00         mov qword ptr [rsp + 0x88], r11
009DAF32  84 D2                           test dl, dl
009DAF34  0F 84 D6 02 00 00               je 0x1409db210
009DAF3A  44 88 44 24 38                  mov byte ptr [rsp + 0x38], r8b
009DAF3F  8B 8C 24 18 01 00 00            mov ecx, dword ptr [rsp + 0x118]
009DAF46  48 85 FF                        test rdi, rdi
009DAF49  74 06                           je 0x1409daf51
009DAF4B  3B F1                           cmp esi, ecx
009DAF4D  73 02                           jae 0x1409daf51
009DAF4F  89 37                           mov dword ptr [rdi], esi
009DAF51  8B FE                           mov edi, esi
009DAF53  48 03 BC 24 10 01 00 00         add rdi, qword ptr [rsp + 0x110]
009DAF5B  48 89 7C 24 68                  mov qword ptr [rsp + 0x68], rdi
009DAF60  48 89 BC 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rdi
009DAF68  83 C6 30                        add esi, 0x30
009DAF6B  89 74 24 3C                     mov dword ptr [rsp + 0x3c], esi
009DAF6F  83 FE 30                        cmp esi, 0x30
009DAF72  73 33                           jae 0x1409dafa7
009DAF74  41 BE 95 00 00 C0               mov r14d, 0xc0000095
009DAF7A  44 89 74 24 34                  mov dword ptr [rsp + 0x34], r14d
009DAF7F  49 8B CD                        mov rcx, r13
009DAF82  E8 DD 04 00 00                  call 0x1409db464
009DAF87  45 33 C0                        xor r8d, r8d
009DAF8A  45 8B E8                        mov r13d, r8d
009DAF8D  4C 89 44 24 70                  mov qword ptr [rsp + 0x70], r8
009DAF92  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
009DAF97  8B 54 24 44                     mov edx, dword ptr [rsp + 0x44]
009DAF9B  FF C2                           inc edx
009DAF9D  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
009DAFA2  E9 F8 FE FF FF                  jmp 0x1409dae9f
009DAFA7  3B F1                           cmp esi, ecx
009DAFA9  72 08                           jb 0x1409dafb3
009DAFAB  41 BE 04 00 00 C0               mov r14d, 0xc0000004
009DAFB1  EB C7                           jmp 0x1409daf7a
009DAFB3  44 89 07                        mov dword ptr [rdi], r8d
009DAFB6  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
009DAFBB  8B 42 2C                        mov eax, dword ptr [rdx + 0x2c]
009DAFBE  89 47 04                        mov dword ptr [rdi + 4], eax
009DAFC1  8B 42 30                        mov eax, dword ptr [rdx + 0x30]
009DAFC4  89 47 08                        mov dword ptr [rdi + 8], eax
009DAFC7  0F B6 42 28                     movzx eax, byte ptr [rdx + 0x28]
009DAFCB  89 47 0C                        mov dword ptr [rdi + 0xc], eax
009DAFCE  8B 42 48                        mov eax, dword ptr [rdx + 0x48]
009DAFD1  89 47 10                        mov dword ptr [rdi + 0x10], eax
009DAFD4  0F 10 42 4C                     movups xmm0, xmmword ptr [rdx + 0x4c]
009DAFD8  F3 0F 7F 47 14                  movdqu xmmword ptr [rdi + 0x14], xmm0
009DAFDD  8B 42 5C                        mov eax, dword ptr [rdx + 0x5c]
009DAFE0  89 47 24                        mov dword ptr [rdi + 0x24], eax
009DAFE3  8B 42 64                        mov eax, dword ptr [rdx + 0x64]
009DAFE6  89 47 28                        mov dword ptr [rdi + 0x28], eax
009DAFE9  8A 42 42                        mov al, byte ptr [rdx + 0x42]
009DAFEC  C0 E8 03                        shr al, 3
009DAFEF  24 01                           and al, 1
009DAFF1  88 47 2C                        mov byte ptr [rdi + 0x2c], al
009DAFF4  44 8B C1                        mov r8d, ecx
009DAFF7  44 2B C6                        sub r8d, esi
009DAFFA  33 C9                           xor ecx, ecx
009DAFFC  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
009DB000  48 8D 57 30                     lea rdx, [rdi + 0x30]
009DB004  4C 8D 4C 24 30                  lea r9, [rsp + 0x30]
009DB009  49 8B CB                        mov rcx, r11
009DB00C  E8 A7 54 F4 FF                  call 0x1409204b8
009DB011  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
009DB015  8B 4C 24 30                     mov ecx, dword ptr [rsp + 0x30]
009DB019  83 C1 07                        add ecx, 7
009DB01C  83 E1 F8                        and ecx, 0xfffffff8
009DB01F  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
009DB023  45 33 C0                        xor r8d, r8d
009DB026  85 C0                           test eax, eax
009DB028  78 26                           js 0x1409db050
009DB02A  66 83 E9 10                     sub cx, 0x10
009DB02E  66 89 4F 32                     mov word ptr [rdi + 0x32], cx
009DB032  48 8B 84 24 08 01 00 00         mov rax, qword ptr [rsp + 0x108]
009DB03A  48 2B 84 24 10 01 00 00         sub rax, qword ptr [rsp + 0x110]
009DB042  48 03 47 38                     add rax, qword ptr [rdi + 0x38]
009DB046  48 89 47 38                     mov qword ptr [rdi + 0x38], rax
009DB04A  8B 4C 24 30                     mov ecx, dword ptr [rsp + 0x30]
009DB04E  EB 07                           jmp 0x1409db057
009DB050  44 8B F0                        mov r14d, eax
009DB053  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
009DB057  03 F1                           add esi, ecx
009DB059  89 74 24 3C                     mov dword ptr [rsp + 0x3c], esi
009DB05D  3B F1                           cmp esi, ecx
009DB05F  0F 82 0F FF FF FF               jb 0x1409daf74
009DB065  4C 8B 8C 24 98 00 00 00         mov r9, qword ptr [rsp + 0x98]
009DB06D  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
009DB075  44 8B 94 24 18 01 00 00         mov r10d, dword ptr [rsp + 0x118]
009DB07D  4C 8B 9C 24 88 00 00 00         mov r11, qword ptr [rsp + 0x88]
009DB085  44 8B FE                        mov r15d, esi
009DB088  4C 03 BC 24 10 01 00 00         add r15, qword ptr [rsp + 0x110]
009DB090  4C 89 BC 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r15
009DB098  83 C6 40                        add esi, 0x40
009DB09B  89 74 24 3C                     mov dword ptr [rsp + 0x3c], esi
009DB09F  83 FE 40                        cmp esi, 0x40
009DB0A2  0F 82 CC FE FF FF               jb 0x1409daf74
009DB0A8  41 3B F2                        cmp esi, r10d
009DB0AB  0F 83 FA FE FF FF               jae 0x1409dafab
009DB0B1  45 89 07                        mov dword ptr [r15], r8d
009DB0B4  49 8B C3                        mov rax, r11
009DB0B7  8B 94 24 00 01 00 00            mov edx, dword ptr [rsp + 0x100]
009DB0BE  85 D2                           test edx, edx
009DB0C0  49 0F 45 C0                     cmovne rax, r8
009DB0C4  49 89 47 08                     mov qword ptr [r15 + 8], rax
009DB0C8  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
009DB0CC  49 89 47 10                     mov qword ptr [r15 + 0x10], rax
009DB0D0  0F B7 41 18                     movzx eax, word ptr [rcx + 0x18]
009DB0D4  66 41 89 47 18                  mov word ptr [r15 + 0x18], ax
009DB0D9  41 8B 01                        mov eax, dword ptr [r9]
009DB0DC  41 89 47 1C                     mov dword ptr [r15 + 0x1c], eax
009DB0E0  41 8B 41 08                     mov eax, dword ptr [r9 + 8]
009DB0E4  41 89 47 20                     mov dword ptr [r15 + 0x20], eax
009DB0E8  41 0F B6 41 1B                  movzx eax, byte ptr [r9 + 0x1b]
009DB0ED  66 41 89 47 1A                  mov word ptr [r15 + 0x1a], ax
009DB0F2  49 8B 41 28                     mov rax, qword ptr [r9 + 0x28]
009DB0F6  48 83 E0 F0                     and rax, 0xfffffffffffffff0
009DB0FA  49 89 47 38                     mov qword ptr [r15 + 0x38], rax
009DB0FE  85 D2                           test edx, edx
009DB100  49 0F 45 C0                     cmovne rax, r8
009DB104  49 89 47 38                     mov qword ptr [r15 + 0x38], rax
009DB108  49 8B C9                        mov rcx, r9
009DB10B  E8 70 39 A3 FF                  call 0x14040ea80
009DB110  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
009DB115  41 8B 50 68                     mov edx, dword ptr [r8 + 0x68]
009DB119  45 8B 40 6C                     mov r8d, dword ptr [r8 + 0x6c]
009DB11D  48 85 C0                        test rax, rax
009DB120  74 06                           je 0x1409db128
009DB122  8B 10                           mov edx, dword ptr [rax]
009DB124  44 8B 40 04                     mov r8d, dword ptr [rax + 4]
009DB128  41 89 57 24                     mov dword ptr [r15 + 0x24], edx
009DB12C  45 89 47 28                     mov dword ptr [r15 + 0x28], r8d
009DB130  49 8B C9                        mov rcx, r9
009DB133  E8 2C 62 AD FF                  call 0x1404b1364
009DB138  45 33 C0                        xor r8d, r8d
009DB13B  48 85 C0                        test rax, rax
009DB13E  74 13                           je 0x1409db153
009DB140  48 8B 00                        mov rax, qword ptr [rax]
009DB143  48 85 C0                        test rax, rax
009DB146  74 0B                           je 0x1409db153
009DB148  48 8B 80 D0 01 00 00            mov rax, qword ptr [rax + 0x1d0]
009DB14F  49 89 47 30                     mov qword ptr [r15 + 0x30], rax
009DB153  44 89 44 24 30                  mov dword ptr [rsp + 0x30], r8d
009DB158  41 8B F8                        mov edi, r8d
009DB15B  44 89 44 24 40                  mov dword ptr [rsp + 0x40], r8d
009DB160  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
009DB165  4C 39 81 A0 00 00 00            cmp qword ptr [rcx + 0xa0], r8
009DB16C  0F 84 B7 00 00 00               je 0x1409db229
009DB172  48 3B 0D 67 B9 5E 00            cmp rcx, qword ptr [rip + 0x5eb967]
009DB179  0F 85 AA 00 00 00               jne 0x1409db229
009DB17F  41 0F 10 43 58                  movups xmm0, xmmword ptr [r11 + 0x58]
009DB184  F3 0F 7F 03                     movdqu xmmword ptr [rbx], xmm0
009DB188  0F B7 03                        movzx eax, word ptr [rbx]
009DB18B  66 85 C0                        test ax, ax
009DB18E  0F 84 6C 01 00 00               je 0x1409db300
009DB194  4C 39 43 08                     cmp qword ptr [rbx + 8], r8
009DB198  0F 84 62 01 00 00               je 0x1409db300
009DB19E  83 C0 02                        add eax, 2
009DB1A1  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
009DB1A5  B9 08 02 00 00                  mov ecx, 0x208
009DB1AA  3B C1                           cmp eax, ecx
009DB1AC  76 0E                           jbe 0x1409db1bc
009DB1AE  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
009DB1B2  8D 41 FE                        lea eax, [rcx - 2]
009DB1B5  66 89 03                        mov word ptr [rbx], ax
009DB1B8  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
009DB1BC  48 83 C3 10                     add rbx, 0x10
009DB1C0  44 8B C0                        mov r8d, eax
009DB1C3  49 83 E8 02                     sub r8, 2
009DB1C7  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
009DB1CC  48 8B 52 08                     mov rdx, qword ptr [rdx + 8]
009DB1D0  48 8B CB                        mov rcx, rbx
009DB1D3  E8 68 B6 CE FF                  call 0x1406c6840
009DB1D8  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
009DB1DD  48 89 59 08                     mov qword ptr [rcx + 8], rbx
009DB1E1  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
009DB1E5  66 89 41 02                     mov word ptr [rcx + 2], ax
009DB1E9  0F B7 01                        movzx eax, word ptr [rcx]
009DB1EC  D1 E8                           shr eax, 1
009DB1EE  45 33 C0                        xor r8d, r8d
009DB1F1  66 44 89 04 43                  mov word ptr [rbx + rax*2], r8w
009DB1F6  41 8D 48 10                     lea ecx, [r8 + 0x10]
009DB1FA  01 4C 24 30                     add dword ptr [rsp + 0x30], ecx
009DB1FE  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
009DB203  44 8B 94 24 18 01 00 00         mov r10d, dword ptr [rsp + 0x118]
009DB20B  E9 F5 00 00 00                  jmp 0x1409db305
009DB210  44 8B 94 24 18 01 00 00         mov r10d, dword ptr [rsp + 0x118]
009DB218  41 3B F2                        cmp esi, r10d
009DB21B  0F 83 64 FE FF FF               jae 0x1409db085
009DB221  41 89 37                        mov dword ptr [r15], esi
009DB224  E9 5C FE FF FF                  jmp 0x1409db085
009DB229  44 88 44 24 20                  mov byte ptr [rsp + 0x20], r8b
009DB22E  4C 8D 4C 24 30                  lea r9, [rsp + 0x30]
009DB233  44 8B 44 24 60                  mov r8d, dword ptr [rsp + 0x60]
009DB238  48 8B D3                        mov rdx, rbx
009DB23B  49 8B CB                        mov rcx, r11
009DB23E  E8 8D CC EC FF                  call 0x1408a7ed0
009DB243  8B F8                           mov edi, eax
009DB245  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
009DB249  3D 04 00 00 C0                  cmp eax, 0xc0000004
009DB24E  0F 85 A1 00 00 00               jne 0x1409db2f5
009DB254  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
009DB258  8B D0                           mov edx, eax
009DB25A  44 8B 94 24 18 01 00 00         mov r10d, dword ptr [rsp + 0x118]
009DB262  48 3B 44 24 60                  cmp rax, qword ptr [rsp + 0x60]
009DB267  0F 86 90 00 00 00               jbe 0x1409db2fd
009DB26D  8D 0C 06                        lea ecx, [rsi + rax]
009DB270  41 3B CA                        cmp ecx, r10d
009DB273  0F 83 84 00 00 00               jae 0x1409db2fd
009DB279  49 8B FC                        mov rdi, r12
009DB27C  B9 00 01 00 00                  mov ecx, 0x100
009DB281  41 B8 4F 62 41 72               mov r8d, 0x7241624f
009DB287  E8 64 6E 1A 00                  call 0x140b820f0
009DB28C  4C 8B E0                        mov r12, rax
009DB28F  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
009DB297  45 33 C0                        xor r8d, r8d
009DB29A  48 85 C0                        test rax, rax
009DB29D  0F 84 D7 00 00 00               je 0x1409db37a
009DB2A3  BA 4F 62 41 72                  mov edx, 0x7241624f
009DB2A8  48 8B CF                        mov rcx, rdi
009DB2AB  E8 C0 75 1A 00                  call 0x140b82870
009DB2B0  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
009DB2B4  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
009DB2B9  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
009DB2C1  49 8B DC                        mov rbx, r12
009DB2C4  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
009DB2C9  48 89 9C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rbx
009DB2D1  33 C9                           xor ecx, ecx
009DB2D3  88 4C 24 20                     mov byte ptr [rsp + 0x20], cl
009DB2D7  4C 8D 4C 24 30                  lea r9, [rsp + 0x30]
009DB2DC  44 8B C0                        mov r8d, eax
009DB2DF  49 8B D4                        mov rdx, r12
009DB2E2  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
009DB2EA  E8 E1 CB EC FF                  call 0x1408a7ed0
009DB2EF  8B F8                           mov edi, eax
009DB2F1  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
009DB2F5  44 8B 94 24 18 01 00 00         mov r10d, dword ptr [rsp + 0x118]
009DB2FD  45 33 C0                        xor r8d, r8d
009DB300  B9 10 00 00 00                  mov ecx, 0x10
009DB305  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
009DB309  85 C0                           test eax, eax
009DB30B  0F 84 BD 00 00 00               je 0x1409db3ce
009DB311  83 C0 07                        add eax, 7
009DB314  83 E0 F8                        and eax, 0xfffffff8
009DB317  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
009DB31B  03 F0                           add esi, eax
009DB31D  89 74 24 3C                     mov dword ptr [rsp + 0x3c], esi
009DB321  3B F0                           cmp esi, eax
009DB323  0F 82 4B FC FF FF               jb 0x1409daf74
009DB329  85 FF                           test edi, edi
009DB32B  78 7A                           js 0x1409db3a7
009DB32D  0F B7 03                        movzx eax, word ptr [rbx]
009DB330  66 85 C0                        test ax, ax
009DB333  74 66                           je 0x1409db39b
009DB335  41 3B F2                        cmp esi, r10d
009DB338  73 61                           jae 0x1409db39b
009DB33A  49 8D 5F 50                     lea rbx, [r15 + 0x50]
009DB33E  BF 02 00 00 00                  mov edi, 2
009DB343  03 F8                           add edi, eax
009DB345  66 41 89 47 40                  mov word ptr [r15 + 0x40], ax
009DB34A  44 0F B7 C7                     movzx r8d, di
009DB34E  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
009DB353  48 8B 52 08                     mov rdx, qword ptr [rdx + 8]
009DB357  48 8B CB                        mov rcx, rbx
009DB35A  E8 E1 B4 CE FF                  call 0x1406c6840
009DB35F  48 2B 9C 24 10 01 00 00         sub rbx, qword ptr [rsp + 0x110]
009DB367  48 03 9C 24 08 01 00 00         add rbx, qword ptr [rsp + 0x108]
009DB36F  49 89 5F 48                     mov qword ptr [r15 + 0x48], rbx
009DB373  66 41 89 7F 42                  mov word ptr [r15 + 0x42], di
009DB378  EB 7F                           jmp 0x1409db3f9
009DB37A  4C 8B E7                        mov r12, rdi
009DB37D  48 89 BC 24 80 00 00 00         mov qword ptr [rsp + 0x80], rdi
009DB385  BF 9A 00 00 C0                  mov edi, 0xc000009a
009DB38A  89 7C 24 40                     mov dword ptr [rsp + 0x40], edi
009DB38E  44 8B 94 24 18 01 00 00         mov r10d, dword ptr [rsp + 0x118]
009DB396  E9 65 FF FF FF                  jmp 0x1409db300
009DB39B  85 FF                           test edi, edi
009DB39D  78 08                           js 0x1409db3a7
009DB39F  66 44 39 03                     cmp word ptr [rbx], r8w
009DB3A3  74 37                           je 0x1409db3dc
009DB3A5  EB 3A                           jmp 0x1409db3e1
009DB3A7  03 F1                           add esi, ecx
009DB3A9  89 74 24 3C                     mov dword ptr [rsp + 0x3c], esi
009DB3AD  3B F1                           cmp esi, ecx
009DB3AF  0F 82 BF FB FF FF               jb 0x1409daf74
009DB3B5  41 3B F2                        cmp esi, r10d
009DB3B8  73 27                           jae 0x1409db3e1
009DB3BA  49 8D 4F 40                     lea rcx, [r15 + 0x40]
009DB3BE  33 D2                           xor edx, edx
009DB3C0  E8 BB F3 A4 FF                  call 0x14042a780
009DB3C5  44 8B F7                        mov r14d, edi
009DB3C8  89 7C 24 34                     mov dword ptr [rsp + 0x34], edi
009DB3CC  EB 2B                           jmp 0x1409db3f9
009DB3CE  03 F1                           add esi, ecx
009DB3D0  89 74 24 3C                     mov dword ptr [rsp + 0x3c], esi
009DB3D4  3B F1                           cmp esi, ecx
009DB3D6  0F 82 98 FB FF FF               jb 0x1409daf74
009DB3DC  41 3B F2                        cmp esi, r10d
009DB3DF  72 0D                           jb 0x1409db3ee
009DB3E1  41 BE 04 00 00 C0               mov r14d, 0xc0000004
009DB3E7  44 89 74 24 34                  mov dword ptr [rsp + 0x34], r14d
009DB3EC  EB 0E                           jmp 0x1409db3fc
009DB3EE  33 D2                           xor edx, edx
009DB3F0  49 8D 4F 40                     lea rcx, [r15 + 0x40]
009DB3F4  E8 87 F3 A4 FF                  call 0x14042a780
009DB3F9  45 33 C0                        xor r8d, r8d
009DB3FC  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
009DB401  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
009DB406  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
009DB40A  8A 54 24 38                     mov dl, byte ptr [rsp + 0x38]
009DB40E  FF C0                           inc eax
009DB410  E9 E2 FA FF FF                  jmp 0x1409daef7
009DB415  48 8B 84 24 20 01 00 00         mov rax, qword ptr [rsp + 0x120]
009DB41D  48 85 C0                        test rax, rax
009DB420  74 02                           je 0x1409db424
009DB422  89 30                           mov dword ptr [rax], esi
009DB424  4D 85 ED                        test r13, r13
009DB427  74 0D                           je 0x1409db436
009DB429  49 8B CD                        mov rcx, r13
009DB42C  E8 33 00 00 00                  call 0x1409db464
009DB431  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
009DB436  E8 29 00 00 00                  call 0x1409db464
009DB43B  BA 4F 62 41 72                  mov edx, 0x7241624f
009DB440  49 8B CC                        mov rcx, r12
009DB443  E8 28 74 1A 00                  call 0x140b82870
009DB448  B8 01 00 00 C0                  mov eax, 0xc0000001
009DB44D  48 85 FF                        test rdi, rdi
009DB450  44 0F 44 F0                     cmove r14d, eax
009DB454  41 8B C6                        mov eax, r14d
009DB457  E9 EA F9 FF FF                  jmp 0x1409dae46
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObGetObjectInformation(int a1, __int64 a2, __int64 a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_mC8;
    unsigned int v_stack_p100;
    unsigned __int64 v_stack_p108;
    unsigned __int64 v_stack_p110;
    unsigned int v_stack_p118;
    unsigned __int8 v_stack_p20;
    unsigned int v_stack_p30;
    unsigned int v_stack_p34;
    unsigned __int8 v_stack_p38;
    unsigned int v_stack_p3C;
    unsigned int v_stack_p40;
    unsigned int v_stack_p44;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pA0;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pB0;

    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned int *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (192);
    v_rdi = 0;
    v_stack_mC8 = 0;
    v_stack_m88 = 0;
    v_stack_m98 = 536;
    result = ExAllocatePool2(256, 536, (unsigned int)(0x7241624FULL), a4);
    v_stack_m78 = result;
    if (result != 0) goto loc_009DAE5A;
loc_009DAE46:
    v_rsp = (v_rsp) + (192);
    return (unsigned int)(0xC000009AULL);
loc_009DAE5A:
    v_stack_p48 = result;
    v_stack_p68 = 0;
    result = ObpCreateTypeArray(*(unsigned __int64 *)(v_rip + 5457901), 536, (unsigned int)(0x7241624FULL), a4);
    v_stack_p78 = result;
    a3 = 0;
    if (result != 0) goto loc_009DAE9C;
    result = ExFreePoolWithTag(result, (unsigned int)(0x7241624FULL), a3, a4);
    goto loc_009DAE46;
loc_009DAE9C:
loc_009DAE9F:
    v_stack_p44 = 0;
    if (0 >= (*(unsigned int *)(result))) goto loc_009DB415;
    if (*(unsigned __int64 *)(result + 0 * 8 + 8) != 0) goto loc_009DAEBC;
    goto loc_009DAF9B;
loc_009DAEBC:
    a1 = (*(unsigned __int64 *)(result + 0 * 8 + 8)) + (80);
    v_stack_p58 = a1;
    if (a1 == (*(unsigned __int64 *)(v_rip + 5457812))) goto loc_009DAF9B;
    result = ObpCreateTypeArray(a1, 0, a3, a4);
    v_stack_p70 = result;
    a3 = 0;
    if (result == 0) goto loc_009DAF97;
    v_stack_p38 = 1;
loc_009DAEF7:
    v_stack_p50 = 0;
    if (0 >= (*(unsigned int *)(result))) goto loc_009DAF7F;
    v_stack_p90 = *(unsigned __int64 *)(result + 0 * 8 + 8);
    if (*(unsigned __int64 *)(result + 0 * 8 + 8) != 0) goto loc_009DAF1A;
    goto loc_009DB40E;
loc_009DAF1A:
    v_stack_p98 = *(unsigned __int64 *)(result + 0 * 8 + 8) + 32;
    v_stack_p88 = *(unsigned __int64 *)(result + 0 * 8 + 8) + 32 + 48;
    if (1 == 0) goto loc_009DB210;
    v_stack_p38 = 0;
    if (0 == 0) goto loc_009DAF51;
    if (0 < ((unsigned int)((unsigned int)(v_stack_p118)))) {
        *(unsigned int *)(v_rdi) = 0;
    }
    v_rdi = (0) + (v_stack_p110);
    v_stack_p68 = v_rdi;
    v_stack_pA0 = v_rdi;
    v_rsi = (unsigned int)((0) + (48));
    v_stack_p3C = (unsigned int)(v_rsi);
    if (((unsigned int)(v_rsi)) >= 48) goto loc_009DAFA7;
loc_009DAF74:
loc_009DAF7A:
    v_stack_p34 = (unsigned int)((unsigned int)(0xC0000095ULL));
loc_009DAF7F:
    result = ObpDestroyTypeArray(result, 1, a3, *(unsigned __int64 *)(result + 0 * 8 + 8) + 32);
    a3 = 0;
    v_stack_p70 = 0;
loc_009DAF97:
loc_009DAF9B:
    a2 = (unsigned int)(((unsigned int)(v_stack_p44)) + 1);
    goto loc_009DAE9F;
loc_009DAFA7:
    if (((unsigned int)(v_rsi)) < ((unsigned int)(v_stack_p78))) goto loc_009DAFB3;
loc_009DAFAB:
    goto loc_009DAF7A;
loc_009DAFB3:
    *(unsigned int *)(v_stack_p68) = 0;
    *(unsigned int *)(v_stack_p68 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p58 + 44)));
    *(unsigned int *)(v_stack_p68 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p58 + 48)));
    *(unsigned int *)(v_stack_p68 + 12) = (unsigned int)(*(unsigned __int8 *)(v_stack_p58 + 40));
    *(unsigned int *)(v_stack_p68 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p58 + 72)));
    *(unsigned __int64 *)(v_stack_p68 + 20) = v_xmm0;
    *(unsigned int *)(v_stack_p68 + 36) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p58 + 92)));
    *(unsigned int *)(v_stack_p68 + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p58 + 100)));
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_p58 + 66)) >> (3));
    result = (unsigned __int8)((result) & (1));
    *(unsigned __int8 *)(v_stack_p68 + 44) = (unsigned __int8)(result);
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p78))) - ((unsigned int)(v_rsi)));
    a1 = 0;
    v_stack_p30 = 0;
    result = ObQueryTypeName(*(unsigned __int64 *)(result + 0 * 8 + 8) + 32 + 48, v_stack_p68 + 48, a3, v_stack_p30);
    v_stack_p40 = (unsigned int)(result);
    a1 = (unsigned int)(((unsigned int)(v_stack_p30)) + (7));
    a1 = (unsigned int)((a1) & (0xFFFFFFF8ULL));
    v_stack_p30 = a1;
    a3 = 0;
    if (sign_flag) goto loc_009DB050;
    a1 = (unsigned __int16)((a1) - (16));
    *(unsigned __int16 *)(v_stack_p68 + 50) = (unsigned __int16)(a1);
    result = (v_stack_p108) - (v_stack_p110);
    result = (result) + (*(unsigned __int64 *)(v_stack_p68 + 56));
    *(unsigned __int64 *)(v_stack_p68 + 56) = result;
    goto loc_009DB057;
loc_009DB050:
    v_stack_p34 = (unsigned int)(result);
loc_009DB057:
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)((unsigned int)(v_stack_p30))));
    v_stack_p3C = (unsigned int)(v_rsi);
    if (((unsigned int)(v_rsi)) < ((unsigned int)((unsigned int)(v_stack_p30)))) goto loc_009DAF74;
loc_009DB085:
    v_r15 = ((unsigned int)((unsigned int)(v_rsi))) + (v_stack_p110);
    v_stack_pA8 = v_r15;
    v_rsi = (unsigned int)((v_rsi) + (64));
    v_stack_p3C = (unsigned int)(v_rsi);
    if (((unsigned int)(v_rsi)) < 64) goto loc_009DAF74;
    if (((unsigned int)(v_rsi)) >= ((unsigned int)((unsigned int)(v_stack_p118)))) goto loc_009DAFAB;
    *(unsigned int *)(v_r15) = 0;
    result = v_stack_p88;
    if ((unsigned int)((unsigned int)(v_stack_p100)) != 0) { result = 0; }
    *(unsigned __int64 *)(v_r15 + 8) = result;
    *(unsigned __int64 *)(v_r15 + 16) = *(unsigned __int64 *)(v_stack_p90 + 16);
    *(unsigned __int16 *)(v_r15 + 24) = (unsigned __int16)(*(unsigned __int16 *)(v_stack_p90 + 24));
    *(unsigned int *)(v_r15 + 28) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p98)));
    *(unsigned int *)(v_r15 + 32) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p98 + 8)));
    *(unsigned __int16 *)(v_r15 + 26) = (unsigned __int16)(*(unsigned __int8 *)(v_stack_p98 + 27));
    result = (*(unsigned __int64 *)(v_stack_p98 + 40)) & (-16);
    *(unsigned __int64 *)(v_r15 + 56) = result;
    if ((unsigned int)((unsigned int)(v_stack_p100)) != 0) { result = 0; }
    *(unsigned __int64 *)(v_r15 + 56) = result;
    result = OBJECT_HEADER_TO_QUOTA_INFO(v_stack_p98, (unsigned int)(v_stack_p100), a3, v_stack_p98);
    if (result != 0) {
        a2 = *(unsigned int *)(result);
        a3 = *(unsigned int *)(result + 4);
    }
    *(unsigned int *)(v_r15 + 36) = (unsigned int)(a2);
    *(unsigned int *)(v_r15 + 40) = (unsigned int)(a3);
    result = OBJECT_HEADER_TO_PROCESS_INFO(v_stack_p98, a2, a3, v_stack_p98);
    a3 = 0;
    if (result == 0) goto loc_009DB153;
    result = *(unsigned __int64 *)(result);
    if (*(unsigned __int64 *)(result) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 464);
        *(unsigned __int64 *)(v_r15 + 48) = result;
    }
    v_stack_p30 = 0;
    v_stack_p40 = 0;
    if ((*(unsigned __int64 *)(v_stack_p58 + 160)) == 0) goto loc_009DB229;
    if (v_stack_p58 != (*(unsigned __int64 *)(v_rip + 6207847))) goto loc_009DB229;
    *(unsigned __int64 *)(result) = v_xmm0;
    if ((unsigned __int16)(*(unsigned __int16 *)(result)) == 0) goto loc_009DB300;
    if ((*(unsigned __int64 *)(result + 8)) == 0) goto loc_009DB300;
    result = (unsigned int)((*(unsigned __int16 *)(result)) + (2));
    v_stack_p30 = (unsigned int)(result);
    if (((unsigned int)(result)) >= = 520) {
        v_stack_p30 = 520;
        result = 520 - 2;
        *(unsigned __int16 *)(result) = (unsigned __int16)(result);
        result = v_stack_p30;
    }
    v_rbx = (result) + (16);
    a3 = ((unsigned int)((unsigned int)(result))) - (2);
    result = memcpy(v_rbx, *(unsigned __int64 *)(v_stack_p48 + 8), a3, v_stack_p98);
    *(unsigned __int64 *)(v_stack_p48 + 8) = v_rbx;
    *(unsigned __int16 *)(v_stack_p48 + 2) = (unsigned __int16)((unsigned int)(v_stack_p30));
    result = (unsigned int)((*(unsigned __int16 *)(v_stack_p48)) >> (1));
    a3 = 0;
    *(unsigned __int16 *)(v_rbx + result * 2) = 0;
    goto loc_009DB305;
loc_009DB210:
    if (((unsigned int)(v_rsi)) >= ((unsigned int)((unsigned int)(v_stack_p118)))) goto loc_009DB085;
    *(unsigned int *)(v_r15) = (unsigned int)(v_rsi);
    goto loc_009DB085;
loc_009DB229:
    v_stack_p20 = 0;
    result = ObQueryNameStringMode(v_stack_p88, v_stack_p48, (unsigned int)(v_stack_p60), v_stack_p30);
    v_stack_p40 = (unsigned int)(result);
    if (((unsigned int)(result)) != 0xC0000004ULL) goto loc_009DB2F5;
    if (((unsigned int)(v_stack_p30)) <= v_stack_p60) goto loc_009DB2FD;
    if (((unsigned int)(v_rsi + (unsigned int)(v_stack_p30) * 1)) >= ((unsigned int)((unsigned int)(v_stack_p118)))) goto loc_009DB2FD;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(v_stack_p30))), (unsigned int)(0x7241624FULL), v_stack_p30);
    v_stack_p80 = result;
    a3 = 0;
    if (result == 0) goto loc_009DB37A;
    result = ExFreePoolWithTag(result, (unsigned int)(0x7241624FULL), a3, v_stack_p30);
    v_stack_p60 = (unsigned int)(v_stack_p30);
    v_stack_p90 = (unsigned int)(v_stack_p30);
    v_stack_p48 = result;
    v_stack_pB0 = result;
    a1 = 0;
    v_stack_p20 = 0;
    result = ObQueryNameStringMode(v_stack_p88, result, (unsigned int)((unsigned int)((unsigned int)(v_stack_p30))), v_stack_p30);
    v_stack_p40 = (unsigned int)(result);
loc_009DB2F5:
loc_009DB2FD:
    a3 = 0;
loc_009DB300:
loc_009DB305:
    if ((unsigned int)((unsigned int)(v_stack_p30)) == 0) goto loc_009DB3CE;
    result = (unsigned int)(((unsigned int)(v_stack_p30)) + (7));
    result = (unsigned int)((result) & (0xFFFFFFF8ULL));
    v_stack_p30 = (unsigned int)(result);
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)(result)));
    v_stack_p3C = (unsigned int)(v_rsi);
    if (((unsigned int)(v_rsi)) < ((unsigned int)(result))) goto loc_009DAF74;
    if (sign_flag) goto loc_009DB3A7;
    if ((unsigned __int16)(*(unsigned __int16 *)(result)) == 0) goto loc_009DB39B;
    if (((unsigned int)(v_rsi)) >= ((unsigned int)((unsigned int)(v_stack_p118)))) goto loc_009DB39B;
    v_rdi = (unsigned int)((2) + ((unsigned int)(*(unsigned __int16 *)(result))));
    *(unsigned __int16 *)(v_r15 + 64) = (unsigned __int16)(*(unsigned __int16 *)(result));
    result = memcpy(v_r15 + 80, *(unsigned __int64 *)(v_stack_p48 + 8), (unsigned __int16)(v_rdi), v_stack_p30);
    v_rbx = (v_r15 + 80) - (v_stack_p110);
    v_rbx = (v_rbx) + (v_stack_p108);
    *(unsigned __int64 *)(v_r15 + 72) = v_rbx;
    *(unsigned __int16 *)(v_r15 + 66) = (unsigned __int16)(v_rdi);
    goto loc_009DB3F9;
loc_009DB37A:
    v_stack_p80 = v_rdi;
    v_stack_p40 = (unsigned int)((unsigned int)(0xC000009AULL));
    goto loc_009DB300;
loc_009DB39B:
    if (sign_flag) goto loc_009DB3A7;
    if ((*(unsigned __int16 *)(v_rbx)) == ((unsigned __int16)((unsigned __int16)(v_rdi)))) goto loc_009DB3DC;
    goto loc_009DB3E1;
loc_009DB3A7:
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)(v_r15 + 80)));
    v_stack_p3C = (unsigned int)(v_rsi);
    if (((unsigned int)(v_rsi)) < ((unsigned int)(v_r15 + 80))) goto loc_009DAF74;
    if (((unsigned int)(v_rsi)) >= ((unsigned int)((unsigned int)(v_stack_p118)))) goto loc_009DB3E1;
    a2 = 0;
    result = RtlInitUnicodeString(v_r15 + 64, a2, (unsigned __int16)(v_rdi), v_stack_p30);
    v_stack_p34 = (unsigned int)((unsigned int)(0xC000009AULL));
    goto loc_009DB3F9;
loc_009DB3CE:
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)(v_r15 + 64)));
    v_stack_p3C = (unsigned int)(v_rsi);
    if (((unsigned int)(v_rsi)) < ((unsigned int)(v_r15 + 64))) goto loc_009DAF74;
loc_009DB3DC:
    if (((unsigned int)(v_rsi)) < ((unsigned int)((unsigned int)(v_stack_p118)))) goto loc_009DB3EE;
loc_009DB3E1:
    v_stack_p34 = (unsigned int)((unsigned int)(0xC0000004ULL));
    goto loc_009DB3FC;
loc_009DB3EE:
    a2 = 0;
    result = RtlInitUnicodeString(v_r15 + 64, a2, (unsigned __int16)(v_rdi), v_stack_p30);
loc_009DB3F9:
    a3 = 0;
loc_009DB3FC:
loc_009DB40E:
    result = (unsigned int)(((unsigned int)(v_stack_p50)) + 1);
    goto loc_009DAEF7;
loc_009DB415:
    if (a5 != 0) {
        *(unsigned int *)(a5) = (unsigned int)(v_rsi);
    }
    result = a5;
    if (0 != 0) {
        a1 = 0;
        result = ObpDestroyTypeArray(a1, v_stack_p38, a3, v_stack_p30);
        a1 = v_stack_p78;
    }
    result = ObpDestroyTypeArray(a1, v_stack_p38, a3, v_stack_p30);
    result = ExFreePoolWithTag(v_rdi, (unsigned int)(0x7241624FULL), a3, v_stack_p30);
    v_r14 = (unsigned int)(0xC0000004ULL);
    if (v_stack_p68 == 0) { v_r14 = (unsigned int)((unsigned int)(0xC0000001ULL)); }
    goto loc_009DAE46;
}
```

## 5. (Beta) C Style

```c
int64_t ObGetObjectInformation(int32_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint32_t v_stack_mC8;
    uint32_t v_stack_p100;
    uint64_t v_stack_p108;
    uint64_t v_stack_p110;
    uint32_t v_stack_p118;
    uint8_t v_stack_p20;
    uint32_t v_stack_p30;
    uint32_t v_stack_p34;
    uint8_t v_stack_p38;
    uint32_t v_stack_p3C;
    uint32_t v_stack_p40;
    uint32_t v_stack_p44;
    uint64_t v_stack_p48;
    uint32_t v_stack_p50;
    uint64_t v_stack_p58;
    uint32_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p80;
    uint64_t v_stack_p88;
    uint64_t v_stack_p90;
    uint64_t v_stack_p98;
    uint64_t v_stack_pA0;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pB0;

    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint32_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (192);
    local_rdi = 0;
    v_stack_mC8 = 0;
    v_stack_m88 = 0;
    v_stack_m98 = 536;
    result = ExAllocatePool2(256, 536, (uint32_t)(0x7241624FULL), Arg4);
    v_stack_m78 = result;
    if (result != 0) goto loc_009DAE5A;
loc_009DAE46:
    local_rsp = (local_rsp) + (192);
    return (uint32_t)(0xC000009AULL);
loc_009DAE5A:
    v_stack_p48 = result;
    v_stack_p68 = 0;
    result = ObpCreateTypeArray(*(uint64_t *)(v_rip + 0x5347ED), 536, (uint32_t)(0x7241624FULL), Arg4);
    v_stack_p78 = result;
    Arg3 = 0;
    if (result != 0) goto loc_009DAE9C;
    result = ExFreePoolWithTag(result, (uint32_t)(0x7241624FULL), Arg3, Arg4);
    goto loc_009DAE46;
loc_009DAE9C:
loc_009DAE9F:
    v_stack_p44 = 0;
    if (0 >= (*(uint32_t *)(result))) goto loc_009DB415;
    if (*(uint64_t *)(result + 0x0 * 8 + 0x8) != 0) goto loc_009DAEBC;
    goto loc_009DAF9B;
loc_009DAEBC:
    Arg1 = (*(uint64_t *)(result + 0x0 * 8 + 0x8)) + (80);
    v_stack_p58 = Arg1;
    if (Arg1 == (*(uint64_t *)(v_rip + 0x534794))) goto loc_009DAF9B;
    result = ObpCreateTypeArray(Arg1, 0, Arg3, Arg4);
    v_stack_p70 = result;
    Arg3 = 0;
    if (result == 0) goto loc_009DAF97;
    v_stack_p38 = 1;
loc_009DAEF7:
    v_stack_p50 = 0;
    if (0 >= (*(uint32_t *)(result))) goto loc_009DAF7F;
    v_stack_p90 = *(uint64_t *)(result + 0x0 * 8 + 0x8);
    if (*(uint64_t *)(result + 0x0 * 8 + 0x8) != 0) goto loc_009DAF1A;
    goto loc_009DB40E;
loc_009DAF1A:
    v_stack_p98 = *(uint64_t *)(result + 0x0 * 8 + 0x8) + 32;
    v_stack_p88 = *(uint64_t *)(result + 0x0 * 8 + 0x8) + 32 + 48;
    if (1 == 0) goto loc_009DB210;
    v_stack_p38 = 0;
    if (0 == 0) goto loc_009DAF51;
    if (0 < ((uint32_t)((uint32_t)(v_stack_p118)))) {
        *(uint32_t *)(local_rdi) = 0;
    }
    local_rdi = (0) + (v_stack_p110);
    v_stack_p68 = local_rdi;
    v_stack_pA0 = local_rdi;
    local_rsi = (uint32_t)((0) + (48));
    v_stack_p3C = (uint32_t)(local_rsi);
    if (((uint32_t)(local_rsi)) >= 48) goto loc_009DAFA7;
loc_009DAF74:
loc_009DAF7A:
    v_stack_p34 = (uint32_t)((uint32_t)(0xC0000095ULL));
loc_009DAF7F:
    result = ObpDestroyTypeArray(result, 1, Arg3, *(uint64_t *)(result + 0x0 * 8 + 0x8) + 32);
    Arg3 = 0;
    v_stack_p70 = 0;
loc_009DAF97:
loc_009DAF9B:
    Arg2 = (uint32_t)(((uint32_t)(v_stack_p44)) + 1);
    goto loc_009DAE9F;
loc_009DAFA7:
    if (((uint32_t)(local_rsi)) < ((uint32_t)(v_stack_p78))) goto loc_009DAFB3;
loc_009DAFAB:
    goto loc_009DAF7A;
loc_009DAFB3:
    *(uint32_t *)(v_stack_p68) = 0;
    *(uint32_t *)(v_stack_p68 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p58 + 0x2C)));
    *(uint32_t *)(v_stack_p68 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p58 + 0x30)));
    *(uint32_t *)(v_stack_p68 + 0xC) = (uint32_t)(*(uint8_t *)(v_stack_p58 + 0x28));
    *(uint32_t *)(v_stack_p68 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p58 + 0x48)));
    *(uint64_t *)(v_stack_p68 + 0x14) = v_xmm0;
    *(uint32_t *)(v_stack_p68 + 0x24) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p58 + 0x5C)));
    *(uint32_t *)(v_stack_p68 + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p58 + 0x64)));
    result = (uint8_t)((*(uint8_t *)(v_stack_p58 + 0x42)) >> (3));
    result = (uint8_t)((result) & (1));
    *(uint8_t *)(v_stack_p68 + 0x2C) = (uint8_t)(result);
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p78))) - ((uint32_t)(local_rsi)));
    Arg1 = 0;
    v_stack_p30 = 0;
    result = ObQueryTypeName(*(uint64_t *)(result + 0x0 * 8 + 0x8) + 32 + 48, v_stack_p68 + 48, Arg3, v_stack_p30);
    v_stack_p40 = (uint32_t)(result);
    Arg1 = (uint32_t)(((uint32_t)(v_stack_p30)) + (7));
    Arg1 = (uint32_t)((Arg1) & (0xFFFFFFF8ULL));
    v_stack_p30 = Arg1;
    Arg3 = 0;
    if (sign_flag) goto loc_009DB050;
    Arg1 = (uint16_t)((Arg1) - (16));
    *(uint16_t *)(v_stack_p68 + 0x32) = (uint16_t)(Arg1);
    result = (v_stack_p108) - (v_stack_p110);
    result = (result) + (*(uint64_t *)(v_stack_p68 + 0x38));
    *(uint64_t *)(v_stack_p68 + 0x38) = result;
    goto loc_009DB057;
loc_009DB050:
    v_stack_p34 = (uint32_t)(result);
loc_009DB057:
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)((uint32_t)(v_stack_p30))));
    v_stack_p3C = (uint32_t)(local_rsi);
    if (((uint32_t)(local_rsi)) < ((uint32_t)((uint32_t)(v_stack_p30)))) goto loc_009DAF74;
loc_009DB085:
    local_r15 = ((uint32_t)((uint32_t)(local_rsi))) + (v_stack_p110);
    v_stack_pA8 = local_r15;
    local_rsi = (uint32_t)((local_rsi) + (64));
    v_stack_p3C = (uint32_t)(local_rsi);
    if (((uint32_t)(local_rsi)) < 64) goto loc_009DAF74;
    if (((uint32_t)(local_rsi)) >= ((uint32_t)((uint32_t)(v_stack_p118)))) goto loc_009DAFAB;
    *(uint32_t *)(local_r15) = 0;
    result = v_stack_p88;
    if ((uint32_t)((uint32_t)(v_stack_p100)) != 0) { result = 0; }
    *(uint64_t *)(local_r15 + 0x8) = result;
    *(uint64_t *)(local_r15 + 0x10) = *(uint64_t *)(v_stack_p90 + 0x10);
    *(uint16_t *)(local_r15 + 0x18) = (uint16_t)(*(uint16_t *)(v_stack_p90 + 0x18));
    *(uint32_t *)(local_r15 + 0x1C) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p98)));
    *(uint32_t *)(local_r15 + 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p98 + 0x8)));
    *(uint16_t *)(local_r15 + 0x1A) = (uint16_t)(*(uint8_t *)(v_stack_p98 + 0x1B));
    result = (*(uint64_t *)(v_stack_p98 + 0x28)) & (-16);
    *(uint64_t *)(local_r15 + 0x38) = result;
    if ((uint32_t)((uint32_t)(v_stack_p100)) != 0) { result = 0; }
    *(uint64_t *)(local_r15 + 0x38) = result;
    result = OBJECT_HEADER_TO_QUOTA_INFO(v_stack_p98, (uint32_t)(v_stack_p100), Arg3, v_stack_p98);
    if (result != 0) {
        Arg2 = *(uint32_t *)(result);
        Arg3 = *(uint32_t *)(result + 0x4);
    }
    *(uint32_t *)(local_r15 + 0x24) = (uint32_t)(Arg2);
    *(uint32_t *)(local_r15 + 0x28) = (uint32_t)(Arg3);
    result = OBJECT_HEADER_TO_PROCESS_INFO(v_stack_p98, Arg2, Arg3, v_stack_p98);
    Arg3 = 0;
    if (result == 0) goto loc_009DB153;
    result = *(uint64_t *)(result);
    if (*(uint64_t *)(result) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result) + 0x1D0);
        *(uint64_t *)(local_r15 + 0x30) = result;
    }
    v_stack_p30 = 0;
    v_stack_p40 = 0;
    if ((*(uint64_t *)(v_stack_p58 + 0xA0)) == 0) goto loc_009DB229;
    if (v_stack_p58 != (*(uint64_t *)(v_rip + 0x5EB967))) goto loc_009DB229;
    *(uint64_t *)(result) = v_xmm0;
    if ((uint16_t)(*(uint16_t *)(result)) == 0) goto loc_009DB300;
    if ((*(uint64_t *)(result + 0x8)) == 0) goto loc_009DB300;
    result = (uint32_t)((*(uint16_t *)(result)) + (2));
    v_stack_p30 = (uint32_t)(result);
    if (((uint32_t)(result)) >= = 520) {
        v_stack_p30 = 520;
        result = 520 - 2;
        *(uint16_t *)(result) = (uint16_t)(result);
        result = v_stack_p30;
    }
    local_rbx = (result) + (16);
    Arg3 = ((uint32_t)((uint32_t)(result))) - (2);
    result = memcpy(local_rbx, *(uint64_t *)(v_stack_p48 + 0x8), Arg3, v_stack_p98);
    *(uint64_t *)(v_stack_p48 + 0x8) = local_rbx;
    *(uint16_t *)(v_stack_p48 + 0x2) = (uint16_t)((uint32_t)(v_stack_p30));
    result = (uint32_t)((*(uint16_t *)(v_stack_p48)) >> (1));
    Arg3 = 0;
    *(uint16_t *)(local_rbx + result * 2) = 0;
    goto loc_009DB305;
loc_009DB210:
    if (((uint32_t)(local_rsi)) >= ((uint32_t)((uint32_t)(v_stack_p118)))) goto loc_009DB085;
    *(uint32_t *)(local_r15) = (uint32_t)(local_rsi);
    goto loc_009DB085;
loc_009DB229:
    v_stack_p20 = 0;
    result = ObQueryNameStringMode(v_stack_p88, v_stack_p48, (uint32_t)(v_stack_p60), v_stack_p30);
    v_stack_p40 = (uint32_t)(result);
    if (((uint32_t)(result)) != 0xC0000004ULL) goto loc_009DB2F5;
    if (((uint32_t)(v_stack_p30)) <= v_stack_p60) goto loc_009DB2FD;
    if (((uint32_t)(local_rsi + (uint32_t)(v_stack_p30) * 1)) >= ((uint32_t)((uint32_t)(v_stack_p118)))) goto loc_009DB2FD;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(v_stack_p30))), (uint32_t)(0x7241624FULL), v_stack_p30);
    v_stack_p80 = result;
    Arg3 = 0;
    if (result == 0) goto loc_009DB37A;
    result = ExFreePoolWithTag(result, (uint32_t)(0x7241624FULL), Arg3, v_stack_p30);
    v_stack_p60 = (uint32_t)(v_stack_p30);
    v_stack_p90 = (uint32_t)(v_stack_p30);
    v_stack_p48 = result;
    v_stack_pB0 = result;
    Arg1 = 0;
    v_stack_p20 = 0;
    result = ObQueryNameStringMode(v_stack_p88, result, (uint32_t)((uint32_t)((uint32_t)(v_stack_p30))), v_stack_p30);
    v_stack_p40 = (uint32_t)(result);
loc_009DB2F5:
loc_009DB2FD:
    Arg3 = 0;
loc_009DB300:
loc_009DB305:
    if ((uint32_t)((uint32_t)(v_stack_p30)) == 0) goto loc_009DB3CE;
    result = (uint32_t)(((uint32_t)(v_stack_p30)) + (7));
    result = (uint32_t)((result) & (0xFFFFFFF8ULL));
    v_stack_p30 = (uint32_t)(result);
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)(result)));
    v_stack_p3C = (uint32_t)(local_rsi);
    if (((uint32_t)(local_rsi)) < ((uint32_t)(result))) goto loc_009DAF74;
    if (sign_flag) goto loc_009DB3A7;
    if ((uint16_t)(*(uint16_t *)(result)) == 0) goto loc_009DB39B;
    if (((uint32_t)(local_rsi)) >= ((uint32_t)((uint32_t)(v_stack_p118)))) goto loc_009DB39B;
    local_rdi = (uint32_t)((2) + ((uint32_t)(*(uint16_t *)(result))));
    *(uint16_t *)(local_r15 + 0x40) = (uint16_t)(*(uint16_t *)(result));
    result = memcpy(local_r15 + 80, *(uint64_t *)(v_stack_p48 + 0x8), (uint16_t)(local_rdi), v_stack_p30);
    local_rbx = (local_r15 + 80) - (v_stack_p110);
    local_rbx = (local_rbx) + (v_stack_p108);
    *(uint64_t *)(local_r15 + 0x48) = local_rbx;
    *(uint16_t *)(local_r15 + 0x42) = (uint16_t)(local_rdi);
    goto loc_009DB3F9;
loc_009DB37A:
    v_stack_p80 = local_rdi;
    v_stack_p40 = (uint32_t)((uint32_t)(0xC000009AULL));
    goto loc_009DB300;
loc_009DB39B:
    if (sign_flag) goto loc_009DB3A7;
    if ((*(uint16_t *)(local_rbx)) == ((uint16_t)((uint16_t)(local_rdi)))) goto loc_009DB3DC;
    goto loc_009DB3E1;
loc_009DB3A7:
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)(local_r15 + 80)));
    v_stack_p3C = (uint32_t)(local_rsi);
    if (((uint32_t)(local_rsi)) < ((uint32_t)(local_r15 + 80))) goto loc_009DAF74;
    if (((uint32_t)(local_rsi)) >= ((uint32_t)((uint32_t)(v_stack_p118)))) goto loc_009DB3E1;
    Arg2 = 0;
    result = RtlInitUnicodeString(local_r15 + 64, Arg2, (uint16_t)(local_rdi), v_stack_p30);
    v_stack_p34 = (uint32_t)((uint32_t)(0xC000009AULL));
    goto loc_009DB3F9;
loc_009DB3CE:
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)(local_r15 + 64)));
    v_stack_p3C = (uint32_t)(local_rsi);
    if (((uint32_t)(local_rsi)) < ((uint32_t)(local_r15 + 64))) goto loc_009DAF74;
loc_009DB3DC:
    if (((uint32_t)(local_rsi)) < ((uint32_t)((uint32_t)(v_stack_p118)))) goto loc_009DB3EE;
loc_009DB3E1:
    v_stack_p34 = (uint32_t)((uint32_t)(0xC0000004ULL));
    goto loc_009DB3FC;
loc_009DB3EE:
    Arg2 = 0;
    result = RtlInitUnicodeString(local_r15 + 64, Arg2, (uint16_t)(local_rdi), v_stack_p30);
loc_009DB3F9:
    Arg3 = 0;
loc_009DB3FC:
loc_009DB40E:
    result = (uint32_t)(((uint32_t)(v_stack_p50)) + 1);
    goto loc_009DAEF7;
loc_009DB415:
    if (Arg5 != 0) {
        *(uint32_t *)(Arg5) = (uint32_t)(local_rsi);
    }
    result = Arg5;
    if (0 != 0) {
        Arg1 = 0;
        result = ObpDestroyTypeArray(Arg1, v_stack_p38, Arg3, v_stack_p30);
        Arg1 = v_stack_p78;
    }
    result = ObpDestroyTypeArray(Arg1, v_stack_p38, Arg3, v_stack_p30);
    result = ExFreePoolWithTag(local_rdi, (uint32_t)(0x7241624FULL), Arg3, v_stack_p30);
    local_r14 = (uint32_t)(0xC0000004ULL);
    if (v_stack_p68 == 0) { local_r14 = (uint32_t)((uint32_t)(0xC0000001ULL)); }
    goto loc_009DAE46;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009DADE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
