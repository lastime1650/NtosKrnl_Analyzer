# PiDmObjectProcessPropertyChange

- RVA: `0x008F8A48`–`0x008F8E78` (길이 `1,072` bytes)
- VA: `0x00000001408F8A48`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00087BC0`
- 디코드: `300`개 명령, `1,072/1,072` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x008F8ABB` → [PiDmGetCachedKeyIndex](PiDmGetCachedKeyIndex_function_008F8E80.md) (function, `0x008F8E80`)
- `0x008F8B16` → [PiDmObjectReleaseLock](../8E/PiDmObjectReleaseLock_function_008E5584.md) (function, `0x008E5584`)
- `0x008F8B2C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008F8B3E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008F8B4B` → [PiDmObjectRelease](../8E/PiDmObjectRelease_function_008E4F70.md) (function, `0x008E4F70`)
- `0x008F8B5D` → [PiDmObjectRelease](../8E/PiDmObjectRelease_function_008E4F70.md) (function, `0x008E4F70`)
- `0x008F8BE3` → [PiDmGetReferencedObjectFromProperty](../A7/PiDmGetReferencedObjectFromProperty_function_00A776F0.md) (function, `0x00A776F0`)
- `0x008F8BFB` → [CmpLockSiloKeyLockTrackerExclusive](CmpLockSiloKeyLockTrackerExclusive_function_008F9EF8.md) (function, `0x008F9EF8`)
- `0x008F8CAE` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E1110.md) (function, `0x008E1110`)
- `0x008F8CD2` → [CmpLockSiloKeyLockTrackerExclusive](CmpLockSiloKeyLockTrackerExclusive_function_008F9EF8.md) (function, `0x008F9EF8`)
- `0x008F8D1E` → [PiDmCacheDataDecode](PiDmCacheDataDecode_function_008F17A0.md) (function, `0x008F17A0`)
- `0x008F8D57` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008F8D7B` → [PiDmCacheDataDecode](PiDmCacheDataDecode_function_008F17A0.md) (function, `0x008F17A0`)
- `0x008F8DA6` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x008F8DBD` → [PiDmObjectReleaseLock](../8E/PiDmObjectReleaseLock_function_008E5584.md) (function, `0x008E5584`)
- `0x008F8DDE` → [PiDmCacheDataFree](PiDmCacheDataFree_function_008F9C48.md) (function, `0x008F9C48`)
- `0x008F8E10` → [PiDmCacheDataEncode](PiDmCacheDataEncode_function_008FB79C.md) (function, `0x008FB79C`)
- `0x008F8E51` → [PiDmGetObject](../8D/PiDmGetObject_function_008DFAE0.md) (function, `0x008DFAE0`)

### Direct callers
- [PiPnpRtlObjectEventWorker](PiPnpRtlObjectEventWorker_function_008F8630.md) at `0x008F871B`

### Static image references
- `0x008F8AAA` → RVA `0x00001A70` (`.rdata`; read)
- `0x008F8AE5` → RVA `0x00001B60` (`.rdata`; read)
- `0x008F8AF6` → RVA `0x00001B90` (`.rdata`; read)
- `0x008F8B73` → RVA `0x00001EE0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x008F8B2C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008F8B3E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008F8D57` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008F8DA6` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008F8A48  48 8B C4                        mov rax, rsp
008F8A4B  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
008F8A4F  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
008F8A53  89 48 08                        mov dword ptr [rax + 8], ecx
008F8A56  55                              push rbp
008F8A57  53                              push rbx
008F8A58  56                              push rsi
008F8A59  57                              push rdi
008F8A5A  41 54                           push r12
008F8A5C  41 55                           push r13
008F8A5E  41 56                           push r14
008F8A60  41 57                           push r15
008F8A62  48 8D 68 B1                     lea rbp, [rax - 0x4f]
008F8A66  48 81 EC 98 00 00 00            sub rsp, 0x98
008F8A6D  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
008F8A71  33 D2                           xor edx, edx
008F8A73  89 55 DF                        mov dword ptr [rbp - 0x21], edx
008F8A76  4D 8B E8                        mov r13, r8
008F8A79  89 55 E3                        mov dword ptr [rbp - 0x1d], edx
008F8A7C  8B F2                           mov esi, edx
008F8A7E  89 55 E7                        mov dword ptr [rbp - 0x19], edx
008F8A81  44 8B FA                        mov r15d, edx
008F8A84  88 10                           mov byte ptr [rax], dl
008F8A86  44 8B E2                        mov r12d, edx
008F8A89  88 55 6F                        mov byte ptr [rbp + 0x6f], dl
008F8A8C  8B DA                           mov ebx, edx
008F8A8E  48 89 55 EF                     mov qword ptr [rbp - 0x11], rdx
008F8A92  48 89 55 F7                     mov qword ptr [rbp - 9], rdx
008F8A96  89 55 DB                        mov dword ptr [rbp - 0x25], edx
008F8A99  89 55 D7                        mov dword ptr [rbp - 0x29], edx
008F8A9C  48 89 55 FF                     mov qword ptr [rbp - 1], rdx
008F8AA0  4D 85 C9                        test r9, r9
008F8AA3  75 26                           jne 0x1408f8acb
008F8AA5  83 E9 01                        sub ecx, 1
008F8AA8  75 36                           jne 0x1408f8ae0
008F8AAA  48 8D 3D BF 8F 70 FF            lea rdi, [rip - 0x8f7041]
008F8AB1  8D 53 0A                        lea edx, [rbx + 0xa]
008F8AB4  4C 8B 45 77                     mov r8, qword ptr [rbp + 0x77]
008F8AB8  48 8B CF                        mov rcx, rdi
008F8ABB  E8 C0 03 00 00                  call 0x1408f8e80
008F8AC0  44 8B F0                        mov r14d, eax
008F8AC3  3B C2                           cmp eax, edx
008F8AC5  0F 82 86 01 00 00               jb 0x1408f8c51
008F8ACB  48 81 C4 98 00 00 00            add rsp, 0x98
008F8AD2  41 5F                           pop r15
008F8AD4  41 5E                           pop r14
008F8AD6  41 5D                           pop r13
008F8AD8  41 5C                           pop r12
008F8ADA  5F                              pop rdi
008F8ADB  5E                              pop rsi
008F8ADC  5B                              pop rbx
008F8ADD  5D                              pop rbp
008F8ADE  C3                              ret
008F8ADF  CC                              int3
008F8AE0  83 E9 02                        sub ecx, 2
008F8AE3  75 0C                           jne 0x1408f8af1
008F8AE5  48 8D 3D 74 90 70 FF            lea rdi, [rip - 0x8f6f8c]
008F8AEC  8D 51 01                        lea edx, [rcx + 1]
008F8AEF  EB C3                           jmp 0x1408f8ab4
008F8AF1  83 F9 02                        cmp ecx, 2
008F8AF4  75 D5                           jne 0x1408f8acb
008F8AF6  48 8D 3D 93 90 70 FF            lea rdi, [rip - 0x8f6f6d]
008F8AFD  8D 51 01                        lea edx, [rcx + 1]
008F8B00  EB B2                           jmp 0x1408f8ab4
008F8B02  83 7D D7 11                     cmp dword ptr [rbp - 0x29], 0x11
008F8B06  75 0B                           jne 0x1408f8b13
008F8B08  41 80 3F FF                     cmp byte ptr [r15], 0xff
008F8B0C  75 05                           jne 0x1408f8b13
008F8B0E  FF C0                           inc eax
008F8B10  89 04 3B                        mov dword ptr [rbx + rdi], eax
008F8B13  48 8B CB                        mov rcx, rbx
008F8B16  E8 69 CA FE FF                  call 0x1408e5584
008F8B1B  48 8B 45 EF                     mov rax, qword ptr [rbp - 0x11]
008F8B1F  48 85 C0                        test rax, rax
008F8B22  74 0D                           je 0x1408f8b31
008F8B24  BA 50 6E 70 5A                  mov edx, 0x5a706e50
008F8B29  48 8B C8                        mov rcx, rax
008F8B2C  E8 3F 9D 28 00                  call 0x140b82870
008F8B31  4D 85 FF                        test r15, r15
008F8B34  74 0D                           je 0x1408f8b43
008F8B36  BA 50 6E 70 5A                  mov edx, 0x5a706e50
008F8B3B  49 8B CF                        mov rcx, r15
008F8B3E  E8 2D 9D 28 00                  call 0x140b82870
008F8B43  48 85 DB                        test rbx, rbx
008F8B46  74 08                           je 0x1408f8b50
008F8B48  48 8B CB                        mov rcx, rbx
008F8B4B  E8 20 C4 FE FF                  call 0x1408e4f70
008F8B50  80 7D 6F 00                     cmp byte ptr [rbp + 0x6f], 0
008F8B54  0F 84 71 FF FF FF               je 0x1408f8acb
008F8B5A  49 8B CD                        mov rcx, r13
008F8B5D  E8 0E C4 FE FF                  call 0x1408e4f70
008F8B62  E9 64 FF FF FF                  jmp 0x1408f8acb
008F8B67  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
008F8B6B  38 18                           cmp byte ptr [rax], bl
008F8B6D  75 AC                           jne 0x1408f8b1b
008F8B6F  4C 8B 55 77                     mov r10, qword ptr [rbp + 0x77]
008F8B73  4C 8D 1D 66 93 70 FF            lea r11, [rip - 0x8f6c9a]
008F8B7A  33 D2                           xor edx, edx
008F8B7C  83 FA 03                        cmp edx, 3
008F8B7F  73 9A                           jae 0x1408f8b1b
008F8B81  8B C2                           mov eax, edx
008F8B83  4C 6B C8 38                     imul r9, rax, 0x38
008F8B87  41 8B 42 10                     mov eax, dword ptr [r10 + 0x10]
008F8B8B  4F 8B 44 19 08                  mov r8, qword ptr [r9 + r11 + 8]
008F8B90  41 39 40 10                     cmp dword ptr [r8 + 0x10], eax
008F8B94  74 04                           je 0x1408f8b9a
008F8B96  FF C2                           inc edx
008F8B98  EB E2                           jmp 0x1408f8b7c
008F8B9A  49 8B 08                        mov rcx, qword ptr [r8]
008F8B9D  49 2B 0A                        sub rcx, qword ptr [r10]
008F8BA0  75 08                           jne 0x1408f8baa
008F8BA2  49 8B 48 08                     mov rcx, qword ptr [r8 + 8]
008F8BA6  49 2B 4A 08                     sub rcx, qword ptr [r10 + 8]
008F8BAA  48 85 C9                        test rcx, rcx
008F8BAD  75 E7                           jne 0x1408f8b96
008F8BAF  8B 4D 57                        mov ecx, dword ptr [rbp + 0x57]
008F8BB2  4B 8D 3C 19                     lea rdi, [r9 + r11]
008F8BB6  3B 0F                           cmp ecx, dword ptr [rdi]
008F8BB8  75 DC                           jne 0x1408f8b96
008F8BBA  48 85 FF                        test rdi, rdi
008F8BBD  0F 84 58 FF FF FF               je 0x1408f8b1b
008F8BC3  48 8B 55 5F                     mov rdx, qword ptr [rbp + 0x5f]
008F8BC7  48 8D 45 FF                     lea rax, [rbp - 1]
008F8BCB  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008F8BD0  4D 8B C5                        mov r8, r13
008F8BD3  8B 47 18                        mov eax, dword ptr [rdi + 0x18]
008F8BD6  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
008F8BDA  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
008F8BDE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008F8BE3  E8 08 EB 17 00                  call 0x140a776f0
008F8BE8  48 8B 5D FF                     mov rbx, qword ptr [rbp - 1]
008F8BEC  85 C0                           test eax, eax
008F8BEE  0F 88 27 FF FF FF               js 0x1408f8b1b
008F8BF4  48 8B 7F 30                     mov rdi, qword ptr [rdi + 0x30]
008F8BF8  48 8B CB                        mov rcx, rbx
008F8BFB  E8 F8 12 00 00                  call 0x1408f9ef8
008F8C00  B9 00 00 00 80                  mov ecx, 0x80000000
008F8C05  85 F6                           test esi, esi
008F8C07  78 40                           js 0x1408f8c49
008F8C09  8B 04 3B                        mov eax, dword ptr [rbx + rdi]
008F8C0C  3B C1                           cmp eax, ecx
008F8C0E  74 39                           je 0x1408f8c49
008F8C10  41 83 FC 11                     cmp r12d, 0x11
008F8C14  0F 85 E8 FE FF FF               jne 0x1408f8b02
008F8C1A  48 8B 4D EF                     mov rcx, qword ptr [rbp - 0x11]
008F8C1E  8A 09                           mov cl, byte ptr [rcx]
008F8C20  80 F9 FF                        cmp cl, 0xff
008F8C23  74 0D                           je 0x1408f8c32
008F8C25  84 C9                           test cl, cl
008F8C27  0F 85 E6 FE FF FF               jne 0x1408f8b13
008F8C2D  E9 D0 FE FF FF                  jmp 0x1408f8b02
008F8C32  83 7D D7 11                     cmp dword ptr [rbp - 0x29], 0x11
008F8C36  75 0A                           jne 0x1408f8c42
008F8C38  41 80 3F 00                     cmp byte ptr [r15], 0
008F8C3C  0F 85 D1 FE FF FF               jne 0x1408f8b13
008F8C42  FF C8                           dec eax
008F8C44  E9 C7 FE FF FF                  jmp 0x1408f8b10
008F8C49  89 0C 3B                        mov dword ptr [rbx + rdi], ecx
008F8C4C  E9 C2 FE FF FF                  jmp 0x1408f8b13
008F8C51  4D 85 ED                        test r13, r13
008F8C54  0F 84 EC 01 00 00               je 0x1408f8e46
008F8C5A  4F 8D 34 76                     lea r14, [r14 + r14*2]
008F8C5E  42 83 7C F7 10 01               cmp dword ptr [rdi + r14*8 + 0x10], 1
008F8C64  75 69                           jne 0x1408f8ccf
008F8C66  44 8B 4D 57                     mov r9d, dword ptr [rbp + 0x57]
008F8C6A  48 8D 45 E7                     lea rax, [rbp - 0x19]
008F8C6E  4C 8B 45 5F                     mov r8, qword ptr [rbp + 0x5f]
008F8C72  BA 10 00 00 00                  mov edx, 0x10
008F8C77  C7 44 24 50 00 00 01 00         mov dword ptr [rsp + 0x50], 0x10000
008F8C7F  B9 50 6E 70 5A                  mov ecx, 0x5a706e50
008F8C84  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
008F8C89  48 8D 45 F7                     lea rax, [rbp - 9]
008F8C8D  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
008F8C92  48 8D 45 D7                     lea rax, [rbp - 0x29]
008F8C96  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008F8C9B  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
008F8C9F  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008F8CA4  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
008F8CA9  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
008F8CAE  E8 5D 84 FE FF                  call 0x1408e1110
008F8CB3  8B F0                           mov esi, eax
008F8CB5  3D 25 02 00 C0                  cmp eax, 0xc0000225
008F8CBA  0F 85 AD 01 00 00               jne 0x1408f8e6d
008F8CC0  41 8B F7                        mov esi, r15d
008F8CC3  44 89 7D D7                     mov dword ptr [rbp - 0x29], r15d
008F8CC7  44 89 7D E3                     mov dword ptr [rbp - 0x1d], r15d
008F8CCB  4C 8B 7D F7                     mov r15, qword ptr [rbp - 9]
008F8CCF  49 8B CD                        mov rcx, r13
008F8CD2  E8 21 12 00 00                  call 0x1408f9ef8
008F8CD7  4F 8D 6C F5 00                  lea r13, [r13 + r14*8]
008F8CDC  49 83 C5 70                     add r13, 0x70
008F8CE0  41 8B 45 00                     mov eax, dword ptr [r13]
008F8CE4  85 C0                           test eax, eax
008F8CE6  0F 84 4D 01 00 00               je 0x1408f8e39
008F8CEC  83 F8 01                        cmp eax, 1
008F8CEF  0F 84 E6 00 00 00               je 0x1408f8ddb
008F8CF5  85 F6                           test esi, esi
008F8CF7  0F 88 DE 00 00 00               js 0x1408f8ddb
008F8CFD  42 39 5C F7 10                  cmp dword ptr [rdi + r14*8 + 0x10], ebx
008F8D02  0F 84 D3 00 00 00               je 0x1408f8ddb
008F8D08  48 8D 45 DF                     lea rax, [rbp - 0x21]
008F8D0C  45 33 C9                        xor r9d, r9d
008F8D0F  45 33 C0                        xor r8d, r8d
008F8D12  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008F8D17  48 8D 55 DB                     lea rdx, [rbp - 0x25]
008F8D1B  49 8B CD                        mov rcx, r13
008F8D1E  E8 7D 8A FF FF                  call 0x1408f17a0
008F8D23  8B F0                           mov esi, eax
008F8D25  3D 25 02 00 C0                  cmp eax, 0xc0000225
008F8D2A  0F 84 F7 00 00 00               je 0x1408f8e27
008F8D30  B9 00 00 00 80                  mov ecx, 0x80000000
008F8D35  03 C1                           add eax, ecx
008F8D37  85 C1                           test ecx, eax
008F8D39  0F 84 DA 00 00 00               je 0x1408f8e19
008F8D3F  8B 75 DF                        mov esi, dword ptr [rbp - 0x21]
008F8D42  85 F6                           test esi, esi
008F8D44  0F 84 E7 00 00 00               je 0x1408f8e31
008F8D4A  8B D6                           mov edx, esi
008F8D4C  B9 00 01 00 00                  mov ecx, 0x100
008F8D51  41 B8 50 6E 70 5A               mov r8d, 0x5a706e50
008F8D57  E8 94 93 28 00                  call 0x140b820f0
008F8D5C  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
008F8D60  48 85 C0                        test rax, rax
008F8D63  74 6D                           je 0x1408f8dd2
008F8D65  48 8D 4D DF                     lea rcx, [rbp - 0x21]
008F8D69  44 8B CE                        mov r9d, esi
008F8D6C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
008F8D71  48 8D 55 DB                     lea rdx, [rbp - 0x25]
008F8D75  49 8B CD                        mov rcx, r13
008F8D78  4C 8B C0                        mov r8, rax
008F8D7B  E8 20 8A FF FF                  call 0x1408f17a0
008F8D80  8B F0                           mov esi, eax
008F8D82  85 C0                           test eax, eax
008F8D84  78 51                           js 0x1408f8dd7
008F8D86  44 8B 65 DB                     mov r12d, dword ptr [rbp - 0x25]
008F8D8A  44 3B 65 D7                     cmp r12d, dword ptr [rbp - 0x29]
008F8D8E  75 4B                           jne 0x1408f8ddb
008F8D90  8B 45 DF                        mov eax, dword ptr [rbp - 0x21]
008F8D93  3B 45 E3                        cmp eax, dword ptr [rbp - 0x1d]
008F8D96  75 43                           jne 0x1408f8ddb
008F8D98  85 C0                           test eax, eax
008F8D9A  74 13                           je 0x1408f8daf
008F8D9C  48 8B 4D EF                     mov rcx, qword ptr [rbp - 0x11]
008F8DA0  44 8B C0                        mov r8d, eax
008F8DA3  49 8B D7                        mov rdx, r15
008F8DA6  E8 65 DD DC FF                  call 0x1406c6b10
008F8DAB  85 C0                           test eax, eax
008F8DAD  75 2C                           jne 0x1408f8ddb
008F8DAF  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
008F8DB3  C6 00 01                        mov byte ptr [rax], 1
008F8DB6  4C 8B 6D 67                     mov r13, qword ptr [rbp + 0x67]
008F8DBA  49 8B CD                        mov rcx, r13
008F8DBD  E8 C2 C7 FE FF                  call 0x1408e5584
008F8DC2  42 39 5C F7 10                  cmp dword ptr [rdi + r14*8 + 0x10], ebx
008F8DC7  0F 84 4E FD FF FF               je 0x1408f8b1b
008F8DCD  E9 95 FD FF FF                  jmp 0x1408f8b67
008F8DD2  BE 9A 00 00 C0                  mov esi, 0xc000009a
008F8DD7  44 8B 65 DB                     mov r12d, dword ptr [rbp - 0x25]
008F8DDB  49 8B CD                        mov rcx, r13
008F8DDE  E8 65 0E 00 00                  call 0x1408f9c48
008F8DE3  85 F6                           test esi, esi
008F8DE5  78 CF                           js 0x1408f8db6
008F8DE7  42 83 7C F7 10 01               cmp dword ptr [rdi + r14*8 + 0x10], 1
008F8DED  75 C7                           jne 0x1408f8db6
008F8DEF  42 8B 44 F7 0C                  mov eax, dword ptr [rdi + r14*8 + 0xc]
008F8DF4  85 C0                           test eax, eax
008F8DF6  75 BE                           jne 0x1408f8db6
008F8DF8  46 8B 4C F7 08                  mov r9d, dword ptr [rdi + r14*8 + 8]
008F8DFD  49 8B D7                        mov rdx, r15
008F8E00  44 8B 45 E3                     mov r8d, dword ptr [rbp - 0x1d]
008F8E04  8B 4D D7                        mov ecx, dword ptr [rbp - 0x29]
008F8E07  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
008F8E0C  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008F8E10  E8 87 29 00 00                  call 0x1408fb79c
008F8E15  8B F0                           mov esi, eax
008F8E17  EB 9D                           jmp 0x1408f8db6
008F8E19  81 FE 23 00 00 C0               cmp esi, 0xc0000023
008F8E1F  0F 84 1A FF FF FF               je 0x1408f8d3f
008F8E25  EB B0                           jmp 0x1408f8dd7
008F8E27  33 F6                           xor esi, esi
008F8E29  39 5D D7                        cmp dword ptr [rbp - 0x29], ebx
008F8E2C  E9 7C FF FF FF                  jmp 0x1408f8dad
008F8E31  48 8B C3                        mov rax, rbx
008F8E34  E9 2C FF FF FF                  jmp 0x1408f8d65
008F8E39  42 39 5C F7 10                  cmp dword ptr [rdi + r14*8 + 0x10], ebx
008F8E3E  0F 84 72 FF FF FF               je 0x1408f8db6
008F8E44  EB 95                           jmp 0x1408f8ddb
008F8E46  48 8B 55 5F                     mov rdx, qword ptr [rbp + 0x5f]
008F8E4A  4C 8D 45 67                     lea r8, [rbp + 0x67]
008F8E4E  8B 4D 57                        mov ecx, dword ptr [rbp + 0x57]
008F8E51  E8 8A 6C FE FF                  call 0x1408dfae0
008F8E56  8B F0                           mov esi, eax
008F8E58  85 C0                           test eax, eax
008F8E5A  0F 88 6B FC FF FF               js 0x1408f8acb
008F8E60  4C 8B 6D 67                     mov r13, qword ptr [rbp + 0x67]
008F8E64  C6 45 6F 01                     mov byte ptr [rbp + 0x6f], 1
008F8E68  E9 ED FD FF FF                  jmp 0x1408f8c5a
008F8E6D  8B 45 E7                        mov eax, dword ptr [rbp - 0x19]
008F8E70  89 45 E3                        mov dword ptr [rbp - 0x1d], eax
008F8E73  E9 53 FE FF FF                  jmp 0x1408f8ccb
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDmObjectProcessPropertyChange(int a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p50;

    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned int *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (152);
    a2 = 0;
    *(unsigned int *)(v_rsp - 79 - 33) = 0;
    *(unsigned int *)(v_rsp - 79 - 29) = 0;
    *(unsigned int *)(v_rsp - 79 - 25) = 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 79 + 127)) = 0;
    *(unsigned __int8 *)(v_rsp - 79 + 111) = 0;
    *(unsigned __int64 *)(v_rsp - 79 - 17) = 0;
    *(unsigned __int64 *)(v_rsp - 79 - 9) = 0;
    *(unsigned int *)(v_rsp - 79 - 37) = 0;
    *(unsigned int *)(v_rsp - 79 - 41) = 0;
    *(unsigned __int64 *)(v_rsp - 79 - 1) = 0;
    if (a4 != 0) goto loc_008F8ACB;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_not_equal) goto loc_008F8AE0;
loc_008F8AB4:
    result = PiDmGetCachedKeyIndex(v_rip - 9400385, 0 + 10, *(unsigned __int64 *)(v_rsp - 79 + 119), a4);
    if (((unsigned int)(result)) < ((unsigned int)(0 + 10))) goto loc_008F8C51;
loc_008F8ACB:
    v_rsp = (v_rsp) + (152);
    return result;
loc_008F8AE0:
    a1 = (unsigned int)((v_rip - 9400385) - (2));
    if (condition_is_not_equal) goto loc_008F8AF1;
    goto loc_008F8AB4;
loc_008F8AF1:
    if (a1 != 2) goto loc_008F8ACB;
    goto loc_008F8AB4;
loc_008F8B02:
    if ((*(unsigned int *)(v_rsp - 79 - 41)) != 17) goto loc_008F8B13;
    if ((*(unsigned __int8 *)(0)) != 255) goto loc_008F8B13;
    result = (unsigned int)((result) + 1);
loc_008F8B10:
    *(unsigned int *)(0 + v_rip - 9400173 * 1) = (unsigned int)(result);
loc_008F8B13:
    result = PiDmObjectReleaseLock(0, a1 + 1, *(unsigned __int64 *)(v_rsp - 79 + 119), a4);
loc_008F8B1B:
    result = *(unsigned __int64 *)(v_rsp - 79 - 17);
    if (*(unsigned __int64 *)(v_rsp - 79 - 17) != 0) {
        a2 = 0x5A706E50ULL;
        a1 = *(unsigned __int64 *)(v_rsp - 79 - 17);
        result = ExFreePoolWithTag(a1, a2, *(unsigned __int64 *)(v_rsp - 79 + 119), a4);
    }
    if (0 != 0) {
        a2 = 0x5A706E50ULL;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, *(unsigned __int64 *)(v_rsp - 79 + 119), a4);
    }
    if (0 != 0) {
        a1 = 0;
        result = PiDmObjectRelease(a1, a2, *(unsigned __int64 *)(v_rsp - 79 + 119), a4);
    }
    if ((*(unsigned __int8 *)(v_rsp - 79 + 111)) == 0) goto loc_008F8ACB;
    result = PiDmObjectRelease(a3, a2, *(unsigned __int64 *)(v_rsp - 79 + 119), a4);
    goto loc_008F8ACB;
loc_008F8B67:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 79 + 127))) != 0) goto loc_008F8B1B;
    a2 = 0;
loc_008F8B7C:
    if (0 >= 3) goto loc_008F8B1B;
    a4 = (a4) * (0);
    if ((*(unsigned int *)(*(unsigned __int64 *)(a4 + v_rip - 9399450 * 1 + 8) + 16)) == ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 79 + 119) + 16))))) goto loc_008F8B9A;
loc_008F8B96:
    a2 = (unsigned int)((a2) + 1);
    goto loc_008F8B7C;
loc_008F8B9A:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + v_rip - 9399450 * 1 + 8))) - (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 79 + 119)));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a4 + v_rip - 9399450 * 1 + 8) + 8);
        a1 = (a1) - (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 79 + 119) + 8));
    }
    if (a1 != 0) goto loc_008F8B96;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 + 87)))) != (*(unsigned int *)(a4 + v_rip - 9399450 * 1))) goto loc_008F8B96;
    if (a4 + v_rip - 9399450 * 1 == 0) goto loc_008F8B1B;
    v_stack_p30 = v_rsp - 79 - 1;
    v_stack_p28 = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + v_rip - 9399450 * 1 + 24)));
    v_stack_p20 = *(unsigned __int64 *)(a4 + v_rip - 9399450 * 1 + 16);
    result = PiDmGetReferencedObjectFromProperty((unsigned int)(*(unsigned int *)(v_rsp - 79 + 87)), *(unsigned __int64 *)(v_rsp - 79 + 95), a3, a4);
    if (sign_flag) goto loc_008F8B1B;
    result = CmpLockSiloKeyLockTrackerExclusive(*(unsigned __int64 *)(v_rsp - 79 - 1), *(unsigned __int64 *)(v_rsp - 79 + 95), a3, a4);
    if (sign_flag) goto loc_008F8C49;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 79 - 1) + *(unsigned __int64 *)(a4 + v_rip - 9399450 * 1 + 48) * 1)))) == ((unsigned int)((unsigned int)(0x80000000ULL)))) goto loc_008F8C49;
    if (0 != 17) goto loc_008F8B02;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 79 - 17)))) == 255) goto loc_008F8C32;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 79 - 17))) != 0) goto loc_008F8B13;
    goto loc_008F8B02;
loc_008F8C32:
    if ((*(unsigned int *)(v_rsp - 79 - 41)) != 17) goto loc_008F8C42;
    if ((*(unsigned __int8 *)(0)) != 0) goto loc_008F8B13;
loc_008F8C42:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 79 - 1) + *(unsigned __int64 *)(a4 + v_rip - 9399450 * 1 + 48) * 1))) - 1);
    goto loc_008F8B10;
loc_008F8C49:
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 79 - 1) + *(unsigned __int64 *)(a4 + v_rip - 9399450 * 1 + 48) * 1) = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 79 - 17)));
    goto loc_008F8B13;
loc_008F8C51:
    if (a3 == 0) goto loc_008F8E46;
loc_008F8C5A:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a4 + v_rip - 9399450 * 1 + 48) + (unsigned int)((unsigned int)(result)) + (unsigned int)((unsigned int)(result)) * 2 * 8 + 16)) != 1) goto loc_008F8CCF;
    v_stack_p50 = 0x10000ULL;
    v_stack_p48 = v_rsp - 79 - 25;
    v_stack_p40 = v_rsp - 79 - 9;
    v_stack_p38 = v_rsp - 79 - 41;
    v_stack_p30 = *(unsigned __int64 *)(v_rsp - 79 + 119);
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    result = PnpGetObjectProperty((unsigned int)(0x5A706E50ULL), 16, *(unsigned __int64 *)(v_rsp - 79 + 95), (unsigned int)(*(unsigned int *)(v_rsp - 79 + 87)));
    if (((unsigned int)(result)) != 0xC0000225ULL) goto loc_008F8E6D;
    *(unsigned int *)(v_rsp - 79 - 41) = 0;
    *(unsigned int *)(v_rsp - 79 - 29) = 0;
loc_008F8CCB:
loc_008F8CCF:
    result = CmpLockSiloKeyLockTrackerExclusive(a3, 16, *(unsigned __int64 *)(v_rsp - 79 + 95), (unsigned int)(*(unsigned int *)(v_rsp - 79 + 87)));
    v_r13 = (a3 + (unsigned int)((unsigned int)(result)) + (unsigned int)((unsigned int)(result)) * 2 * 8) + (112);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_r13))) == 0) goto loc_008F8E39;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r13)))) == 1) goto loc_008F8DDB;
    if (sign_flag) goto loc_008F8DDB;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a4 + v_rip - 9399450 * 1 + 48) + (unsigned int)((unsigned int)(result)) + (unsigned int)((unsigned int)(result)) * 2 * 8 + 16)) == ((unsigned int)(*(unsigned __int64 *)(v_rsp - 79 - 1)))) goto loc_008F8DDB;
    a4 = 0;
    a3 = 0;
    v_stack_p20 = v_rsp - 79 - 33;
    result = PiDmCacheDataDecode(v_r13, v_rsp - 79 - 37, a3, a4);
    if (((unsigned int)(result)) == 0xC0000225ULL) goto loc_008F8E27;
    result = (unsigned int)((result) + ((unsigned int)((unsigned int)(0x80000000ULL))));
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)(result))) == 0) goto loc_008F8E19;
loc_008F8D3F:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 33))) == 0) goto loc_008F8E31;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 33)))), (unsigned int)(0x5A706E50ULL), a4);
    *(unsigned __int64 *)(v_rsp - 79 - 17) = result;
    if (result == 0) goto loc_008F8DD2;
loc_008F8D65:
    v_stack_p20 = v_rsp - 79 - 33;
    result = PiDmCacheDataDecode(v_r13, v_rsp - 79 - 37, result, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 33)))));
    if (sign_flag) goto loc_008F8DD7;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 37)))) != (*(unsigned int *)(v_rsp - 79 - 41))) goto loc_008F8DDB;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 33)))) != (*(unsigned int *)(v_rsp - 79 - 29))) goto loc_008F8DDB;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 33))) == 0) goto loc_008F8DAF;
    result = memcmp(*(unsigned __int64 *)(v_rsp - 79 - 17), *(unsigned __int64 *)(v_rsp - 79 - 9), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 33)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 33)))));
loc_008F8DAD:
    if ((unsigned int)(result) != 0) goto loc_008F8DDB;
loc_008F8DAF:
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 79 + 127)) = 1;
loc_008F8DB6:
    result = PiDmObjectReleaseLock(*(unsigned __int64 *)(v_rsp - 79 + 103), *(unsigned __int64 *)(v_rsp - 79 - 9), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 33)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 33)))));
    if ((*(unsigned int *)(*(unsigned __int64 *)(a4 + v_rip - 9399450 * 1 + 48) + (unsigned int)((unsigned int)(result)) + (unsigned int)((unsigned int)(result)) * 2 * 8 + 16)) == ((unsigned int)(*(unsigned __int64 *)(v_rsp - 79 - 1)))) goto loc_008F8B1B;
    goto loc_008F8B67;
loc_008F8DD2:
loc_008F8DD7:
loc_008F8DDB:
    result = PiDmCacheDataFree(*(unsigned __int64 *)(v_rsp - 79 + 103), *(unsigned __int64 *)(v_rsp - 79 - 9), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 33)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 33)))));
    if (sign_flag) goto loc_008F8DB6;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a4 + v_rip - 9399450 * 1 + 48) + (unsigned int)((unsigned int)(result)) + (unsigned int)((unsigned int)(result)) * 2 * 8 + 16)) != 1) goto loc_008F8DB6;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + v_rip - 9399450 * 1 + 48) + (unsigned int)((unsigned int)(result)) + (unsigned int)((unsigned int)(result)) * 2 * 8 + 12))) != 0) goto loc_008F8DB6;
    v_stack_p28 = *(unsigned __int64 *)(v_rsp - 79 + 103);
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + v_rip - 9399450 * 1 + 48) + (unsigned int)((unsigned int)(result)) + (unsigned int)((unsigned int)(result)) * 2 * 8 + 12)));
    result = PiDmCacheDataEncode((unsigned int)(*(unsigned int *)(v_rsp - 79 - 41)), *(unsigned __int64 *)(v_rsp - 79 - 9), (unsigned int)(*(unsigned int *)(v_rsp - 79 - 29)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + v_rip - 9399450 * 1 + 48) + (unsigned int)((unsigned int)(result)) + (unsigned int)((unsigned int)(result)) * 2 * 8 + 8)));
    goto loc_008F8DB6;
loc_008F8E19:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 0xC0000023ULL) goto loc_008F8D3F;
    goto loc_008F8DD7;
loc_008F8E27:
    v_rsi = 0;
    goto loc_008F8DAD;
loc_008F8E31:
    goto loc_008F8D65;
loc_008F8E39:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a4 + v_rip - 9399450 * 1 + 48) + (unsigned int)((unsigned int)(result)) + (unsigned int)((unsigned int)(result)) * 2 * 8 + 16)) == ((unsigned int)(*(unsigned __int64 *)(v_rsp - 79 - 1)))) goto loc_008F8DB6;
    goto loc_008F8DDB;
loc_008F8E46:
    result = PiDmGetObject((unsigned int)(*(unsigned int *)(v_rsp - 79 + 87)), *(unsigned __int64 *)(v_rsp - 79 + 95), v_rsp - 79 + 103, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + v_rip - 9399450 * 1 + 48) + (unsigned int)((unsigned int)(result)) + (unsigned int)((unsigned int)(result)) * 2 * 8 + 8)));
    if (sign_flag) goto loc_008F8ACB;
    *(unsigned __int8 *)(v_rsp - 79 + 111) = 1;
    goto loc_008F8C5A;
loc_008F8E6D:
    *(unsigned int *)(v_rsp - 79 - 29) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 25)));
    goto loc_008F8CCB;
}
```

## 5. (Beta) C Style

```c
int64_t PiDmObjectProcessPropertyChange(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r13;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint32_t v_stack_p50;

    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint32_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (152);
    Arg2 = 0;
    *(uint32_t *)(local_rsp - 0x4F - 0x21) = 0;
    *(uint32_t *)(local_rsp - 0x4F - 0x1D) = 0;
    *(uint32_t *)(local_rsp - 0x4F - 0x19) = 0;
    *(uint8_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x7F)) = 0;
    *(uint8_t *)(local_rsp - 0x4F + 0x6F) = 0;
    *(uint64_t *)(local_rsp - 0x4F - 0x11) = 0;
    *(uint64_t *)(local_rsp - 0x4F - 0x9) = 0;
    *(uint32_t *)(local_rsp - 0x4F - 0x25) = 0;
    *(uint32_t *)(local_rsp - 0x4F - 0x29) = 0;
    *(uint64_t *)(local_rsp - 0x4F - 0x1) = 0;
    if (Arg4 != 0) goto loc_008F8ACB;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_not_equal) goto loc_008F8AE0;
loc_008F8AB4:
    result = PiDmGetCachedKeyIndex(v_rip - 9400385, 0 + 10, *(uint64_t *)(local_rsp - 0x4F + 0x77), Arg4);
    if (((uint32_t)(result)) < ((uint32_t)(0 + 10))) goto loc_008F8C51;
loc_008F8ACB:
    local_rsp = (local_rsp) + (152);
    return result;
loc_008F8AE0:
    Arg1 = (uint32_t)((v_rip - 9400385) - (2));
    if (condition_is_not_equal) goto loc_008F8AF1;
    goto loc_008F8AB4;
loc_008F8AF1:
    if (Arg1 != 2) goto loc_008F8ACB;
    goto loc_008F8AB4;
loc_008F8B02:
    if ((*(uint32_t *)(local_rsp - 0x4F - 0x29)) != 17) goto loc_008F8B13;
    if ((*(uint8_t *)(0)) != 255) goto loc_008F8B13;
    result = (uint32_t)((result) + 1);
loc_008F8B10:
    *(uint32_t *)(0 + v_rip - 0x8F6F6D * 1) = (uint32_t)(result);
loc_008F8B13:
    result = PiDmObjectReleaseLock(0, Arg1 + 1, *(uint64_t *)(local_rsp - 0x4F + 0x77), Arg4);
loc_008F8B1B:
    result = *(uint64_t *)(local_rsp - 0x4F - 0x11);
    if (*(uint64_t *)(local_rsp - 0x4F - 0x11) != 0) {
        Arg2 = 0x5A706E50ULL;
        Arg1 = *(uint64_t *)(local_rsp - 0x4F - 0x11);
        result = ExFreePoolWithTag(Arg1, Arg2, *(uint64_t *)(local_rsp - 0x4F + 0x77), Arg4);
    }
    if (0 != 0) {
        Arg2 = 0x5A706E50ULL;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, *(uint64_t *)(local_rsp - 0x4F + 0x77), Arg4);
    }
    if (0 != 0) {
        Arg1 = 0;
        result = PiDmObjectRelease(Arg1, Arg2, *(uint64_t *)(local_rsp - 0x4F + 0x77), Arg4);
    }
    if ((*(uint8_t *)(local_rsp - 0x4F + 0x6F)) == 0) goto loc_008F8ACB;
    result = PiDmObjectRelease(Arg3, Arg2, *(uint64_t *)(local_rsp - 0x4F + 0x77), Arg4);
    goto loc_008F8ACB;
loc_008F8B67:
    if ((*(uint8_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x7F))) != 0) goto loc_008F8B1B;
    Arg2 = 0;
loc_008F8B7C:
    if (0 >= 3) goto loc_008F8B1B;
    Arg4 = (Arg4) * (0);
    if ((*(uint32_t *)(*(uint64_t *)(Arg4 + v_rip - 0x8F6C9A * 1 + 0x8) + 0x10)) == ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x77) + 0x10))))) goto loc_008F8B9A;
loc_008F8B96:
    Arg2 = (uint32_t)((Arg2) + 1);
    goto loc_008F8B7C;
loc_008F8B9A:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(Arg4 + v_rip - 0x8F6C9A * 1 + 0x8))) - (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x77)));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(Arg4 + v_rip - 0x8F6C9A * 1 + 0x8) + 0x8);
        Arg1 = (Arg1) - (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x77) + 0x8));
    }
    if (Arg1 != NULL) goto loc_008F8B96;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x57)))) != (*(uint32_t *)(Arg4 + v_rip - 0x8F6C9A * 1))) goto loc_008F8B96;
    if (Arg4 + v_rip - 9399450 * 1 == 0) goto loc_008F8B1B;
    v_stack_p30 = local_rsp - 79 - 1;
    v_stack_p28 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + v_rip - 0x8F6C9A * 1 + 0x18)));
    v_stack_p20 = *(uint64_t *)(Arg4 + v_rip - 0x8F6C9A * 1 + 0x10);
    result = PiDmGetReferencedObjectFromProperty((uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x57)), *(uint64_t *)(local_rsp - 0x4F + 0x5F), Arg3, Arg4);
    if (sign_flag) goto loc_008F8B1B;
    result = CmpLockSiloKeyLockTrackerExclusive(*(uint64_t *)(local_rsp - 0x4F - 0x1), *(uint64_t *)(local_rsp - 0x4F + 0x5F), Arg3, Arg4);
    if (sign_flag) goto loc_008F8C49;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x4F - 0x1) + *(uint64_t *)(Arg4 + v_rip - 0x8F6C9A * 1 + 0x30) * 1)))) == ((uint32_t)((uint32_t)(0x80000000ULL)))) goto loc_008F8C49;
    if (0 != 17) goto loc_008F8B02;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(local_rsp - 0x4F - 0x11)))) == 255) goto loc_008F8C32;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(local_rsp - 0x4F - 0x11))) != 0) goto loc_008F8B13;
    goto loc_008F8B02;
loc_008F8C32:
    if ((*(uint32_t *)(local_rsp - 0x4F - 0x29)) != 17) goto loc_008F8C42;
    if ((*(uint8_t *)(0)) != 0) goto loc_008F8B13;
loc_008F8C42:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x4F - 0x1) + *(uint64_t *)(Arg4 + v_rip - 0x8F6C9A * 1 + 0x30) * 1))) - 1);
    goto loc_008F8B10;
loc_008F8C49:
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x4F - 0x1) + *(uint64_t *)(Arg4 + v_rip - 0x8F6C9A * 1 + 0x30) * 1) = (uint32_t)(*(uint8_t *)(*(uint64_t *)(local_rsp - 0x4F - 0x11)));
    goto loc_008F8B13;
loc_008F8C51:
    if (Arg3 == 0) goto loc_008F8E46;
loc_008F8C5A:
    if ((*(uint32_t *)(*(uint64_t *)(Arg4 + v_rip - 0x8F6C9A * 1 + 0x30) + (uint32_t)((uint32_t)(result)) + (uint32_t)((uint32_t)(result)) * 2 * 8 + 0x10)) != 1) goto loc_008F8CCF;
    v_stack_p50 = 0x10000ULL;
    v_stack_p48 = local_rsp - 79 - 25;
    v_stack_p40 = local_rsp - 79 - 9;
    v_stack_p38 = local_rsp - 79 - 41;
    v_stack_p30 = *(uint64_t *)(local_rsp - 0x4F + 0x77);
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    result = PnpGetObjectProperty((uint32_t)(0x5A706E50ULL), 16, *(uint64_t *)(local_rsp - 0x4F + 0x5F), (uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x57)));
    if (((uint32_t)(result)) != 0xC0000225ULL) goto loc_008F8E6D;
    *(uint32_t *)(local_rsp - 0x4F - 0x29) = 0;
    *(uint32_t *)(local_rsp - 0x4F - 0x1D) = 0;
loc_008F8CCB:
loc_008F8CCF:
    result = CmpLockSiloKeyLockTrackerExclusive(Arg3, 16, *(uint64_t *)(local_rsp - 0x4F + 0x5F), (uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x57)));
    local_r13 = (Arg3 + (uint32_t)((uint32_t)(result)) + (uint32_t)((uint32_t)(result)) * 2 * 8) + (112);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_r13))) == 0) goto loc_008F8E39;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r13)))) == 1) goto loc_008F8DDB;
    if (sign_flag) goto loc_008F8DDB;
    if ((*(uint32_t *)(*(uint64_t *)(Arg4 + v_rip - 0x8F6C9A * 1 + 0x30) + (uint32_t)((uint32_t)(result)) + (uint32_t)((uint32_t)(result)) * 2 * 8 + 0x10)) == ((uint32_t)(*(uint64_t *)(local_rsp - 0x4F - 0x1)))) goto loc_008F8DDB;
    Arg4 = 0;
    Arg3 = 0;
    v_stack_p20 = local_rsp - 79 - 33;
    result = PiDmCacheDataDecode(local_r13, local_rsp - 79 - 37, Arg3, Arg4);
    if (((uint32_t)(result)) == 0xC0000225ULL) goto loc_008F8E27;
    result = (uint32_t)((result) + ((uint32_t)((uint32_t)(0x80000000ULL))));
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)(result))) == 0) goto loc_008F8E19;
loc_008F8D3F:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x21))) == 0) goto loc_008F8E31;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x21)))), (uint32_t)(0x5A706E50ULL), Arg4);
    *(uint64_t *)(local_rsp - 0x4F - 0x11) = result;
    if (result == 0) goto loc_008F8DD2;
loc_008F8D65:
    v_stack_p20 = local_rsp - 79 - 33;
    result = PiDmCacheDataDecode(local_r13, local_rsp - 79 - 37, result, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x21)))));
    if (sign_flag) goto loc_008F8DD7;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x25)))) != (*(uint32_t *)(local_rsp - 0x4F - 0x29))) goto loc_008F8DDB;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x21)))) != (*(uint32_t *)(local_rsp - 0x4F - 0x1D))) goto loc_008F8DDB;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x21))) == 0) goto loc_008F8DAF;
    result = memcmp(*(uint64_t *)(local_rsp - 0x4F - 0x11), *(uint64_t *)(local_rsp - 0x4F - 0x9), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x21)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x21)))));
loc_008F8DAD:
    if ((uint32_t)(result) != 0) goto loc_008F8DDB;
loc_008F8DAF:
    *(uint8_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x7F)) = 1;
loc_008F8DB6:
    result = PiDmObjectReleaseLock(*(uint64_t *)(local_rsp - 0x4F + 0x67), *(uint64_t *)(local_rsp - 0x4F - 0x9), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x21)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x21)))));
    if ((*(uint32_t *)(*(uint64_t *)(Arg4 + v_rip - 0x8F6C9A * 1 + 0x30) + (uint32_t)((uint32_t)(result)) + (uint32_t)((uint32_t)(result)) * 2 * 8 + 0x10)) == ((uint32_t)(*(uint64_t *)(local_rsp - 0x4F - 0x1)))) goto loc_008F8B1B;
    goto loc_008F8B67;
loc_008F8DD2:
loc_008F8DD7:
loc_008F8DDB:
    result = PiDmCacheDataFree(*(uint64_t *)(local_rsp - 0x4F + 0x67), *(uint64_t *)(local_rsp - 0x4F - 0x9), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x21)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x21)))));
    if (sign_flag) goto loc_008F8DB6;
    if ((*(uint32_t *)(*(uint64_t *)(Arg4 + v_rip - 0x8F6C9A * 1 + 0x30) + (uint32_t)((uint32_t)(result)) + (uint32_t)((uint32_t)(result)) * 2 * 8 + 0x10)) != 1) goto loc_008F8DB6;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + v_rip - 0x8F6C9A * 1 + 0x30) + (uint32_t)((uint32_t)(result)) + (uint32_t)((uint32_t)(result)) * 2 * 8 + 0xC))) != 0) goto loc_008F8DB6;
    v_stack_p28 = *(uint64_t *)(local_rsp - 0x4F + 0x67);
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + v_rip - 0x8F6C9A * 1 + 0x30) + (uint32_t)((uint32_t)(result)) + (uint32_t)((uint32_t)(result)) * 2 * 8 + 0xC)));
    result = PiDmCacheDataEncode((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x29)), *(uint64_t *)(local_rsp - 0x4F - 0x9), (uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x1D)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + v_rip - 0x8F6C9A * 1 + 0x30) + (uint32_t)((uint32_t)(result)) + (uint32_t)((uint32_t)(result)) * 2 * 8 + 0x8)));
    goto loc_008F8DB6;
loc_008F8E19:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 0xC0000023ULL) goto loc_008F8D3F;
    goto loc_008F8DD7;
loc_008F8E27:
    local_rsi = 0;
    goto loc_008F8DAD;
loc_008F8E31:
    goto loc_008F8D65;
loc_008F8E39:
    if ((*(uint32_t *)(*(uint64_t *)(Arg4 + v_rip - 0x8F6C9A * 1 + 0x30) + (uint32_t)((uint32_t)(result)) + (uint32_t)((uint32_t)(result)) * 2 * 8 + 0x10)) == ((uint32_t)(*(uint64_t *)(local_rsp - 0x4F - 0x1)))) goto loc_008F8DB6;
    goto loc_008F8DDB;
loc_008F8E46:
    result = PiDmGetObject((uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x57)), *(uint64_t *)(local_rsp - 0x4F + 0x5F), local_rsp - 79 + 103, (uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + v_rip - 0x8F6C9A * 1 + 0x30) + (uint32_t)((uint32_t)(result)) + (uint32_t)((uint32_t)(result)) * 2 * 8 + 0x8)));
    if (sign_flag) goto loc_008F8ACB;
    *(uint8_t *)(local_rsp - 0x4F + 0x6F) = 1;
    goto loc_008F8C5A;
loc_008F8E6D:
    *(uint32_t *)(local_rsp - 0x4F - 0x1D) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x19)));
    goto loc_008F8CCB;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008F8A48&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
