# HalpAllocateDomainCommonBufferInternal

- RVA: `0x003E8B64`–`0x003E8FE9` (길이 `1,157` bytes)
- VA: `0x00000001403E8B64`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000957C4`
- 디코드: `313`개 명령, `1,157/1,157` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **20**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x003E8BDF` → [HalpDmaReferenceDomainObject](HalpDmaReferenceDomainObject_function_003E9B08.md) (function, `0x003E9B08`)
- `0x003E8D15` → [MmAllocateContiguousMemoryEx](MmAllocateContiguousMemoryEx_function_003E9B80.md) (function, `0x003E9B80`)
- `0x003E8D47` → [HalpDmaCvmMakeContiguousVirtualBufferShared](../../page/70/HalpDmaCvmMakeContiguousVirtualBufferShared_function_00709484.md) (function, `0x00709484`)
- `0x003E8D71` → [CvmDebugLog](../4F/CvmDebugLog_function_004FD2C8.md) (function, `0x004FD2C8`)
- `0x003E8D7E` → [MmFreeContiguousMemory](../3F/MmFreeContiguousMemory_function_003F6F60.md) (function, `0x003F6F60`)
- `0x003E8D9F` → [MmFreeContiguousMemory](../3F/MmFreeContiguousMemory_function_003F6F60.md) (function, `0x003F6F60`)
- `0x003E8DEC` → [MmAllocatePagesForMdlEx](MmAllocatePagesForMdlEx_function_003EA8C0.md) (function, `0x003EA8C0`)
- `0x003E8E06` → [MmAllocateNodePagesForMdlEx](MmAllocateNodePagesForMdlEx_function_003EA920.md) (function, `0x003EA920`)
- `0x003E8E30` → [MmMapLockedPagesSpecifyCache](../31/MmMapLockedPagesSpecifyCache_function_00318800.md) (function, `0x00318800`)
- `0x003E8E44` → [MmGetPhysicalAddress](../23/MmGetPhysicalAddress_function_0023A500.md) (function, `0x0023A500`)
- `0x003E8EAA` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x003E8EDE` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x003E8F0D` → [HalpAllocateCommonBufferEntry](HalpAllocateCommonBufferEntry_function_003E99F4.md) (function, `0x003E99F4`)
- `0x003E8F4E` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x003E8F76` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x003E8F86` → [HalpDmaDereferenceDomainObject](../3F/HalpDmaDereferenceDomainObject_function_003F69DC.md) (function, `0x003F69DC`)
- `0x003E8F9B` → [MmUnmapLockedPages](../24/MmUnmapLockedPages_function_00246E60.md) (function, `0x00246E60`)
- `0x003E8FA2` → [MmFreeContiguousMemory](../3F/MmFreeContiguousMemory_function_003F6F60.md) (function, `0x003F6F60`)
- `0x003E8FB9` → [MiFreePagesFromMdl](../3F/MiFreePagesFromMdl_function_003F8300.md) (function, `0x003F8300`)
- `0x003E8FC3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [HalAllocateCommonBufferExV3](HalAllocateCommonBufferExV3_function_003E8880.md) at `0x003E88EC`
- [HalAllocateCommonBufferWithBounds](../55/HalAllocateCommonBufferWithBounds_function_00550240.md) at `0x00550289`
- [HalAllocateDomainCommonBuffer](../55/HalAllocateDomainCommonBuffer_function_00551620.md) at `0x0055166A`

### Static image references
- `0x003E8D22` → RVA `0x00FC18A0` (`.data`; read)
- `0x003E8D50` → RVA `0x00024F00` (`.rdata`; read)
- `0x003E8E6D` → RVA `0x00FC1778` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x003E8D47` → [HalpDmaCvmMakeContiguousVirtualBufferShared](../../page/70/HalpDmaCvmMakeContiguousVirtualBufferShared_function_00709484.md) (`.text` → `PAGE`)
  - `0x003E8FC3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003E8B64  48 8B C4                        mov rax, rsp
003E8B67  48 89 70 08                     mov qword ptr [rax + 8], rsi
003E8B6B  48 89 78 10                     mov qword ptr [rax + 0x10], rdi
003E8B6F  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
003E8B73  55                              push rbp
003E8B74  41 54                           push r12
003E8B76  41 55                           push r13
003E8B78  41 56                           push r14
003E8B7A  41 57                           push r15
003E8B7C  48 8D 68 C9                     lea rbp, [rax - 0x37]
003E8B80  48 81 EC C0 00 00 00            sub rsp, 0xc0
003E8B87  48 83 65 F7 00                  and qword ptr [rbp - 9], 0
003E8B8C  33 C0                           xor eax, eax
003E8B8E  48 83 65 FF 00                  and qword ptr [rbp - 1], 0
003E8B93  41 81 C1 FF 0F 00 00            add r9d, 0xfff
003E8B9A  48 83 65 C7 00                  and qword ptr [rbp - 0x39], 0
003E8B9F  41 81 E1 00 F0 FF FF            and r9d, 0xfffff000
003E8BA6  48 21 45 CF                     and qword ptr [rbp - 0x31], rax
003E8BAA  0F 57 C0                        xorps xmm0, xmm0
003E8BAD  48 21 45 BF                     and qword ptr [rbp - 0x41], rax
003E8BB1  45 33 E4                        xor r12d, r12d
003E8BB4  44 89 4D A3                     mov dword ptr [rbp - 0x5d], r9d
003E8BB8  48 8B FA                        mov rdi, rdx
003E8BBB  4C 8B E9                        mov r13, rcx
003E8BBE  89 45 EF                        mov dword ptr [rbp - 0x11], eax
003E8BC1  0F 11 45 DF                     movups xmmword ptr [rbp - 0x21], xmm0
003E8BC5  4C 89 65 B7                     mov qword ptr [rbp - 0x49], r12
003E8BC9  45 33 FF                        xor r15d, r15d
003E8BCC  88 45 A1                        mov byte ptr [rbp - 0x5f], al
003E8BCF  88 45 A0                        mov byte ptr [rbp - 0x60], al
003E8BD2  88 45 57                        mov byte ptr [rbp + 0x57], al
003E8BD5  88 45 9F                        mov byte ptr [rbp - 0x61], al
003E8BD8  C7 45 A7 15 00 00 00            mov dword ptr [rbp - 0x59], 0x15
003E8BDF  E8 24 0F 00 00                  call 0x1403e9b08
003E8BE4  44 8B F0                        mov r14d, eax
003E8BE7  85 C0                           test eax, eax
003E8BE9  0F 88 D9 03 00 00               js 0x1403e8fc8
003E8BEF  49 8B 45 38                     mov rax, qword ptr [r13 + 0x38]
003E8BF3  45 8D 74 24 01                  lea r14d, [r12 + 1]
003E8BF8  48 85 C0                        test rax, rax
003E8BFB  74 07                           je 0x1403e8c04
003E8BFD  44 88 B0 0C 02 00 00            mov byte ptr [rax + 0x20c], r14b
003E8C04  33 F6                           xor esi, esi
003E8C06  48 85 FF                        test rdi, rdi
003E8C09  74 03                           je 0x1403e8c0e
003E8C0B  48 8B 37                        mov rsi, qword ptr [rdi]
003E8C0E  48 8B 45 4F                     mov rax, qword ptr [rbp + 0x4f]
003E8C12  49 8B 7D 10                     mov rdi, qword ptr [r13 + 0x10]
003E8C16  48 85 C0                        test rax, rax
003E8C19  74 0A                           je 0x1403e8c25
003E8C1B  48 8B 00                        mov rax, qword ptr [rax]
003E8C1E  48 3B F8                        cmp rdi, rax
003E8C21  48 0F 47 F8                     cmova rdi, rax
003E8C25  48 8B 45 67                     mov rax, qword ptr [rbp + 0x67]
003E8C29  33 D2                           xor edx, edx
003E8C2B  41 38 55 20                     cmp byte ptr [r13 + 0x20], dl
003E8C2F  0F 95 C2                        setne dl
003E8C32  89 55 AB                        mov dword ptr [rbp - 0x55], edx
003E8C35  48 85 C0                        test rax, rax
003E8C38  74 19                           je 0x1403e8c53
003E8C3A  8B 10                           mov edx, dword ptr [rax]
003E8C3C  89 55 AB                        mov dword ptr [rbp - 0x55], edx
003E8C3F  85 D2                           test edx, edx
003E8C41  74 10                           je 0x1403e8c53
003E8C43  41 3B D6                        cmp edx, r14d
003E8C46  74 0B                           je 0x1403e8c53
003E8C48  41 BE 0D 00 00 C0               mov r14d, 0xc000000d
003E8C4E  E9 30 03 00 00                  jmp 0x1403e8f83
003E8C53  4D 8B 4D 18                     mov r9, qword ptr [r13 + 0x18]
003E8C57  8B C2                           mov eax, edx
003E8C59  44 8B 45 A3                     mov r8d, dword ptr [rbp - 0x5d]
003E8C5D  F7 D8                           neg eax
003E8C5F  45 1B D2                        sbb r10d, r10d
003E8C62  41 81 E2 00 FE FF FF            and r10d, 0xfffffe00
003E8C69  41 81 C2 04 02 00 00            add r10d, 0x204
003E8C70  44 84 75 5F                     test byte ptr [rbp + 0x5f], r14b
003E8C74  74 38                           je 0x1403e8cae
003E8C76  41 81 C0 FF FF 1F 00            add r8d, 0x1fffff
003E8C7D  41 8B CE                        mov ecx, r14d
003E8C80  41 81 E0 00 00 E0 FF            and r8d, 0xffe00000
003E8C87  44 89 45 A3                     mov dword ptr [rbp - 0x5d], r8d
003E8C8B  45 8B C8                        mov r9d, r8d
003E8C8E  49 8B C6                        mov rax, r14
003E8C91  48 D3 E0                        shl rax, cl
003E8C94  49 3B C1                        cmp rax, r9
003E8C97  73 08                           jae 0x1403e8ca1
003E8C99  41 03 CE                        add ecx, r14d
003E8C9C  83 F9 3F                        cmp ecx, 0x3f
003E8C9F  72 ED                           jb 0x1403e8c8e
003E8CA1  4D 8B CE                        mov r9, r14
003E8CA4  C7 45 A7 65 00 00 00            mov dword ptr [rbp - 0x59], 0x65
003E8CAB  49 D3 E1                        shl r9, cl
003E8CAE  41 8B 4D 30                     mov ecx, dword ptr [r13 + 0x30]
003E8CB2  83 F9 02                        cmp ecx, 2
003E8CB5  75 05                           jne 0x1403e8cbc
003E8CB7  45 8B DE                        mov r11d, r14d
003E8CBA  EB 1D                           jmp 0x1403e8cd9
003E8CBC  45 33 DB                        xor r11d, r11d
003E8CBF  85 C9                           test ecx, ecx
003E8CC1  74 16                           je 0x1403e8cd9
003E8CC3  41 2B CE                        sub ecx, r14d
003E8CC6  74 0D                           je 0x1403e8cd5
003E8CC8  41 3B CE                        cmp ecx, r14d
003E8CCB  74 0C                           je 0x1403e8cd9
003E8CCD  8B 45 A7                        mov eax, dword ptr [rbp - 0x59]
003E8CD0  E9 EB 00 00 00                  jmp 0x1403e8dc0
003E8CD5  44 88 75 9F                     mov byte ptr [rbp - 0x61], r14b
003E8CD9  45 8B F0                        mov r14d, r8d
003E8CDC  48 8D 45 B7                     lea rax, [rbp - 0x49]
003E8CE0  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
003E8CE5  48 8D 4D AF                     lea rcx, [rbp - 0x51]
003E8CE9  8B 45 6F                        mov eax, dword ptr [rbp + 0x6f]
003E8CEC  4C 8B C7                        mov r8, rdi
003E8CEF  44 89 5C 24 40                  mov dword ptr [rsp + 0x40], r11d
003E8CF4  48 8B D6                        mov rdx, rsi
003E8CF7  C7 44 24 38 48 61 6C 44         mov dword ptr [rsp + 0x38], 0x446c6148
003E8CFF  4C 21 64 24 30                  and qword ptr [rsp + 0x30], r12
003E8D04  44 89 54 24 28                  mov dword ptr [rsp + 0x28], r10d
003E8D09  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
003E8D0D  4C 89 75 D7                     mov qword ptr [rbp - 0x29], r14
003E8D11  4C 89 75 AF                     mov qword ptr [rbp - 0x51], r14
003E8D15  E8 66 0E 00 00                  call 0x1403e9b80
003E8D1A  85 C0                           test eax, eax
003E8D1C  0F 88 82 00 00 00               js 0x1403e8da4
003E8D22  44 38 25 77 8B BD 00            cmp byte ptr [rip + 0xbd8b77], r12b
003E8D29  74 5D                           je 0x1403e8d88
003E8D2B  4C 39 75 AF                     cmp qword ptr [rbp - 0x51], r14
003E8D2F  75 57                           jne 0x1403e8d88
003E8D31  48 8B 45 B7                     mov rax, qword ptr [rbp - 0x49]
003E8D35  4C 8D 4D C7                     lea r9, [rbp - 0x39]
003E8D39  48 8B C8                        mov rcx, rax
003E8D3C  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
003E8D40  4C 8D 45 B7                     lea r8, [rbp - 0x49]
003E8D44  41 8B D6                        mov edx, r14d
003E8D47  E8 38 07 32 00                  call 0x140709484
003E8D4C  4C 8B 65 B7                     mov r12, qword ptr [rbp - 0x49]
003E8D50  48 8D 0D A9 C1 C3 FF            lea rcx, [rip - 0x3c3e57]
003E8D57  4C 8B 45 AF                     mov r8, qword ptr [rbp - 0x51]
003E8D5B  44 8B F0                        mov r14d, eax
003E8D5E  48 8B 45 C7                     mov rax, qword ptr [rbp - 0x39]
003E8D62  4D 8B CC                        mov r9, r12
003E8D65  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003E8D6A  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
003E8D6E  48 8B D0                        mov rdx, rax
003E8D71  E8 52 45 11 00                  call 0x1404fd2c8
003E8D76  45 85 F6                        test r14d, r14d
003E8D79  79 13                           jns 0x1403e8d8e
003E8D7B  48 8B C8                        mov rcx, rax
003E8D7E  E8 DD E1 00 00                  call 0x1403f6f60
003E8D83  E9 FB 01 00 00                  jmp 0x1403e8f83
003E8D88  4C 8B 65 B7                     mov r12, qword ptr [rbp - 0x49]
003E8D8C  EB 04                           jmp 0x1403e8d92
003E8D8E  4C 8B 75 D7                     mov r14, qword ptr [rbp - 0x29]
003E8D92  4C 39 75 AF                     cmp qword ptr [rbp - 0x51], r14
003E8D96  0F 84 9C 00 00 00               je 0x1403e8e38
003E8D9C  49 8B CC                        mov rcx, r12
003E8D9F  E8 BC E1 00 00                  call 0x1403f6f60
003E8DA4  45 33 E4                        xor r12d, r12d
003E8DA7  41 83 7D 30 02                  cmp dword ptr [r13 + 0x30], 2
003E8DAC  0F 85 CB 01 00 00               jne 0x1403e8f7d
003E8DB2  8B 45 A7                        mov eax, dword ptr [rbp - 0x59]
003E8DB5  45 8D 74 24 01                  lea r14d, [r12 + 1]
003E8DBA  8B 55 AB                        mov edx, dword ptr [rbp - 0x55]
003E8DBD  83 E0 EF                        and eax, 0xffffffef
003E8DC0  44 8B 4D A3                     mov r9d, dword ptr [rbp - 0x5d]
003E8DC4  45 33 C0                        xor r8d, r8d
003E8DC7  8B 4D 6F                        mov ecx, dword ptr [rbp + 0x6f]
003E8DCA  44 88 75 57                     mov byte ptr [rbp + 0x57], r14b
003E8DCE  45 8B F1                        mov r14d, r9d
003E8DD1  4C 89 4D D7                     mov qword ptr [rbp - 0x29], r9
003E8DD5  81 F9 00 00 00 80               cmp ecx, 0x80000000
003E8DDB  75 16                           jne 0x1403e8df3
003E8DDD  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
003E8DE1  48 8B CE                        mov rcx, rsi
003E8DE4  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
003E8DE8  49 8B 55 10                     mov rdx, qword ptr [r13 + 0x10]
003E8DEC  E8 CF 1A 00 00                  call 0x1403ea8c0
003E8DF1  EB 18                           jmp 0x1403e8e0b
003E8DF3  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
003E8DF7  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
003E8DFB  48 8B CE                        mov rcx, rsi
003E8DFE  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
003E8E02  49 8B 55 10                     mov rdx, qword ptr [r13 + 0x10]
003E8E06  E8 15 1B 00 00                  call 0x1403ea920
003E8E0B  4C 8B F8                        mov r15, rax
003E8E0E  48 85 C0                        test rax, rax
003E8E11  0F 84 66 01 00 00               je 0x1403e8f7d
003E8E17  44 8B 45 AB                     mov r8d, dword ptr [rbp - 0x55]
003E8E1B  45 33 C9                        xor r9d, r9d
003E8E1E  C7 44 24 28 10 00 00 40         mov dword ptr [rsp + 0x28], 0x40000010
003E8E26  33 D2                           xor edx, edx
003E8E28  83 64 24 20 00                  and dword ptr [rsp + 0x20], 0
003E8E2D  48 8B C8                        mov rcx, rax
003E8E30  E8 CB F9 F2 FF                  call 0x140318800
003E8E35  4C 8B E0                        mov r12, rax
003E8E38  4D 85 E4                        test r12, r12
003E8E3B  0F 84 3C 01 00 00               je 0x1403e8f7d
003E8E41  49 8B CC                        mov rcx, r12
003E8E44  E8 B7 16 E5 FF                  call 0x14023a500
003E8E49  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
003E8E4D  4D 85 FF                        test r15, r15
003E8E50  75 11                           jne 0x1403e8e63
003E8E52  C7 45 DF 01 00 00 00            mov dword ptr [rbp - 0x21], 1
003E8E59  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
003E8E5D  4C 89 75 EF                     mov qword ptr [rbp - 0x11], r14
003E8E61  EB 04                           jmp 0x1403e8e67
003E8E63  4C 89 7D E7                     mov qword ptr [rbp - 0x19], r15
003E8E67  80 7D 57 00                     cmp byte ptr [rbp + 0x57], 0
003E8E6B  74 53                           je 0x1403e8ec0
003E8E6D  48 8B 05 04 89 BD 00            mov rax, qword ptr [rip + 0xbd8904]
003E8E74  48 8D 4D BF                     lea rcx, [rbp - 0x41]
003E8E78  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
003E8E7D  4C 8D 45 DF                     lea r8, [rbp - 0x21]
003E8E81  48 8D 4D F7                     lea rcx, [rbp - 9]
003E8E85  48 89 75 FF                     mov qword ptr [rbp - 1], rsi
003E8E89  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
003E8E8E  45 33 C9                        xor r9d, r9d
003E8E91  48 8D 4D FF                     lea rcx, [rbp - 1]
003E8E95  48 89 7D F7                     mov qword ptr [rbp - 9], rdi
003E8E99  48 8B 40 38                     mov rax, qword ptr [rax + 0x38]
003E8E9D  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
003E8EA2  49 8B 4D 28                     mov rcx, qword ptr [r13 + 0x28]
003E8EA6  41 8D 51 03                     lea edx, [r9 + 3]
003E8EAA  E8 21 1C 2D 00                  call 0x1406baad0
003E8EAF  44 8B F0                        mov r14d, eax
003E8EB2  85 C0                           test eax, eax
003E8EB4  0F 88 C9 00 00 00               js 0x1403e8f83
003E8EBA  C6 45 A1 01                     mov byte ptr [rbp - 0x5f], 1
003E8EBE  EB 32                           jmp 0x1403e8ef2
003E8EC0  80 7D 9F 00                     cmp byte ptr [rbp - 0x61], 0
003E8EC4  74 2C                           je 0x1403e8ef2
003E8EC6  48 8B 05 AB 88 BD 00            mov rax, qword ptr [rip + 0xbd88ab]
003E8ECD  4C 8D 45 DF                     lea r8, [rbp - 0x21]
003E8ED1  49 8B 4D 28                     mov rcx, qword ptr [r13 + 0x28]
003E8ED5  BA 03 00 00 00                  mov edx, 3
003E8EDA  48 8B 40 48                     mov rax, qword ptr [rax + 0x48]
003E8EDE  E8 ED 1B 2D 00                  call 0x1406baad0
003E8EE3  44 8B F0                        mov r14d, eax
003E8EE6  85 C0                           test eax, eax
003E8EE8  0F 88 95 00 00 00               js 0x1403e8f83
003E8EEE  C6 45 A0 01                     mov byte ptr [rbp - 0x60], 1
003E8EF2  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
003E8EF6  4D 8B CD                        mov r9, r13
003E8EF9  4C 8B 45 BF                     mov r8, qword ptr [rbp - 0x41]
003E8EFD  49 8B D4                        mov rdx, r12
003E8F00  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
003E8F05  49 8B CF                        mov rcx, r15
003E8F08  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
003E8F0D  E8 E2 0A 00 00                  call 0x1403e99f4
003E8F12  44 8B F0                        mov r14d, eax
003E8F15  8B F8                           mov edi, eax
003E8F17  85 C0                           test eax, eax
003E8F19  78 17                           js 0x1403e8f32
003E8F1B  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
003E8F1F  48 8B 4D 77                     mov rcx, qword ptr [rbp + 0x77]
003E8F23  48 89 01                        mov qword ptr [rcx], rax
003E8F26  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
003E8F2A  4C 89 20                        mov qword ptr [rax], r12
003E8F2D  E9 96 00 00 00                  jmp 0x1403e8fc8
003E8F32  80 7D A0 00                     cmp byte ptr [rbp - 0x60], 0
003E8F36  49 8B F7                        mov rsi, r15
003E8F39  74 1A                           je 0x1403e8f55
003E8F3B  48 8B 05 36 88 BD 00            mov rax, qword ptr [rip + 0xbd8836]
003E8F42  48 8D 55 DF                     lea rdx, [rbp - 0x21]
003E8F46  49 8B 4D 28                     mov rcx, qword ptr [r13 + 0x28]
003E8F4A  48 8B 40 50                     mov rax, qword ptr [rax + 0x50]
003E8F4E  E8 7D 1B 2D 00                  call 0x1406baad0
003E8F53  EB 2E                           jmp 0x1403e8f83
003E8F55  80 7D A1 00                     cmp byte ptr [rbp - 0x5f], 0
003E8F59  74 28                           je 0x1403e8f83
003E8F5B  48 8B 05 16 88 BD 00            mov rax, qword ptr [rip + 0xbd8816]
003E8F62  4C 8B 45 D7                     mov r8, qword ptr [rbp - 0x29]
003E8F66  48 8B 55 BF                     mov rdx, qword ptr [rbp - 0x41]
003E8F6A  49 8B 4D 28                     mov rcx, qword ptr [r13 + 0x28]
003E8F6E  48 8B 40 40                     mov rax, qword ptr [rax + 0x40]
003E8F72  49 C1 E8 0C                     shr r8, 0xc
003E8F76  E8 55 1B 2D 00                  call 0x1406baad0
003E8F7B  EB 06                           jmp 0x1403e8f83
003E8F7D  41 BE 9A 00 00 C0               mov r14d, 0xc000009a
003E8F83  49 8B CD                        mov rcx, r13
003E8F86  E8 51 DA 00 00                  call 0x1403f69dc
003E8F8B  4D 85 E4                        test r12, r12
003E8F8E  74 19                           je 0x1403e8fa9
003E8F90  49 8B CC                        mov rcx, r12
003E8F93  4D 85 FF                        test r15, r15
003E8F96  74 0A                           je 0x1403e8fa2
003E8F98  49 8B D7                        mov rdx, r15
003E8F9B  E8 C0 DE E5 FF                  call 0x140246e60
003E8FA0  EB 0C                           jmp 0x1403e8fae
003E8FA2  E8 B9 DF 00 00                  call 0x1403f6f60
003E8FA7  EB 1F                           jmp 0x1403e8fc8
003E8FA9  4D 85 FF                        test r15, r15
003E8FAC  74 1A                           je 0x1403e8fc8
003E8FAE  45 33 C9                        xor r9d, r9d
003E8FB1  45 33 C0                        xor r8d, r8d
003E8FB4  33 D2                           xor edx, edx
003E8FB6  49 8B CF                        mov rcx, r15
003E8FB9  E8 42 F3 00 00                  call 0x1403f8300
003E8FBE  33 D2                           xor edx, edx
003E8FC0  49 8B CF                        mov rcx, r15
003E8FC3  E8 A8 98 79 00                  call 0x140b82870
003E8FC8  4C 8D 9C 24 C0 00 00 00         lea r11, [rsp + 0xc0]
003E8FD0  41 8B C6                        mov eax, r14d
003E8FD3  49 8B 73 30                     mov rsi, qword ptr [r11 + 0x30]
003E8FD7  49 8B 7B 38                     mov rdi, qword ptr [r11 + 0x38]
003E8FDB  49 8B E3                        mov rsp, r11
003E8FDE  41 5F                           pop r15
003E8FE0  41 5E                           pop r14
003E8FE2  41 5D                           pop r13
003E8FE4  41 5C                           pop r12
003E8FE6  5D                              pop rbp
003E8FE7  C3                              ret
003E8FE8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpAllocateDomainCommonBufferInternal(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA8;
    unsigned int v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned int v_stack_mC8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 16) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (192);
    result = 0;
    a4 = (unsigned int)((a4) + (0xFFFULL));
    a4 = (unsigned int)((a4) & (0xFFFFF000ULL));
    v_r12 = 0;
    *(unsigned int *)(v_rsp - 55 - 93) = a4;
    *(unsigned int *)(v_rsp - 55 - 17) = 0;
    *(unsigned __int64 *)(v_rsp - 55 - 33) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 55 - 73) = 0;
    v_r15 = 0;
    *(unsigned __int8 *)(v_rsp - 55 - 95) = 0;
    *(unsigned __int8 *)(v_rsp - 55 - 96) = 0;
    *(unsigned __int8 *)(v_rsp - 55 + 87) = 0;
    *(unsigned __int8 *)(v_rsp - 55 - 97) = 0;
    *(unsigned int *)(v_rsp - 55 - 89) = 21;
    result = HalpDmaReferenceDomainObject(a1, a2, a3, a4);
    if (sign_flag) goto loc_003E8FC8;
    if (*(unsigned __int64 *)(a1 + 56) != 0) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 56) + 524) = (unsigned __int8)(v_r12 + 1);
    }
    v_rsi = 0;
    if (a2 != 0) {
        v_rsi = *(unsigned __int64 *)(a2);
    }
    result = *(unsigned __int64 *)(v_rsp - 55 + 79);
    v_rdi = *(unsigned __int64 *)(a1 + 16);
    if (*(unsigned __int64 *)(v_rsp - 55 + 79) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 55 + 79));
        v_rdi = *(unsigned __int64 *)(a1 + 16);
        if ((*(unsigned __int64 *)(a1 + 16)) > result) { v_rdi = result; }
    }
    a2 = 0;
    a2 = ((*(unsigned __int8 *)(a1 + 32)) != 0) ? 1 : 0;
    *(unsigned int *)(v_rsp - 55 - 85) = (unsigned int)(a2);
    if (*(unsigned __int64 *)(v_rsp - 55 + 103) == 0) goto loc_003E8C53;
    *(unsigned int *)(v_rsp - 55 - 85) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 55 + 103))));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 55 + 103)))) == 0) goto loc_003E8C53;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 55 + 103))))) == ((unsigned int)(v_r12 + 1))) goto loc_003E8C53;
    goto loc_003E8F83;
loc_003E8C53:
    result = (unsigned int)(-((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 55 + 103)))))));
    v_r10 = (unsigned int)((v_r10) & (0xFFFFFE00ULL));
    v_r10 = (unsigned int)((v_r10) + (516));
    if (((*(unsigned __int8 *)(v_rsp - 55 + 95)) & ((unsigned __int8)((unsigned int)(0xC000000DULL)))) == 0) goto loc_003E8CAE;
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 55 - 93))) + (0x1FFFFFULL));
    a3 = (unsigned int)((a3) & (0xFFE00000ULL));
    *(unsigned int *)(v_rsp - 55 - 93) = (unsigned int)(a3);
loc_003E8C8E:
    result = ((unsigned int)(0xC000000DULL)) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)))));
    if (result >= ((unsigned int)((unsigned int)(a3)))) goto loc_003E8CA1;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)))) + ((unsigned int)((unsigned int)(0xC000000DULL))));
    if (((unsigned int)(a1)) < 63) goto loc_003E8C8E;
loc_003E8CA1:
    *(unsigned int *)(v_rsp - 55 - 89) = 101;
    a4 = ((unsigned int)(0xC000000DULL)) << ((unsigned __int8)(a1));
loc_003E8CAE:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)))) != 2) goto loc_003E8CBC;
    goto loc_003E8CD9;
loc_003E8CBC:
    v_r11 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48))) == 0) goto loc_003E8CD9;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 48))) - ((unsigned int)((unsigned int)(0xC000000DULL))));
    if (condition_is_equal) goto loc_003E8CD5;
    if (((unsigned int)(a1)) == ((unsigned int)((unsigned int)(0xC000000DULL)))) goto loc_003E8CD9;
    goto loc_003E8DC0;
loc_003E8CD5:
    *(unsigned __int8 *)(v_rsp - 55 - 97) = (unsigned __int8)((unsigned int)(0xC000000DULL));
loc_003E8CD9:
    v_stack_mA0 = v_rsp - 55 - 73;
    v_stack_mA8 = 0;
    v_stack_mB0 = 0x446C6148ULL;
    v_stack_mC0 = (unsigned int)(v_r10);
    v_stack_mC8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 55 + 111)));
    *(unsigned __int64 *)(v_rsp - 55 - 41) = (unsigned int)((unsigned int)(a3));
    *(unsigned __int64 *)(v_rsp - 55 - 81) = (unsigned int)((unsigned int)(a3));
    result = MmAllocateContiguousMemoryEx(v_rsp - 55 - 81, v_rsi, v_rdi, a4);
    if (sign_flag) goto loc_003E8DA4;
    if ((*(unsigned __int8 *)(v_rip + 12422007)) == 0) goto loc_003E8D88;
    if ((*(unsigned __int64 *)(v_rsp - 55 - 81)) != ((unsigned int)((unsigned int)(a3)))) goto loc_003E8D88;
    *(unsigned __int64 *)(v_rsp - 55 - 49) = *(unsigned __int64 *)(v_rsp - 55 - 73);
    result = HalpDmaCvmMakeContiguousVirtualBufferShared(*(unsigned __int64 *)(v_rsp - 55 - 73), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a3)))), v_rsp - 55 - 73, v_rsp - 55 - 57);
    v_stack_mC8 = *(unsigned __int64 *)(v_rsp - 55 - 57);
    result = CvmDebugLog(v_rip - 3948119, *(unsigned __int64 *)(v_rsp - 55 - 49), *(unsigned __int64 *)(v_rsp - 55 - 81), *(unsigned __int64 *)(v_rsp - 55 - 73));
    if (!sign_flag) goto loc_003E8D8E;
    result = MmFreeContiguousMemory(result, *(unsigned __int64 *)(v_rsp - 55 - 49), *(unsigned __int64 *)(v_rsp - 55 - 81), *(unsigned __int64 *)(v_rsp - 55 - 73));
    goto loc_003E8F83;
loc_003E8D88:
    goto loc_003E8D92;
loc_003E8D8E:
loc_003E8D92:
    if ((*(unsigned __int64 *)(v_rsp - 55 - 81)) == (*(unsigned __int64 *)(v_rsp - 55 - 41))) goto loc_003E8E38;
    result = MmFreeContiguousMemory(*(unsigned __int64 *)(v_rsp - 55 - 73), *(unsigned __int64 *)(v_rsp - 55 - 49), *(unsigned __int64 *)(v_rsp - 55 - 81), *(unsigned __int64 *)(v_rsp - 55 - 73));
loc_003E8DA4:
    v_r12 = 0;
    if ((*(unsigned int *)(a1 + 48)) != 2) goto loc_003E8F7D;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 55 - 89))) & (0xFFFFFFEFULL));
loc_003E8DC0:
    a3 = 0;
    *(unsigned __int8 *)(v_rsp - 55 + 87) = (unsigned __int8)(v_r12 + 1);
    *(unsigned __int64 *)(v_rsp - 55 - 41) = (unsigned int)(*(unsigned int *)(v_rsp - 55 - 93));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 55 + 111)))) != 0x80000000ULL) goto loc_003E8DF3;
    v_stack_mC0 = (unsigned int)(result);
    v_stack_mC8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 55 - 85)));
    result = MmAllocatePagesForMdlEx(v_rsi, *(unsigned __int64 *)(a1 + 16), a3, (unsigned int)(*(unsigned int *)(v_rsp - 55 - 93)));
    goto loc_003E8E0B;
loc_003E8DF3:
    v_stack_mB8 = (unsigned int)(result);
    v_stack_mC0 = (unsigned int)(v_rsi);
    v_stack_mC8 = (unsigned int)(*(unsigned __int64 *)(a1 + 16));
    result = MmAllocateNodePagesForMdlEx(v_rsi, *(unsigned __int64 *)(a1 + 16), a3, (unsigned int)(*(unsigned int *)(v_rsp - 55 - 93)));
loc_003E8E0B:
    if (result == 0) goto loc_003E8F7D;
    a4 = 0;
    v_stack_mC0 = 0x40000010ULL;
    a2 = 0;
    result = MmMapLockedPagesSpecifyCache(result, a2, (unsigned int)(*(unsigned int *)(v_rsp - 55 - 85)), a4);
loc_003E8E38:
    if (result == 0) goto loc_003E8F7D;
    result = MmGetPhysicalAddress(result, a2, (unsigned int)(*(unsigned int *)(v_rsp - 55 - 85)), a4);
    *(unsigned __int64 *)(v_rsp - 55 - 65) = result;
    if (result != 0) goto loc_003E8E63;
    *(unsigned int *)(v_rsp - 55 - 33) = 1;
    *(unsigned __int64 *)(v_rsp - 55 - 25) = result;
    *(unsigned __int64 *)(v_rsp - 55 - 17) = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 55 - 93))));
    goto loc_003E8E67;
loc_003E8E63:
    *(unsigned __int64 *)(v_rsp - 55 - 25) = result;
loc_003E8E67:
    if ((*(unsigned __int8 *)(v_rsp - 55 + 87)) == 0) goto loc_003E8EC0;
    v_stack_mB8 = v_rsp - 55 - 65;
    *(unsigned __int64 *)(v_rsp - 55 - 1) = v_rsi;
    v_stack_mC0 = v_rsp - 55 - 9;
    a4 = 0;
    *(unsigned __int64 *)(v_rsp - 55 - 9) = v_rdi;
    v_stack_mC8 = v_rsp - 55 - 1;
    result = guard_dispatch_icall(*(unsigned __int64 *)(a1 + 40), a4 + 3, v_rsp - 55 - 33, a4);
    if (sign_flag) goto loc_003E8F83;
    *(unsigned __int8 *)(v_rsp - 55 - 95) = 1;
    goto loc_003E8EF2;
loc_003E8EC0:
    if ((*(unsigned __int8 *)(v_rsp - 55 - 97)) == 0) goto loc_003E8EF2;
    result = guard_dispatch_icall(*(unsigned __int64 *)(a1 + 40), 3, v_rsp - 55 - 33, a4);
    if (sign_flag) goto loc_003E8F83;
    *(unsigned __int8 *)(v_rsp - 55 - 96) = 1;
loc_003E8EF2:
    v_stack_mC0 = *(unsigned __int64 *)(v_rsp - 55 - 49);
    v_stack_mC8 = 1;
    result = HalpAllocateCommonBufferEntry(result, result, *(unsigned __int64 *)(v_rsp - 55 - 65), a1);
    if (sign_flag) goto loc_003E8F32;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 55 + 119)) = *(unsigned __int64 *)(v_rsp - 55 - 65);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 55 + 127)) = result;
    goto loc_003E8FC8;
loc_003E8F32:
    if ((*(unsigned __int8 *)(v_rsp - 55 - 96)) == 0) goto loc_003E8F55;
    result = guard_dispatch_icall(*(unsigned __int64 *)(a1 + 40), v_rsp - 55 - 33, *(unsigned __int64 *)(v_rsp - 55 - 65), a1);
    goto loc_003E8F83;
loc_003E8F55:
    if ((*(unsigned __int8 *)(v_rsp - 55 - 95)) == 0) goto loc_003E8F83;
    a3 = (*(unsigned __int64 *)(v_rsp - 55 - 41)) >> (12);
    result = guard_dispatch_icall(*(unsigned __int64 *)(a1 + 40), *(unsigned __int64 *)(v_rsp - 55 - 65), a3, a1);
    goto loc_003E8F83;
loc_003E8F7D:
loc_003E8F83:
    result = HalpDmaDereferenceDomainObject(a1, *(unsigned __int64 *)(v_rsp - 55 - 65), a3, a1);
    if (result == 0) goto loc_003E8FA9;
    if (result == 0) goto loc_003E8FA2;
    result = MmUnmapLockedPages(result, result, a3, a1);
    goto loc_003E8FAE;
loc_003E8FA2:
    result = MmFreeContiguousMemory(result, result, a3, a1);
    goto loc_003E8FC8;
loc_003E8FA9:
    if (result != 0) {
        a4 = 0;
        a3 = 0;
        a2 = 0;
        a1 = result;
        result = MiFreePagesFromMdl(a1, a2, a3, a4);
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    return (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL)));
}
```

## 5. (Beta) C Style

```c
int64_t HalpAllocateDomainCommonBufferInternal(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA8;
    uint32_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint32_t v_stack_mC8;

    *(uint64_t *)(local_rsp + 0x8) = local_rsi;
    *(uint64_t *)(local_rsp + 0x10) = local_rdi;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (192);
    result = 0;
    Arg4 = (uint32_t)((Arg4) + (0xFFFULL));
    Arg4 = (uint32_t)((Arg4) & (0xFFFFF000ULL));
    local_r12 = 0;
    *(uint32_t *)(local_rsp - 0x37 - 0x5D) = Arg4;
    *(uint32_t *)(local_rsp - 0x37 - 0x11) = 0;
    *(uint64_t *)(local_rsp - 0x37 - 0x21) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x37 - 0x49) = 0;
    local_r15 = 0;
    *(uint8_t *)(local_rsp - 0x37 - 0x5F) = 0;
    *(uint8_t *)(local_rsp - 0x37 - 0x60) = 0;
    *(uint8_t *)(local_rsp - 0x37 + 0x57) = 0;
    *(uint8_t *)(local_rsp - 0x37 - 0x61) = 0;
    *(uint32_t *)(local_rsp - 0x37 - 0x59) = 21;
    result = HalpDmaReferenceDomainObject(Arg1, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_003E8FC8;
    if (*(uint64_t *)(arg1 + 0x38) != 0) {
        *(uint8_t *)(*(uint64_t *)(arg1 + 0x38) + 0x20C) = (uint8_t)(local_r12 + 1);
    }
    local_rsi = 0;
    if (Arg2 != 0) {
        local_rsi = *(uint64_t *)(Arg2);
    }
    result = *(uint64_t *)(local_rsp - 0x37 + 0x4F);
    local_rdi = *(uint64_t *)(arg1 + 0x10);
    if (*(uint64_t *)(local_rsp - 0x37 + 0x4F) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x37 + 0x4F));
        local_rdi = *(uint64_t *)(arg1 + 0x10);
        if ((*(uint64_t *)(arg1 + 0x10)) > result) { local_rdi = result; }
    }
    Arg2 = 0;
    Arg2 = ((*(uint8_t *)(arg1 + 0x20)) != 0) ? 1 : 0;
    *(uint32_t *)(local_rsp - 0x37 - 0x55) = (uint32_t)(Arg2);
    if (*(uint64_t *)(local_rsp - 0x37 + 0x67) == 0) goto loc_003E8C53;
    *(uint32_t *)(local_rsp - 0x37 - 0x55) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x37 + 0x67))));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x37 + 0x67)))) == 0) goto loc_003E8C53;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x37 + 0x67))))) == ((uint32_t)(local_r12 + 1))) goto loc_003E8C53;
    goto loc_003E8F83;
loc_003E8C53:
    result = (uint32_t)(-((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x37 + 0x67)))))));
    local_r10 = (uint32_t)((local_r10) & (0xFFFFFE00ULL));
    local_r10 = (uint32_t)((local_r10) + (516));
    if (((*(uint8_t *)(local_rsp - 0x37 + 0x5F)) & ((uint8_t)((uint32_t)(0xC000000DULL)))) == 0) goto loc_003E8CAE;
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x37 - 0x5D))) + (0x1FFFFFULL));
    Arg3 = (uint32_t)((Arg3) & (0xFFE00000ULL));
    *(uint32_t *)(local_rsp - 0x37 - 0x5D) = (uint32_t)(Arg3);
loc_003E8C8E:
    result = ((uint32_t)(0xC000000DULL)) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)))));
    if (result >= ((uint32_t)((uint32_t)(Arg3)))) goto loc_003E8CA1;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)))) + ((uint32_t)((uint32_t)(0xC000000DULL))));
    if (((uint32_t)(Arg1)) < 63) goto loc_003E8C8E;
loc_003E8CA1:
    *(uint32_t *)(local_rsp - 0x37 - 0x59) = 101;
    Arg4 = ((uint32_t)(0xC000000DULL)) << ((uint8_t)(Arg1));
loc_003E8CAE:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))) != 2) goto loc_003E8CBC;
    goto loc_003E8CD9;
loc_003E8CBC:
    local_r11 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30))) == 0) goto loc_003E8CD9;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x30))) - ((uint32_t)((uint32_t)(0xC000000DULL))));
    if (condition_is_equal) goto loc_003E8CD5;
    if (((uint32_t)(Arg1)) == ((uint32_t)((uint32_t)(0xC000000DULL)))) goto loc_003E8CD9;
    goto loc_003E8DC0;
loc_003E8CD5:
    *(uint8_t *)(local_rsp - 0x37 - 0x61) = (uint8_t)((uint32_t)(0xC000000DULL));
loc_003E8CD9:
    v_stack_mA0 = local_rsp - 55 - 73;
    v_stack_mA8 = 0;
    v_stack_mB0 = 0x446C6148ULL;
    v_stack_mC0 = (uint32_t)(local_r10);
    v_stack_mC8 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x37 + 0x6F)));
    *(uint64_t *)(local_rsp - 0x37 - 0x29) = (uint32_t)((uint32_t)(Arg3));
    *(uint64_t *)(local_rsp - 0x37 - 0x51) = (uint32_t)((uint32_t)(Arg3));
    result = MmAllocateContiguousMemoryEx(local_rsp - 55 - 81, local_rsi, local_rdi, Arg4);
    if (sign_flag) goto loc_003E8DA4;
    if ((*(uint8_t *)(v_rip + 0xBD8B77)) == 0) goto loc_003E8D88;
    if ((*(uint64_t *)(local_rsp - 0x37 - 0x51)) != ((uint32_t)((uint32_t)(Arg3)))) goto loc_003E8D88;
    *(uint64_t *)(local_rsp - 0x37 - 0x31) = *(uint64_t *)(local_rsp - 0x37 - 0x49);
    result = HalpDmaCvmMakeContiguousVirtualBufferShared(*(uint64_t *)(local_rsp - 0x37 - 0x49), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg3)))), local_rsp - 55 - 73, local_rsp - 55 - 57);
    v_stack_mC8 = *(uint64_t *)(local_rsp - 0x37 - 0x39);
    result = CvmDebugLog(v_rip - 3948119, *(uint64_t *)(local_rsp - 0x37 - 0x31), *(uint64_t *)(local_rsp - 0x37 - 0x51), *(uint64_t *)(local_rsp - 0x37 - 0x49));
    if (!sign_flag) goto loc_003E8D8E;
    result = MmFreeContiguousMemory(result, *(uint64_t *)(local_rsp - 0x37 - 0x31), *(uint64_t *)(local_rsp - 0x37 - 0x51), *(uint64_t *)(local_rsp - 0x37 - 0x49));
    goto loc_003E8F83;
loc_003E8D88:
    goto loc_003E8D92;
loc_003E8D8E:
loc_003E8D92:
    if ((*(uint64_t *)(local_rsp - 0x37 - 0x51)) == (*(uint64_t *)(local_rsp - 0x37 - 0x29))) goto loc_003E8E38;
    result = MmFreeContiguousMemory(*(uint64_t *)(local_rsp - 0x37 - 0x49), *(uint64_t *)(local_rsp - 0x37 - 0x31), *(uint64_t *)(local_rsp - 0x37 - 0x51), *(uint64_t *)(local_rsp - 0x37 - 0x49));
loc_003E8DA4:
    local_r12 = 0;
    if ((*(uint32_t *)(arg1 + 0x30)) != 2) goto loc_003E8F7D;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x37 - 0x59))) & (0xFFFFFFEFULL));
loc_003E8DC0:
    Arg3 = 0;
    *(uint8_t *)(local_rsp - 0x37 + 0x57) = (uint8_t)(local_r12 + 1);
    *(uint64_t *)(local_rsp - 0x37 - 0x29) = (uint32_t)(*(uint32_t *)(local_rsp - 0x37 - 0x5D));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x37 + 0x6F)))) != 0x80000000ULL) goto loc_003E8DF3;
    v_stack_mC0 = (uint32_t)(result);
    v_stack_mC8 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x37 - 0x55)));
    result = MmAllocatePagesForMdlEx(local_rsi, *(uint64_t *)(arg1 + 0x10), Arg3, (uint32_t)(*(uint32_t *)(local_rsp - 0x37 - 0x5D)));
    goto loc_003E8E0B;
loc_003E8DF3:
    v_stack_mB8 = (uint32_t)(result);
    v_stack_mC0 = (uint32_t)(local_rsi);
    v_stack_mC8 = (uint32_t)(*(uint64_t *)(arg1 + 0x10));
    result = MmAllocateNodePagesForMdlEx(local_rsi, *(uint64_t *)(arg1 + 0x10), Arg3, (uint32_t)(*(uint32_t *)(local_rsp - 0x37 - 0x5D)));
loc_003E8E0B:
    if (result == 0) goto loc_003E8F7D;
    Arg4 = 0;
    v_stack_mC0 = 0x40000010ULL;
    Arg2 = 0;
    result = MmMapLockedPagesSpecifyCache(result, Arg2, (uint32_t)(*(uint32_t *)(local_rsp - 0x37 - 0x55)), Arg4);
loc_003E8E38:
    if (result == 0) goto loc_003E8F7D;
    result = MmGetPhysicalAddress(result, Arg2, (uint32_t)(*(uint32_t *)(local_rsp - 0x37 - 0x55)), Arg4);
    *(uint64_t *)(local_rsp - 0x37 - 0x41) = result;
    if (result != 0) goto loc_003E8E63;
    *(uint32_t *)(local_rsp - 0x37 - 0x21) = 1;
    *(uint64_t *)(local_rsp - 0x37 - 0x19) = result;
    *(uint64_t *)(local_rsp - 0x37 - 0x11) = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x37 - 0x5D))));
    goto loc_003E8E67;
loc_003E8E63:
    *(uint64_t *)(local_rsp - 0x37 - 0x19) = result;
loc_003E8E67:
    if ((*(uint8_t *)(local_rsp - 0x37 + 0x57)) == 0) goto loc_003E8EC0;
    v_stack_mB8 = local_rsp - 55 - 65;
    *(uint64_t *)(local_rsp - 0x37 - 0x1) = local_rsi;
    v_stack_mC0 = local_rsp - 55 - 9;
    Arg4 = 0;
    *(uint64_t *)(local_rsp - 0x37 - 0x9) = local_rdi;
    v_stack_mC8 = local_rsp - 55 - 1;
    result = guard_dispatch_icall(*(uint64_t *)(arg1 + 0x28), Arg4 + 3, local_rsp - 55 - 33, Arg4);
    if (sign_flag) goto loc_003E8F83;
    *(uint8_t *)(local_rsp - 0x37 - 0x5F) = 1;
    goto loc_003E8EF2;
loc_003E8EC0:
    if ((*(uint8_t *)(local_rsp - 0x37 - 0x61)) == 0) goto loc_003E8EF2;
    result = guard_dispatch_icall(*(uint64_t *)(arg1 + 0x28), 3, local_rsp - 55 - 33, Arg4);
    if (sign_flag) goto loc_003E8F83;
    *(uint8_t *)(local_rsp - 0x37 - 0x60) = 1;
loc_003E8EF2:
    v_stack_mC0 = *(uint64_t *)(local_rsp - 0x37 - 0x31);
    v_stack_mC8 = 1;
    result = HalpAllocateCommonBufferEntry(result, result, *(uint64_t *)(local_rsp - 0x37 - 0x41), Arg1);
    if (sign_flag) goto loc_003E8F32;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x37 + 0x77)) = *(uint64_t *)(local_rsp - 0x37 - 0x41);
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x37 + 0x7F)) = result;
    goto loc_003E8FC8;
loc_003E8F32:
    if ((*(uint8_t *)(local_rsp - 0x37 - 0x60)) == 0) goto loc_003E8F55;
    result = guard_dispatch_icall(*(uint64_t *)(arg1 + 0x28), local_rsp - 55 - 33, *(uint64_t *)(local_rsp - 0x37 - 0x41), Arg1);
    goto loc_003E8F83;
loc_003E8F55:
    if ((*(uint8_t *)(local_rsp - 0x37 - 0x5F)) == 0) goto loc_003E8F83;
    Arg3 = (*(uint64_t *)(local_rsp - 0x37 - 0x29)) >> (12);
    result = guard_dispatch_icall(*(uint64_t *)(arg1 + 0x28), *(uint64_t *)(local_rsp - 0x37 - 0x41), Arg3, Arg1);
    goto loc_003E8F83;
loc_003E8F7D:
loc_003E8F83:
    result = HalpDmaDereferenceDomainObject(Arg1, *(uint64_t *)(local_rsp - 0x37 - 0x41), Arg3, Arg1);
    if (result == 0) goto loc_003E8FA9;
    if (result == 0) goto loc_003E8FA2;
    result = MmUnmapLockedPages(result, result, Arg3, Arg1);
    goto loc_003E8FAE;
loc_003E8FA2:
    result = MmFreeContiguousMemory(result, result, Arg3, Arg1);
    goto loc_003E8FC8;
loc_003E8FA9:
    if (result != 0) {
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = result;
        result = MiFreePagesFromMdl(Arg1, Arg2, Arg3, Arg4);
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    return (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `8` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003E8B64&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
