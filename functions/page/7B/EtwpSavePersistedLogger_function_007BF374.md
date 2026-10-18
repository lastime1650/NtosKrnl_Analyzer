# EtwpSavePersistedLogger

- RVA: `0x007BF374`–`0x007BF907` (길이 `1,427` bytes)
- VA: `0x00000001407BF374`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D3CE8`
- 디코드: `383`개 명령, `1,427/1,427` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **29**; 고유 호출 대상: **23**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x007BF3FA` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007BF40A` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007BF428` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x007BF457` → [MmAllocateMappingAddressEx](../A7/MmAllocateMappingAddressEx_function_00A726B0.md) (function, `0x00A726B0`)
- `0x007BF483` → [IoAllocateMdl](../../text/29/IoAllocateMdl_function_0029EBF0.md) (function, `0x0029EBF0`)
- `0x007BF4A7` → [EtwpQueryPersistedMemory](EtwpQueryPersistedMemory_function_007BF288.md) (function, `0x007BF288`)
- `0x007BF4C4` → [RtlCreateUnicodeString](../9B/RtlCreateUnicodeString_function_009BD860.md) (function, `0x009BD860`)
- `0x007BF529` → [EtwpExpandFileName](../9C/EtwpExpandFileName_function_009C147C.md) (function, `0x009C147C`)
- `0x007BF55D` → [EtwpDelayCreate](../9C/EtwpDelayCreate_function_009C1188.md) (function, `0x009C1188`)
- `0x007BF591` → [ZwSetInformationFile](../../text/6A/ZwSetInformationFile_function_006AD5B0.md) (function, `0x006AD5B0`)
- `0x007BF5A0` → [EtwpInitializeCompressedWriter](EtwpInitializeCompressedWriter_function_007BED7C.md) (function, `0x007BED7C`)
- `0x007BF647` → [MmMapLockedPagesWithReservedMapping](../../text/3E/MmMapLockedPagesWithReservedMapping_function_003E8910.md) (function, `0x003E8910`)
- `0x007BF697` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007BF6B1` → [EtwpWriteBufferCompressed](EtwpWriteBufferCompressed_function_007BFB64.md) (function, `0x007BFB64`)
- `0x007BF6C7` → [MmUnmapReservedMapping](../../text/3E/MmUnmapReservedMapping_function_003E7BE0.md) (function, `0x003E7BE0`)
- `0x007BF70C` → [EtwpWriteRemainingCompressedData](EtwpWriteRemainingCompressedData_function_007BFD34.md) (function, `0x007BFD34`)
- `0x007BF788` → [MmMapLockedPagesWithReservedMapping](../../text/3E/MmMapLockedPagesWithReservedMapping_function_003E8910.md) (function, `0x003E8910`)
- `0x007BF7FF` → [ZwWriteFile](../../text/6A/ZwWriteFile_function_006AD1D0.md) (function, `0x006AD1D0`)
- `0x007BF811` → [MmUnmapReservedMapping](../../text/3E/MmUnmapReservedMapping_function_003E7BE0.md) (function, `0x003E7BE0`)
- `0x007BF83D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007BF852` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007BF864` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007BF876` → [MmFreeMappingAddress](../A7/MmFreeMappingAddress_function_00A75F20.md) (function, `0x00A75F20`)
- `0x007BF885` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007BF896` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007BF8A9` → `ext-ms-win-ntos-ksr-l1-1-5.dll!KsrFreePersistedMemoryBlock` (import, 간접 대상; import `ext-ms-win-ntos-ksr-l1-1-5.dll!KsrFreePersistedMemoryBlock`)
- `0x007BF8CF` → [EtwpTraceSavePersistedLoggerStop](EtwpTraceSavePersistedLoggerStop_function_007BFA54.md) (function, `0x007BFA54`)
- `0x007BF8D8` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x007BF8E6` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [EtwpSavePersistedLoggersWorker](EtwpSavePersistedLoggersWorker_function_007BF940.md) at `0x007BF9FF`

### Static image references
- `0x007BF390` → RVA `0x00E0A740` (`.data`; read)
- `0x007BF40F` → RVA `0x00EFF840` (`.data`; read)
- `0x007BF416` → RVA `0x000226C8` (`.rdata`; read)
- `0x007BF89F` → RVA `0x00B4AEA0` (`EtwpKsrGuid`; read)
- `0x007BF8A9` → RVA `0x00151320` (`ext-ms-win-ntos-ksr-l1-1-5.dll!KsrFreePersistedMemoryBlock (IAT)`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **17**
  - `0x007BF3FA` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007BF40A` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x007BF428` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x007BF483` → [IoAllocateMdl](../../text/29/IoAllocateMdl_function_0029EBF0.md) (`PAGE` → `.text`)
  - `0x007BF591` → [ZwSetInformationFile](../../text/6A/ZwSetInformationFile_function_006AD5B0.md) (`PAGE` → `.text`)
  - `0x007BF647` → [MmMapLockedPagesWithReservedMapping](../../text/3E/MmMapLockedPagesWithReservedMapping_function_003E8910.md) (`PAGE` → `.text`)
  - `0x007BF697` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x007BF6C7` → [MmUnmapReservedMapping](../../text/3E/MmUnmapReservedMapping_function_003E7BE0.md) (`PAGE` → `.text`)
  - `0x007BF788` → [MmMapLockedPagesWithReservedMapping](../../text/3E/MmMapLockedPagesWithReservedMapping_function_003E8910.md) (`PAGE` → `.text`)
  - `0x007BF7FF` → [ZwWriteFile](../../text/6A/ZwWriteFile_function_006AD1D0.md) (`PAGE` → `.text`)
  - `0x007BF811` → [MmUnmapReservedMapping](../../text/3E/MmUnmapReservedMapping_function_003E7BE0.md) (`PAGE` → `.text`)
  - `0x007BF83D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007BF852` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007BF864` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007BF885` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007BF896` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007BF8E6` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007BF374  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
007BF379  55                              push rbp
007BF37A  56                              push rsi
007BF37B  57                              push rdi
007BF37C  41 54                           push r12
007BF37E  41 55                           push r13
007BF380  41 56                           push r14
007BF382  41 57                           push r15
007BF384  48 8D 6C 24 C0                  lea rbp, [rsp - 0x40]
007BF389  48 81 EC 40 01 00 00            sub rsp, 0x140
007BF390  48 8B 05 A9 B3 64 00            mov rax, qword ptr [rip + 0x64b3a9]
007BF397  48 33 C4                        xor rax, rsp
007BF39A  48 89 45 38                     mov qword ptr [rbp + 0x38], rax
007BF39E  45 33 E4                        xor r12d, r12d
007BF3A1  48 89 55 98                     mov qword ptr [rbp - 0x68], rdx
007BF3A5  0F 57 C0                        xorps xmm0, xmm0
007BF3A8  48 89 4D 80                     mov qword ptr [rbp - 0x80], rcx
007BF3AC  48 8B D9                        mov rbx, rcx
007BF3AF  4C 89 65 B0                     mov qword ptr [rbp - 0x50], r12
007BF3B3  33 C0                           xor eax, eax
007BF3B5  44 89 64 24 58                  mov dword ptr [rsp + 0x58], r12d
007BF3BA  0F 57 C9                        xorps xmm1, xmm1
007BF3BD  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
007BF3C1  33 D2                           xor edx, edx
007BF3C3  4C 89 64 24 70                  mov qword ptr [rsp + 0x70], r12
007BF3C8  48 8D 4D 88                     lea rcx, [rbp - 0x78]
007BF3CC  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
007BF3D1  0F 11 45 10                     movups xmmword ptr [rbp + 0x10], xmm0
007BF3D5  45 8B F4                        mov r14d, r12d
007BF3D8  41 8B F4                        mov esi, r12d
007BF3DB  0F 11 45 20                     movups xmmword ptr [rbp + 0x20], xmm0
007BF3DF  45 8B EC                        mov r13d, r12d
007BF3E2  44 89 64 24 60                  mov dword ptr [rsp + 0x60], r12d
007BF3E7  0F 11 45 88                     movups xmmword ptr [rbp - 0x78], xmm0
007BF3EB  45 8B FC                        mov r15d, r12d
007BF3EE  41 8B FC                        mov edi, r12d
007BF3F1  0F 11 4D B8                     movups xmmword ptr [rbp - 0x48], xmm1
007BF3F5  4C 89 64 24 78                  mov qword ptr [rsp + 0x78], r12
007BF3FA  E8 81 B3 C6 FF                  call 0x14042a780
007BF3FF  33 D2                           xor edx, edx
007BF401  45 8D 44 24 40                  lea r8d, [r12 + 0x40]
007BF406  48 8D 4D D0                     lea rcx, [rbp - 0x30]
007BF40A  E8 31 78 F0 FF                  call 0x1406c6c40
007BF40F  48 8B 0D 2A 04 74 00            mov rcx, qword ptr [rip + 0x74042a]
007BF416  48 8D 15 AB 32 86 FF            lea rdx, [rip - 0x79cd55]
007BF41D  45 33 C9                        xor r9d, r9d
007BF420  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
007BF425  45 33 C0                        xor r8d, r8d
007BF428  E8 F3 D2 C5 FF                  call 0x14041c720
007BF42D  44 8B 63 08                     mov r12d, dword ptr [rbx + 8]
007BF431  44 89 64 24 5C                  mov dword ptr [rsp + 0x5c], r12d
007BF436  45 85 E4                        test r12d, r12d
007BF439  0F 84 EE 03 00 00               je 0x1407bf82d
007BF43F  41 F7 C4 FF 0F 00 00            test r12d, 0xfff
007BF446  0F 85 E1 03 00 00               jne 0x1407bf82d
007BF44C  41 8B CC                        mov ecx, r12d
007BF44F  45 33 C0                        xor r8d, r8d
007BF452  BA 45 74 77 4B                  mov edx, 0x4b777445
007BF457  E8 54 32 2B 00                  call 0x140a726b0
007BF45C  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
007BF461  48 8B F8                        mov rdi, rax
007BF464  48 85 C0                        test rax, rax
007BF467  75 0A                           jne 0x1407bf473
007BF469  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007BF46E  E9 BF 03 00 00                  jmp 0x1407bf832
007BF473  48 21 74 24 20                  and qword ptr [rsp + 0x20], rsi
007BF478  45 33 C9                        xor r9d, r9d
007BF47B  45 33 C0                        xor r8d, r8d
007BF47E  41 8B D4                        mov edx, r12d
007BF481  33 C9                           xor ecx, ecx
007BF483  E8 68 F7 AD FF                  call 0x14029ebf0
007BF488  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
007BF48C  4C 8B F8                        mov r15, rax
007BF48F  48 85 C0                        test rax, rax
007BF492  74 D5                           je 0x1407bf469
007BF494  48 8B 55 98                     mov rdx, qword ptr [rbp - 0x68]
007BF498  4C 8D 4C 24 58                  lea r9, [rsp + 0x58]
007BF49D  66 83 48 0A 02                  or word ptr [rax + 0xa], 2
007BF4A2  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
007BF4A7  E8 DC FD FF FF                  call 0x1407bf288
007BF4AC  8B D8                           mov ebx, eax
007BF4AE  85 C0                           test eax, eax
007BF4B0  0F 88 7C 03 00 00               js 0x1407bf832
007BF4B6  48 8B 5D 80                     mov rbx, qword ptr [rbp - 0x80]
007BF4BA  48 8D 4D 88                     lea rcx, [rbp - 0x78]
007BF4BE  8B 53 0C                        mov edx, dword ptr [rbx + 0xc]
007BF4C1  48 03 D3                        add rdx, rbx
007BF4C4  E8 97 E3 1F 00                  call 0x1409bd860
007BF4C9  84 C0                           test al, al
007BF4CB  75 0A                           jne 0x1407bf4d7
007BF4CD  BB 17 00 00 C0                  mov ebx, 0xc0000017
007BF4D2  E9 5B 03 00 00                  jmp 0x1407bf832
007BF4D7  33 D2                           xor edx, edx
007BF4D9  45 33 C0                        xor r8d, r8d
007BF4DC  44 3B 44 24 58                  cmp r8d, dword ptr [rsp + 0x58]
007BF4E1  73 24                           jae 0x1407bf507
007BF4E3  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
007BF4E8  4E 8B 0C C0                     mov r9, qword ptr [rax + r8*8]
007BF4EC  49 C1 E9 28                     shr r9, 0x28
007BF4F0  4D 85 C9                        test r9, r9
007BF4F3  74 08                           je 0x1407bf4fd
007BF4F5  49 03 D1                        add rdx, r9
007BF4F8  41 FF C0                        inc r8d
007BF4FB  EB DF                           jmp 0x1407bf4dc
007BF4FD  BB 30 00 19 C0                  mov ebx, 0xc0190030
007BF502  E9 2B 03 00 00                  jmp 0x1407bf832
007BF507  8B 43 04                        mov eax, dword ptr [rbx + 4]
007BF50A  49 0F AF C4                     imul rax, r12
007BF50E  48 C1 E2 0C                     shl rdx, 0xc
007BF512  48 3B D0                        cmp rdx, rax
007BF515  75 E6                           jne 0x1407bf4fd
007BF517  4C 8D 4D 88                     lea r9, [rbp - 0x78]
007BF51B  40 88 74 24 20                  mov byte ptr [rsp + 0x20], sil
007BF520  45 33 C0                        xor r8d, r8d
007BF523  48 8D 55 88                     lea rdx, [rbp - 0x78]
007BF527  33 C9                           xor ecx, ecx
007BF529  E8 4E 1F 20 00                  call 0x1409c147c
007BF52E  33 C9                           xor ecx, ecx
007BF530  8B D8                           mov ebx, eax
007BF532  85 C0                           test eax, eax
007BF534  0F 88 F8 02 00 00               js 0x1407bf832
007BF53A  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
007BF53F  4C 8D 44 24 54                  lea r8, [rsp + 0x54]
007BF544  88 4C 24 54                     mov byte ptr [rsp + 0x54], cl
007BF548  48 8D 55 88                     lea rdx, [rbp - 0x78]
007BF54C  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
007BF551  41 B1 01                        mov r9b, 1
007BF554  88 4C 24 20                     mov byte ptr [rsp + 0x20], cl
007BF558  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
007BF55D  E8 26 1C 20 00                  call 0x1409c1188
007BF562  4C 8B 74 24 70                  mov r14, qword ptr [rsp + 0x70]
007BF567  8B D8                           mov ebx, eax
007BF569  85 C0                           test eax, eax
007BF56B  0F 88 C1 02 00 00               js 0x1407bf832
007BF571  41 B9 28 00 00 00               mov r9d, 0x28
007BF577  C7 45 30 00 20 00 00            mov dword ptr [rbp + 0x30], 0x2000
007BF57E  4C 8D 45 10                     lea r8, [rbp + 0x10]
007BF582  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
007BF58A  48 8D 55 B8                     lea rdx, [rbp - 0x48]
007BF58E  49 8B CE                        mov rcx, r14
007BF591  E8 1A E0 EE FF                  call 0x1406ad5b0
007BF596  4D 8B C6                        mov r8, r14
007BF599  48 8D 4D D0                     lea rcx, [rbp - 0x30]
007BF59D  41 8B D4                        mov edx, r12d
007BF5A0  E8 D7 F7 FF FF                  call 0x1407bed7c
007BF5A5  8B D8                           mov ebx, eax
007BF5A7  85 C0                           test eax, eax
007BF5A9  0F 88 83 02 00 00               js 0x1407bf832
007BF5AF  45 33 DB                        xor r11d, r11d
007BF5B2  49 8D 4F 30                     lea rcx, [r15 + 0x30]
007BF5B6  33 FF                           xor edi, edi
007BF5B8  44 89 5C 24 64                  mov dword ptr [rsp + 0x64], r11d
007BF5BD  45 8B F4                        mov r14d, r12d
007BF5C0  89 7C 24 58                     mov dword ptr [rsp + 0x58], edi
007BF5C4  48 89 4D A0                     mov qword ptr [rbp - 0x60], rcx
007BF5C8  41 C1 EE 0C                     shr r14d, 0xc
007BF5CC  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
007BF5D0  44 3B 68 04                     cmp r13d, dword ptr [rax + 4]
007BF5D4  0F 83 24 01 00 00               jae 0x1407bf6fe
007BF5DA  45 85 F6                        test r14d, r14d
007BF5DD  74 55                           je 0x1407bf634
007BF5DF  4C 8B C9                        mov r9, rcx
007BF5E2  45 8B D6                        mov r10d, r14d
007BF5E5  49 BC FF FF FF FF FF 00 00 00   movabs r12, 0xffffffffff
007BF5EF  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
007BF5F4  8B C7                           mov eax, edi
007BF5F6  FF C7                           inc edi
007BF5F8  45 8B C3                        mov r8d, r11d
007BF5FB  4A 8B 0C C2                     mov rcx, qword ptr [rdx + r8*8]
007BF5FF  49 23 CC                        and rcx, r12
007BF602  48 03 C8                        add rcx, rax
007BF605  8B C7                           mov eax, edi
007BF607  49 89 09                        mov qword ptr [r9], rcx
007BF60A  4A 8B 0C C2                     mov rcx, qword ptr [rdx + r8*8]
007BF60E  48 C1 E9 28                     shr rcx, 0x28
007BF612  48 3B C1                        cmp rax, rcx
007BF615  75 05                           jne 0x1407bf61c
007BF617  41 FF C3                        inc r11d
007BF61A  33 FF                           xor edi, edi
007BF61C  49 83 C1 08                     add r9, 8
007BF620  49 83 EA 01                     sub r10, 1
007BF624  75 C9                           jne 0x1407bf5ef
007BF626  44 8B 64 24 5C                  mov r12d, dword ptr [rsp + 0x5c]
007BF62B  44 89 5C 24 64                  mov dword ptr [rsp + 0x64], r11d
007BF630  89 7C 24 58                     mov dword ptr [rsp + 0x58], edi
007BF634  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
007BF639  41 B9 01 00 00 00               mov r9d, 1
007BF63F  4D 8B C7                        mov r8, r15
007BF642  BA 45 74 77 4B                  mov edx, 0x4b777445
007BF647  E8 C4 92 C2 FF                  call 0x1403e8910
007BF64C  48 8B F8                        mov rdi, rax
007BF64F  44 39 20                        cmp dword ptr [rax], r12d
007BF652  74 0D                           je 0x1407bf661
007BF654  FF C6                           inc esi
007BF656  BB 06 02 00 C0                  mov ebx, 0xc0000206
007BF65B  89 74 24 50                     mov dword ptr [rsp + 0x50], esi
007BF65F  EB 5B                           jmp 0x1407bf6bc
007BF661  8B 40 08                        mov eax, dword ptr [rax + 8]
007BF664  3B 07                           cmp eax, dword ptr [rdi]
007BF666  76 05                           jbe 0x1407bf66d
007BF668  8B 47 04                        mov eax, dword ptr [rdi + 4]
007BF66B  EB 03                           jmp 0x1407bf670
007BF66D  8B 47 08                        mov eax, dword ptr [rdi + 8]
007BF670  89 47 30                        mov dword ptr [rdi + 0x30], eax
007BF673  41 3B C4                        cmp eax, r12d
007BF676  76 06                           jbe 0x1407bf67e
007BF678  8B 74 24 50                     mov esi, dword ptr [rsp + 0x50]
007BF67C  EB D6                           jmp 0x1407bf654
007BF67E  83 F8 48                        cmp eax, 0x48
007BF681  76 35                           jbe 0x1407bf6b8
007BF683  41 8B CC                        mov ecx, r12d
007BF686  2B C8                           sub ecx, eax
007BF688  74 12                           je 0x1407bf69c
007BF68A  44 8B C1                        mov r8d, ecx
007BF68D  BA FF 00 00 00                  mov edx, 0xff
007BF692  8B C8                           mov ecx, eax
007BF694  48 03 CF                        add rcx, rdi
007BF697  E8 A4 75 F0 FF                  call 0x1406c6c40
007BF69C  45 85 ED                        test r13d, r13d
007BF69F  75 09                           jne 0x1407bf6aa
007BF6A1  41 8B C4                        mov eax, r12d
007BF6A4  48 01 45 D8                     add qword ptr [rbp - 0x28], rax
007BF6A8  EB 0E                           jmp 0x1407bf6b8
007BF6AA  48 8B D7                        mov rdx, rdi
007BF6AD  48 8D 4D D0                     lea rcx, [rbp - 0x30]
007BF6B1  E8 AE 04 00 00                  call 0x1407bfb64
007BF6B6  8B D8                           mov ebx, eax
007BF6B8  8B 74 24 50                     mov esi, dword ptr [rsp + 0x50]
007BF6BC  4D 8B C7                        mov r8, r15
007BF6BF  BA 45 74 77 4B                  mov edx, 0x4b777445
007BF6C4  48 8B CF                        mov rcx, rdi
007BF6C7  E8 14 85 C2 FF                  call 0x1403e7be0
007BF6CC  85 DB                           test ebx, ebx
007BF6CE  79 05                           jns 0x1407bf6d5
007BF6D0  45 85 ED                        test r13d, r13d
007BF6D3  74 15                           je 0x1407bf6ea
007BF6D5  8B 7C 24 58                     mov edi, dword ptr [rsp + 0x58]
007BF6D9  49 8D 4F 30                     lea rcx, [r15 + 0x30]
007BF6DD  44 8B 5C 24 64                  mov r11d, dword ptr [rsp + 0x64]
007BF6E2  41 FF C5                        inc r13d
007BF6E5  E9 E2 FE FF FF                  jmp 0x1407bf5cc
007BF6EA  44 8B 6C 24 60                  mov r13d, dword ptr [rsp + 0x60]
007BF6EF  4C 8B 74 24 70                  mov r14, qword ptr [rsp + 0x70]
007BF6F4  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
007BF6F9  E9 34 01 00 00                  jmp 0x1407bf832
007BF6FE  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
007BF703  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
007BF708  48 8D 4D D0                     lea rcx, [rbp - 0x30]
007BF70C  E8 23 06 00 00                  call 0x1407bfd34
007BF711  45 33 DB                        xor r11d, r11d
007BF714  45 85 F6                        test r14d, r14d
007BF717  74 5C                           je 0x1407bf775
007BF719  4C 8B 7D A0                     mov r15, qword ptr [rbp - 0x60]
007BF71D  41 8B DE                        mov ebx, r14d
007BF720  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
007BF725  44 8D 57 01                     lea r10d, [rdi + 1]
007BF729  45 8B C3                        mov r8d, r11d
007BF72C  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
007BF736  4A 8B 0C C2                     mov rcx, qword ptr [rdx + r8*8]
007BF73A  48 23 C8                        and rcx, rax
007BF73D  8B C7                           mov eax, edi
007BF73F  48 03 C8                        add rcx, rax
007BF742  41 8D 43 01                     lea eax, [r11 + 1]
007BF746  49 89 0F                        mov qword ptr [r15], rcx
007BF749  4D 8D 7F 08                     lea r15, [r15 + 8]
007BF74D  4E 8B 0C C2                     mov r9, qword ptr [rdx + r8*8]
007BF751  49 C1 E9 28                     shr r9, 0x28
007BF755  41 8B CA                        mov ecx, r10d
007BF758  49 3B C9                        cmp rcx, r9
007BF75B  41 0F 45 C3                     cmovne eax, r11d
007BF75F  33 FF                           xor edi, edi
007BF761  49 3B C9                        cmp rcx, r9
007BF764  44 8B D8                        mov r11d, eax
007BF767  41 0F 45 FA                     cmovne edi, r10d
007BF76B  48 83 EB 01                     sub rbx, 1
007BF76F  75 AF                           jne 0x1407bf720
007BF771  4C 8B 7D A8                     mov r15, qword ptr [rbp - 0x58]
007BF775  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
007BF77A  41 B9 01 00 00 00               mov r9d, 1
007BF780  4D 8B C7                        mov r8, r15
007BF783  BA 45 74 77 4B                  mov edx, 0x4b777445
007BF788  E8 83 91 C2 FF                  call 0x1403e8910
007BF78D  44 8B 6C 24 60                  mov r13d, dword ptr [rsp + 0x60]
007BF792  48 8B F8                        mov rdi, rax
007BF795  8B 74 24 50                     mov esi, dword ptr [rsp + 0x50]
007BF799  0F BA A8 88 00 00 00 1A         bts dword ptr [rax + 0x88], 0x1a
007BF7A1  83 B8 94 00 00 00 04            cmp dword ptr [rax + 0x94], 4
007BF7A8  45 8D 65 01                     lea r12d, [r13 + 1]
007BF7AC  44 89 A0 8C 00 00 00            mov dword ptr [rax + 0x8c], r12d
007BF7B3  C7 40 2C 03 00 00 00            mov dword ptr [rax + 0x2c], 3
007BF7BA  75 08                           jne 0x1407bf7c4
007BF7BC  01 B0 74 01 00 00               add dword ptr [rax + 0x174], esi
007BF7C2  EB 06                           jmp 0x1407bf7ca
007BF7C4  01 B0 7C 01 00 00               add dword ptr [rax + 0x17c], esi
007BF7CA  48 83 64 24 40 00               and qword ptr [rsp + 0x40], 0
007BF7D0  48 8D 45 B0                     lea rax, [rbp - 0x50]
007BF7D4  4C 8B 74 24 70                  mov r14, qword ptr [rsp + 0x70]
007BF7D9  45 33 C9                        xor r9d, r9d
007BF7DC  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
007BF7E1  45 33 C0                        xor r8d, r8d
007BF7E4  8B 44 24 5C                     mov eax, dword ptr [rsp + 0x5c]
007BF7E8  33 D2                           xor edx, edx
007BF7EA  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
007BF7EE  49 8B CE                        mov rcx, r14
007BF7F1  48 8D 45 B8                     lea rax, [rbp - 0x48]
007BF7F5  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
007BF7FA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007BF7FF  E8 CC D9 EE FF                  call 0x1406ad1d0
007BF804  4D 8B C7                        mov r8, r15
007BF807  BA 45 74 77 4B                  mov edx, 0x4b777445
007BF80C  48 8B CF                        mov rcx, rdi
007BF80F  8B D8                           mov ebx, eax
007BF811  E8 CA 83 C2 FF                  call 0x1403e7be0
007BF816  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
007BF81B  85 DB                           test ebx, ebx
007BF81D  79 09                           jns 0x1407bf828
007BF81F  FF C6                           inc esi
007BF821  44 8B 64 24 5C                  mov r12d, dword ptr [rsp + 0x5c]
007BF826  EB 0A                           jmp 0x1407bf832
007BF828  45 8B EC                        mov r13d, r12d
007BF82B  EB F4                           jmp 0x1407bf821
007BF82D  BB 0D 00 1A C0                  mov ebx, 0xc01a000d
007BF832  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
007BF836  48 85 C9                        test rcx, rcx
007BF839  74 0C                           je 0x1407bf847
007BF83B  33 D2                           xor edx, edx
007BF83D  E8 2E 30 3C 00                  call 0x140b82870
007BF842  48 83 65 F0 00                  and qword ptr [rbp - 0x10], 0
007BF847  48 8B 4D F8                     mov rcx, qword ptr [rbp - 8]
007BF84B  48 85 C9                        test rcx, rcx
007BF84E  74 0C                           je 0x1407bf85c
007BF850  33 D2                           xor edx, edx
007BF852  E8 19 30 3C 00                  call 0x140b82870
007BF857  48 83 65 F8 00                  and qword ptr [rbp - 8], 0
007BF85C  4D 85 F6                        test r14, r14
007BF85F  74 08                           je 0x1407bf869
007BF861  49 8B CE                        mov rcx, r14
007BF864  E8 47 DA EE FF                  call 0x1406ad2b0
007BF869  48 85 FF                        test rdi, rdi
007BF86C  74 0D                           je 0x1407bf87b
007BF86E  BA 45 74 77 4B                  mov edx, 0x4b777445
007BF873  48 8B CF                        mov rcx, rdi
007BF876  E8 A5 66 2B 00                  call 0x140a75f20
007BF87B  4D 85 FF                        test r15, r15
007BF87E  74 0A                           je 0x1407bf88a
007BF880  33 D2                           xor edx, edx
007BF882  49 8B CF                        mov rcx, r15
007BF885  E8 E6 2F 3C 00                  call 0x140b82870
007BF88A  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
007BF88F  48 85 C9                        test rcx, rcx
007BF892  74 07                           je 0x1407bf89b
007BF894  33 D2                           xor edx, edx
007BF896  E8 D5 2F 3C 00                  call 0x140b82870
007BF89B  48 8B 55 98                     mov rdx, qword ptr [rbp - 0x68]
007BF89F  48 8D 0D FA B5 38 00            lea rcx, [rip + 0x38b5fa]
007BF8A6  41 B0 01                        mov r8b, 1
007BF8A9  48 FF 15 70 1A 99 FF            call qword ptr [rip - 0x66e590]
007BF8B0  0F 1F 44 00 00                  nop dword ptr [rax + rax]
007BF8B5  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
007BF8B9  48 8D 4D 88                     lea rcx, [rbp - 0x78]
007BF8BD  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
007BF8C1  45 8B CD                        mov r9d, r13d
007BF8C4  41 8B D4                        mov edx, r12d
007BF8C7  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
007BF8CB  44 8B 40 04                     mov r8d, dword ptr [rax + 4]
007BF8CF  E8 80 01 00 00                  call 0x1407bfa54
007BF8D4  48 8D 4D 88                     lea rcx, [rbp - 0x78]
007BF8D8  E8 23 0F 20 00                  call 0x1409c0800
007BF8DD  8B C3                           mov eax, ebx
007BF8DF  48 8B 4D 38                     mov rcx, qword ptr [rbp + 0x38]
007BF8E3  48 33 CC                        xor rcx, rsp
007BF8E6  E8 55 CD EE FF                  call 0x1406ac640
007BF8EB  48 8B 9C 24 90 01 00 00         mov rbx, qword ptr [rsp + 0x190]
007BF8F3  48 81 C4 40 01 00 00            add rsp, 0x140
007BF8FA  41 5F                           pop r15
007BF8FC  41 5E                           pop r14
007BF8FE  41 5D                           pop r13
007BF900  41 5C                           pop r12
007BF902  5F                              pop rdi
007BF903  5E                              pop rsi
007BF904  5D                              pop rbp
007BF905  C3                              ret
007BF906  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpSavePersistedLogger(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned int v_stack_m114;
    unsigned int v_stack_m118;
    unsigned int v_stack_m11C;
    unsigned int v_stack_m120;
    unsigned __int64 v_stack_m124;
    unsigned int v_stack_m128;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int8 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (320);
    result = (*(unsigned __int64 *)(v_rip + 6599593)) ^ (v_rsp);
    v_stack_m40 = result;
    v_r12 = 0;
    v_stack_mE0 = a2;
    v_stack_mF8 = a1;
    v_stack_mC8 = 0;
    result = 0;
    v_stack_m120 = 0;
    v_stack_m48 = 0;
    a2 = 0;
    v_stack_m108 = 0;
    v_stack_m128 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    v_stack_m118 = 0;
    v_stack_mF0 = v_xmm0;
    v_stack_mC0 = v_xmm1;
    v_stack_m100 = 0;
    result = RtlInitUnicodeString(v_stack_mF0, a2, a3, a4);
    a2 = 0;
    result = memset(v_stack_mA8, a2, v_r12 + 64, a4);
    a4 = 0;
    v_stack_m158 = 0;
    a3 = 0;
    result = EtwWrite(*(unsigned __int64 *)(v_rip + 7603242), v_rip - 7982421, a3, a4);
    v_stack_m11C = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8))) == 0) goto loc_007BF82D;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)))) & (0xFFFULL)) != 0) goto loc_007BF82D;
    a3 = 0;
    result = MmAllocateMappingAddressEx((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)))), (unsigned int)(0x4B777445ULL), a3, a4);
    v_stack_m110 = result;
    if (result != 0) goto loc_007BF473;
loc_007BF469:
    goto loc_007BF832;
loc_007BF473:
    a4 = 0;
    a3 = 0;
    a1 = 0;
    result = IoAllocateMdl(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)))), a3, a4);
    v_stack_mD0 = result;
    if (result == 0) goto loc_007BF469;
    result = EtwpQueryPersistedMemory(a1, v_stack_mE0, v_stack_m100, v_stack_m120);
    if (sign_flag) goto loc_007BF832;
    a2 = ((unsigned int)(*(unsigned int *)(v_stack_mF8 + 12))) + (v_stack_mF8);
    result = RtlCreateUnicodeString(v_stack_mF0, a2, v_stack_m100, v_stack_m120);
    if ((unsigned __int8)(result) != 0) goto loc_007BF4D7;
    goto loc_007BF832;
loc_007BF4D7:
    a2 = 0;
    a3 = 0;
loc_007BF4DC:
    if (0 >= v_stack_m120) goto loc_007BF507;
    a4 = (*(unsigned __int64 *)(v_stack_m100 + a3 * 8)) >> (40);
    if (a4 == 0) goto loc_007BF4FD;
    a2 = (a2) + (a4);
    a3 = (unsigned int)((a3) + 1);
    goto loc_007BF4DC;
loc_007BF4FD:
    goto loc_007BF832;
loc_007BF507:
    result = ((unsigned int)(*(unsigned int *)((unsigned int)(0xC0190030ULL) + 4))) * ((unsigned int)(*(unsigned int *)(a1 + 8)));
    a2 = (a2) << (12);
    if (a2 != result) goto loc_007BF4FD;
    v_stack_m158 = 0;
    a3 = 0;
    a1 = 0;
    result = EtwpExpandFileName(a1, v_stack_mF0, a3, v_stack_mF0);
    a1 = 0;
    if (sign_flag) goto loc_007BF832;
    v_stack_m148 = 0;
    v_stack_m124 = 0;
    v_stack_m150 = 1;
    v_stack_m158 = 0;
    result = EtwpDelayCreate(v_stack_m108, v_stack_mF0, v_stack_m124, 1);
    if (sign_flag) goto loc_007BF832;
    v_stack_m48 = 0x2000ULL;
    v_stack_m158 = 4;
    result = ZwSetInformationFile(v_stack_m108, v_stack_mC0, v_stack_m68, 40);
    result = EtwpInitializeCompressedWriter(v_stack_mA8, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)))), v_stack_m108, 40);
    if (sign_flag) goto loc_007BF832;
    v_r11 = 0;
    v_rdi = 0;
    v_stack_m114 = 0;
    v_stack_m120 = 0;
    v_stack_mD8 = result + 48;
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8))))) >> (12));
loc_007BF5CC:
    if (0 >= (*(unsigned int *)(v_stack_mF8 + 4))) goto loc_007BF6FE;
    if ((unsigned int)(v_r14) == 0) goto loc_007BF634;
loc_007BF5EF:
    v_rdi = (unsigned int)((v_rdi) + 1);
    a1 = (*(unsigned __int64 *)(v_stack_m100 + 0 * 8)) & ((unsigned int)(*(unsigned int *)(a1 + 8)));
    a1 = (a1) + (0);
    *(unsigned __int64 *)(result + 48) = a1;
    a1 = (*(unsigned __int64 *)(v_stack_m100 + 0 * 8)) >> (40);
    if (((unsigned int)((unsigned int)(v_rdi))) == a1) {
        v_r11 = (unsigned int)((v_r11) + 1);
        v_rdi = 0;
    }
    a4 = (result + 48) + (8);
    v_r10 = ((unsigned int)((unsigned int)(v_r14))) - (1);
    if (condition_is_not_equal) goto loc_007BF5EF;
    v_stack_m114 = (unsigned int)(v_r11);
    v_stack_m120 = 0;
loc_007BF634:
    result = MmMapLockedPagesWithReservedMapping(v_stack_m110, (unsigned int)(0x4B777445ULL), result, 1);
    if ((*(unsigned int *)(result)) == ((unsigned int)((unsigned int)(v_stack_m11C)))) goto loc_007BF661;
loc_007BF654:
    v_rsi = (unsigned int)((0) + 1);
    v_stack_m128 = (unsigned int)(v_rsi);
    goto loc_007BF6BC;
loc_007BF661:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 8)))) <= (*(unsigned int *)(result))) goto loc_007BF66D;
    goto loc_007BF670;
loc_007BF66D:
loc_007BF670:
    *(unsigned int *)(result + 48) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 8)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 8)))) <= ((unsigned int)((unsigned int)(v_stack_m11C)))) goto loc_007BF67E;
    goto loc_007BF654;
loc_007BF67E:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 8)))) <= 72) goto loc_007BF6B8;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m11C)))) - ((unsigned int)((unsigned int)(*(unsigned int *)(result + 8)))));
    result = (unsigned int)(*(unsigned int *)(result + 8));
    if (!(condition_is_equal)) {
        a3 = (unsigned int)(a1);
        a2 = 255;
        a1 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 8)));
        a1 = (a1) + (result);
        result = memset(a1, a2, a3, 1);
    }
    if (0 != 0) goto loc_007BF6AA;
    goto loc_007BF6B8;
loc_007BF6AA:
    result = EtwpWriteBufferCompressed(v_stack_mA8, result, a3, 1);
loc_007BF6B8:
loc_007BF6BC:
    result = MmUnmapReservedMapping(result, (unsigned int)(0x4B777445ULL), result, 1);
    if (!sign_flag) goto loc_007BF6D5;
    if (0 == 0) goto loc_007BF6EA;
loc_007BF6D5:
    v_r13 = (unsigned int)((0) + 1);
    goto loc_007BF5CC;
loc_007BF6EA:
    goto loc_007BF832;
loc_007BF6FE:
    result = EtwpWriteRemainingCompressedData(v_stack_mA8, v_stack_m118, v_stack_m128, 1);
    v_r11 = 0;
    if ((unsigned int)(v_stack_m108) == 0) goto loc_007BF775;
loc_007BF720:
    a1 = (*(unsigned __int64 *)(v_stack_m100 + 0 * 8)) & (result);
    a1 = (a1) + ((unsigned int)((unsigned int)(v_stack_m110)));
    *(unsigned __int64 *)(v_stack_mD8) = a1;
    a4 = (*(unsigned __int64 *)(v_stack_m100 + 0 * 8)) >> (40);
    result = v_r11 + 1;
    if (((unsigned int)((unsigned int)(v_stack_m110 + 1))) != a4) { result = 0; }
    v_rdi = 0;
    if (((unsigned int)((unsigned int)(v_stack_m110 + 1))) != a4) { v_rdi = (unsigned int)(v_stack_m110 + 1); }
    v_rbx = ((unsigned int)((unsigned int)(v_stack_m108))) - (1);
    if (condition_is_not_equal) goto loc_007BF720;
loc_007BF775:
    result = MmMapLockedPagesWithReservedMapping(v_stack_m110, (unsigned int)(0x4B777445ULL), v_stack_mD0, 1);
    *(unsigned int *)(result + 140) = (unsigned int)((unsigned int)(v_stack_m118) + 1);
    *(unsigned int *)(result + 44) = 3;
    if ((*(unsigned int *)(result + 148)) != 4) goto loc_007BF7C4;
    goto loc_007BF7CA;
loc_007BF7C4:
loc_007BF7CA:
    a4 = 0;
    v_stack_m140 = v_stack_mC8;
    a3 = 0;
    a2 = 0;
    v_stack_m148 = (unsigned int)((unsigned int)(v_stack_m11C));
    v_stack_m150 = result;
    v_stack_m158 = v_stack_mC0;
    result = ZwWriteFile(v_stack_m108, a2, a3, a4);
    result = MmUnmapReservedMapping(result, (unsigned int)(0x4B777445ULL), v_stack_mD0, a4);
    if (!sign_flag) goto loc_007BF828;
    v_rsi = (unsigned int)(((unsigned int)(v_stack_m128)) + 1);
loc_007BF821:
    goto loc_007BF832;
loc_007BF828:
    goto loc_007BF821;
loc_007BF82D:
loc_007BF832:
    if (v_stack_m88 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m88, a2, v_stack_mD0, a4);
    }
    if (v_stack_m80 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m80, a2, v_stack_mD0, a4);
    }
    if (v_stack_m108 != 0) {
        a1 = v_stack_m108;
        result = ZwClose(a1, a2, v_stack_mD0, a4);
    }
    if (v_stack_m110 != 0) {
        a2 = 0x4B777445ULL;
        a1 = v_stack_m110;
        result = MmFreeMappingAddress(a1, a2, v_stack_mD0, a4);
    }
    if (v_stack_mD0 != 0) {
        a2 = 0;
        a1 = v_stack_mD0;
        result = ExFreePoolWithTag(a1, a2, v_stack_mD0, a4);
    }
    if (v_stack_m100 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m100, a2, v_stack_mD0, a4);
    }
    result = ext_ms_win_ntos_ksr_l1_1_5_dll_KsrFreePersistedMemoryBlock(v_rip + 3716602, v_stack_mE0, 1, a4);
    v_stack_m150 = (unsigned int)((unsigned int)(0xC01A000DULL));
    v_stack_m158 = (unsigned int)(v_rsi);
    result = EtwpTraceSavePersistedLoggerStop(v_stack_mF0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m11C))), (unsigned int)(*(unsigned int *)(v_stack_mF8 + 4)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m11C))))));
    result = RtlFreeAnsiString(v_stack_mF0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m11C))), (unsigned int)(*(unsigned int *)(v_stack_mF8 + 4)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m11C))))));
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)((unsigned int)((unsigned int)(v_stack_m11C))), (unsigned int)(*(unsigned int *)(v_stack_mF8 + 4)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m11C))))));
    v_rsp = (v_rsp) + (320);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpSavePersistedLogger(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint32_t v_stack_m114;
    uint32_t v_stack_m118;
    uint32_t v_stack_m11C;
    uint32_t v_stack_m120;
    uint64_t v_stack_m124;
    uint32_t v_stack_m128;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint8_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (320);
    result = (*(uint64_t *)(v_rip + 0x64B3A9)) ^ (local_rsp);
    v_stack_m40 = result;
    local_r12 = 0;
    v_stack_mE0 = Arg2;
    v_stack_mF8 = Arg1;
    v_stack_mC8 = 0;
    result = 0;
    v_stack_m120 = 0;
    v_stack_m48 = 0;
    Arg2 = 0;
    v_stack_m108 = 0;
    v_stack_m128 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    v_stack_m118 = 0;
    v_stack_mF0 = v_xmm0;
    v_stack_mC0 = v_xmm1;
    v_stack_m100 = 0;
    result = RtlInitUnicodeString(v_stack_mF0, Arg2, Arg3, Arg4);
    Arg2 = 0;
    result = memset(v_stack_mA8, Arg2, local_r12 + 64, Arg4);
    Arg4 = 0;
    v_stack_m158 = 0;
    Arg3 = 0;
    result = EtwWrite(*(uint64_t *)(v_rip + 0x74042A), v_rip - 7982421, Arg3, Arg4);
    v_stack_m11C = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8))) == 0) goto loc_007BF82D;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)))) & (0xFFFULL)) != 0) goto loc_007BF82D;
    Arg3 = 0;
    result = MmAllocateMappingAddressEx((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)))), (uint32_t)(0x4B777445ULL), Arg3, Arg4);
    v_stack_m110 = result;
    if (result != 0) goto loc_007BF473;
loc_007BF469:
    goto loc_007BF832;
loc_007BF473:
    Arg4 = 0;
    Arg3 = 0;
    Arg1 = 0;
    result = IoAllocateMdl(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)))), Arg3, Arg4);
    v_stack_mD0 = result;
    if (result == 0) goto loc_007BF469;
    result = EtwpQueryPersistedMemory(Arg1, v_stack_mE0, v_stack_m100, v_stack_m120);
    if (sign_flag) goto loc_007BF832;
    Arg2 = ((uint32_t)(*(uint32_t *)(v_stack_mF8 + 0xC))) + (v_stack_mF8);
    result = RtlCreateUnicodeString(v_stack_mF0, Arg2, v_stack_m100, v_stack_m120);
    if ((uint8_t)(result) != 0) goto loc_007BF4D7;
    goto loc_007BF832;
loc_007BF4D7:
    Arg2 = 0;
    Arg3 = 0;
loc_007BF4DC:
    if (0 >= v_stack_m120) goto loc_007BF507;
    Arg4 = (*(uint64_t *)(v_stack_m100 + Arg3 * 8)) >> (40);
    if (Arg4 == 0) goto loc_007BF4FD;
    Arg2 = (Arg2) + (Arg4);
    Arg3 = (uint32_t)((Arg3) + 1);
    goto loc_007BF4DC;
loc_007BF4FD:
    goto loc_007BF832;
loc_007BF507:
    result = ((uint32_t)(*(uint32_t *)((uint32_t)(0xC0190030ULL) + 0x4))) * ((uint32_t)(*(uint32_t *)(arg1 + 0x8)));
    Arg2 = (Arg2) << (12);
    if (Arg2 != result) goto loc_007BF4FD;
    v_stack_m158 = 0;
    Arg3 = 0;
    Arg1 = 0;
    result = EtwpExpandFileName(Arg1, v_stack_mF0, Arg3, v_stack_mF0);
    Arg1 = 0;
    if (sign_flag) goto loc_007BF832;
    v_stack_m148 = 0;
    v_stack_m124 = 0;
    v_stack_m150 = 1;
    v_stack_m158 = 0;
    result = EtwpDelayCreate(v_stack_m108, v_stack_mF0, v_stack_m124, 1);
    if (sign_flag) goto loc_007BF832;
    v_stack_m48 = 0x2000ULL;
    v_stack_m158 = 4;
    result = ZwSetInformationFile(v_stack_m108, v_stack_mC0, v_stack_m68, 40);
    result = EtwpInitializeCompressedWriter(v_stack_mA8, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)))), v_stack_m108, 40);
    if (sign_flag) goto loc_007BF832;
    local_r11 = 0;
    local_rdi = 0;
    v_stack_m114 = 0;
    v_stack_m120 = 0;
    v_stack_mD8 = result + 48;
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8))))) >> (12));
loc_007BF5CC:
    if (0 >= (*(uint32_t *)(v_stack_mF8 + 0x4))) goto loc_007BF6FE;
    if ((uint32_t)(local_r14) == 0) goto loc_007BF634;
loc_007BF5EF:
    local_rdi = (uint32_t)((local_rdi) + 1);
    Arg1 = (*(uint64_t *)(v_stack_m100 + 0x0 * 8)) & ((uint32_t)(*(uint32_t *)(arg1 + 0x8)));
    Arg1 = (Arg1) + (0);
    *(void **)(result + 0x30) = Arg1;
    Arg1 = (*(uint64_t *)(v_stack_m100 + 0x0 * 8)) >> (40);
    if (((uint32_t)((uint32_t)(local_rdi))) == Arg1) {
        local_r11 = (uint32_t)((local_r11) + 1);
        local_rdi = 0;
    }
    Arg4 = (result + 48) + (8);
    local_r10 = ((uint32_t)((uint32_t)(local_r14))) - (1);
    if (condition_is_not_equal) goto loc_007BF5EF;
    v_stack_m114 = (uint32_t)(local_r11);
    v_stack_m120 = 0;
loc_007BF634:
    result = MmMapLockedPagesWithReservedMapping(v_stack_m110, (uint32_t)(0x4B777445ULL), result, 1);
    if ((*(uint32_t *)(result)) == ((uint32_t)((uint32_t)(v_stack_m11C)))) goto loc_007BF661;
loc_007BF654:
    local_rsi = (uint32_t)((0) + 1);
    v_stack_m128 = (uint32_t)(local_rsi);
    goto loc_007BF6BC;
loc_007BF661:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8)))) <= (*(uint32_t *)(result))) goto loc_007BF66D;
    goto loc_007BF670;
loc_007BF66D:
loc_007BF670:
    *(uint32_t *)(result + 0x30) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8)))) <= ((uint32_t)((uint32_t)(v_stack_m11C)))) goto loc_007BF67E;
    goto loc_007BF654;
loc_007BF67E:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8)))) <= 72) goto loc_007BF6B8;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m11C)))) - ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8)))));
    result = (uint32_t)(*(uint32_t *)(result + 0x8));
    if (!(condition_is_equal)) {
        Arg3 = (uint32_t)(Arg1);
        Arg2 = 255;
        Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8)));
        Arg1 = (Arg1) + (result);
        result = memset(Arg1, Arg2, Arg3, 1);
    }
    if (0 != 0) goto loc_007BF6AA;
    goto loc_007BF6B8;
loc_007BF6AA:
    result = EtwpWriteBufferCompressed(v_stack_mA8, result, Arg3, 1);
loc_007BF6B8:
loc_007BF6BC:
    result = MmUnmapReservedMapping(result, (uint32_t)(0x4B777445ULL), result, 1);
    if (!sign_flag) goto loc_007BF6D5;
    if (0 == 0) goto loc_007BF6EA;
loc_007BF6D5:
    local_r13 = (uint32_t)((0) + 1);
    goto loc_007BF5CC;
loc_007BF6EA:
    goto loc_007BF832;
loc_007BF6FE:
    result = EtwpWriteRemainingCompressedData(v_stack_mA8, v_stack_m118, v_stack_m128, 1);
    local_r11 = 0;
    if ((uint32_t)(v_stack_m108) == 0) goto loc_007BF775;
loc_007BF720:
    Arg1 = (*(uint64_t *)(v_stack_m100 + 0x0 * 8)) & (result);
    Arg1 = (Arg1) + ((uint32_t)((uint32_t)(v_stack_m110)));
    *(void **)(v_stack_mD8) = Arg1;
    Arg4 = (*(uint64_t *)(v_stack_m100 + 0x0 * 8)) >> (40);
    result = local_r11 + 1;
    if (((uint32_t)((uint32_t)(v_stack_m110 + 1))) != Arg4) { result = 0; }
    local_rdi = 0;
    if (((uint32_t)((uint32_t)(v_stack_m110 + 1))) != Arg4) { local_rdi = (uint32_t)(v_stack_m110 + 1); }
    local_rbx = ((uint32_t)((uint32_t)(v_stack_m108))) - (1);
    if (condition_is_not_equal) goto loc_007BF720;
loc_007BF775:
    result = MmMapLockedPagesWithReservedMapping(v_stack_m110, (uint32_t)(0x4B777445ULL), v_stack_mD0, 1);
    *(uint32_t *)(result + 0x8C) = (uint32_t)((uint32_t)(v_stack_m118) + 1);
    *(uint32_t *)(result + 0x2C) = 3;
    if ((*(uint32_t *)(result + 0x94)) != 4) goto loc_007BF7C4;
    goto loc_007BF7CA;
loc_007BF7C4:
loc_007BF7CA:
    Arg4 = 0;
    v_stack_m140 = v_stack_mC8;
    Arg3 = 0;
    Arg2 = 0;
    v_stack_m148 = (uint32_t)((uint32_t)(v_stack_m11C));
    v_stack_m150 = result;
    v_stack_m158 = v_stack_mC0;
    result = ZwWriteFile(v_stack_m108, Arg2, Arg3, Arg4);
    result = MmUnmapReservedMapping(result, (uint32_t)(0x4B777445ULL), v_stack_mD0, Arg4);
    if (!sign_flag) goto loc_007BF828;
    local_rsi = (uint32_t)(((uint32_t)(v_stack_m128)) + 1);
loc_007BF821:
    goto loc_007BF832;
loc_007BF828:
    goto loc_007BF821;
loc_007BF82D:
loc_007BF832:
    if (v_stack_m88 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m88, Arg2, v_stack_mD0, Arg4);
    }
    if (v_stack_m80 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m80, Arg2, v_stack_mD0, Arg4);
    }
    if (v_stack_m108 != 0) {
        Arg1 = v_stack_m108;
        result = ZwClose(Arg1, Arg2, v_stack_mD0, Arg4);
    }
    if (v_stack_m110 != 0) {
        Arg2 = 0x4B777445ULL;
        Arg1 = v_stack_m110;
        result = MmFreeMappingAddress(Arg1, Arg2, v_stack_mD0, Arg4);
    }
    if (v_stack_mD0 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_mD0;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_mD0, Arg4);
    }
    if (v_stack_m100 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m100, Arg2, v_stack_mD0, Arg4);
    }
    result = kernel_indirect_call(v_rip + 3716602, v_stack_mE0, 1, Arg4);
    v_stack_m150 = (uint32_t)((uint32_t)(0xC01A000DULL));
    v_stack_m158 = (uint32_t)(local_rsi);
    result = EtwpTraceSavePersistedLoggerStop(v_stack_mF0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m11C))), (uint32_t)(*(uint32_t *)(v_stack_mF8 + 0x4)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m11C))))));
    result = RtlFreeAnsiString(v_stack_mF0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m11C))), (uint32_t)(*(uint32_t *)(v_stack_mF8 + 0x4)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m11C))))));
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)((uint32_t)((uint32_t)(v_stack_m11C))), (uint32_t)(*(uint32_t *)(v_stack_mF8 + 0x4)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m11C))))));
    local_rsp = (local_rsp) + (320);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007BF374&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
