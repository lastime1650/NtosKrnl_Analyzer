# PropertyEval

- RVA: `0x009CB300`–`0x009D0138` (길이 `20,024` bytes)
- VA: `0x00000001409CB300`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A1050`
- 디코드: `4,804`개 명령, `20,024/20,024` bytes 표시
- 미해석 바이트: `9` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **14**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x009CB44C` → [StringListContains](../A2/StringListContains_function_00A22E24.md) (function, `0x00A22E24`)
- `0x009CB675` → [SubstringMatch](../A3/SubstringMatch_function_00A3408C.md) (function, `0x00A3408C`)
- `0x009CD932` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x009CD97D` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x009CFBE8` → [CompareFileTimeType](../83/CompareFileTimeType_function_00835C6C.md) (function, `0x00835C6C`)
- `0x009CFC01` → [CompareFileTimeType](../83/CompareFileTimeType_function_00835C6C.md) (function, `0x00835C6C`)
- `0x009CFC25` → [CompareFileTimeType](../83/CompareFileTimeType_function_00835C6C.md) (function, `0x00835C6C`)
- `0x009CFC3E` → [CompareFileTimeType](../83/CompareFileTimeType_function_00835C6C.md) (function, `0x00835C6C`)
- `0x009CFC62` → [CompareFileTimeType](../83/CompareFileTimeType_function_00835C6C.md) (function, `0x00835C6C`)
- `0x009CFC7F` → [CompareFileTimeType](../83/CompareFileTimeType_function_00835C6C.md) (function, `0x00835C6C`)
- `0x009CFC9C` → [CompareFileTimeType](../83/CompareFileTimeType_function_00835C6C.md) (function, `0x00835C6C`)
- `0x009CFD66` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x009CFDAE` → [StringListElementSubstringMatch](../83/StringListElementSubstringMatch_function_00835DA8.md) (function, `0x00835DA8`)
- `0x009CFDFC` → [ArrayContains](../../text/6A/ArrayContains_function_006A305C.md) (function, `0x006A305C`)

### Direct callers
- [FilterEvalImpliedAnd](../8D/FilterEvalImpliedAnd_function_008DE898.md) at `0x008DE968`
- [FilterEvalStrict](../8E/FilterEvalStrict_function_008E0ADC.md) at `0x008E0C11`
- [sub_00B1CF9C](../B1/Unknown_function_00B1CF9C.md) at `0x00B1D06A`

### Static image references
- `0x009CB3B5` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x009CFFDF` → RVA `0x239D9C9C` (`image boundary/outside`; read/write)
- `0x009D00C7` → RVA `0x-31626254` (`image boundary/outside`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x009CD932` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x009CD97D` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x009CFD66` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x009CFDFC` → [ArrayContains](../../text/6A/ArrayContains_function_006A305C.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x009D000D` → `0x-4B8CFF52` (`tail-transfer`)
  - `0x009D001D` → `0x-2055FF42` (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009CB300  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
009CB305  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
009CB30A  57                              push rdi
009CB30B  41 54                           push r12
009CB30D  41 57                           push r15
009CB30F  48 83 EC 40                     sub rsp, 0x40
009CB313  45 8B D8                        mov r11d, r8d
009CB316  4C 8B E2                        mov r12, rdx
009CB319  44 8B D1                        mov r10d, ecx
009CB31C  33 F6                           xor esi, esi
009CB31E  8B FE                           mov edi, esi
009CB320  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
009CB324  41 8B D9                        mov ebx, r9d
009CB327  81 E3 00 00 01 00               and ebx, 0x10000
009CB32D  89 5C 24 78                     mov dword ptr [rsp + 0x78], ebx
009CB331  45 8B C1                        mov r8d, r9d
009CB334  41 81 E0 00 00 02 00            and r8d, 0x20000
009CB33B  41 81 E1 FF FF 00 F0            and r9d, 0xf000ffff
009CB342  4C 8B BC 24 98 00 00 00         mov r15, qword ptr [rsp + 0x98]
009CB34A  41 89 37                        mov dword ptr [r15], esi
009CB34D  45 85 C0                        test r8d, r8d
009CB350  0F 85 F3 26 00 00               jne 0x1409cda49
009CB356  41 83 F9 01                     cmp r9d, 1
009CB35A  0F 84 81 00 00 00               je 0x1409cb3e1
009CB360  85 C9                           test ecx, ecx
009CB362  0F 84 9E 4A 00 00               je 0x1409cfe06
009CB368  8B 8C 24 80 00 00 00            mov ecx, dword ptr [rsp + 0x80]
009CB36F  85 C9                           test ecx, ecx
009CB371  0F 84 8F 4A 00 00               je 0x1409cfe06
009CB377  41 83 FA 0D                     cmp r10d, 0xd
009CB37B  75 23                           jne 0x1409cb3a0
009CB37D  41 3B CA                        cmp ecx, r10d
009CB380  75 54                           jne 0x1409cb3d6
009CB382  41 83 F9 02                     cmp r9d, 2
009CB386  75 4E                           jne 0x1409cb3d6
009CB388  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
009CB390  8B 01                           mov eax, dword ptr [rcx]
009CB392  39 02                           cmp dword ptr [rdx], eax
009CB394  74 5A                           je 0x1409cb3f0
009CB396  8B C6                           mov eax, esi
009CB398  41 89 07                        mov dword ptr [r15], eax
009CB39B  E9 7A 4A 00 00                  jmp 0x1409cfe1a
009CB3A0  41 81 FA 03 10 00 00            cmp r10d, 0x1003
009CB3A7  77 66                           ja 0x1409cb40f
009CB3A9  0F 84 49 25 00 00               je 0x1409cd8f8
009CB3AF  41 83 FA 19                     cmp r10d, 0x19
009CB3B3  77 21                           ja 0x1409cb3d6
009CB3B5  48 8D 15 44 4C 63 FF            lea rdx, [rip - 0x9cb3bc]
009CB3BC  42 8B 84 92 44 FE 9C 00         mov eax, dword ptr [rdx + r10*4 + 0x9cfe44]
009CB3C4  48 03 C2                        add rax, rdx
009CB3C7  FF E0                           jmp rax
009CB3C9  CC                              int3
009CB3CA  CC                              int3
009CB3CB  CC                              int3
009CB3CC  CC                              int3
009CB3CD  83 F9 12                        cmp ecx, 0x12
009CB3D0  0F 84 74 02 00 00               je 0x1409cb64a
009CB3D6  BF BB 00 00 C0                  mov edi, 0xc00000bb
009CB3DB  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
009CB3DF  EB BA                           jmp 0x1409cb39b
009CB3E1  8B C6                           mov eax, esi
009CB3E3  85 C9                           test ecx, ecx
009CB3E5  0F 95 C0                        setne al
009CB3E8  41 89 07                        mov dword ptr [r15], eax
009CB3EB  E9 2A 4A 00 00                  jmp 0x1409cfe1a
009CB3F0  8B 41 04                        mov eax, dword ptr [rcx + 4]
009CB3F3  39 42 04                        cmp dword ptr [rdx + 4], eax
009CB3F6  75 9E                           jne 0x1409cb396
009CB3F8  8B 41 08                        mov eax, dword ptr [rcx + 8]
009CB3FB  39 42 08                        cmp dword ptr [rdx + 8], eax
009CB3FE  75 96                           jne 0x1409cb396
009CB400  8B 41 0C                        mov eax, dword ptr [rcx + 0xc]
009CB403  39 42 0C                        cmp dword ptr [rdx + 0xc], eax
009CB406  75 8E                           jne 0x1409cb396
009CB408  B8 01 00 00 00                  mov eax, 1
009CB40D  EB 89                           jmp 0x1409cb398
009CB40F  41 81 FA 0D 10 00 00            cmp r10d, 0x100d
009CB416  0F 84 9C 49 00 00               je 0x1409cfdb8
009CB41C  41 81 FA 12 20 00 00            cmp r10d, 0x2012
009CB423  75 B1                           jne 0x1409cb3d6
009CB425  8D 41 EE                        lea eax, [rcx - 0x12]
009CB428  A9 FF DF FF FF                  test eax, 0xffffdfff
009CB42D  75 A7                           jne 0x1409cb3d6
009CB42F  41 81 F9 00 10 00 00            cmp r9d, 0x1000
009CB436  0F 85 C2 24 00 00               jne 0x1409cd8fe
009CB43C  45 8B C8                        mov r9d, r8d
009CB43F  4C 8B 84 24 88 00 00 00         mov r8, qword ptr [rsp + 0x88]
009CB447  8B D1                           mov edx, ecx
009CB449  49 8B CC                        mov rcx, r12
009CB44C  E8 D3 79 05 00                  call 0x140a22e24
009CB451  41 89 07                        mov dword ptr [r15], eax
009CB454  E9 42 FF FF FF                  jmp 0x1409cb39b
009CB459  83 C1 FE                        add ecx, -2
009CB45C  83 F9 0D                        cmp ecx, 0xd
009CB45F  0F 87 71 FF FF FF               ja 0x1409cb3d6
009CB465  8B 8C 8A AC FE 9C 00            mov ecx, dword ptr [rdx + rcx*4 + 0x9cfeac]
009CB46C  48 03 CA                        add rcx, rdx
009CB46F  FF E1                           jmp rcx
009CB471  CC                              int3
009CB472  CC                              int3
009CB473  CC                              int3
009CB474  CC                              int3
009CB475  41 83 E9 02                     sub r9d, 2
009CB479  0F 84 5B 10 00 00               je 0x1409cc4da
009CB47F  41 83 E9 01                     sub r9d, 1
009CB483  0F 84 BA 14 00 00               je 0x1409cc943
009CB489  41 83 E9 01                     sub r9d, 1
009CB48D  0F 84 88 14 00 00               je 0x1409cc91b
009CB493  41 83 E9 01                     sub r9d, 1
009CB497  0F 84 5A 14 00 00               je 0x1409cc8f7
009CB49D  41 83 F9 01                     cmp r9d, 1
009CB4A1  0F 85 2F FF FF FF               jne 0x1409cb3d6
009CB4A7  41 0F BE 04 24                  movsx eax, byte ptr [r12]
009CB4AC  66 0F 6E C8                     movd xmm1, eax
009CB4B0  0F 5B C9                        cvtdq2ps xmm1, xmm1
009CB4B3  8B CE                           mov ecx, esi
009CB4B5  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CB4BD  F3 0F 10 00                     movss xmm0, dword ptr [rax]
009CB4C1  0F 2F C1                        comiss xmm0, xmm1
009CB4C4  0F 93 C1                        setae cl
009CB4C7  41 89 0F                        mov dword ptr [r15], ecx
009CB4CA  E9 CC FE FF FF                  jmp 0x1409cb39b
009CB4CF  41 83 F9 02                     cmp r9d, 2
009CB4D3  0F 85 FD FE FF FF               jne 0x1409cb3d6
009CB4D9  83 F9 11                        cmp ecx, 0x11
009CB4DC  0F 85 F4 FE FF FF               jne 0x1409cb3d6
009CB4E2  8B D6                           mov edx, esi
009CB4E4  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CB4EC  0F B6 08                        movzx ecx, byte ptr [rax]
009CB4EF  41 38 0C 24                     cmp byte ptr [r12], cl
009CB4F3  0F 94 C2                        sete dl
009CB4F6  41 89 17                        mov dword ptr [r15], edx
009CB4F9  E9 9D FE FF FF                  jmp 0x1409cb39b
009CB4FE  83 C1 FE                        add ecx, -2
009CB501  83 F9 0D                        cmp ecx, 0xd
009CB504  0F 87 CC FE FF FF               ja 0x1409cb3d6
009CB50A  8B 8C 8A E4 FE 9C 00            mov ecx, dword ptr [rdx + rcx*4 + 0x9cfee4]
009CB511  48 03 CA                        add rcx, rdx
009CB514  FF E1                           jmp rcx
009CB516  CC                              int3
009CB517  CC                              int3
009CB518  CC                              int3
009CB519  CC                              int3
009CB51A  41 83 E9 02                     sub r9d, 2
009CB51E  0F 84 0B 15 00 00               je 0x1409cca2f
009CB524  41 83 E9 01                     sub r9d, 1
009CB528  0F 84 E5 14 00 00               je 0x1409cca13
009CB52E  41 83 E9 01                     sub r9d, 1
009CB532  0F 84 BF 14 00 00               je 0x1409cc9f7
009CB538  41 83 E9 01                     sub r9d, 1
009CB53C  0F 84 99 14 00 00               je 0x1409cc9db
009CB542  41 83 F9 01                     cmp r9d, 1
009CB546  0F 85 8A FE FF FF               jne 0x1409cb3d6
009CB54C  41 0F B6 14 24                  movzx edx, byte ptr [r12]
009CB551  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CB559  0F BE 08                        movsx ecx, byte ptr [rax]
009CB55C  8B C6                           mov eax, esi
009CB55E  3B D1                           cmp edx, ecx
009CB560  0F 9E C0                        setle al
009CB563  E9 30 FE FF FF                  jmp 0x1409cb398
009CB568  83 C1 FE                        add ecx, -2
009CB56B  83 F9 0D                        cmp ecx, 0xd
009CB56E  0F 87 62 FE FF FF               ja 0x1409cb3d6
009CB574  8B 8C 8A 1C FF 9C 00            mov ecx, dword ptr [rdx + rcx*4 + 0x9cff1c]
009CB57B  48 03 CA                        add rcx, rdx
009CB57E  FF E1                           jmp rcx
009CB580  CC                              int3
009CB581  CC                              int3
009CB582  CC                              int3
009CB583  CC                              int3
009CB584  41 83 E9 02                     sub r9d, 2
009CB588  0F 84 0B 1F 00 00               je 0x1409cd499
009CB58E  41 83 E9 01                     sub r9d, 1
009CB592  0F 84 F7 1E 00 00               je 0x1409cd48f
009CB598  41 83 E9 01                     sub r9d, 1
009CB59C  0F 84 E3 1E 00 00               je 0x1409cd485
009CB5A2  41 83 E9 01                     sub r9d, 1
009CB5A6  0F 85 C5 1E 00 00               jne 0x1409cd471
009CB5AC  41 0F B7 04 24                  movzx eax, word ptr [r12]
009CB5B1  66 0F 6E C0                     movd xmm0, eax
009CB5B5  F3 0F E6 C0                     cvtdq2pd xmm0, xmm0
009CB5B9  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CB5C1  66 0F 2F 00                     comisd xmm0, xmmword ptr [rax]
009CB5C5  8B CE                           mov ecx, esi
009CB5C7  0F 93 C1                        setae cl
009CB5CA  41 89 0F                        mov dword ptr [r15], ecx
009CB5CD  E9 C9 FD FF FF                  jmp 0x1409cb39b
009CB5D2  83 C1 FE                        add ecx, -2
009CB5D5  83 F9 0D                        cmp ecx, 0xd
009CB5D8  0F 87 F8 FD FF FF               ja 0x1409cb3d6
009CB5DE  8B 8C 8A 54 FF 9C 00            mov ecx, dword ptr [rdx + rcx*4 + 0x9cff54]
009CB5E5  48 03 CA                        add rcx, rdx
009CB5E8  FF E1                           jmp rcx
009CB5EA  CC                              int3
009CB5EB  CC                              int3
009CB5EC  CC                              int3
009CB5ED  CC                              int3
009CB5EE  41 83 E9 02                     sub r9d, 2
009CB5F2  0F 84 0C 1B 00 00               je 0x1409cd104
009CB5F8  41 83 E9 01                     sub r9d, 1
009CB5FC  0F 84 7A 0F 00 00               je 0x1409cc57c
009CB602  41 83 E9 01                     sub r9d, 1
009CB606  0F 84 46 0F 00 00               je 0x1409cc552
009CB60C  41 83 E9 01                     sub r9d, 1
009CB610  0F 84 E4 1A 00 00               je 0x1409cd0fa
009CB616  41 83 F9 01                     cmp r9d, 1
009CB61A  0F 85 B6 FD FF FF               jne 0x1409cb3d6
009CB620  41 0F BF 04 24                  movsx eax, word ptr [r12]
009CB625  66 0F 6E C8                     movd xmm1, eax
009CB629  F3 0F E6 C9                     cvtdq2pd xmm1, xmm1
009CB62D  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CB635  F2 0F 10 00                     movsd xmm0, qword ptr [rax]
009CB639  66 0F 2F C1                     comisd xmm0, xmm1
009CB63D  8B CE                           mov ecx, esi
009CB63F  0F 93 C1                        setae cl
009CB642  41 89 0F                        mov dword ptr [r15], ecx
009CB645  E9 51 FD FF FF                  jmp 0x1409cb39b
009CB64A  41 83 F9 0B                     cmp r9d, 0xb
009CB64E  74 1A                           je 0x1409cb66a
009CB650  41 8B C9                        mov ecx, r9d
009CB653  83 E9 02                        sub ecx, 2
009CB656  0F 84 DF 46 00 00               je 0x1409cfd3b
009CB65C  83 E9 07                        sub ecx, 7
009CB65F  74 09                           je 0x1409cb66a
009CB661  83 F9 01                        cmp ecx, 1
009CB664  0F 85 6C FD FF FF               jne 0x1409cb3d6
009CB66A  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
009CB672  49 8B CC                        mov rcx, r12
009CB675  E8 12 8A 06 00                  call 0x140a3408c
009CB67A  E9 19 FD FF FF                  jmp 0x1409cb398
009CB67F  83 C1 FE                        add ecx, -2
009CB682  83 F9 0D                        cmp ecx, 0xd
009CB685  0F 87 4B FD FF FF               ja 0x1409cb3d6
009CB68B  8B 8C 8A 8C FF 9C 00            mov ecx, dword ptr [rdx + rcx*4 + 0x9cff8c]
009CB692  48 03 CA                        add rcx, rdx
009CB695  FF E1                           jmp rcx
009CB697  CC                              int3
009CB698  CC                              int3
009CB699  CC                              int3
009CB69A  CC                              int3
009CB69B  41 83 E9 02                     sub r9d, 2
009CB69F  0F 84 E0 20 00 00               je 0x1409cd785
009CB6A5  41 83 E9 01                     sub r9d, 1
009CB6A9  0F 84 CB 20 00 00               je 0x1409cd77a
009CB6AF  41 83 E9 01                     sub r9d, 1
009CB6B3  0F 84 B6 20 00 00               je 0x1409cd76f
009CB6B9  41 83 E9 01                     sub r9d, 1
009CB6BD  0F 84 A1 20 00 00               je 0x1409cd764
009CB6C3  41 83 F9 01                     cmp r9d, 1
009CB6C7  0F 85 09 FD FF FF               jne 0x1409cb3d6
009CB6CD  66 41 0F 6E 0C 24               movd xmm1, dword ptr [r12]
009CB6D3  E9 51 FF FF FF                  jmp 0x1409cb629
009CB6D8  41 8D 41 F9                     lea eax, [r9 - 7]
009CB6DC  83 F8 01                        cmp eax, 1
009CB6DF  0F 86 96 27 00 00               jbe 0x1409cde7b
009CB6E5  83 F9 09                        cmp ecx, 9
009CB6E8  0F 84 B0 0C 00 00               je 0x1409cc39e
009CB6EE  83 F9 0E                        cmp ecx, 0xe
009CB6F1  0F 84 63 0C 00 00               je 0x1409cc35a
009CB6F7  83 F9 0F                        cmp ecx, 0xf
009CB6FA  0F 84 23 0D 00 00               je 0x1409cc423
009CB700  83 F9 02                        cmp ecx, 2
009CB703  0F 84 D9 0C 00 00               je 0x1409cc3e2
009CB709  83 C1 FD                        add ecx, -3
009CB70C  83 F9 08                        cmp ecx, 8
009CB70F  0F 87 C1 FC FF FF               ja 0x1409cb3d6
009CB715  8B 8C 8A C4 FF 9C 00            mov ecx, dword ptr [rdx + rcx*4 + 0x9cffc4]
009CB71C  48 03 CA                        add rcx, rdx
009CB71F  FF E1                           jmp rcx
009CB721  CC                              int3
009CB722  CC                              int3
009CB723  CC                              int3
009CB724  CC                              int3
009CB725  41 83 F9 04                     cmp r9d, 4
009CB729  0F 84 90 20 00 00               je 0x1409cd7bf
009CB72F  41 83 E9 02                     sub r9d, 2
009CB733  0F 85 57 20 00 00               jne 0x1409cd790
009CB739  41 8B 04 24                     mov eax, dword ptr [r12]
009CB73D  0F 57 C0                        xorps xmm0, xmm0
009CB740  F3 48 0F 2A C0                  cvtsi2ss xmm0, rax
009CB745  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CB74D  0F 2E 00                        ucomiss xmm0, dword ptr [rax]
009CB750  E9 9C 0D 00 00                  jmp 0x1409cc4f1
009CB755  41 0F BF 04 24                  movsx eax, word ptr [r12]
009CB75A  66 0F 6E C8                     movd xmm1, eax
009CB75E  0F 5B C9                        cvtdq2ps xmm1, xmm1
009CB761  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CB769  F3 0F 10 00                     movss xmm0, dword ptr [rax]
009CB76D  0F 2F C1                        comiss xmm0, xmm1
009CB770  8B CE                           mov ecx, esi
009CB772  0F 97 C1                        seta cl
009CB775  41 89 0F                        mov dword ptr [r15], ecx
009CB778  E9 1E FC FF FF                  jmp 0x1409cb39b
009CB77D  41 83 E9 02                     sub r9d, 2
009CB781  0F 84 D3 0F 00 00               je 0x1409cc75a
009CB787  41 83 E9 01                     sub r9d, 1
009CB78B  0F 84 AD 0F 00 00               je 0x1409cc73e
009CB791  41 83 E9 01                     sub r9d, 1
009CB795  0F 84 87 0F 00 00               je 0x1409cc722
009CB79B  41 83 E9 01                     sub r9d, 1
009CB79F  0F 84 61 0F 00 00               je 0x1409cc706
009CB7A5  41 83 F9 01                     cmp r9d, 1
009CB7A9  0F 85 27 FC FF FF               jne 0x1409cb3d6
009CB7AF  41 0F BE 14 24                  movsx edx, byte ptr [r12]
009CB7B4  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CB7BC  0F B7 08                        movzx ecx, word ptr [rax]
009CB7BF  8B C6                           mov eax, esi
009CB7C1  3B D1                           cmp edx, ecx
009CB7C3  0F 9E C0                        setle al
009CB7C6  E9 CD FB FF FF                  jmp 0x1409cb398
009CB7CB  41 83 E9 02                     sub r9d, 2
009CB7CF  0F 84 76 1F 00 00               je 0x1409cd74b
009CB7D5  41 83 E9 01                     sub r9d, 1
009CB7D9  0F 84 53 1F 00 00               je 0x1409cd732
009CB7DF  41 83 E9 01                     sub r9d, 1
009CB7E3  0F 84 3E 1F 00 00               je 0x1409cd727
009CB7E9  41 83 E9 01                     sub r9d, 1
009CB7ED  0F 84 1B 1F 00 00               je 0x1409cd70e
009CB7F3  41 83 F9 01                     cmp r9d, 1
009CB7F7  0F 85 D9 FB FF FF               jne 0x1409cb3d6
009CB7FD  66 41 0F 6E 0C 24               movd xmm1, dword ptr [r12]
009CB803  0F 5B C9                        cvtdq2ps xmm1, xmm1
009CB806  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CB80E  F3 0F 10 00                     movss xmm0, dword ptr [rax]
009CB812  0F 2F C1                        comiss xmm0, xmm1
009CB815  8B CE                           mov ecx, esi
009CB817  0F 93 C1                        setae cl
009CB81A  41 89 0F                        mov dword ptr [r15], ecx
009CB81D  E9 79 FB FF FF                  jmp 0x1409cb39b
009CB822  41 83 E9 02                     sub r9d, 2
009CB826  0F 84 3D 0E 00 00               je 0x1409cc669
009CB82C  41 83 E9 01                     sub r9d, 1
009CB830  0F 84 17 0E 00 00               je 0x1409cc64d
009CB836  41 83 E9 01                     sub r9d, 1
009CB83A  0F 84 F1 0D 00 00               je 0x1409cc631
009CB840  41 83 E9 01                     sub r9d, 1
009CB844  0F 84 CB 0D 00 00               je 0x1409cc615
009CB84A  41 83 F9 01                     cmp r9d, 1
009CB84E  0F 85 82 FB FF FF               jne 0x1409cb3d6
009CB854  41 0F BE 14 24                  movsx edx, byte ptr [r12]
009CB859  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CB861  0F B6 08                        movzx ecx, byte ptr [rax]
009CB864  8B C6                           mov eax, esi
009CB866  3B D1                           cmp edx, ecx
009CB868  0F 9E C0                        setle al
009CB86B  E9 28 FB FF FF                  jmp 0x1409cb398
009CB870  41 83 E9 02                     sub r9d, 2
009CB874  0F 84 6F 0E 00 00               je 0x1409cc6e9
009CB87A  41 83 E9 01                     sub r9d, 1
009CB87E  0F 84 48 0E 00 00               je 0x1409cc6cc
009CB884  41 83 E9 01                     sub r9d, 1
009CB888  0F 84 21 0E 00 00               je 0x1409cc6af
009CB88E  41 83 E9 01                     sub r9d, 1
009CB892  0F 85 F0 0D 00 00               jne 0x1409cc688
009CB898  41 0F BE 0C 24                  movsx ecx, byte ptr [r12]
009CB89D  8B D6                           mov edx, esi
009CB89F  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CB8A7  66 3B 08                        cmp cx, word ptr [rax]
009CB8AA  0F 9D C2                        setge dl
009CB8AD  41 89 17                        mov dword ptr [r15], edx
009CB8B0  E9 E6 FA FF FF                  jmp 0x1409cb39b
009CB8B5  41 83 E9 02                     sub r9d, 2
009CB8B9  0F 84 12 11 00 00               je 0x1409cc9d1
009CB8BF  41 83 E9 01                     sub r9d, 1
009CB8C3  0F 84 E2 10 00 00               je 0x1409cc9ab
009CB8C9  41 83 E9 01                     sub r9d, 1
009CB8CD  0F 84 AE 10 00 00               je 0x1409cc981
009CB8D3  41 83 E9 01                     sub r9d, 1
009CB8D7  0F 85 70 10 00 00               jne 0x1409cc94d
009CB8DD  41 0F BE 04 24                  movsx eax, byte ptr [r12]
009CB8E2  66 0F 6E C0                     movd xmm0, eax
009CB8E6  F3 0F E6 C0                     cvtdq2pd xmm0, xmm0
009CB8EA  8B CE                           mov ecx, esi
009CB8EC  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CB8F4  66 0F 2F 00                     comisd xmm0, xmmword ptr [rax]
009CB8F8  0F 93 C1                        setae cl
009CB8FB  41 89 0F                        mov dword ptr [r15], ecx
009CB8FE  E9 98 FA FF FF                  jmp 0x1409cb39b
009CB903  41 83 E9 02                     sub r9d, 2
009CB907  0F 84 E1 11 00 00               je 0x1409ccaee
009CB90D  41 83 E9 01                     sub r9d, 1
009CB911  0F 84 BA 11 00 00               je 0x1409ccad1
009CB917  41 83 E9 01                     sub r9d, 1
009CB91B  0F 84 93 11 00 00               je 0x1409ccab4
009CB921  41 83 E9 01                     sub r9d, 1
009CB925  0F 85 62 11 00 00               jne 0x1409cca8d
009CB92B  41 0F B6 14 24                  movzx edx, byte ptr [r12]
009CB930  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CB938  0F B7 08                        movzx ecx, word ptr [rax]
009CB93B  8B C6                           mov eax, esi
009CB93D  66 3B D1                        cmp dx, cx
009CB940  0F 9D C0                        setge al
009CB943  E9 50 FA FF FF                  jmp 0x1409cb398
009CB948  41 83 E9 02                     sub r9d, 2
009CB94C  0F 84 1A 12 00 00               je 0x1409ccb6c
009CB952  41 83 E9 01                     sub r9d, 1
009CB956  0F 84 F3 11 00 00               je 0x1409ccb4f
009CB95C  41 83 E9 01                     sub r9d, 1
009CB960  0F 84 CC 11 00 00               je 0x1409ccb32
009CB966  41 83 E9 01                     sub r9d, 1
009CB96A  0F 85 9B 11 00 00               jne 0x1409ccb0b
009CB970  41 0F B6 0C 24                  movzx ecx, byte ptr [r12]
009CB975  8B D6                           mov edx, esi
009CB977  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CB97F  66 3B 08                        cmp cx, word ptr [rax]
009CB982  0F 93 C2                        setae dl
009CB985  41 89 17                        mov dword ptr [r15], edx
009CB988  E9 0E FA FF FF                  jmp 0x1409cb39b
009CB98D  41 83 E9 02                     sub r9d, 2
009CB991  0F 84 AC 13 00 00               je 0x1409ccd43
009CB997  41 83 E9 01                     sub r9d, 1
009CB99B  0F 84 66 0B 00 00               je 0x1409cc507
009CB9A1  41 83 E9 01                     sub r9d, 1
009CB9A5  0F 84 8E 13 00 00               je 0x1409ccd39
009CB9AB  41 83 E9 01                     sub r9d, 1
009CB9AF  0F 85 52 13 00 00               jne 0x1409ccd07
009CB9B5  41 0F B6 04 24                  movzx eax, byte ptr [r12]
009CB9BA  E9 01 01 00 00                  jmp 0x1409cbac0
009CB9BF  41 83 E9 02                     sub r9d, 2
009CB9C3  0F 84 5A 0B 00 00               je 0x1409cc523
009CB9C9  41 83 E9 01                     sub r9d, 1
009CB9CD  0F 84 CA 13 00 00               je 0x1409ccd9d
009CB9D3  41 83 E9 01                     sub r9d, 1
009CB9D7  0F 84 B6 13 00 00               je 0x1409ccd93
009CB9DD  41 83 E9 01                     sub r9d, 1
009CB9E1  0F 85 78 13 00 00               jne 0x1409ccd5f
009CB9E7  41 0F B6 04 24                  movzx eax, byte ptr [r12]
009CB9EC  66 0F 6E C0                     movd xmm0, eax
009CB9F0  F3 0F E6 C0                     cvtdq2pd xmm0, xmm0
009CB9F4  8B CE                           mov ecx, esi
009CB9F6  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CB9FE  66 0F 2F 00                     comisd xmm0, xmmword ptr [rax]
009CBA02  0F 93 C1                        setae cl
009CBA05  41 89 0F                        mov dword ptr [r15], ecx
009CBA08  E9 8E F9 FF FF                  jmp 0x1409cb39b
009CBA0D  41 83 E9 02                     sub r9d, 2
009CBA11  0F 84 E8 13 00 00               je 0x1409ccdff
009CBA17  41 83 E9 01                     sub r9d, 1
009CBA1B  0F 84 C4 13 00 00               je 0x1409ccde5
009CBA21  41 83 E9 01                     sub r9d, 1
009CBA25  0F 84 A0 13 00 00               je 0x1409ccdcb
009CBA2B  41 83 E9 01                     sub r9d, 1
009CBA2F  0F 85 72 13 00 00               jne 0x1409ccda7
009CBA35  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CBA3D  0F BE 08                        movsx ecx, byte ptr [rax]
009CBA40  8B C6                           mov eax, esi
009CBA42  66 41 39 0C 24                  cmp word ptr [r12], cx
009CBA47  0F 9D C0                        setge al
009CBA4A  E9 49 F9 FF FF                  jmp 0x1409cb398
009CBA4F  41 83 E9 02                     sub r9d, 2
009CBA53  0F 84 D7 14 00 00               je 0x1409ccf30
009CBA59  41 83 E9 01                     sub r9d, 1
009CBA5D  0F 84 B1 14 00 00               je 0x1409ccf14
009CBA63  41 83 E9 01                     sub r9d, 1
009CBA67  0F 84 8B 14 00 00               je 0x1409ccef8
009CBA6D  41 83 E9 01                     sub r9d, 1
009CBA71  0F 85 5B 14 00 00               jne 0x1409cced2
009CBA77  41 0F BF 14 24                  movsx edx, word ptr [r12]
009CBA7C  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CBA84  0F B7 08                        movzx ecx, word ptr [rax]
009CBA87  8B C6                           mov eax, esi
009CBA89  3B D1                           cmp edx, ecx
009CBA8B  0F 9D C0                        setge al
009CBA8E  E9 05 F9 FF FF                  jmp 0x1409cb398
009CBA93  41 83 E9 02                     sub r9d, 2
009CBA97  0F 84 41 16 00 00               je 0x1409cd0de
009CBA9D  41 83 E9 01                     sub r9d, 1
009CBAA1  0F 84 1B 16 00 00               je 0x1409cd0c2
009CBAA7  41 83 E9 01                     sub r9d, 1
009CBAAB  0F 84 A4 FC FF FF               je 0x1409cb755
009CBAB1  41 83 E9 01                     sub r9d, 1
009CBAB5  0F 85 F3 15 00 00               jne 0x1409cd0ae
009CBABB  41 0F BF 04 24                  movsx eax, word ptr [r12]
009CBAC0  66 0F 6E C0                     movd xmm0, eax
009CBAC4  0F 5B C0                        cvtdq2ps xmm0, xmm0
009CBAC7  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CBACF  0F 2F 00                        comiss xmm0, dword ptr [rax]
009CBAD2  E9 66 FB FF FF                  jmp 0x1409cb63d
009CBAD7  41 83 E9 02                     sub r9d, 2
009CBADB  0F 84 8B 16 00 00               je 0x1409cd16c
009CBAE1  41 83 E9 01                     sub r9d, 1
009CBAE5  0F 84 65 16 00 00               je 0x1409cd150
009CBAEB  41 83 E9 01                     sub r9d, 1
009CBAEF  0F 84 3F 16 00 00               je 0x1409cd134
009CBAF5  41 83 E9 01                     sub r9d, 1
009CBAF9  0F 85 0F 16 00 00               jne 0x1409cd10e
009CBAFF  41 0F B7 14 24                  movzx edx, word ptr [r12]
009CBB04  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CBB0C  0F BE 08                        movsx ecx, byte ptr [rax]
009CBB0F  8B C6                           mov eax, esi
009CBB11  3B D1                           cmp edx, ecx
009CBB13  0F 9D C0                        setge al
009CBB16  E9 7D F8 FF FF                  jmp 0x1409cb398
009CBB1B  41 83 E9 02                     sub r9d, 2
009CBB1F  0F 84 19 17 00 00               je 0x1409cd23e
009CBB25  41 83 E9 01                     sub r9d, 1
009CBB29  0F 84 F3 16 00 00               je 0x1409cd222
009CBB2F  41 83 E9 01                     sub r9d, 1
009CBB33  0F 84 CD 16 00 00               je 0x1409cd206
009CBB39  41 83 E9 01                     sub r9d, 1
009CBB3D  0F 85 9D 16 00 00               jne 0x1409cd1e0
009CBB43  41 0F B7 14 24                  movzx edx, word ptr [r12]
009CBB48  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CBB50  0F BF 08                        movsx ecx, word ptr [rax]
009CBB53  8B C6                           mov eax, esi
009CBB55  3B D1                           cmp edx, ecx
009CBB57  0F 9D C0                        setge al
009CBB5A  E9 39 F8 FF FF                  jmp 0x1409cb398
009CBB5F  41 83 E9 02                     sub r9d, 2
009CBB63  0F 84 EC 18 00 00               je 0x1409cd455
009CBB69  41 83 E9 01                     sub r9d, 1
009CBB6D  0F 84 C6 18 00 00               je 0x1409cd439
009CBB73  41 83 E9 01                     sub r9d, 1
009CBB77  0F 84 B2 18 00 00               je 0x1409cd42f
009CBB7D  41 83 E9 01                     sub r9d, 1
009CBB81  0F 85 CD 08 00 00               jne 0x1409cc454
009CBB87  41 0F B7 04 24                  movzx eax, word ptr [r12]
009CBB8C  66 0F 6E C0                     movd xmm0, eax
009CBB90  0F 5B C0                        cvtdq2ps xmm0, xmm0
009CBB93  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CBB9B  0F 2F 00                        comiss xmm0, dword ptr [rax]
009CBB9E  E9 9A FA FF FF                  jmp 0x1409cb63d
009CBBA3  41 83 E9 02                     sub r9d, 2
009CBBA7  0F 84 57 1F 00 00               je 0x1409cdb04
009CBBAD  41 83 E9 01                     sub r9d, 1
009CBBB1  0F 84 DD 16 00 00               je 0x1409cd294
009CBBB7  41 83 E9 01                     sub r9d, 1
009CBBBB  0F 84 B6 16 00 00               je 0x1409cd277
009CBBC1  41 83 E9 01                     sub r9d, 1
009CBBC5  0F 84 8F 16 00 00               je 0x1409cd25a
009CBBCB  41 83 F9 01                     cmp r9d, 1
009CBBCF  0F 85 01 F8 FF FF               jne 0x1409cb3d6
009CBBD5  8B D6                           mov edx, esi
009CBBD7  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CBBDF  0F B7 08                        movzx ecx, word ptr [rax]
009CBBE2  66 41 39 0C 24                  cmp word ptr [r12], cx
009CBBE7  0F 96 C2                        setbe dl
009CBBEA  41 89 17                        mov dword ptr [r15], edx
009CBBED  E9 A9 F7 FF FF                  jmp 0x1409cb39b
009CBBF2  41 83 F9 06                     cmp r9d, 6
009CBBF6  0F 84 8A 08 00 00               je 0x1409cc486
009CBBFC  41 83 E9 02                     sub r9d, 2
009CBC00  0F 84 1B 1F 00 00               je 0x1409cdb21
009CBC06  41 83 E9 01                     sub r9d, 1
009CBC0A  0F 84 62 13 00 00               je 0x1409ccf72
009CBC10  41 83 E9 01                     sub r9d, 1
009CBC14  0F 85 32 13 00 00               jne 0x1409ccf4c
009CBC1A  41 0F BF 0C 24                  movsx ecx, word ptr [r12]
009CBC1F  8B D6                           mov edx, esi
009CBC21  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CBC29  3B 08                           cmp ecx, dword ptr [rax]
009CBC2B  0F 9C C2                        setl dl
009CBC2E  41 89 17                        mov dword ptr [r15], edx
009CBC31  E9 65 F7 FF FF                  jmp 0x1409cb39b
009CBC36  41 83 F9 06                     cmp r9d, 6
009CBC3A  0F 84 62 08 00 00               je 0x1409cc4a2
009CBC40  41 83 E9 02                     sub r9d, 2
009CBC44  0F 84 98 F8 FF FF               je 0x1409cb4e2
009CBC4A  41 83 E9 01                     sub r9d, 1
009CBC4E  0F 84 A5 09 00 00               je 0x1409cc5f9
009CBC54  41 83 E9 01                     sub r9d, 1
009CBC58  0F 85 75 09 00 00               jne 0x1409cc5d3
009CBC5E  8B D6                           mov edx, esi
009CBC60  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CBC68  0F B6 08                        movzx ecx, byte ptr [rax]
009CBC6B  41 38 0C 24                     cmp byte ptr [r12], cl
009CBC6F  0F 9C C2                        setl dl
009CBC72  41 89 17                        mov dword ptr [r15], edx
009CBC75  E9 21 F7 FF FF                  jmp 0x1409cb39b
009CBC7A  41 83 F9 06                     cmp r9d, 6
009CBC7E  0F 84 3A 08 00 00               je 0x1409cc4be
009CBC84  41 83 E9 02                     sub r9d, 2
009CBC88  0F 84 54 F8 FF FF               je 0x1409cb4e2
009CBC8E  41 83 E9 01                     sub r9d, 1
009CBC92  0F 84 D9 0D 00 00               je 0x1409cca71
009CBC98  41 83 E9 01                     sub r9d, 1
009CBC9C  0F 85 A9 0D 00 00               jne 0x1409cca4b
009CBCA2  8B D6                           mov edx, esi
009CBCA4  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CBCAC  0F B6 08                        movzx ecx, byte ptr [rax]
009CBCAF  41 38 0C 24                     cmp byte ptr [r12], cl
009CBCB3  0F 92 C2                        setb dl
009CBCB6  41 89 17                        mov dword ptr [r15], edx
009CBCB9  E9 DD F6 FF FF                  jmp 0x1409cb39b
009CBCBE  41 83 E9 02                     sub r9d, 2
009CBCC2  0F 84 B0 1D 00 00               je 0x1409cda78
009CBCC8  41 83 E9 01                     sub r9d, 1
009CBCCC  0F 84 E9 0A 00 00               je 0x1409cc7bb
009CBCD2  41 83 E9 01                     sub r9d, 1
009CBCD6  0F 84 C3 0A 00 00               je 0x1409cc79f
009CBCDC  41 83 E9 01                     sub r9d, 1
009CBCE0  0F 85 93 0A 00 00               jne 0x1409cc779
009CBCE6  41 0F BE 0C 24                  movsx ecx, byte ptr [r12]
009CBCEB  8B D6                           mov edx, esi
009CBCED  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CBCF5  3B 08                           cmp ecx, dword ptr [rax]
009CBCF7  0F 9D C2                        setge dl
009CBCFA  41 89 17                        mov dword ptr [r15], edx
009CBCFD  E9 99 F6 FF FF                  jmp 0x1409cb39b
009CBD02  41 83 E9 02                     sub r9d, 2
009CBD06  0F 84 6C 1D 00 00               je 0x1409cda78
009CBD0C  41 83 E9 01                     sub r9d, 1
009CBD10  0F 84 03 0B 00 00               je 0x1409cc819
009CBD16  41 83 E9 01                     sub r9d, 1
009CBD1A  0F 84 DD 0A 00 00               je 0x1409cc7fd
009CBD20  41 83 E9 01                     sub r9d, 1
009CBD24  0F 85 AD 0A 00 00               jne 0x1409cc7d7
009CBD2A  41 0F BE 0C 24                  movsx ecx, byte ptr [r12]
009CBD2F  8B D6                           mov edx, esi
009CBD31  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CBD39  3B 08                           cmp ecx, dword ptr [rax]
009CBD3B  0F 93 C2                        setae dl
009CBD3E  41 89 17                        mov dword ptr [r15], edx
009CBD41  E9 55 F6 FF FF                  jmp 0x1409cb39b
009CBD46  41 83 E9 02                     sub r9d, 2
009CBD4A  0F 84 44 1D 00 00               je 0x1409cda94
009CBD50  41 83 E9 01                     sub r9d, 1
009CBD54  0F 84 1F 0B 00 00               je 0x1409cc879
009CBD5A  41 83 E9 01                     sub r9d, 1
009CBD5E  0F 84 F8 0A 00 00               je 0x1409cc85c
009CBD64  41 83 E9 01                     sub r9d, 1
009CBD68  0F 85 C7 0A 00 00               jne 0x1409cc835
009CBD6E  49 0F BE 0C 24                  movsx rcx, byte ptr [r12]
009CBD73  8B D6                           mov edx, esi
009CBD75  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CBD7D  48 3B 08                        cmp rcx, qword ptr [rax]
009CBD80  0F 9D C2                        setge dl
009CBD83  41 89 17                        mov dword ptr [r15], edx
009CBD86  E9 10 F6 FF FF                  jmp 0x1409cb39b
009CBD8B  41 83 E9 02                     sub r9d, 2
009CBD8F  0F 84 FF 1C 00 00               je 0x1409cda94
009CBD95  41 83 E9 01                     sub r9d, 1
009CBD99  0F 84 3B 0B 00 00               je 0x1409cc8da
009CBD9F  41 83 E9 01                     sub r9d, 1
009CBDA3  0F 84 14 0B 00 00               je 0x1409cc8bd
009CBDA9  41 83 E9 01                     sub r9d, 1
009CBDAD  0F 85 E3 0A 00 00               jne 0x1409cc896
009CBDB3  49 0F BE 0C 24                  movsx rcx, byte ptr [r12]
009CBDB8  8B D6                           mov edx, esi
009CBDBA  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CBDC2  48 3B 08                        cmp rcx, qword ptr [rax]
009CBDC5  0F 93 C2                        setae dl
009CBDC8  41 89 17                        mov dword ptr [r15], edx
009CBDCB  E9 CB F5 FF FF                  jmp 0x1409cb39b
009CBDD0  41 83 E9 02                     sub r9d, 2
009CBDD4  0F 84 D7 1C 00 00               je 0x1409cdab1
009CBDDA  41 83 E9 01                     sub r9d, 1
009CBDDE  0F 84 E7 0D 00 00               je 0x1409ccbcb
009CBDE4  41 83 E9 01                     sub r9d, 1
009CBDE8  0F 84 C1 0D 00 00               je 0x1409ccbaf
009CBDEE  41 83 E9 01                     sub r9d, 1
009CBDF2  0F 85 91 0D 00 00               jne 0x1409ccb89
009CBDF8  41 0F B6 0C 24                  movzx ecx, byte ptr [r12]
009CBDFD  8B D6                           mov edx, esi
009CBDFF  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CBE07  3B 08                           cmp ecx, dword ptr [rax]
009CBE09  0F 9D C2                        setge dl
009CBE0C  41 89 17                        mov dword ptr [r15], edx
009CBE0F  E9 87 F5 FF FF                  jmp 0x1409cb39b
009CBE14  41 83 E9 02                     sub r9d, 2
009CBE18  0F 84 93 1C 00 00               je 0x1409cdab1
009CBE1E  41 83 E9 01                     sub r9d, 1
009CBE22  0F 84 01 0E 00 00               je 0x1409ccc29
009CBE28  41 83 E9 01                     sub r9d, 1
009CBE2C  0F 84 DB 0D 00 00               je 0x1409ccc0d
009CBE32  41 83 E9 01                     sub r9d, 1
009CBE36  0F 85 AB 0D 00 00               jne 0x1409ccbe7
009CBE3C  41 0F B6 0C 24                  movzx ecx, byte ptr [r12]
009CBE41  8B D6                           mov edx, esi
009CBE43  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CBE4B  3B 08                           cmp ecx, dword ptr [rax]
009CBE4D  0F 93 C2                        setae dl
009CBE50  41 89 17                        mov dword ptr [r15], edx
009CBE53  E9 43 F5 FF FF                  jmp 0x1409cb39b
009CBE58  41 83 E9 02                     sub r9d, 2
009CBE5C  0F 84 6B 1C 00 00               je 0x1409cdacd
009CBE62  41 83 E9 01                     sub r9d, 1
009CBE66  0F 84 1D 0E 00 00               je 0x1409ccc89
009CBE6C  41 83 E9 01                     sub r9d, 1
009CBE70  0F 84 F6 0D 00 00               je 0x1409ccc6c
009CBE76  41 83 E9 01                     sub r9d, 1
009CBE7A  0F 85 C5 0D 00 00               jne 0x1409ccc45
009CBE80  41 0F B6 0C 24                  movzx ecx, byte ptr [r12]
009CBE85  8B D6                           mov edx, esi
009CBE87  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CBE8F  48 3B 08                        cmp rcx, qword ptr [rax]
009CBE92  0F 9D C2                        setge dl
009CBE95  41 89 17                        mov dword ptr [r15], edx
009CBE98  E9 FE F4 FF FF                  jmp 0x1409cb39b
009CBE9D  41 83 E9 02                     sub r9d, 2
009CBEA1  0F 84 26 1C 00 00               je 0x1409cdacd
009CBEA7  41 83 E9 01                     sub r9d, 1
009CBEAB  0F 84 39 0E 00 00               je 0x1409cccea
009CBEB1  41 83 E9 01                     sub r9d, 1
009CBEB5  0F 84 12 0E 00 00               je 0x1409ccccd
009CBEBB  41 83 E9 01                     sub r9d, 1
009CBEBF  0F 85 E1 0D 00 00               jne 0x1409ccca6
009CBEC5  41 0F B6 0C 24                  movzx ecx, byte ptr [r12]
009CBECA  8B D6                           mov edx, esi
009CBECC  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CBED4  48 3B 08                        cmp rcx, qword ptr [rax]
009CBED7  0F 93 C2                        setae dl
009CBEDA  41 89 17                        mov dword ptr [r15], edx
009CBEDD  E9 B9 F4 FF FF                  jmp 0x1409cb39b
009CBEE2  41 83 E9 02                     sub r9d, 2
009CBEE6  0F 84 FE 1B 00 00               je 0x1409cdaea
009CBEEC  41 83 E9 01                     sub r9d, 1
009CBEF0  0F 84 61 0F 00 00               je 0x1409cce57
009CBEF6  41 83 E9 01                     sub r9d, 1
009CBEFA  0F 84 3D 0F 00 00               je 0x1409cce3d
009CBF00  41 83 E9 01                     sub r9d, 1
009CBF04  0F 85 0F 0F 00 00               jne 0x1409cce19
009CBF0A  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CBF12  0F B6 08                        movzx ecx, byte ptr [rax]
009CBF15  8B C6                           mov eax, esi
009CBF17  66 41 39 0C 24                  cmp word ptr [r12], cx
009CBF1C  0F 9D C0                        setge al
009CBF1F  E9 74 F4 FF FF                  jmp 0x1409cb398
009CBF24  41 83 E9 02                     sub r9d, 2
009CBF28  0F 84 D6 1B 00 00               je 0x1409cdb04
009CBF2E  41 83 E9 01                     sub r9d, 1
009CBF32  0F 84 7D 0F 00 00               je 0x1409cceb5
009CBF38  41 83 E9 01                     sub r9d, 1
009CBF3C  0F 84 56 0F 00 00               je 0x1409cce98
009CBF42  41 83 E9 01                     sub r9d, 1
009CBF46  0F 85 25 0F 00 00               jne 0x1409cce71
009CBF4C  8B D6                           mov edx, esi
009CBF4E  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CBF56  0F B7 08                        movzx ecx, word ptr [rax]
009CBF59  66 41 39 0C 24                  cmp word ptr [r12], cx
009CBF5E  0F 9D C2                        setge dl
009CBF61  41 89 17                        mov dword ptr [r15], edx
009CBF64  E9 32 F4 FF FF                  jmp 0x1409cb39b
009CBF69  41 83 E9 02                     sub r9d, 2
009CBF6D  0F 84 AE 1B 00 00               je 0x1409cdb21
009CBF73  41 83 E9 01                     sub r9d, 1
009CBF77  0F 84 53 10 00 00               je 0x1409ccfd0
009CBF7D  41 83 E9 01                     sub r9d, 1
009CBF81  0F 84 2D 10 00 00               je 0x1409ccfb4
009CBF87  41 83 E9 01                     sub r9d, 1
009CBF8B  0F 85 FD 0F 00 00               jne 0x1409ccf8e
009CBF91  41 0F BF 0C 24                  movsx ecx, word ptr [r12]
009CBF96  8B D6                           mov edx, esi
009CBF98  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CBFA0  3B 08                           cmp ecx, dword ptr [rax]
009CBFA2  0F 93 C2                        setae dl
009CBFA5  41 89 17                        mov dword ptr [r15], edx
009CBFA8  E9 EE F3 FF FF                  jmp 0x1409cb39b
009CBFAD  41 83 E9 02                     sub r9d, 2
009CBFB1  0F 84 86 1B 00 00               je 0x1409cdb3d
009CBFB7  41 83 E9 01                     sub r9d, 1
009CBFBB  0F 84 6F 10 00 00               je 0x1409cd030
009CBFC1  41 83 E9 01                     sub r9d, 1
009CBFC5  0F 84 48 10 00 00               je 0x1409cd013
009CBFCB  41 83 E9 01                     sub r9d, 1
009CBFCF  0F 85 17 10 00 00               jne 0x1409ccfec
009CBFD5  49 0F BF 0C 24                  movsx rcx, word ptr [r12]
009CBFDA  8B D6                           mov edx, esi
009CBFDC  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CBFE4  48 3B 08                        cmp rcx, qword ptr [rax]
009CBFE7  0F 9D C2                        setge dl
009CBFEA  41 89 17                        mov dword ptr [r15], edx
009CBFED  E9 A9 F3 FF FF                  jmp 0x1409cb39b
009CBFF2  41 83 E9 02                     sub r9d, 2
009CBFF6  0F 84 41 1B 00 00               je 0x1409cdb3d
009CBFFC  41 83 E9 01                     sub r9d, 1
009CC000  0F 84 8B 10 00 00               je 0x1409cd091
009CC006  41 83 E9 01                     sub r9d, 1
009CC00A  0F 84 64 10 00 00               je 0x1409cd074
009CC010  41 83 E9 01                     sub r9d, 1
009CC014  0F 85 33 10 00 00               jne 0x1409cd04d
009CC01A  49 0F BF 0C 24                  movsx rcx, word ptr [r12]
009CC01F  8B D6                           mov edx, esi
009CC021  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC029  48 3B 08                        cmp rcx, qword ptr [rax]
009CC02C  0F 93 C2                        setae dl
009CC02F  41 89 17                        mov dword ptr [r15], edx
009CC032  E9 64 F3 FF FF                  jmp 0x1409cb39b
009CC037  41 83 E9 02                     sub r9d, 2
009CC03B  0F 84 A9 1A 00 00               je 0x1409cdaea
009CC041  41 83 E9 01                     sub r9d, 1
009CC045  0F 84 7B 11 00 00               je 0x1409cd1c6
009CC04B  41 83 E9 01                     sub r9d, 1
009CC04F  0F 84 57 11 00 00               je 0x1409cd1ac
009CC055  41 83 E9 01                     sub r9d, 1
009CC059  0F 85 29 11 00 00               jne 0x1409cd188
009CC05F  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC067  0F B6 08                        movzx ecx, byte ptr [rax]
009CC06A  8B C6                           mov eax, esi
009CC06C  66 41 39 0C 24                  cmp word ptr [r12], cx
009CC071  0F 93 C0                        setae al
009CC074  E9 1F F3 FF FF                  jmp 0x1409cb398
009CC079  41 83 E9 02                     sub r9d, 2
009CC07D  0F 84 D7 1A 00 00               je 0x1409cdb5a
009CC083  41 83 E9 01                     sub r9d, 1
009CC087  0F 84 66 12 00 00               je 0x1409cd2f3
009CC08D  41 83 E9 01                     sub r9d, 1
009CC091  0F 84 40 12 00 00               je 0x1409cd2d7
009CC097  41 83 E9 01                     sub r9d, 1
009CC09B  0F 85 10 12 00 00               jne 0x1409cd2b1
009CC0A1  41 0F B7 0C 24                  movzx ecx, word ptr [r12]
009CC0A6  8B D6                           mov edx, esi
009CC0A8  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC0B0  3B 08                           cmp ecx, dword ptr [rax]
009CC0B2  0F 9D C2                        setge dl
009CC0B5  41 89 17                        mov dword ptr [r15], edx
009CC0B8  E9 DE F2 FF FF                  jmp 0x1409cb39b
009CC0BD  41 83 E9 02                     sub r9d, 2
009CC0C1  0F 84 93 1A 00 00               je 0x1409cdb5a
009CC0C7  41 83 E9 01                     sub r9d, 1
009CC0CB  0F 84 80 12 00 00               je 0x1409cd351
009CC0D1  41 83 E9 01                     sub r9d, 1
009CC0D5  0F 84 5A 12 00 00               je 0x1409cd335
009CC0DB  41 83 E9 01                     sub r9d, 1
009CC0DF  0F 85 2A 12 00 00               jne 0x1409cd30f
009CC0E5  41 0F B7 0C 24                  movzx ecx, word ptr [r12]
009CC0EA  8B D6                           mov edx, esi
009CC0EC  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC0F4  3B 08                           cmp ecx, dword ptr [rax]
009CC0F6  0F 93 C2                        setae dl
009CC0F9  41 89 17                        mov dword ptr [r15], edx
009CC0FC  E9 9A F2 FF FF                  jmp 0x1409cb39b
009CC101  41 83 E9 02                     sub r9d, 2
009CC105  0F 84 6B 1A 00 00               je 0x1409cdb76
009CC10B  41 83 E9 01                     sub r9d, 1
009CC10F  0F 84 9C 12 00 00               je 0x1409cd3b1
009CC115  41 83 E9 01                     sub r9d, 1
009CC119  0F 84 75 12 00 00               je 0x1409cd394
009CC11F  41 83 E9 01                     sub r9d, 1
009CC123  0F 85 44 12 00 00               jne 0x1409cd36d
009CC129  41 0F B7 0C 24                  movzx ecx, word ptr [r12]
009CC12E  8B D6                           mov edx, esi
009CC130  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC138  48 3B 08                        cmp rcx, qword ptr [rax]
009CC13B  0F 9D C2                        setge dl
009CC13E  41 89 17                        mov dword ptr [r15], edx
009CC141  E9 55 F2 FF FF                  jmp 0x1409cb39b
009CC146  41 83 E9 02                     sub r9d, 2
009CC14A  0F 84 26 1A 00 00               je 0x1409cdb76
009CC150  41 83 E9 01                     sub r9d, 1
009CC154  0F 84 B8 12 00 00               je 0x1409cd412
009CC15A  41 83 E9 01                     sub r9d, 1
009CC15E  0F 84 91 12 00 00               je 0x1409cd3f5
009CC164  41 83 E9 01                     sub r9d, 1
009CC168  0F 85 60 12 00 00               jne 0x1409cd3ce
009CC16E  41 0F B7 0C 24                  movzx ecx, word ptr [r12]
009CC173  8B D6                           mov edx, esi
009CC175  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC17D  48 3B 08                        cmp rcx, qword ptr [rax]
009CC180  0F 93 C2                        setae dl
009CC183  41 89 17                        mov dword ptr [r15], edx
009CC186  E9 10 F2 FF FF                  jmp 0x1409cb39b
009CC18B  41 83 E9 02                     sub r9d, 2
009CC18F  0F 84 FE 19 00 00               je 0x1409cdb93
009CC195  41 83 E9 01                     sub r9d, 1
009CC199  0F 84 40 13 00 00               je 0x1409cd4df
009CC19F  41 83 E9 01                     sub r9d, 1
009CC1A3  0F 84 1D 13 00 00               je 0x1409cd4c6
009CC1A9  41 83 E9 01                     sub r9d, 1
009CC1AD  0F 85 F0 12 00 00               jne 0x1409cd4a3
009CC1B3  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC1BB  0F BE 08                        movsx ecx, byte ptr [rax]
009CC1BE  8B C6                           mov eax, esi
009CC1C0  41 39 0C 24                     cmp dword ptr [r12], ecx
009CC1C4  0F 9D C0                        setge al
009CC1C7  E9 CC F1 FF FF                  jmp 0x1409cb398
009CC1CC  41 83 E9 02                     sub r9d, 2
009CC1D0  0F 84 D6 19 00 00               je 0x1409cdbac
009CC1D6  41 83 E9 01                     sub r9d, 1
009CC1DA  0F 84 54 13 00 00               je 0x1409cd534
009CC1E0  41 83 E9 01                     sub r9d, 1
009CC1E4  0F 84 31 13 00 00               je 0x1409cd51b
009CC1EA  41 83 E9 01                     sub r9d, 1
009CC1EE  0F 85 04 13 00 00               jne 0x1409cd4f8
009CC1F4  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC1FC  0F B6 08                        movzx ecx, byte ptr [rax]
009CC1FF  8B C6                           mov eax, esi
009CC201  41 39 0C 24                     cmp dword ptr [r12], ecx
009CC205  0F 9D C0                        setge al
009CC208  E9 8B F1 FF FF                  jmp 0x1409cb398
009CC20D  41 83 E9 02                     sub r9d, 2
009CC211  0F 84 AE 19 00 00               je 0x1409cdbc5
009CC217  41 83 E9 01                     sub r9d, 1
009CC21B  0F 84 68 13 00 00               je 0x1409cd589
009CC221  41 83 E9 01                     sub r9d, 1
009CC225  0F 84 45 13 00 00               je 0x1409cd570
009CC22B  41 83 E9 01                     sub r9d, 1
009CC22F  0F 85 18 13 00 00               jne 0x1409cd54d
009CC235  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC23D  0F BF 08                        movsx ecx, word ptr [rax]
009CC240  8B C6                           mov eax, esi
009CC242  41 39 0C 24                     cmp dword ptr [r12], ecx
009CC246  0F 9D C0                        setge al
009CC249  E9 4A F1 FF FF                  jmp 0x1409cb398
009CC24E  41 83 E9 02                     sub r9d, 2
009CC252  0F 84 86 19 00 00               je 0x1409cdbde
009CC258  41 83 E9 01                     sub r9d, 1
009CC25C  0F 84 7C 13 00 00               je 0x1409cd5de
009CC262  41 83 E9 01                     sub r9d, 1
009CC266  0F 84 59 13 00 00               je 0x1409cd5c5
009CC26C  41 83 E9 01                     sub r9d, 1
009CC270  0F 85 2C 13 00 00               jne 0x1409cd5a2
009CC276  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC27E  0F B7 08                        movzx ecx, word ptr [rax]
009CC281  8B C6                           mov eax, esi
009CC283  41 39 0C 24                     cmp dword ptr [r12], ecx
009CC287  0F 9D C0                        setge al
009CC28A  E9 09 F1 FF FF                  jmp 0x1409cb398
009CC28F  41 83 E9 02                     sub r9d, 2
009CC293  0F 84 6F 3A 00 00               je 0x1409cfd08
009CC299  41 83 E9 01                     sub r9d, 1
009CC29D  0F 84 94 13 00 00               je 0x1409cd637
009CC2A3  41 83 E9 01                     sub r9d, 1
009CC2A7  0F 84 6F 13 00 00               je 0x1409cd61c
009CC2AD  41 83 E9 01                     sub r9d, 1
009CC2B1  0F 85 40 13 00 00               jne 0x1409cd5f7
009CC2B7  8B D6                           mov edx, esi
009CC2B9  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC2C1  8B 08                           mov ecx, dword ptr [rax]
009CC2C3  41 39 0C 24                     cmp dword ptr [r12], ecx
009CC2C7  0F 9D C2                        setge dl
009CC2CA  41 89 17                        mov dword ptr [r15], edx
009CC2CD  E9 C9 F0 FF FF                  jmp 0x1409cb39b
009CC2D2  41 83 E9 02                     sub r9d, 2
009CC2D6  0F 84 6C 19 00 00               je 0x1409cdc48
009CC2DC  41 83 E9 01                     sub r9d, 1
009CC2E0  0F 84 AE 13 00 00               je 0x1409cd694
009CC2E6  41 83 E9 01                     sub r9d, 1
009CC2EA  0F 84 88 13 00 00               je 0x1409cd678
009CC2F0  41 83 E9 01                     sub r9d, 1
009CC2F4  0F 85 58 13 00 00               jne 0x1409cd652
009CC2FA  49 63 0C 24                     movsxd rcx, dword ptr [r12]
009CC2FE  8B D6                           mov edx, esi
009CC300  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC308  48 3B 08                        cmp rcx, qword ptr [rax]
009CC30B  0F 9D C2                        setge dl
009CC30E  41 89 17                        mov dword ptr [r15], edx
009CC311  E9 85 F0 FF FF                  jmp 0x1409cb39b
009CC316  41 83 E9 02                     sub r9d, 2
009CC31A  0F 84 28 19 00 00               je 0x1409cdc48
009CC320  41 83 E9 01                     sub r9d, 1
009CC324  0F 84 C8 13 00 00               je 0x1409cd6f2
009CC32A  41 83 E9 01                     sub r9d, 1
009CC32E  0F 84 A2 13 00 00               je 0x1409cd6d6
009CC334  41 83 E9 01                     sub r9d, 1
009CC338  0F 85 72 13 00 00               jne 0x1409cd6b0
009CC33E  49 63 0C 24                     movsxd rcx, dword ptr [r12]
009CC342  8B D6                           mov edx, esi
009CC344  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC34C  48 3B 08                        cmp rcx, qword ptr [rax]
009CC34F  0F 93 C2                        setae dl
009CC352  41 89 17                        mov dword ptr [r15], edx
009CC355  E9 41 F0 FF FF                  jmp 0x1409cb39b
009CC35A  41 83 F9 04                     cmp r9d, 4
009CC35E  0F 84 04 15 00 00               je 0x1409cd868
009CC364  41 83 E9 02                     sub r9d, 2
009CC368  0F 84 F1 1A 00 00               je 0x1409cde5f
009CC36E  41 83 E9 01                     sub r9d, 1
009CC372  0F 84 D4 14 00 00               je 0x1409cd84c
009CC378  41 83 E9 02                     sub r9d, 2
009CC37C  0F 85 12 16 00 00               jne 0x1409cd994
009CC382  41 8B 0C 24                     mov ecx, dword ptr [r12]
009CC386  8B D6                           mov edx, esi
009CC388  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC390  48 3B 08                        cmp rcx, qword ptr [rax]
009CC393  0F 9D C2                        setge dl
009CC396  41 89 17                        mov dword ptr [r15], edx
009CC399  E9 FD EF FF FF                  jmp 0x1409cb39b
009CC39E  41 83 F9 04                     cmp r9d, 4
009CC3A2  0F 84 F8 14 00 00               je 0x1409cd8a0
009CC3A8  41 83 E9 02                     sub r9d, 2
009CC3AC  0F 84 AD 1A 00 00               je 0x1409cde5f
009CC3B2  41 83 E9 01                     sub r9d, 1
009CC3B6  0F 84 C8 14 00 00               je 0x1409cd884
009CC3BC  41 83 E9 02                     sub r9d, 2
009CC3C0  0F 85 F4 15 00 00               jne 0x1409cd9ba
009CC3C6  41 8B 0C 24                     mov ecx, dword ptr [r12]
009CC3CA  8B D6                           mov edx, esi
009CC3CC  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC3D4  48 3B 08                        cmp rcx, qword ptr [rax]
009CC3D7  0F 93 C2                        setae dl
009CC3DA  41 89 17                        mov dword ptr [r15], edx
009CC3DD  E9 B9 EF FF FF                  jmp 0x1409cb39b
009CC3E2  41 83 F9 04                     cmp r9d, 4
009CC3E6  0F 84 07 14 00 00               je 0x1409cd7f3
009CC3EC  41 83 E9 02                     sub r9d, 2
009CC3F0  0F 84 9D 17 00 00               je 0x1409cdb93
009CC3F6  41 83 E9 01                     sub r9d, 1
009CC3FA  0F 84 24 1A 00 00               je 0x1409cde24
009CC400  41 83 E9 02                     sub r9d, 2
009CC404  0F 85 C6 13 00 00               jne 0x1409cd7d0
009CC40A  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC412  0F BE 08                        movsx ecx, byte ptr [rax]
009CC415  8B C6                           mov eax, esi
009CC417  41 39 0C 24                     cmp dword ptr [r12], ecx
009CC41B  0F 93 C0                        setae al
009CC41E  E9 75 EF FF FF                  jmp 0x1409cb398
009CC423  41 83 F9 04                     cmp r9d, 4
009CC427  0F 84 0E 14 00 00               je 0x1409cd83b
009CC42D  41 83 E9 02                     sub r9d, 2
009CC431  0F 85 D5 13 00 00               jne 0x1409cd80c
009CC437  41 8B 04 24                     mov eax, dword ptr [r12]
009CC43B  0F 57 C0                        xorps xmm0, xmm0
009CC43E  F2 48 0F 2A C0                  cvtsi2sd xmm0, rax
009CC443  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC44B  66 0F 2E 00                     ucomisd xmm0, qword ptr [rax]
009CC44F  E9 9D 00 00 00                  jmp 0x1409cc4f1
009CC454  41 83 F9 01                     cmp r9d, 1
009CC458  0F 85 78 EF FF FF               jne 0x1409cb3d6
009CC45E  41 0F B7 04 24                  movzx eax, word ptr [r12]
009CC463  66 0F 6E C8                     movd xmm1, eax
009CC467  0F 5B C9                        cvtdq2ps xmm1, xmm1
009CC46A  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC472  F3 0F 10 00                     movss xmm0, dword ptr [rax]
009CC476  0F 2F C1                        comiss xmm0, xmm1
009CC479  8B CE                           mov ecx, esi
009CC47B  0F 93 C1                        setae cl
009CC47E  41 89 0F                        mov dword ptr [r15], ecx
009CC481  E9 15 EF FF FF                  jmp 0x1409cb39b
009CC486  41 0F BF 0C 24                  movsx ecx, word ptr [r12]
009CC48B  8B D6                           mov edx, esi
009CC48D  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC495  3B 08                           cmp ecx, dword ptr [rax]
009CC497  0F 9E C2                        setle dl
009CC49A  41 89 17                        mov dword ptr [r15], edx
009CC49D  E9 F9 EE FF FF                  jmp 0x1409cb39b
009CC4A2  8B D6                           mov edx, esi
009CC4A4  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC4AC  0F B6 08                        movzx ecx, byte ptr [rax]
009CC4AF  41 38 0C 24                     cmp byte ptr [r12], cl
009CC4B3  0F 9E C2                        setle dl
009CC4B6  41 89 17                        mov dword ptr [r15], edx
009CC4B9  E9 DD EE FF FF                  jmp 0x1409cb39b
009CC4BE  8B D6                           mov edx, esi
009CC4C0  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC4C8  0F B6 08                        movzx ecx, byte ptr [rax]
009CC4CB  41 38 0C 24                     cmp byte ptr [r12], cl
009CC4CF  0F 96 C2                        setbe dl
009CC4D2  41 89 17                        mov dword ptr [r15], edx
009CC4D5  E9 C1 EE FF FF                  jmp 0x1409cb39b
009CC4DA  41 0F BE 04 24                  movsx eax, byte ptr [r12]
009CC4DF  66 0F 6E C0                     movd xmm0, eax
009CC4E3  0F 5B C0                        cvtdq2ps xmm0, xmm0
009CC4E6  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC4EE  0F 2E 00                        ucomiss xmm0, dword ptr [rax]
009CC4F1  0F 8A 9F EE FF FF               jp 0x1409cb396
009CC4F7  B8 01 00 00 00                  mov eax, 1
009CC4FC  0F 84 96 EE FF FF               je 0x1409cb398
009CC502  E9 8F EE FF FF                  jmp 0x1409cb396
009CC507  41 0F B6 04 24                  movzx eax, byte ptr [r12]
009CC50C  66 0F 6E C0                     movd xmm0, eax
009CC510  0F 5B C0                        cvtdq2ps xmm0, xmm0
009CC513  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC51B  0F 2F 00                        comiss xmm0, dword ptr [rax]
009CC51E  E9 4D F2 FF FF                  jmp 0x1409cb770
009CC523  41 0F B6 04 24                  movzx eax, byte ptr [r12]
009CC528  66 0F 6E C0                     movd xmm0, eax
009CC52C  F3 0F E6 C0                     cvtdq2pd xmm0, xmm0
009CC530  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC538  66 0F 2E 00                     ucomisd xmm0, qword ptr [rax]
009CC53C  0F 8A 54 EE FF FF               jp 0x1409cb396
009CC542  B8 01 00 00 00                  mov eax, 1
009CC547  0F 84 4B EE FF FF               je 0x1409cb398
009CC54D  E9 44 EE FF FF                  jmp 0x1409cb396
009CC552  41 0F BF 04 24                  movsx eax, word ptr [r12]
009CC557  66 0F 6E C8                     movd xmm1, eax
009CC55B  F3 0F E6 C9                     cvtdq2pd xmm1, xmm1
009CC55F  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC567  F2 0F 10 00                     movsd xmm0, qword ptr [rax]
009CC56B  66 0F 2F C1                     comisd xmm0, xmm1
009CC56F  8B CE                           mov ecx, esi
009CC571  0F 97 C1                        seta cl
009CC574  41 89 0F                        mov dword ptr [r15], ecx
009CC577  E9 1F EE FF FF                  jmp 0x1409cb39b
009CC57C  41 0F BF 04 24                  movsx eax, word ptr [r12]
009CC581  66 0F 6E C0                     movd xmm0, eax
009CC585  F3 0F E6 C0                     cvtdq2pd xmm0, xmm0
009CC589  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC591  66 0F 2F 00                     comisd xmm0, xmmword ptr [rax]
009CC595  8B CE                           mov ecx, esi
009CC597  0F 97 C1                        seta cl
009CC59A  41 89 0F                        mov dword ptr [r15], ecx
009CC59D  E9 F9 ED FF FF                  jmp 0x1409cb39b
009CC5A2  83 F9 01                        cmp ecx, 1
009CC5A5  0F 85 2B EE FF FF               jne 0x1409cb3d6
009CC5AB  41 83 F9 02                     cmp r9d, 2
009CC5AF  0F 85 21 EE FF FF               jne 0x1409cb3d6
009CC5B5  4D 85 E4                        test r12, r12
009CC5B8  0F 85 D8 ED FF FF               jne 0x1409cb396
009CC5BE  4C 39 A4 24 88 00 00 00         cmp qword ptr [rsp + 0x88], r12
009CC5C6  0F 85 CA ED FF FF               jne 0x1409cb396
009CC5CC  8B C1                           mov eax, ecx
009CC5CE  E9 C5 ED FF FF                  jmp 0x1409cb398
009CC5D3  41 83 F9 01                     cmp r9d, 1
009CC5D7  0F 85 F9 ED FF FF               jne 0x1409cb3d6
009CC5DD  8B D6                           mov edx, esi
009CC5DF  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC5E7  0F B6 08                        movzx ecx, byte ptr [rax]
009CC5EA  41 38 0C 24                     cmp byte ptr [r12], cl
009CC5EE  0F 9D C2                        setge dl
009CC5F1  41 89 17                        mov dword ptr [r15], edx
009CC5F4  E9 A2 ED FF FF                  jmp 0x1409cb39b
009CC5F9  8B D6                           mov edx, esi
009CC5FB  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC603  0F B6 08                        movzx ecx, byte ptr [rax]
009CC606  41 38 0C 24                     cmp byte ptr [r12], cl
009CC60A  0F 9F C2                        setg dl
009CC60D  41 89 17                        mov dword ptr [r15], edx
009CC610  E9 86 ED FF FF                  jmp 0x1409cb39b
009CC615  41 0F BE 14 24                  movsx edx, byte ptr [r12]
009CC61A  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC622  0F B6 08                        movzx ecx, byte ptr [rax]
009CC625  8B C6                           mov eax, esi
009CC627  3B D1                           cmp edx, ecx
009CC629  0F 9D C0                        setge al
009CC62C  E9 67 ED FF FF                  jmp 0x1409cb398
009CC631  41 0F BE 14 24                  movsx edx, byte ptr [r12]
009CC636  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC63E  0F B6 08                        movzx ecx, byte ptr [rax]
009CC641  8B C6                           mov eax, esi
009CC643  3B D1                           cmp edx, ecx
009CC645  0F 9C C0                        setl al
009CC648  E9 4B ED FF FF                  jmp 0x1409cb398
009CC64D  41 0F BE 14 24                  movsx edx, byte ptr [r12]
009CC652  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC65A  0F B6 08                        movzx ecx, byte ptr [rax]
009CC65D  8B C6                           mov eax, esi
009CC65F  3B D1                           cmp edx, ecx
009CC661  0F 9F C0                        setg al
009CC664  E9 2F ED FF FF                  jmp 0x1409cb398
009CC669  41 0F BE 14 24                  movsx edx, byte ptr [r12]
009CC66E  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC676  0F B6 08                        movzx ecx, byte ptr [rax]
009CC679  8B C6                           mov eax, esi
009CC67B  3B D1                           cmp edx, ecx
009CC67D  0F 94 C0                        sete al
009CC680  41 89 07                        mov dword ptr [r15], eax
009CC683  E9 13 ED FF FF                  jmp 0x1409cb39b
009CC688  41 83 F9 01                     cmp r9d, 1
009CC68C  0F 85 44 ED FF FF               jne 0x1409cb3d6
009CC692  41 0F BE 0C 24                  movsx ecx, byte ptr [r12]
009CC697  8B D6                           mov edx, esi
009CC699  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC6A1  66 3B 08                        cmp cx, word ptr [rax]
009CC6A4  0F 9E C2                        setle dl
009CC6A7  41 89 17                        mov dword ptr [r15], edx
009CC6AA  E9 EC EC FF FF                  jmp 0x1409cb39b
009CC6AF  41 0F BE 0C 24                  movsx ecx, byte ptr [r12]
009CC6B4  8B D6                           mov edx, esi
009CC6B6  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC6BE  66 3B 08                        cmp cx, word ptr [rax]
009CC6C1  0F 9C C2                        setl dl
009CC6C4  41 89 17                        mov dword ptr [r15], edx
009CC6C7  E9 CF EC FF FF                  jmp 0x1409cb39b
009CC6CC  41 0F BE 0C 24                  movsx ecx, byte ptr [r12]
009CC6D1  8B D6                           mov edx, esi
009CC6D3  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC6DB  66 3B 08                        cmp cx, word ptr [rax]
009CC6DE  0F 9F C2                        setg dl
009CC6E1  41 89 17                        mov dword ptr [r15], edx
009CC6E4  E9 B2 EC FF FF                  jmp 0x1409cb39b
009CC6E9  41 0F BE 0C 24                  movsx ecx, byte ptr [r12]
009CC6EE  8B D6                           mov edx, esi
009CC6F0  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC6F8  66 3B 08                        cmp cx, word ptr [rax]
009CC6FB  0F 94 C2                        sete dl
009CC6FE  41 89 17                        mov dword ptr [r15], edx
009CC701  E9 95 EC FF FF                  jmp 0x1409cb39b
009CC706  41 0F BE 14 24                  movsx edx, byte ptr [r12]
009CC70B  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC713  0F B7 08                        movzx ecx, word ptr [rax]
009CC716  8B C6                           mov eax, esi
009CC718  3B D1                           cmp edx, ecx
009CC71A  0F 9D C0                        setge al
009CC71D  E9 76 EC FF FF                  jmp 0x1409cb398
009CC722  41 0F BE 14 24                  movsx edx, byte ptr [r12]
009CC727  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC72F  0F B7 08                        movzx ecx, word ptr [rax]
009CC732  8B C6                           mov eax, esi
009CC734  3B D1                           cmp edx, ecx
009CC736  0F 9C C0                        setl al
009CC739  E9 5A EC FF FF                  jmp 0x1409cb398
009CC73E  41 0F BE 14 24                  movsx edx, byte ptr [r12]
009CC743  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC74B  0F B7 08                        movzx ecx, word ptr [rax]
009CC74E  8B C6                           mov eax, esi
009CC750  3B D1                           cmp edx, ecx
009CC752  0F 9F C0                        setg al
009CC755  E9 3E EC FF FF                  jmp 0x1409cb398
009CC75A  41 0F BE 14 24                  movsx edx, byte ptr [r12]
009CC75F  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC767  0F B7 08                        movzx ecx, word ptr [rax]
009CC76A  8B C6                           mov eax, esi
009CC76C  3B D1                           cmp edx, ecx
009CC76E  0F 94 C0                        sete al
009CC771  41 89 07                        mov dword ptr [r15], eax
009CC774  E9 22 EC FF FF                  jmp 0x1409cb39b
009CC779  41 83 F9 01                     cmp r9d, 1
009CC77D  0F 85 53 EC FF FF               jne 0x1409cb3d6
009CC783  41 0F BE 0C 24                  movsx ecx, byte ptr [r12]
009CC788  8B D6                           mov edx, esi
009CC78A  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC792  3B 08                           cmp ecx, dword ptr [rax]
009CC794  0F 9E C2                        setle dl
009CC797  41 89 17                        mov dword ptr [r15], edx
009CC79A  E9 FC EB FF FF                  jmp 0x1409cb39b
009CC79F  41 0F BE 0C 24                  movsx ecx, byte ptr [r12]
009CC7A4  8B D6                           mov edx, esi
009CC7A6  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC7AE  3B 08                           cmp ecx, dword ptr [rax]
009CC7B0  0F 9C C2                        setl dl
009CC7B3  41 89 17                        mov dword ptr [r15], edx
009CC7B6  E9 E0 EB FF FF                  jmp 0x1409cb39b
009CC7BB  41 0F BE 0C 24                  movsx ecx, byte ptr [r12]
009CC7C0  8B D6                           mov edx, esi
009CC7C2  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC7CA  3B 08                           cmp ecx, dword ptr [rax]
009CC7CC  0F 9F C2                        setg dl
009CC7CF  41 89 17                        mov dword ptr [r15], edx
009CC7D2  E9 C4 EB FF FF                  jmp 0x1409cb39b
009CC7D7  41 83 F9 01                     cmp r9d, 1
009CC7DB  0F 85 F5 EB FF FF               jne 0x1409cb3d6
009CC7E1  41 0F BE 0C 24                  movsx ecx, byte ptr [r12]
009CC7E6  8B D6                           mov edx, esi
009CC7E8  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC7F0  3B 08                           cmp ecx, dword ptr [rax]
009CC7F2  0F 96 C2                        setbe dl
009CC7F5  41 89 17                        mov dword ptr [r15], edx
009CC7F8  E9 9E EB FF FF                  jmp 0x1409cb39b
009CC7FD  41 0F BE 0C 24                  movsx ecx, byte ptr [r12]
009CC802  8B D6                           mov edx, esi
009CC804  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC80C  3B 08                           cmp ecx, dword ptr [rax]
009CC80E  0F 92 C2                        setb dl
009CC811  41 89 17                        mov dword ptr [r15], edx
009CC814  E9 82 EB FF FF                  jmp 0x1409cb39b
009CC819  41 0F BE 0C 24                  movsx ecx, byte ptr [r12]
009CC81E  8B D6                           mov edx, esi
009CC820  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC828  3B 08                           cmp ecx, dword ptr [rax]
009CC82A  0F 97 C2                        seta dl
009CC82D  41 89 17                        mov dword ptr [r15], edx
009CC830  E9 66 EB FF FF                  jmp 0x1409cb39b
009CC835  41 83 F9 01                     cmp r9d, 1
009CC839  0F 85 97 EB FF FF               jne 0x1409cb3d6
009CC83F  49 0F BE 0C 24                  movsx rcx, byte ptr [r12]
009CC844  8B D6                           mov edx, esi
009CC846  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC84E  48 3B 08                        cmp rcx, qword ptr [rax]
009CC851  0F 9E C2                        setle dl
009CC854  41 89 17                        mov dword ptr [r15], edx
009CC857  E9 3F EB FF FF                  jmp 0x1409cb39b
009CC85C  49 0F BE 0C 24                  movsx rcx, byte ptr [r12]
009CC861  8B D6                           mov edx, esi
009CC863  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC86B  48 3B 08                        cmp rcx, qword ptr [rax]
009CC86E  0F 9C C2                        setl dl
009CC871  41 89 17                        mov dword ptr [r15], edx
009CC874  E9 22 EB FF FF                  jmp 0x1409cb39b
009CC879  49 0F BE 0C 24                  movsx rcx, byte ptr [r12]
009CC87E  8B D6                           mov edx, esi
009CC880  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC888  48 3B 08                        cmp rcx, qword ptr [rax]
009CC88B  0F 9F C2                        setg dl
009CC88E  41 89 17                        mov dword ptr [r15], edx
009CC891  E9 05 EB FF FF                  jmp 0x1409cb39b
009CC896  41 83 F9 01                     cmp r9d, 1
009CC89A  0F 85 36 EB FF FF               jne 0x1409cb3d6
009CC8A0  49 0F BE 0C 24                  movsx rcx, byte ptr [r12]
009CC8A5  8B D6                           mov edx, esi
009CC8A7  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC8AF  48 3B 08                        cmp rcx, qword ptr [rax]
009CC8B2  0F 96 C2                        setbe dl
009CC8B5  41 89 17                        mov dword ptr [r15], edx
009CC8B8  E9 DE EA FF FF                  jmp 0x1409cb39b
009CC8BD  49 0F BE 0C 24                  movsx rcx, byte ptr [r12]
009CC8C2  8B D6                           mov edx, esi
009CC8C4  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC8CC  48 3B 08                        cmp rcx, qword ptr [rax]
009CC8CF  0F 92 C2                        setb dl
009CC8D2  41 89 17                        mov dword ptr [r15], edx
009CC8D5  E9 C1 EA FF FF                  jmp 0x1409cb39b
009CC8DA  49 0F BE 0C 24                  movsx rcx, byte ptr [r12]
009CC8DF  8B D6                           mov edx, esi
009CC8E1  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC8E9  48 3B 08                        cmp rcx, qword ptr [rax]
009CC8EC  0F 97 C2                        seta dl
009CC8EF  41 89 17                        mov dword ptr [r15], edx
009CC8F2  E9 A4 EA FF FF                  jmp 0x1409cb39b
009CC8F7  41 0F BE 04 24                  movsx eax, byte ptr [r12]
009CC8FC  66 0F 6E C0                     movd xmm0, eax
009CC900  0F 5B C0                        cvtdq2ps xmm0, xmm0
009CC903  8B CE                           mov ecx, esi
009CC905  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC90D  0F 2F 00                        comiss xmm0, dword ptr [rax]
009CC910  0F 93 C1                        setae cl
009CC913  41 89 0F                        mov dword ptr [r15], ecx
009CC916  E9 80 EA FF FF                  jmp 0x1409cb39b
009CC91B  41 0F BE 04 24                  movsx eax, byte ptr [r12]
009CC920  66 0F 6E C8                     movd xmm1, eax
009CC924  0F 5B C9                        cvtdq2ps xmm1, xmm1
009CC927  8B CE                           mov ecx, esi
009CC929  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC931  F3 0F 10 00                     movss xmm0, dword ptr [rax]
009CC935  0F 2F C1                        comiss xmm0, xmm1
009CC938  0F 97 C1                        seta cl
009CC93B  41 89 0F                        mov dword ptr [r15], ecx
009CC93E  E9 58 EA FF FF                  jmp 0x1409cb39b
009CC943  41 0F BE 04 24                  movsx eax, byte ptr [r12]
009CC948  E9 BF FB FF FF                  jmp 0x1409cc50c
009CC94D  41 83 F9 01                     cmp r9d, 1
009CC951  0F 85 7F EA FF FF               jne 0x1409cb3d6
009CC957  41 0F BE 04 24                  movsx eax, byte ptr [r12]
009CC95C  66 0F 6E C8                     movd xmm1, eax
009CC960  F3 0F E6 C9                     cvtdq2pd xmm1, xmm1
009CC964  8B CE                           mov ecx, esi
009CC966  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC96E  F2 0F 10 00                     movsd xmm0, qword ptr [rax]
009CC972  66 0F 2F C1                     comisd xmm0, xmm1
009CC976  0F 93 C1                        setae cl
009CC979  41 89 0F                        mov dword ptr [r15], ecx
009CC97C  E9 1A EA FF FF                  jmp 0x1409cb39b
009CC981  41 0F BE 04 24                  movsx eax, byte ptr [r12]
009CC986  66 0F 6E C8                     movd xmm1, eax
009CC98A  F3 0F E6 C9                     cvtdq2pd xmm1, xmm1
009CC98E  8B CE                           mov ecx, esi
009CC990  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC998  F2 0F 10 00                     movsd xmm0, qword ptr [rax]
009CC99C  66 0F 2F C1                     comisd xmm0, xmm1
009CC9A0  0F 97 C1                        seta cl
009CC9A3  41 89 0F                        mov dword ptr [r15], ecx
009CC9A6  E9 F0 E9 FF FF                  jmp 0x1409cb39b
009CC9AB  41 0F BE 04 24                  movsx eax, byte ptr [r12]
009CC9B0  66 0F 6E C0                     movd xmm0, eax
009CC9B4  F3 0F E6 C0                     cvtdq2pd xmm0, xmm0
009CC9B8  8B CE                           mov ecx, esi
009CC9BA  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC9C2  66 0F 2F 00                     comisd xmm0, xmmword ptr [rax]
009CC9C6  0F 97 C1                        seta cl
009CC9C9  41 89 0F                        mov dword ptr [r15], ecx
009CC9CC  E9 CA E9 FF FF                  jmp 0x1409cb39b
009CC9D1  41 0F BE 04 24                  movsx eax, byte ptr [r12]
009CC9D6  E9 4D FB FF FF                  jmp 0x1409cc528
009CC9DB  41 0F B6 14 24                  movzx edx, byte ptr [r12]
009CC9E0  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CC9E8  0F BE 08                        movsx ecx, byte ptr [rax]
009CC9EB  8B C6                           mov eax, esi
009CC9ED  3B D1                           cmp edx, ecx
009CC9EF  0F 9D C0                        setge al
009CC9F2  E9 A1 E9 FF FF                  jmp 0x1409cb398
009CC9F7  41 0F B6 14 24                  movzx edx, byte ptr [r12]
009CC9FC  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCA04  0F BE 08                        movsx ecx, byte ptr [rax]
009CCA07  8B C6                           mov eax, esi
009CCA09  3B D1                           cmp edx, ecx
009CCA0B  0F 9C C0                        setl al
009CCA0E  E9 85 E9 FF FF                  jmp 0x1409cb398
009CCA13  41 0F B6 14 24                  movzx edx, byte ptr [r12]
009CCA18  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCA20  0F BE 08                        movsx ecx, byte ptr [rax]
009CCA23  8B C6                           mov eax, esi
009CCA25  3B D1                           cmp edx, ecx
009CCA27  0F 9F C0                        setg al
009CCA2A  E9 69 E9 FF FF                  jmp 0x1409cb398
009CCA2F  41 0F B6 14 24                  movzx edx, byte ptr [r12]
009CCA34  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCA3C  0F BE 08                        movsx ecx, byte ptr [rax]
009CCA3F  8B C6                           mov eax, esi
009CCA41  3B D1                           cmp edx, ecx
009CCA43  0F 94 C0                        sete al
009CCA46  E9 4D E9 FF FF                  jmp 0x1409cb398
009CCA4B  41 83 F9 01                     cmp r9d, 1
009CCA4F  0F 85 81 E9 FF FF               jne 0x1409cb3d6
009CCA55  8B D6                           mov edx, esi
009CCA57  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCA5F  0F B6 08                        movzx ecx, byte ptr [rax]
009CCA62  41 38 0C 24                     cmp byte ptr [r12], cl
009CCA66  0F 93 C2                        setae dl
009CCA69  41 89 17                        mov dword ptr [r15], edx
009CCA6C  E9 2A E9 FF FF                  jmp 0x1409cb39b
009CCA71  8B D6                           mov edx, esi
009CCA73  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCA7B  0F B6 08                        movzx ecx, byte ptr [rax]
009CCA7E  41 38 0C 24                     cmp byte ptr [r12], cl
009CCA82  0F 97 C2                        seta dl
009CCA85  41 89 17                        mov dword ptr [r15], edx
009CCA88  E9 0E E9 FF FF                  jmp 0x1409cb39b
009CCA8D  41 83 F9 01                     cmp r9d, 1
009CCA91  0F 85 3F E9 FF FF               jne 0x1409cb3d6
009CCA97  41 0F B6 14 24                  movzx edx, byte ptr [r12]
009CCA9C  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCAA4  0F B7 08                        movzx ecx, word ptr [rax]
009CCAA7  8B C6                           mov eax, esi
009CCAA9  66 3B D1                        cmp dx, cx
009CCAAC  0F 9E C0                        setle al
009CCAAF  E9 E4 E8 FF FF                  jmp 0x1409cb398
009CCAB4  41 0F B6 14 24                  movzx edx, byte ptr [r12]
009CCAB9  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCAC1  0F B7 08                        movzx ecx, word ptr [rax]
009CCAC4  8B C6                           mov eax, esi
009CCAC6  66 3B D1                        cmp dx, cx
009CCAC9  0F 9C C0                        setl al
009CCACC  E9 C7 E8 FF FF                  jmp 0x1409cb398
009CCAD1  41 0F B6 14 24                  movzx edx, byte ptr [r12]
009CCAD6  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCADE  0F B7 08                        movzx ecx, word ptr [rax]
009CCAE1  8B C6                           mov eax, esi
009CCAE3  66 3B D1                        cmp dx, cx
009CCAE6  0F 9F C0                        setg al
009CCAE9  E9 AA E8 FF FF                  jmp 0x1409cb398
009CCAEE  41 0F B6 14 24                  movzx edx, byte ptr [r12]
009CCAF3  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCAFB  0F B7 08                        movzx ecx, word ptr [rax]
009CCAFE  8B C6                           mov eax, esi
009CCB00  66 3B D1                        cmp dx, cx
009CCB03  0F 94 C0                        sete al
009CCB06  E9 8D E8 FF FF                  jmp 0x1409cb398
009CCB0B  41 83 F9 01                     cmp r9d, 1
009CCB0F  0F 85 C1 E8 FF FF               jne 0x1409cb3d6
009CCB15  41 0F B6 0C 24                  movzx ecx, byte ptr [r12]
009CCB1A  8B D6                           mov edx, esi
009CCB1C  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCB24  66 3B 08                        cmp cx, word ptr [rax]
009CCB27  0F 96 C2                        setbe dl
009CCB2A  41 89 17                        mov dword ptr [r15], edx
009CCB2D  E9 69 E8 FF FF                  jmp 0x1409cb39b
009CCB32  41 0F B6 0C 24                  movzx ecx, byte ptr [r12]
009CCB37  8B D6                           mov edx, esi
009CCB39  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCB41  66 3B 08                        cmp cx, word ptr [rax]
009CCB44  0F 92 C2                        setb dl
009CCB47  41 89 17                        mov dword ptr [r15], edx
009CCB4A  E9 4C E8 FF FF                  jmp 0x1409cb39b
009CCB4F  41 0F B6 0C 24                  movzx ecx, byte ptr [r12]
009CCB54  8B D6                           mov edx, esi
009CCB56  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCB5E  66 3B 08                        cmp cx, word ptr [rax]
009CCB61  0F 97 C2                        seta dl
009CCB64  41 89 17                        mov dword ptr [r15], edx
009CCB67  E9 2F E8 FF FF                  jmp 0x1409cb39b
009CCB6C  41 0F B6 0C 24                  movzx ecx, byte ptr [r12]
009CCB71  8B D6                           mov edx, esi
009CCB73  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCB7B  66 3B 08                        cmp cx, word ptr [rax]
009CCB7E  0F 94 C2                        sete dl
009CCB81  41 89 17                        mov dword ptr [r15], edx
009CCB84  E9 12 E8 FF FF                  jmp 0x1409cb39b
009CCB89  41 83 F9 01                     cmp r9d, 1
009CCB8D  0F 85 43 E8 FF FF               jne 0x1409cb3d6
009CCB93  41 0F B6 0C 24                  movzx ecx, byte ptr [r12]
009CCB98  8B D6                           mov edx, esi
009CCB9A  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCBA2  3B 08                           cmp ecx, dword ptr [rax]
009CCBA4  0F 9E C2                        setle dl
009CCBA7  41 89 17                        mov dword ptr [r15], edx
009CCBAA  E9 EC E7 FF FF                  jmp 0x1409cb39b
009CCBAF  41 0F B6 0C 24                  movzx ecx, byte ptr [r12]
009CCBB4  8B D6                           mov edx, esi
009CCBB6  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCBBE  3B 08                           cmp ecx, dword ptr [rax]
009CCBC0  0F 9C C2                        setl dl
009CCBC3  41 89 17                        mov dword ptr [r15], edx
009CCBC6  E9 D0 E7 FF FF                  jmp 0x1409cb39b
009CCBCB  41 0F B6 0C 24                  movzx ecx, byte ptr [r12]
009CCBD0  8B D6                           mov edx, esi
009CCBD2  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCBDA  3B 08                           cmp ecx, dword ptr [rax]
009CCBDC  0F 9F C2                        setg dl
009CCBDF  41 89 17                        mov dword ptr [r15], edx
009CCBE2  E9 B4 E7 FF FF                  jmp 0x1409cb39b
009CCBE7  41 83 F9 01                     cmp r9d, 1
009CCBEB  0F 85 E5 E7 FF FF               jne 0x1409cb3d6
009CCBF1  41 0F B6 0C 24                  movzx ecx, byte ptr [r12]
009CCBF6  8B D6                           mov edx, esi
009CCBF8  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCC00  3B 08                           cmp ecx, dword ptr [rax]
009CCC02  0F 96 C2                        setbe dl
009CCC05  41 89 17                        mov dword ptr [r15], edx
009CCC08  E9 8E E7 FF FF                  jmp 0x1409cb39b
009CCC0D  41 0F B6 0C 24                  movzx ecx, byte ptr [r12]
009CCC12  8B D6                           mov edx, esi
009CCC14  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCC1C  3B 08                           cmp ecx, dword ptr [rax]
009CCC1E  0F 92 C2                        setb dl
009CCC21  41 89 17                        mov dword ptr [r15], edx
009CCC24  E9 72 E7 FF FF                  jmp 0x1409cb39b
009CCC29  41 0F B6 0C 24                  movzx ecx, byte ptr [r12]
009CCC2E  8B D6                           mov edx, esi
009CCC30  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCC38  3B 08                           cmp ecx, dword ptr [rax]
009CCC3A  0F 97 C2                        seta dl
009CCC3D  41 89 17                        mov dword ptr [r15], edx
009CCC40  E9 56 E7 FF FF                  jmp 0x1409cb39b
009CCC45  41 83 F9 01                     cmp r9d, 1
009CCC49  0F 85 87 E7 FF FF               jne 0x1409cb3d6
009CCC4F  41 0F B6 0C 24                  movzx ecx, byte ptr [r12]
009CCC54  8B D6                           mov edx, esi
009CCC56  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCC5E  48 3B 08                        cmp rcx, qword ptr [rax]
009CCC61  0F 9E C2                        setle dl
009CCC64  41 89 17                        mov dword ptr [r15], edx
009CCC67  E9 2F E7 FF FF                  jmp 0x1409cb39b
009CCC6C  41 0F B6 0C 24                  movzx ecx, byte ptr [r12]
009CCC71  8B D6                           mov edx, esi
009CCC73  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCC7B  48 3B 08                        cmp rcx, qword ptr [rax]
009CCC7E  0F 9C C2                        setl dl
009CCC81  41 89 17                        mov dword ptr [r15], edx
009CCC84  E9 12 E7 FF FF                  jmp 0x1409cb39b
009CCC89  41 0F B6 0C 24                  movzx ecx, byte ptr [r12]
009CCC8E  8B D6                           mov edx, esi
009CCC90  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCC98  48 3B 08                        cmp rcx, qword ptr [rax]
009CCC9B  0F 9F C2                        setg dl
009CCC9E  41 89 17                        mov dword ptr [r15], edx
009CCCA1  E9 F5 E6 FF FF                  jmp 0x1409cb39b
009CCCA6  41 83 F9 01                     cmp r9d, 1
009CCCAA  0F 85 26 E7 FF FF               jne 0x1409cb3d6
009CCCB0  41 0F B6 0C 24                  movzx ecx, byte ptr [r12]
009CCCB5  8B D6                           mov edx, esi
009CCCB7  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCCBF  48 3B 08                        cmp rcx, qword ptr [rax]
009CCCC2  0F 96 C2                        setbe dl
009CCCC5  41 89 17                        mov dword ptr [r15], edx
009CCCC8  E9 CE E6 FF FF                  jmp 0x1409cb39b
009CCCCD  41 0F B6 0C 24                  movzx ecx, byte ptr [r12]
009CCCD2  8B D6                           mov edx, esi
009CCCD4  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCCDC  48 3B 08                        cmp rcx, qword ptr [rax]
009CCCDF  0F 92 C2                        setb dl
009CCCE2  41 89 17                        mov dword ptr [r15], edx
009CCCE5  E9 B1 E6 FF FF                  jmp 0x1409cb39b
009CCCEA  41 0F B6 0C 24                  movzx ecx, byte ptr [r12]
009CCCEF  8B D6                           mov edx, esi
009CCCF1  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCCF9  48 3B 08                        cmp rcx, qword ptr [rax]
009CCCFC  0F 97 C2                        seta dl
009CCCFF  41 89 17                        mov dword ptr [r15], edx
009CCD02  E9 94 E6 FF FF                  jmp 0x1409cb39b
009CCD07  41 83 F9 01                     cmp r9d, 1
009CCD0B  0F 85 C5 E6 FF FF               jne 0x1409cb3d6
009CCD11  41 0F B6 04 24                  movzx eax, byte ptr [r12]
009CCD16  66 0F 6E C8                     movd xmm1, eax
009CCD1A  0F 5B C9                        cvtdq2ps xmm1, xmm1
009CCD1D  8B CE                           mov ecx, esi
009CCD1F  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCD27  F3 0F 10 00                     movss xmm0, dword ptr [rax]
009CCD2B  0F 2F C1                        comiss xmm0, xmm1
009CCD2E  0F 93 C1                        setae cl
009CCD31  41 89 0F                        mov dword ptr [r15], ecx
009CCD34  E9 62 E6 FF FF                  jmp 0x1409cb39b
009CCD39  41 0F B6 04 24                  movzx eax, byte ptr [r12]
009CCD3E  E9 17 EA FF FF                  jmp 0x1409cb75a
009CCD43  41 0F B6 04 24                  movzx eax, byte ptr [r12]
009CCD48  66 0F 6E C0                     movd xmm0, eax
009CCD4C  0F 5B C0                        cvtdq2ps xmm0, xmm0
009CCD4F  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCD57  0F 2E 00                        ucomiss xmm0, dword ptr [rax]
009CCD5A  E9 92 F7 FF FF                  jmp 0x1409cc4f1
009CCD5F  41 83 F9 01                     cmp r9d, 1
009CCD63  0F 85 6D E6 FF FF               jne 0x1409cb3d6
009CCD69  41 0F B6 04 24                  movzx eax, byte ptr [r12]
009CCD6E  66 0F 6E C8                     movd xmm1, eax
009CCD72  F3 0F E6 C9                     cvtdq2pd xmm1, xmm1
009CCD76  8B CE                           mov ecx, esi
009CCD78  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCD80  F2 0F 10 00                     movsd xmm0, qword ptr [rax]
009CCD84  66 0F 2F C1                     comisd xmm0, xmm1
009CCD88  0F 93 C1                        setae cl
009CCD8B  41 89 0F                        mov dword ptr [r15], ecx
009CCD8E  E9 08 E6 FF FF                  jmp 0x1409cb39b
009CCD93  41 0F B6 04 24                  movzx eax, byte ptr [r12]
009CCD98  E9 BA F7 FF FF                  jmp 0x1409cc557
009CCD9D  41 0F B6 04 24                  movzx eax, byte ptr [r12]
009CCDA2  E9 DA F7 FF FF                  jmp 0x1409cc581
009CCDA7  41 83 F9 01                     cmp r9d, 1
009CCDAB  0F 85 25 E6 FF FF               jne 0x1409cb3d6
009CCDB1  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCDB9  0F BE 08                        movsx ecx, byte ptr [rax]
009CCDBC  8B C6                           mov eax, esi
009CCDBE  66 41 39 0C 24                  cmp word ptr [r12], cx
009CCDC3  0F 9E C0                        setle al
009CCDC6  E9 CD E5 FF FF                  jmp 0x1409cb398
009CCDCB  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCDD3  0F BE 08                        movsx ecx, byte ptr [rax]
009CCDD6  8B C6                           mov eax, esi
009CCDD8  66 41 39 0C 24                  cmp word ptr [r12], cx
009CCDDD  0F 9C C0                        setl al
009CCDE0  E9 B3 E5 FF FF                  jmp 0x1409cb398
009CCDE5  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCDED  0F BE 08                        movsx ecx, byte ptr [rax]
009CCDF0  8B C6                           mov eax, esi
009CCDF2  66 41 39 0C 24                  cmp word ptr [r12], cx
009CCDF7  0F 9F C0                        setg al
009CCDFA  E9 99 E5 FF FF                  jmp 0x1409cb398
009CCDFF  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCE07  0F BE 08                        movsx ecx, byte ptr [rax]
009CCE0A  8B C6                           mov eax, esi
009CCE0C  66 41 39 0C 24                  cmp word ptr [r12], cx
009CCE11  0F 94 C0                        sete al
009CCE14  E9 7F E5 FF FF                  jmp 0x1409cb398
009CCE19  41 83 F9 01                     cmp r9d, 1
009CCE1D  0F 85 B3 E5 FF FF               jne 0x1409cb3d6
009CCE23  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCE2B  0F B6 08                        movzx ecx, byte ptr [rax]
009CCE2E  8B C6                           mov eax, esi
009CCE30  66 41 39 0C 24                  cmp word ptr [r12], cx
009CCE35  0F 9E C0                        setle al
009CCE38  E9 5B E5 FF FF                  jmp 0x1409cb398
009CCE3D  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCE45  0F B6 08                        movzx ecx, byte ptr [rax]
009CCE48  8B C6                           mov eax, esi
009CCE4A  66 41 39 0C 24                  cmp word ptr [r12], cx
009CCE4F  0F 9C C0                        setl al
009CCE52  E9 41 E5 FF FF                  jmp 0x1409cb398
009CCE57  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCE5F  0F B6 08                        movzx ecx, byte ptr [rax]
009CCE62  8B C6                           mov eax, esi
009CCE64  66 41 39 0C 24                  cmp word ptr [r12], cx
009CCE69  0F 9F C0                        setg al
009CCE6C  E9 27 E5 FF FF                  jmp 0x1409cb398
009CCE71  41 83 F9 01                     cmp r9d, 1
009CCE75  0F 85 5B E5 FF FF               jne 0x1409cb3d6
009CCE7B  8B D6                           mov edx, esi
009CCE7D  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCE85  0F B7 08                        movzx ecx, word ptr [rax]
009CCE88  66 41 39 0C 24                  cmp word ptr [r12], cx
009CCE8D  0F 9E C2                        setle dl
009CCE90  41 89 17                        mov dword ptr [r15], edx
009CCE93  E9 03 E5 FF FF                  jmp 0x1409cb39b
009CCE98  8B D6                           mov edx, esi
009CCE9A  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCEA2  0F B7 08                        movzx ecx, word ptr [rax]
009CCEA5  66 41 39 0C 24                  cmp word ptr [r12], cx
009CCEAA  0F 9C C2                        setl dl
009CCEAD  41 89 17                        mov dword ptr [r15], edx
009CCEB0  E9 E6 E4 FF FF                  jmp 0x1409cb39b
009CCEB5  8B D6                           mov edx, esi
009CCEB7  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCEBF  0F B7 08                        movzx ecx, word ptr [rax]
009CCEC2  66 41 39 0C 24                  cmp word ptr [r12], cx
009CCEC7  0F 9F C2                        setg dl
009CCECA  41 89 17                        mov dword ptr [r15], edx
009CCECD  E9 C9 E4 FF FF                  jmp 0x1409cb39b
009CCED2  41 83 F9 01                     cmp r9d, 1
009CCED6  0F 85 FA E4 FF FF               jne 0x1409cb3d6
009CCEDC  41 0F BF 14 24                  movsx edx, word ptr [r12]
009CCEE1  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCEE9  0F B7 08                        movzx ecx, word ptr [rax]
009CCEEC  8B C6                           mov eax, esi
009CCEEE  3B D1                           cmp edx, ecx
009CCEF0  0F 9E C0                        setle al
009CCEF3  E9 A0 E4 FF FF                  jmp 0x1409cb398
009CCEF8  41 0F BF 14 24                  movsx edx, word ptr [r12]
009CCEFD  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCF05  0F B7 08                        movzx ecx, word ptr [rax]
009CCF08  8B C6                           mov eax, esi
009CCF0A  3B D1                           cmp edx, ecx
009CCF0C  0F 9C C0                        setl al
009CCF0F  E9 84 E4 FF FF                  jmp 0x1409cb398
009CCF14  41 0F BF 14 24                  movsx edx, word ptr [r12]
009CCF19  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCF21  0F B7 08                        movzx ecx, word ptr [rax]
009CCF24  8B C6                           mov eax, esi
009CCF26  3B D1                           cmp edx, ecx
009CCF28  0F 9F C0                        setg al
009CCF2B  E9 68 E4 FF FF                  jmp 0x1409cb398
009CCF30  41 0F BF 14 24                  movsx edx, word ptr [r12]
009CCF35  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCF3D  0F B7 08                        movzx ecx, word ptr [rax]
009CCF40  8B C6                           mov eax, esi
009CCF42  3B D1                           cmp edx, ecx
009CCF44  0F 94 C0                        sete al
009CCF47  E9 4C E4 FF FF                  jmp 0x1409cb398
009CCF4C  41 83 F9 01                     cmp r9d, 1
009CCF50  0F 85 80 E4 FF FF               jne 0x1409cb3d6
009CCF56  41 0F BF 0C 24                  movsx ecx, word ptr [r12]
009CCF5B  8B D6                           mov edx, esi
009CCF5D  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCF65  3B 08                           cmp ecx, dword ptr [rax]
009CCF67  0F 9D C2                        setge dl
009CCF6A  41 89 17                        mov dword ptr [r15], edx
009CCF6D  E9 29 E4 FF FF                  jmp 0x1409cb39b
009CCF72  41 0F BF 0C 24                  movsx ecx, word ptr [r12]
009CCF77  8B D6                           mov edx, esi
009CCF79  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCF81  3B 08                           cmp ecx, dword ptr [rax]
009CCF83  0F 9F C2                        setg dl
009CCF86  41 89 17                        mov dword ptr [r15], edx
009CCF89  E9 0D E4 FF FF                  jmp 0x1409cb39b
009CCF8E  41 83 F9 01                     cmp r9d, 1
009CCF92  0F 85 3E E4 FF FF               jne 0x1409cb3d6
009CCF98  41 0F BF 0C 24                  movsx ecx, word ptr [r12]
009CCF9D  8B D6                           mov edx, esi
009CCF9F  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCFA7  3B 08                           cmp ecx, dword ptr [rax]
009CCFA9  0F 96 C2                        setbe dl
009CCFAC  41 89 17                        mov dword ptr [r15], edx
009CCFAF  E9 E7 E3 FF FF                  jmp 0x1409cb39b
009CCFB4  41 0F BF 0C 24                  movsx ecx, word ptr [r12]
009CCFB9  8B D6                           mov edx, esi
009CCFBB  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCFC3  3B 08                           cmp ecx, dword ptr [rax]
009CCFC5  0F 92 C2                        setb dl
009CCFC8  41 89 17                        mov dword ptr [r15], edx
009CCFCB  E9 CB E3 FF FF                  jmp 0x1409cb39b
009CCFD0  41 0F BF 0C 24                  movsx ecx, word ptr [r12]
009CCFD5  8B D6                           mov edx, esi
009CCFD7  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CCFDF  3B 08                           cmp ecx, dword ptr [rax]
009CCFE1  0F 97 C2                        seta dl
009CCFE4  41 89 17                        mov dword ptr [r15], edx
009CCFE7  E9 AF E3 FF FF                  jmp 0x1409cb39b
009CCFEC  41 83 F9 01                     cmp r9d, 1
009CCFF0  0F 85 E0 E3 FF FF               jne 0x1409cb3d6
009CCFF6  49 0F BF 0C 24                  movsx rcx, word ptr [r12]
009CCFFB  8B D6                           mov edx, esi
009CCFFD  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD005  48 3B 08                        cmp rcx, qword ptr [rax]
009CD008  0F 9E C2                        setle dl
009CD00B  41 89 17                        mov dword ptr [r15], edx
009CD00E  E9 88 E3 FF FF                  jmp 0x1409cb39b
009CD013  49 0F BF 0C 24                  movsx rcx, word ptr [r12]
009CD018  8B D6                           mov edx, esi
009CD01A  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD022  48 3B 08                        cmp rcx, qword ptr [rax]
009CD025  0F 9C C2                        setl dl
009CD028  41 89 17                        mov dword ptr [r15], edx
009CD02B  E9 6B E3 FF FF                  jmp 0x1409cb39b
009CD030  49 0F BF 0C 24                  movsx rcx, word ptr [r12]
009CD035  8B D6                           mov edx, esi
009CD037  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD03F  48 3B 08                        cmp rcx, qword ptr [rax]
009CD042  0F 9F C2                        setg dl
009CD045  41 89 17                        mov dword ptr [r15], edx
009CD048  E9 4E E3 FF FF                  jmp 0x1409cb39b
009CD04D  41 83 F9 01                     cmp r9d, 1
009CD051  0F 85 7F E3 FF FF               jne 0x1409cb3d6
009CD057  49 0F BF 0C 24                  movsx rcx, word ptr [r12]
009CD05C  8B D6                           mov edx, esi
009CD05E  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD066  48 3B 08                        cmp rcx, qword ptr [rax]
009CD069  0F 96 C2                        setbe dl
009CD06C  41 89 17                        mov dword ptr [r15], edx
009CD06F  E9 27 E3 FF FF                  jmp 0x1409cb39b
009CD074  49 0F BF 0C 24                  movsx rcx, word ptr [r12]
009CD079  8B D6                           mov edx, esi
009CD07B  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD083  48 3B 08                        cmp rcx, qword ptr [rax]
009CD086  0F 92 C2                        setb dl
009CD089  41 89 17                        mov dword ptr [r15], edx
009CD08C  E9 0A E3 FF FF                  jmp 0x1409cb39b
009CD091  49 0F BF 0C 24                  movsx rcx, word ptr [r12]
009CD096  8B D6                           mov edx, esi
009CD098  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD0A0  48 3B 08                        cmp rcx, qword ptr [rax]
009CD0A3  0F 97 C2                        seta dl
009CD0A6  41 89 17                        mov dword ptr [r15], edx
009CD0A9  E9 ED E2 FF FF                  jmp 0x1409cb39b
009CD0AE  41 83 F9 01                     cmp r9d, 1
009CD0B2  0F 85 1E E3 FF FF               jne 0x1409cb3d6
009CD0B8  41 0F BF 04 24                  movsx eax, word ptr [r12]
009CD0BD  E9 A1 F3 FF FF                  jmp 0x1409cc463
009CD0C2  41 0F BF 04 24                  movsx eax, word ptr [r12]
009CD0C7  66 0F 6E C0                     movd xmm0, eax
009CD0CB  0F 5B C0                        cvtdq2ps xmm0, xmm0
009CD0CE  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD0D6  0F 2F 00                        comiss xmm0, dword ptr [rax]
009CD0D9  E9 92 E6 FF FF                  jmp 0x1409cb770
009CD0DE  41 0F BF 04 24                  movsx eax, word ptr [r12]
009CD0E3  66 0F 6E C0                     movd xmm0, eax
009CD0E7  0F 5B C0                        cvtdq2ps xmm0, xmm0
009CD0EA  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD0F2  0F 2E 00                        ucomiss xmm0, dword ptr [rax]
009CD0F5  E9 F7 F3 FF FF                  jmp 0x1409cc4f1
009CD0FA  41 0F BF 04 24                  movsx eax, word ptr [r12]
009CD0FF  E9 AD E4 FF FF                  jmp 0x1409cb5b1
009CD104  41 0F BF 04 24                  movsx eax, word ptr [r12]
009CD109  E9 1A F4 FF FF                  jmp 0x1409cc528
009CD10E  41 83 F9 01                     cmp r9d, 1
009CD112  0F 85 BE E2 FF FF               jne 0x1409cb3d6
009CD118  41 0F B7 14 24                  movzx edx, word ptr [r12]
009CD11D  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD125  0F BE 08                        movsx ecx, byte ptr [rax]
009CD128  8B C6                           mov eax, esi
009CD12A  3B D1                           cmp edx, ecx
009CD12C  0F 9E C0                        setle al
009CD12F  E9 64 E2 FF FF                  jmp 0x1409cb398
009CD134  41 0F B7 14 24                  movzx edx, word ptr [r12]
009CD139  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD141  0F BE 08                        movsx ecx, byte ptr [rax]
009CD144  8B C6                           mov eax, esi
009CD146  3B D1                           cmp edx, ecx
009CD148  0F 9C C0                        setl al
009CD14B  E9 48 E2 FF FF                  jmp 0x1409cb398
009CD150  41 0F B7 14 24                  movzx edx, word ptr [r12]
009CD155  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD15D  0F BE 08                        movsx ecx, byte ptr [rax]
009CD160  8B C6                           mov eax, esi
009CD162  3B D1                           cmp edx, ecx
009CD164  0F 9F C0                        setg al
009CD167  E9 2C E2 FF FF                  jmp 0x1409cb398
009CD16C  41 0F B7 14 24                  movzx edx, word ptr [r12]
009CD171  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD179  0F BE 08                        movsx ecx, byte ptr [rax]
009CD17C  8B C6                           mov eax, esi
009CD17E  3B D1                           cmp edx, ecx
009CD180  0F 94 C0                        sete al
009CD183  E9 10 E2 FF FF                  jmp 0x1409cb398
009CD188  41 83 F9 01                     cmp r9d, 1
009CD18C  0F 85 44 E2 FF FF               jne 0x1409cb3d6
009CD192  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD19A  0F B6 08                        movzx ecx, byte ptr [rax]
009CD19D  8B C6                           mov eax, esi
009CD19F  66 41 39 0C 24                  cmp word ptr [r12], cx
009CD1A4  0F 96 C0                        setbe al
009CD1A7  E9 EC E1 FF FF                  jmp 0x1409cb398
009CD1AC  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD1B4  0F B6 08                        movzx ecx, byte ptr [rax]
009CD1B7  8B C6                           mov eax, esi
009CD1B9  66 41 39 0C 24                  cmp word ptr [r12], cx
009CD1BE  0F 92 C0                        setb al
009CD1C1  E9 D2 E1 FF FF                  jmp 0x1409cb398
009CD1C6  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD1CE  0F B6 08                        movzx ecx, byte ptr [rax]
009CD1D1  8B C6                           mov eax, esi
009CD1D3  66 41 39 0C 24                  cmp word ptr [r12], cx
009CD1D8  0F 97 C0                        seta al
009CD1DB  E9 B8 E1 FF FF                  jmp 0x1409cb398
009CD1E0  41 83 F9 01                     cmp r9d, 1
009CD1E4  0F 85 EC E1 FF FF               jne 0x1409cb3d6
009CD1EA  41 0F B7 14 24                  movzx edx, word ptr [r12]
009CD1EF  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD1F7  0F BF 08                        movsx ecx, word ptr [rax]
009CD1FA  8B C6                           mov eax, esi
009CD1FC  3B D1                           cmp edx, ecx
009CD1FE  0F 9E C0                        setle al
009CD201  E9 92 E1 FF FF                  jmp 0x1409cb398
009CD206  41 0F B7 14 24                  movzx edx, word ptr [r12]
009CD20B  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD213  0F BF 08                        movsx ecx, word ptr [rax]
009CD216  8B C6                           mov eax, esi
009CD218  3B D1                           cmp edx, ecx
009CD21A  0F 9C C0                        setl al
009CD21D  E9 76 E1 FF FF                  jmp 0x1409cb398
009CD222  41 0F B7 14 24                  movzx edx, word ptr [r12]
009CD227  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD22F  0F BF 08                        movsx ecx, word ptr [rax]
009CD232  8B C6                           mov eax, esi
009CD234  3B D1                           cmp edx, ecx
009CD236  0F 9F C0                        setg al
009CD239  E9 5A E1 FF FF                  jmp 0x1409cb398
009CD23E  41 0F B7 14 24                  movzx edx, word ptr [r12]
009CD243  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD24B  0F BF 08                        movsx ecx, word ptr [rax]
009CD24E  8B C6                           mov eax, esi
009CD250  3B D1                           cmp edx, ecx
009CD252  0F 94 C0                        sete al
009CD255  E9 3E E1 FF FF                  jmp 0x1409cb398
009CD25A  8B D6                           mov edx, esi
009CD25C  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD264  0F B7 08                        movzx ecx, word ptr [rax]
009CD267  66 41 39 0C 24                  cmp word ptr [r12], cx
009CD26C  0F 93 C2                        setae dl
009CD26F  41 89 17                        mov dword ptr [r15], edx
009CD272  E9 24 E1 FF FF                  jmp 0x1409cb39b
009CD277  8B D6                           mov edx, esi
009CD279  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD281  0F B7 08                        movzx ecx, word ptr [rax]
009CD284  66 41 39 0C 24                  cmp word ptr [r12], cx
009CD289  0F 92 C2                        setb dl
009CD28C  41 89 17                        mov dword ptr [r15], edx
009CD28F  E9 07 E1 FF FF                  jmp 0x1409cb39b
009CD294  8B D6                           mov edx, esi
009CD296  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD29E  0F B7 08                        movzx ecx, word ptr [rax]
009CD2A1  66 41 39 0C 24                  cmp word ptr [r12], cx
009CD2A6  0F 97 C2                        seta dl
009CD2A9  41 89 17                        mov dword ptr [r15], edx
009CD2AC  E9 EA E0 FF FF                  jmp 0x1409cb39b
009CD2B1  41 83 F9 01                     cmp r9d, 1
009CD2B5  0F 85 1B E1 FF FF               jne 0x1409cb3d6
009CD2BB  41 0F B7 0C 24                  movzx ecx, word ptr [r12]
009CD2C0  8B D6                           mov edx, esi
009CD2C2  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD2CA  3B 08                           cmp ecx, dword ptr [rax]
009CD2CC  0F 9E C2                        setle dl
009CD2CF  41 89 17                        mov dword ptr [r15], edx
009CD2D2  E9 C4 E0 FF FF                  jmp 0x1409cb39b
009CD2D7  41 0F B7 0C 24                  movzx ecx, word ptr [r12]
009CD2DC  8B D6                           mov edx, esi
009CD2DE  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD2E6  3B 08                           cmp ecx, dword ptr [rax]
009CD2E8  0F 9C C2                        setl dl
009CD2EB  41 89 17                        mov dword ptr [r15], edx
009CD2EE  E9 A8 E0 FF FF                  jmp 0x1409cb39b
009CD2F3  41 0F B7 0C 24                  movzx ecx, word ptr [r12]
009CD2F8  8B D6                           mov edx, esi
009CD2FA  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD302  3B 08                           cmp ecx, dword ptr [rax]
009CD304  0F 9F C2                        setg dl
009CD307  41 89 17                        mov dword ptr [r15], edx
009CD30A  E9 8C E0 FF FF                  jmp 0x1409cb39b
009CD30F  41 83 F9 01                     cmp r9d, 1
009CD313  0F 85 BD E0 FF FF               jne 0x1409cb3d6
009CD319  41 0F B7 0C 24                  movzx ecx, word ptr [r12]
009CD31E  8B D6                           mov edx, esi
009CD320  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD328  3B 08                           cmp ecx, dword ptr [rax]
009CD32A  0F 96 C2                        setbe dl
009CD32D  41 89 17                        mov dword ptr [r15], edx
009CD330  E9 66 E0 FF FF                  jmp 0x1409cb39b
009CD335  41 0F B7 0C 24                  movzx ecx, word ptr [r12]
009CD33A  8B D6                           mov edx, esi
009CD33C  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD344  3B 08                           cmp ecx, dword ptr [rax]
009CD346  0F 92 C2                        setb dl
009CD349  41 89 17                        mov dword ptr [r15], edx
009CD34C  E9 4A E0 FF FF                  jmp 0x1409cb39b
009CD351  41 0F B7 0C 24                  movzx ecx, word ptr [r12]
009CD356  8B D6                           mov edx, esi
009CD358  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD360  3B 08                           cmp ecx, dword ptr [rax]
009CD362  0F 97 C2                        seta dl
009CD365  41 89 17                        mov dword ptr [r15], edx
009CD368  E9 2E E0 FF FF                  jmp 0x1409cb39b
009CD36D  41 83 F9 01                     cmp r9d, 1
009CD371  0F 85 5F E0 FF FF               jne 0x1409cb3d6
009CD377  41 0F B7 0C 24                  movzx ecx, word ptr [r12]
009CD37C  8B D6                           mov edx, esi
009CD37E  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD386  48 3B 08                        cmp rcx, qword ptr [rax]
009CD389  0F 9E C2                        setle dl
009CD38C  41 89 17                        mov dword ptr [r15], edx
009CD38F  E9 07 E0 FF FF                  jmp 0x1409cb39b
009CD394  41 0F B7 0C 24                  movzx ecx, word ptr [r12]
009CD399  8B D6                           mov edx, esi
009CD39B  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD3A3  48 3B 08                        cmp rcx, qword ptr [rax]
009CD3A6  0F 9C C2                        setl dl
009CD3A9  41 89 17                        mov dword ptr [r15], edx
009CD3AC  E9 EA DF FF FF                  jmp 0x1409cb39b
009CD3B1  41 0F B7 0C 24                  movzx ecx, word ptr [r12]
009CD3B6  8B D6                           mov edx, esi
009CD3B8  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD3C0  48 3B 08                        cmp rcx, qword ptr [rax]
009CD3C3  0F 9F C2                        setg dl
009CD3C6  41 89 17                        mov dword ptr [r15], edx
009CD3C9  E9 CD DF FF FF                  jmp 0x1409cb39b
009CD3CE  41 83 F9 01                     cmp r9d, 1
009CD3D2  0F 85 FE DF FF FF               jne 0x1409cb3d6
009CD3D8  41 0F B7 0C 24                  movzx ecx, word ptr [r12]
009CD3DD  8B D6                           mov edx, esi
009CD3DF  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD3E7  48 3B 08                        cmp rcx, qword ptr [rax]
009CD3EA  0F 96 C2                        setbe dl
009CD3ED  41 89 17                        mov dword ptr [r15], edx
009CD3F0  E9 A6 DF FF FF                  jmp 0x1409cb39b
009CD3F5  41 0F B7 0C 24                  movzx ecx, word ptr [r12]
009CD3FA  8B D6                           mov edx, esi
009CD3FC  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD404  48 3B 08                        cmp rcx, qword ptr [rax]
009CD407  0F 92 C2                        setb dl
009CD40A  41 89 17                        mov dword ptr [r15], edx
009CD40D  E9 89 DF FF FF                  jmp 0x1409cb39b
009CD412  41 0F B7 0C 24                  movzx ecx, word ptr [r12]
009CD417  8B D6                           mov edx, esi
009CD419  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD421  48 3B 08                        cmp rcx, qword ptr [rax]
009CD424  0F 97 C2                        seta dl
009CD427  41 89 17                        mov dword ptr [r15], edx
009CD42A  E9 6C DF FF FF                  jmp 0x1409cb39b
009CD42F  41 0F B7 04 24                  movzx eax, word ptr [r12]
009CD434  E9 21 E3 FF FF                  jmp 0x1409cb75a
009CD439  41 0F B7 04 24                  movzx eax, word ptr [r12]
009CD43E  66 0F 6E C0                     movd xmm0, eax
009CD442  0F 5B C0                        cvtdq2ps xmm0, xmm0
009CD445  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD44D  0F 2F 00                        comiss xmm0, dword ptr [rax]
009CD450  E9 1B E3 FF FF                  jmp 0x1409cb770
009CD455  41 0F B7 04 24                  movzx eax, word ptr [r12]
009CD45A  66 0F 6E C0                     movd xmm0, eax
009CD45E  0F 5B C0                        cvtdq2ps xmm0, xmm0
009CD461  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD469  0F 2E 00                        ucomiss xmm0, dword ptr [rax]
009CD46C  E9 80 F0 FF FF                  jmp 0x1409cc4f1
009CD471  41 83 F9 01                     cmp r9d, 1
009CD475  0F 85 5B DF FF FF               jne 0x1409cb3d6
009CD47B  41 0F B7 04 24                  movzx eax, word ptr [r12]
009CD480  E9 A0 E1 FF FF                  jmp 0x1409cb625
009CD485  41 0F B7 04 24                  movzx eax, word ptr [r12]
009CD48A  E9 C8 F0 FF FF                  jmp 0x1409cc557
009CD48F  41 0F B7 04 24                  movzx eax, word ptr [r12]
009CD494  E9 E8 F0 FF FF                  jmp 0x1409cc581
009CD499  41 0F B7 04 24                  movzx eax, word ptr [r12]
009CD49E  E9 85 F0 FF FF                  jmp 0x1409cc528
009CD4A3  41 83 F9 01                     cmp r9d, 1
009CD4A7  0F 85 29 DF FF FF               jne 0x1409cb3d6
009CD4AD  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD4B5  0F BE 08                        movsx ecx, byte ptr [rax]
009CD4B8  8B C6                           mov eax, esi
009CD4BA  41 39 0C 24                     cmp dword ptr [r12], ecx
009CD4BE  0F 9E C0                        setle al
009CD4C1  E9 D2 DE FF FF                  jmp 0x1409cb398
009CD4C6  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD4CE  0F BE 08                        movsx ecx, byte ptr [rax]
009CD4D1  8B C6                           mov eax, esi
009CD4D3  41 39 0C 24                     cmp dword ptr [r12], ecx
009CD4D7  0F 9C C0                        setl al
009CD4DA  E9 B9 DE FF FF                  jmp 0x1409cb398
009CD4DF  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD4E7  0F BE 08                        movsx ecx, byte ptr [rax]
009CD4EA  8B C6                           mov eax, esi
009CD4EC  41 39 0C 24                     cmp dword ptr [r12], ecx
009CD4F0  0F 9F C0                        setg al
009CD4F3  E9 A0 DE FF FF                  jmp 0x1409cb398
009CD4F8  41 83 F9 01                     cmp r9d, 1
009CD4FC  0F 85 D4 DE FF FF               jne 0x1409cb3d6
009CD502  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD50A  0F B6 08                        movzx ecx, byte ptr [rax]
009CD50D  8B C6                           mov eax, esi
009CD50F  41 39 0C 24                     cmp dword ptr [r12], ecx
009CD513  0F 9E C0                        setle al
009CD516  E9 7D DE FF FF                  jmp 0x1409cb398
009CD51B  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD523  0F B6 08                        movzx ecx, byte ptr [rax]
009CD526  8B C6                           mov eax, esi
009CD528  41 39 0C 24                     cmp dword ptr [r12], ecx
009CD52C  0F 9C C0                        setl al
009CD52F  E9 64 DE FF FF                  jmp 0x1409cb398
009CD534  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD53C  0F B6 08                        movzx ecx, byte ptr [rax]
009CD53F  8B C6                           mov eax, esi
009CD541  41 39 0C 24                     cmp dword ptr [r12], ecx
009CD545  0F 9F C0                        setg al
009CD548  E9 4B DE FF FF                  jmp 0x1409cb398
009CD54D  41 83 F9 01                     cmp r9d, 1
009CD551  0F 85 7F DE FF FF               jne 0x1409cb3d6
009CD557  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD55F  0F BF 08                        movsx ecx, word ptr [rax]
009CD562  8B C6                           mov eax, esi
009CD564  41 39 0C 24                     cmp dword ptr [r12], ecx
009CD568  0F 9E C0                        setle al
009CD56B  E9 28 DE FF FF                  jmp 0x1409cb398
009CD570  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD578  0F BF 08                        movsx ecx, word ptr [rax]
009CD57B  8B C6                           mov eax, esi
009CD57D  41 39 0C 24                     cmp dword ptr [r12], ecx
009CD581  0F 9C C0                        setl al
009CD584  E9 0F DE FF FF                  jmp 0x1409cb398
009CD589  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD591  0F BF 08                        movsx ecx, word ptr [rax]
009CD594  8B C6                           mov eax, esi
009CD596  41 39 0C 24                     cmp dword ptr [r12], ecx
009CD59A  0F 9F C0                        setg al
009CD59D  E9 F6 DD FF FF                  jmp 0x1409cb398
009CD5A2  41 83 F9 01                     cmp r9d, 1
009CD5A6  0F 85 2A DE FF FF               jne 0x1409cb3d6
009CD5AC  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD5B4  0F B7 08                        movzx ecx, word ptr [rax]
009CD5B7  8B C6                           mov eax, esi
009CD5B9  41 39 0C 24                     cmp dword ptr [r12], ecx
009CD5BD  0F 9E C0                        setle al
009CD5C0  E9 D3 DD FF FF                  jmp 0x1409cb398
009CD5C5  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD5CD  0F B7 08                        movzx ecx, word ptr [rax]
009CD5D0  8B C6                           mov eax, esi
009CD5D2  41 39 0C 24                     cmp dword ptr [r12], ecx
009CD5D6  0F 9C C0                        setl al
009CD5D9  E9 BA DD FF FF                  jmp 0x1409cb398
009CD5DE  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD5E6  0F B7 08                        movzx ecx, word ptr [rax]
009CD5E9  8B C6                           mov eax, esi
009CD5EB  41 39 0C 24                     cmp dword ptr [r12], ecx
009CD5EF  0F 9F C0                        setg al
009CD5F2  E9 A1 DD FF FF                  jmp 0x1409cb398
009CD5F7  41 83 F9 01                     cmp r9d, 1
009CD5FB  0F 85 D5 DD FF FF               jne 0x1409cb3d6
009CD601  8B D6                           mov edx, esi
009CD603  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD60B  8B 08                           mov ecx, dword ptr [rax]
009CD60D  41 39 0C 24                     cmp dword ptr [r12], ecx
009CD611  0F 9E C2                        setle dl
009CD614  41 89 17                        mov dword ptr [r15], edx
009CD617  E9 7F DD FF FF                  jmp 0x1409cb39b
009CD61C  8B D6                           mov edx, esi
009CD61E  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD626  8B 08                           mov ecx, dword ptr [rax]
009CD628  41 39 0C 24                     cmp dword ptr [r12], ecx
009CD62C  0F 9C C2                        setl dl
009CD62F  41 89 17                        mov dword ptr [r15], edx
009CD632  E9 64 DD FF FF                  jmp 0x1409cb39b
009CD637  8B D6                           mov edx, esi
009CD639  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD641  8B 08                           mov ecx, dword ptr [rax]
009CD643  41 39 0C 24                     cmp dword ptr [r12], ecx
009CD647  0F 9F C2                        setg dl
009CD64A  41 89 17                        mov dword ptr [r15], edx
009CD64D  E9 49 DD FF FF                  jmp 0x1409cb39b
009CD652  41 83 F9 01                     cmp r9d, 1
009CD656  0F 85 7A DD FF FF               jne 0x1409cb3d6
009CD65C  49 63 0C 24                     movsxd rcx, dword ptr [r12]
009CD660  8B D6                           mov edx, esi
009CD662  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD66A  48 3B 08                        cmp rcx, qword ptr [rax]
009CD66D  0F 9E C2                        setle dl
009CD670  41 89 17                        mov dword ptr [r15], edx
009CD673  E9 23 DD FF FF                  jmp 0x1409cb39b
009CD678  49 63 0C 24                     movsxd rcx, dword ptr [r12]
009CD67C  8B D6                           mov edx, esi
009CD67E  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD686  48 3B 08                        cmp rcx, qword ptr [rax]
009CD689  0F 9C C2                        setl dl
009CD68C  41 89 17                        mov dword ptr [r15], edx
009CD68F  E9 07 DD FF FF                  jmp 0x1409cb39b
009CD694  49 63 0C 24                     movsxd rcx, dword ptr [r12]
009CD698  8B D6                           mov edx, esi
009CD69A  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD6A2  48 3B 08                        cmp rcx, qword ptr [rax]
009CD6A5  0F 9F C2                        setg dl
009CD6A8  41 89 17                        mov dword ptr [r15], edx
009CD6AB  E9 EB DC FF FF                  jmp 0x1409cb39b
009CD6B0  41 83 F9 01                     cmp r9d, 1
009CD6B4  0F 85 1C DD FF FF               jne 0x1409cb3d6
009CD6BA  49 63 0C 24                     movsxd rcx, dword ptr [r12]
009CD6BE  8B D6                           mov edx, esi
009CD6C0  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD6C8  48 3B 08                        cmp rcx, qword ptr [rax]
009CD6CB  0F 96 C2                        setbe dl
009CD6CE  41 89 17                        mov dword ptr [r15], edx
009CD6D1  E9 C5 DC FF FF                  jmp 0x1409cb39b
009CD6D6  49 63 0C 24                     movsxd rcx, dword ptr [r12]
009CD6DA  8B D6                           mov edx, esi
009CD6DC  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD6E4  48 3B 08                        cmp rcx, qword ptr [rax]
009CD6E7  0F 92 C2                        setb dl
009CD6EA  41 89 17                        mov dword ptr [r15], edx
009CD6ED  E9 A9 DC FF FF                  jmp 0x1409cb39b
009CD6F2  49 63 0C 24                     movsxd rcx, dword ptr [r12]
009CD6F6  8B D6                           mov edx, esi
009CD6F8  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD700  48 3B 08                        cmp rcx, qword ptr [rax]
009CD703  0F 97 C2                        seta dl
009CD706  41 89 17                        mov dword ptr [r15], edx
009CD709  E9 8D DC FF FF                  jmp 0x1409cb39b
009CD70E  66 41 0F 6E 04 24               movd xmm0, dword ptr [r12]
009CD714  0F 5B C0                        cvtdq2ps xmm0, xmm0
009CD717  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD71F  0F 2F 00                        comiss xmm0, dword ptr [rax]
009CD722  E9 16 DF FF FF                  jmp 0x1409cb63d
009CD727  66 41 0F 6E 0C 24               movd xmm1, dword ptr [r12]
009CD72D  E9 2C E0 FF FF                  jmp 0x1409cb75e
009CD732  66 41 0F 6E 04 24               movd xmm0, dword ptr [r12]
009CD738  0F 5B C0                        cvtdq2ps xmm0, xmm0
009CD73B  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD743  0F 2F 00                        comiss xmm0, dword ptr [rax]
009CD746  E9 25 E0 FF FF                  jmp 0x1409cb770
009CD74B  66 41 0F 6E 04 24               movd xmm0, dword ptr [r12]
009CD751  0F 5B C0                        cvtdq2ps xmm0, xmm0
009CD754  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD75C  0F 2E 00                        ucomiss xmm0, dword ptr [rax]
009CD75F  E9 8D ED FF FF                  jmp 0x1409cc4f1
009CD764  66 41 0F 6E 04 24               movd xmm0, dword ptr [r12]
009CD76A  E9 46 DE FF FF                  jmp 0x1409cb5b5
009CD76F  66 41 0F 6E 0C 24               movd xmm1, dword ptr [r12]
009CD775  E9 E1 ED FF FF                  jmp 0x1409cc55b
009CD77A  66 41 0F 6E 04 24               movd xmm0, dword ptr [r12]
009CD780  E9 00 EE FF FF                  jmp 0x1409cc585
009CD785  66 41 0F 6E 04 24               movd xmm0, dword ptr [r12]
009CD78B  E9 9C ED FF FF                  jmp 0x1409cc52c
009CD790  41 83 E9 01                     sub r9d, 1
009CD794  0F 84 79 06 00 00               je 0x1409cde13
009CD79A  41 83 E9 02                     sub r9d, 2
009CD79E  0F 84 5E 06 00 00               je 0x1409cde02
009CD7A4  41 83 F9 01                     cmp r9d, 1
009CD7A8  0F 85 28 DC FF FF               jne 0x1409cb3d6
009CD7AE  41 8B 04 24                     mov eax, dword ptr [r12]
009CD7B2  0F 57 C9                        xorps xmm1, xmm1
009CD7B5  F3 48 0F 2A C8                  cvtsi2ss xmm1, rax
009CD7BA  E9 AB EC FF FF                  jmp 0x1409cc46a
009CD7BF  41 8B 04 24                     mov eax, dword ptr [r12]
009CD7C3  0F 57 C9                        xorps xmm1, xmm1
009CD7C6  F3 48 0F 2A C8                  cvtsi2ss xmm1, rax
009CD7CB  E9 91 DF FF FF                  jmp 0x1409cb761
009CD7D0  41 83 F9 01                     cmp r9d, 1
009CD7D4  0F 85 FC DB FF FF               jne 0x1409cb3d6
009CD7DA  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD7E2  0F BE 08                        movsx ecx, byte ptr [rax]
009CD7E5  8B C6                           mov eax, esi
009CD7E7  41 39 0C 24                     cmp dword ptr [r12], ecx
009CD7EB  0F 96 C0                        setbe al
009CD7EE  E9 A5 DB FF FF                  jmp 0x1409cb398
009CD7F3  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD7FB  0F BE 08                        movsx ecx, byte ptr [rax]
009CD7FE  8B C6                           mov eax, esi
009CD800  41 39 0C 24                     cmp dword ptr [r12], ecx
009CD804  0F 92 C0                        setb al
009CD807  E9 8C DB FF FF                  jmp 0x1409cb398
009CD80C  41 83 E9 01                     sub r9d, 1
009CD810  0F 84 38 06 00 00               je 0x1409cde4e
009CD816  41 83 E9 02                     sub r9d, 2
009CD81A  0F 84 1D 06 00 00               je 0x1409cde3d
009CD820  41 83 F9 01                     cmp r9d, 1
009CD824  0F 85 AC DB FF FF               jne 0x1409cb3d6
009CD82A  41 8B 04 24                     mov eax, dword ptr [r12]
009CD82E  0F 57 C9                        xorps xmm1, xmm1
009CD831  F2 48 0F 2A C8                  cvtsi2sd xmm1, rax
009CD836  E9 F2 DD FF FF                  jmp 0x1409cb62d
009CD83B  41 8B 04 24                     mov eax, dword ptr [r12]
009CD83F  0F 57 C9                        xorps xmm1, xmm1
009CD842  F2 48 0F 2A C8                  cvtsi2sd xmm1, rax
009CD847  E9 13 ED FF FF                  jmp 0x1409cc55f
009CD84C  41 8B 0C 24                     mov ecx, dword ptr [r12]
009CD850  8B D6                           mov edx, esi
009CD852  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD85A  48 3B 08                        cmp rcx, qword ptr [rax]
009CD85D  0F 9F C2                        setg dl
009CD860  41 89 17                        mov dword ptr [r15], edx
009CD863  E9 33 DB FF FF                  jmp 0x1409cb39b
009CD868  41 8B 0C 24                     mov ecx, dword ptr [r12]
009CD86C  8B D6                           mov edx, esi
009CD86E  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD876  48 3B 08                        cmp rcx, qword ptr [rax]
009CD879  0F 9C C2                        setl dl
009CD87C  41 89 17                        mov dword ptr [r15], edx
009CD87F  E9 17 DB FF FF                  jmp 0x1409cb39b
009CD884  41 8B 0C 24                     mov ecx, dword ptr [r12]
009CD888  8B D6                           mov edx, esi
009CD88A  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD892  48 3B 08                        cmp rcx, qword ptr [rax]
009CD895  0F 97 C2                        seta dl
009CD898  41 89 17                        mov dword ptr [r15], edx
009CD89B  E9 FB DA FF FF                  jmp 0x1409cb39b
009CD8A0  41 8B 0C 24                     mov ecx, dword ptr [r12]
009CD8A4  8B D6                           mov edx, esi
009CD8A6  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD8AE  48 3B 08                        cmp rcx, qword ptr [rax]
009CD8B1  0F 92 C2                        setb dl
009CD8B4  41 89 17                        mov dword ptr [r15], edx
009CD8B7  E9 DF DA FF FF                  jmp 0x1409cb39b
009CD8BC  83 F9 07                        cmp ecx, 7
009CD8BF  0F 85 83 11 00 00               jne 0x1409cea48
009CD8C5  41 83 F9 02                     cmp r9d, 2
009CD8C9  0F 85 5F 17 00 00               jne 0x1409cf02e
009CD8CF  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD8D7  8B 08                           mov ecx, dword ptr [rax]
009CD8D9  0F 57 C9                        xorps xmm1, xmm1
009CD8DC  F3 48 0F 2A C9                  cvtsi2ss xmm1, rcx
009CD8E1  F3 41 0F 10 04 24               movss xmm0, dword ptr [r12]
009CD8E7  0F 2E C1                        ucomiss xmm0, xmm1
009CD8EA  E9 02 EC FF FF                  jmp 0x1409cc4f1
009CD8EF  83 F9 0C                        cmp ecx, 0xc
009CD8F2  0F 85 DE DA FF FF               jne 0x1409cb3d6
009CD8F8  41 83 F9 02                     cmp r9d, 2
009CD8FC  EB 0D                           jmp 0x1409cd90b
009CD8FE  41 83 F9 02                     cmp r9d, 2
009CD902  0F 85 72 24 00 00               jne 0x1409cfd7a
009CD908  45 85 C0                        test r8d, r8d
009CD90B  0F 85 C5 DA FF FF               jne 0x1409cb3d6
009CD911  44 3B 9C 24 90 00 00 00         cmp r11d, dword ptr [rsp + 0x90]
009CD919  0F 85 77 DA FF FF               jne 0x1409cb396
009CD91F  45 85 DB                        test r11d, r11d
009CD922  74 1B                           je 0x1409cd93f
009CD924  4D 8B C3                        mov r8, r11
009CD927  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
009CD92F  49 8B CC                        mov rcx, r12
009CD932  E8 D9 91 CF FF                  call 0x1406c6b10
009CD937  85 C0                           test eax, eax
009CD939  0F 85 57 DA FF FF               jne 0x1409cb396
009CD93F  B8 01 00 00 00                  mov eax, 1
009CD944  E9 4F DA FF FF                  jmp 0x1409cb398
009CD949  83 F9 17                        cmp ecx, 0x17
009CD94C  0F 85 84 DA FF FF               jne 0x1409cb3d6
009CD952  41 83 F9 02                     cmp r9d, 2
009CD956  0F 85 7A DA FF FF               jne 0x1409cb3d6
009CD95C  44 3B 9C 24 90 00 00 00         cmp r11d, dword ptr [rsp + 0x90]
009CD964  0F 85 2C DA FF FF               jne 0x1409cb396
009CD96A  45 85 DB                        test r11d, r11d
009CD96D  74 D0                           je 0x1409cd93f
009CD96F  4D 8B C3                        mov r8, r11
009CD972  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
009CD97A  49 8B CC                        mov rcx, r12
009CD97D  E8 8E 91 CF FF                  call 0x1406c6b10
009CD982  85 C0                           test eax, eax
009CD984  0F 85 0C DA FF FF               jne 0x1409cb396
009CD98A  B8 01 00 00 00                  mov eax, 1
009CD98F  E9 04 DA FF FF                  jmp 0x1409cb398
009CD994  41 83 F9 01                     cmp r9d, 1
009CD998  0F 85 38 DA FF FF               jne 0x1409cb3d6
009CD99E  41 8B 0C 24                     mov ecx, dword ptr [r12]
009CD9A2  8B D6                           mov edx, esi
009CD9A4  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD9AC  48 3B 08                        cmp rcx, qword ptr [rax]
009CD9AF  0F 9E C2                        setle dl
009CD9B2  41 89 17                        mov dword ptr [r15], edx
009CD9B5  E9 E1 D9 FF FF                  jmp 0x1409cb39b
009CD9BA  41 83 F9 01                     cmp r9d, 1
009CD9BE  0F 85 12 DA FF FF               jne 0x1409cb3d6
009CD9C4  41 8B 0C 24                     mov ecx, dword ptr [r12]
009CD9C8  8B D6                           mov edx, esi
009CD9CA  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CD9D2  48 3B 08                        cmp rcx, qword ptr [rax]
009CD9D5  0F 96 C2                        setbe dl
009CD9D8  41 89 17                        mov dword ptr [r15], edx
009CD9DB  E9 BB D9 FF FF                  jmp 0x1409cb39b
009CD9E0  83 C1 FE                        add ecx, -2
009CD9E3  83 F9 0D                        cmp ecx, 0xd
009CD9E6  0F 87 EA D9 FF FF               ja 0x1409cb3d6
009CD9EC  8B 8C 8A E8 FF 9C 00            mov ecx, dword ptr [rdx + rcx*4 + 0x9cffe8]
009CD9F3  48 03 CA                        add rcx, rdx
009CD9F6  FF E1                           jmp rcx
009CD9F8  CC                              int3
009CD9F9  CC                              int3
009CD9FA  CC                              int3
009CD9FB  CC                              int3
009CD9FC  41 83 E9 02                     sub r9d, 2
009CDA00  0F 84 02 23 00 00               je 0x1409cfd08
009CDA06  41 83 E9 01                     sub r9d, 1
009CDA0A  0F 84 1D 02 00 00               je 0x1409cdc2d
009CDA10  41 83 E9 01                     sub r9d, 1
009CDA14  0F 84 F8 01 00 00               je 0x1409cdc12
009CDA1A  41 83 E9 01                     sub r9d, 1
009CDA1E  0F 84 D3 01 00 00               je 0x1409cdbf7
009CDA24  41 83 F9 01                     cmp r9d, 1
009CDA28  0F 85 A8 D9 FF FF               jne 0x1409cb3d6
009CDA2E  8B D6                           mov edx, esi
009CDA30  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDA38  8B 08                           mov ecx, dword ptr [rax]
009CDA3A  41 39 0C 24                     cmp dword ptr [r12], ecx
009CDA3E  0F 96 C2                        setbe dl
009CDA41  41 89 17                        mov dword ptr [r15], edx
009CDA44  E9 52 D9 FF FF                  jmp 0x1409cb39b
009CDA49  41 81 FA 12 20 00 00            cmp r10d, 0x2012
009CDA50  0F 84 00 D9 FF FF               je 0x1409cb356
009CDA56  41 83 FA 12                     cmp r10d, 0x12
009CDA5A  0F 84 F6 D8 FF FF               je 0x1409cb356
009CDA60  41 83 FA 19                     cmp r10d, 0x19
009CDA64  0F 84 EC D8 FF FF               je 0x1409cb356
009CDA6A  BF BB 00 00 C0                  mov edi, 0xc00000bb
009CDA6F  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
009CDA73  E9 A2 23 00 00                  jmp 0x1409cfe1a
009CDA78  41 0F BE 0C 24                  movsx ecx, byte ptr [r12]
009CDA7D  8B D6                           mov edx, esi
009CDA7F  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDA87  3B 08                           cmp ecx, dword ptr [rax]
009CDA89  0F 94 C2                        sete dl
009CDA8C  41 89 17                        mov dword ptr [r15], edx
009CDA8F  E9 07 D9 FF FF                  jmp 0x1409cb39b
009CDA94  49 0F BE 0C 24                  movsx rcx, byte ptr [r12]
009CDA99  8B D6                           mov edx, esi
009CDA9B  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDAA3  48 3B 08                        cmp rcx, qword ptr [rax]
009CDAA6  0F 94 C2                        sete dl
009CDAA9  41 89 17                        mov dword ptr [r15], edx
009CDAAC  E9 EA D8 FF FF                  jmp 0x1409cb39b
009CDAB1  41 0F B6 0C 24                  movzx ecx, byte ptr [r12]
009CDAB6  8B D6                           mov edx, esi
009CDAB8  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDAC0  3B 08                           cmp ecx, dword ptr [rax]
009CDAC2  0F 94 C2                        sete dl
009CDAC5  41 89 17                        mov dword ptr [r15], edx
009CDAC8  E9 CE D8 FF FF                  jmp 0x1409cb39b
009CDACD  41 0F B6 0C 24                  movzx ecx, byte ptr [r12]
009CDAD2  8B D6                           mov edx, esi
009CDAD4  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDADC  48 3B 08                        cmp rcx, qword ptr [rax]
009CDADF  0F 94 C2                        sete dl
009CDAE2  41 89 17                        mov dword ptr [r15], edx
009CDAE5  E9 B1 D8 FF FF                  jmp 0x1409cb39b
009CDAEA  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDAF2  0F B6 08                        movzx ecx, byte ptr [rax]
009CDAF5  8B C6                           mov eax, esi
009CDAF7  66 41 39 0C 24                  cmp word ptr [r12], cx
009CDAFC  0F 94 C0                        sete al
009CDAFF  E9 94 D8 FF FF                  jmp 0x1409cb398
009CDB04  8B D6                           mov edx, esi
009CDB06  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDB0E  0F B7 08                        movzx ecx, word ptr [rax]
009CDB11  66 41 39 0C 24                  cmp word ptr [r12], cx
009CDB16  0F 94 C2                        sete dl
009CDB19  41 89 17                        mov dword ptr [r15], edx
009CDB1C  E9 7A D8 FF FF                  jmp 0x1409cb39b
009CDB21  41 0F BF 0C 24                  movsx ecx, word ptr [r12]
009CDB26  8B D6                           mov edx, esi
009CDB28  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDB30  3B 08                           cmp ecx, dword ptr [rax]
009CDB32  0F 94 C2                        sete dl
009CDB35  41 89 17                        mov dword ptr [r15], edx
009CDB38  E9 5E D8 FF FF                  jmp 0x1409cb39b
009CDB3D  49 0F BF 0C 24                  movsx rcx, word ptr [r12]
009CDB42  8B D6                           mov edx, esi
009CDB44  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDB4C  48 3B 08                        cmp rcx, qword ptr [rax]
009CDB4F  0F 94 C2                        sete dl
009CDB52  41 89 17                        mov dword ptr [r15], edx
009CDB55  E9 41 D8 FF FF                  jmp 0x1409cb39b
009CDB5A  41 0F B7 0C 24                  movzx ecx, word ptr [r12]
009CDB5F  8B D6                           mov edx, esi
009CDB61  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDB69  3B 08                           cmp ecx, dword ptr [rax]
009CDB6B  0F 94 C2                        sete dl
009CDB6E  41 89 17                        mov dword ptr [r15], edx
009CDB71  E9 25 D8 FF FF                  jmp 0x1409cb39b
009CDB76  41 0F B7 0C 24                  movzx ecx, word ptr [r12]
009CDB7B  8B D6                           mov edx, esi
009CDB7D  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDB85  48 3B 08                        cmp rcx, qword ptr [rax]
009CDB88  0F 94 C2                        sete dl
009CDB8B  41 89 17                        mov dword ptr [r15], edx
009CDB8E  E9 08 D8 FF FF                  jmp 0x1409cb39b
009CDB93  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDB9B  0F BE 08                        movsx ecx, byte ptr [rax]
009CDB9E  8B C6                           mov eax, esi
009CDBA0  41 39 0C 24                     cmp dword ptr [r12], ecx
009CDBA4  0F 94 C0                        sete al
009CDBA7  E9 EC D7 FF FF                  jmp 0x1409cb398
009CDBAC  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDBB4  0F B6 08                        movzx ecx, byte ptr [rax]
009CDBB7  8B C6                           mov eax, esi
009CDBB9  41 39 0C 24                     cmp dword ptr [r12], ecx
009CDBBD  0F 94 C0                        sete al
009CDBC0  E9 D3 D7 FF FF                  jmp 0x1409cb398
009CDBC5  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDBCD  0F BF 08                        movsx ecx, word ptr [rax]
009CDBD0  8B C6                           mov eax, esi
009CDBD2  41 39 0C 24                     cmp dword ptr [r12], ecx
009CDBD6  0F 94 C0                        sete al
009CDBD9  E9 BA D7 FF FF                  jmp 0x1409cb398
009CDBDE  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDBE6  0F B7 08                        movzx ecx, word ptr [rax]
009CDBE9  8B C6                           mov eax, esi
009CDBEB  41 39 0C 24                     cmp dword ptr [r12], ecx
009CDBEF  0F 94 C0                        sete al
009CDBF2  E9 A1 D7 FF FF                  jmp 0x1409cb398
009CDBF7  8B D6                           mov edx, esi
009CDBF9  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDC01  8B 08                           mov ecx, dword ptr [rax]
009CDC03  41 39 0C 24                     cmp dword ptr [r12], ecx
009CDC07  0F 93 C2                        setae dl
009CDC0A  41 89 17                        mov dword ptr [r15], edx
009CDC0D  E9 89 D7 FF FF                  jmp 0x1409cb39b
009CDC12  8B D6                           mov edx, esi
009CDC14  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDC1C  8B 08                           mov ecx, dword ptr [rax]
009CDC1E  41 39 0C 24                     cmp dword ptr [r12], ecx
009CDC22  0F 92 C2                        setb dl
009CDC25  41 89 17                        mov dword ptr [r15], edx
009CDC28  E9 6E D7 FF FF                  jmp 0x1409cb39b
009CDC2D  8B D6                           mov edx, esi
009CDC2F  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDC37  8B 08                           mov ecx, dword ptr [rax]
009CDC39  41 39 0C 24                     cmp dword ptr [r12], ecx
009CDC3D  0F 97 C2                        seta dl
009CDC40  41 89 17                        mov dword ptr [r15], edx
009CDC43  E9 53 D7 FF FF                  jmp 0x1409cb39b
009CDC48  49 63 0C 24                     movsxd rcx, dword ptr [r12]
009CDC4C  8B D6                           mov edx, esi
009CDC4E  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDC56  48 3B 08                        cmp rcx, qword ptr [rax]
009CDC59  0F 94 C2                        sete dl
009CDC5C  41 89 17                        mov dword ptr [r15], edx
009CDC5F  E9 37 D7 FF FF                  jmp 0x1409cb39b
009CDC64  41 83 E9 02                     sub r9d, 2
009CDC68  0F 84 3E FF FF FF               je 0x1409cdbac
009CDC6E  41 83 E9 01                     sub r9d, 1
009CDC72  74 61                           je 0x1409cdcd5
009CDC74  41 83 E9 01                     sub r9d, 1
009CDC78  74 42                           je 0x1409cdcbc
009CDC7A  41 83 E9 01                     sub r9d, 1
009CDC7E  74 23                           je 0x1409cdca3
009CDC80  41 83 F9 01                     cmp r9d, 1
009CDC84  0F 85 4C D7 FF FF               jne 0x1409cb3d6
009CDC8A  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDC92  0F B6 08                        movzx ecx, byte ptr [rax]
009CDC95  8B C6                           mov eax, esi
009CDC97  41 39 0C 24                     cmp dword ptr [r12], ecx
009CDC9B  0F 96 C0                        setbe al
009CDC9E  E9 F5 D6 FF FF                  jmp 0x1409cb398
009CDCA3  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDCAB  0F B6 08                        movzx ecx, byte ptr [rax]
009CDCAE  8B C6                           mov eax, esi
009CDCB0  41 39 0C 24                     cmp dword ptr [r12], ecx
009CDCB4  0F 93 C0                        setae al
009CDCB7  E9 DC D6 FF FF                  jmp 0x1409cb398
009CDCBC  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDCC4  0F B6 08                        movzx ecx, byte ptr [rax]
009CDCC7  8B C6                           mov eax, esi
009CDCC9  41 39 0C 24                     cmp dword ptr [r12], ecx
009CDCCD  0F 92 C0                        setb al
009CDCD0  E9 C3 D6 FF FF                  jmp 0x1409cb398
009CDCD5  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDCDD  0F B6 08                        movzx ecx, byte ptr [rax]
009CDCE0  8B C6                           mov eax, esi
009CDCE2  41 39 0C 24                     cmp dword ptr [r12], ecx
009CDCE6  0F 97 C0                        seta al
009CDCE9  E9 AA D6 FF FF                  jmp 0x1409cb398
009CDCEE  41 83 E9 02                     sub r9d, 2
009CDCF2  0F 84 CD FE FF FF               je 0x1409cdbc5
009CDCF8  41 83 E9 01                     sub r9d, 1
009CDCFC  74 61                           je 0x1409cdd5f
009CDCFE  41 83 E9 01                     sub r9d, 1
009CDD02  74 42                           je 0x1409cdd46
009CDD04  41 83 E9 01                     sub r9d, 1
009CDD08  74 23                           je 0x1409cdd2d
009CDD0A  41 83 F9 01                     cmp r9d, 1
009CDD0E  0F 85 C2 D6 FF FF               jne 0x1409cb3d6
009CDD14  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDD1C  0F BF 08                        movsx ecx, word ptr [rax]
009CDD1F  8B C6                           mov eax, esi
009CDD21  41 39 0C 24                     cmp dword ptr [r12], ecx
009CDD25  0F 96 C0                        setbe al
009CDD28  E9 6B D6 FF FF                  jmp 0x1409cb398
009CDD2D  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDD35  0F BF 08                        movsx ecx, word ptr [rax]
009CDD38  8B C6                           mov eax, esi
009CDD3A  41 39 0C 24                     cmp dword ptr [r12], ecx
009CDD3E  0F 93 C0                        setae al
009CDD41  E9 52 D6 FF FF                  jmp 0x1409cb398
009CDD46  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDD4E  0F BF 08                        movsx ecx, word ptr [rax]
009CDD51  8B C6                           mov eax, esi
009CDD53  41 39 0C 24                     cmp dword ptr [r12], ecx
009CDD57  0F 92 C0                        setb al
009CDD5A  E9 39 D6 FF FF                  jmp 0x1409cb398
009CDD5F  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDD67  0F BF 08                        movsx ecx, word ptr [rax]
009CDD6A  8B C6                           mov eax, esi
009CDD6C  41 39 0C 24                     cmp dword ptr [r12], ecx
009CDD70  0F 97 C0                        seta al
009CDD73  E9 20 D6 FF FF                  jmp 0x1409cb398
009CDD78  41 83 E9 02                     sub r9d, 2
009CDD7C  0F 84 5C FE FF FF               je 0x1409cdbde
009CDD82  41 83 E9 01                     sub r9d, 1
009CDD86  74 61                           je 0x1409cdde9
009CDD88  41 83 E9 01                     sub r9d, 1
009CDD8C  74 42                           je 0x1409cddd0
009CDD8E  41 83 E9 01                     sub r9d, 1
009CDD92  74 23                           je 0x1409cddb7
009CDD94  41 83 F9 01                     cmp r9d, 1
009CDD98  0F 85 38 D6 FF FF               jne 0x1409cb3d6
009CDD9E  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDDA6  0F B7 08                        movzx ecx, word ptr [rax]
009CDDA9  8B C6                           mov eax, esi
009CDDAB  41 39 0C 24                     cmp dword ptr [r12], ecx
009CDDAF  0F 96 C0                        setbe al
009CDDB2  E9 E1 D5 FF FF                  jmp 0x1409cb398
009CDDB7  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDDBF  0F B7 08                        movzx ecx, word ptr [rax]
009CDDC2  8B C6                           mov eax, esi
009CDDC4  41 39 0C 24                     cmp dword ptr [r12], ecx
009CDDC8  0F 93 C0                        setae al
009CDDCB  E9 C8 D5 FF FF                  jmp 0x1409cb398
009CDDD0  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDDD8  0F B7 08                        movzx ecx, word ptr [rax]
009CDDDB  8B C6                           mov eax, esi
009CDDDD  41 39 0C 24                     cmp dword ptr [r12], ecx
009CDDE1  0F 92 C0                        setb al
009CDDE4  E9 AF D5 FF FF                  jmp 0x1409cb398
009CDDE9  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDDF1  0F B7 08                        movzx ecx, word ptr [rax]
009CDDF4  8B C6                           mov eax, esi
009CDDF6  41 39 0C 24                     cmp dword ptr [r12], ecx
009CDDFA  0F 97 C0                        seta al
009CDDFD  E9 96 D5 FF FF                  jmp 0x1409cb398
009CDE02  41 8B 04 24                     mov eax, dword ptr [r12]
009CDE06  0F 57 C0                        xorps xmm0, xmm0
009CDE09  F3 48 0F 2A C0                  cvtsi2ss xmm0, rax
009CDE0E  E9 B4 DC FF FF                  jmp 0x1409cbac7
009CDE13  41 8B 04 24                     mov eax, dword ptr [r12]
009CDE17  0F 57 C0                        xorps xmm0, xmm0
009CDE1A  F3 48 0F 2A C0                  cvtsi2ss xmm0, rax
009CDE1F  E9 EF E6 FF FF                  jmp 0x1409cc513
009CDE24  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDE2C  0F BE 08                        movsx ecx, byte ptr [rax]
009CDE2F  8B C6                           mov eax, esi
009CDE31  41 39 0C 24                     cmp dword ptr [r12], ecx
009CDE35  0F 97 C0                        seta al
009CDE38  E9 5B D5 FF FF                  jmp 0x1409cb398
009CDE3D  41 8B 04 24                     mov eax, dword ptr [r12]
009CDE41  0F 57 C0                        xorps xmm0, xmm0
009CDE44  F2 48 0F 2A C0                  cvtsi2sd xmm0, rax
009CDE49  E9 6B D7 FF FF                  jmp 0x1409cb5b9
009CDE4E  41 8B 04 24                     mov eax, dword ptr [r12]
009CDE52  0F 57 C0                        xorps xmm0, xmm0
009CDE55  F2 48 0F 2A C0                  cvtsi2sd xmm0, rax
009CDE5A  E9 2A E7 FF FF                  jmp 0x1409cc589
009CDE5F  41 8B 0C 24                     mov ecx, dword ptr [r12]
009CDE63  8B D6                           mov edx, esi
009CDE65  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDE6D  48 3B 08                        cmp rcx, qword ptr [rax]
009CDE70  0F 94 C2                        sete dl
009CDE73  41 89 17                        mov dword ptr [r15], edx
009CDE76  E9 20 D5 FF FF                  jmp 0x1409cb39b
009CDE7B  83 F9 07                        cmp ecx, 7
009CDE7E  0F 85 52 D5 FF FF               jne 0x1409cb3d6
009CDE84  41 8B 0C 24                     mov ecx, dword ptr [r12]
009CDE88  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDE90  8B 10                           mov edx, dword ptr [rax]
009CDE92  41 83 F9 07                     cmp r9d, 7
009CDE96  75 07                           jne 0x1409cde9f
009CDE98  23 CA                           and ecx, edx
009CDE9A  E9 D6 D8 FF FF                  jmp 0x1409cb775
009CDE9F  0B CA                           or ecx, edx
009CDEA1  E9 CF D8 FF FF                  jmp 0x1409cb775
009CDEA6  83 C1 FE                        add ecx, -2
009CDEA9  83 F9 0D                        cmp ecx, 0xd
009CDEAC  0F 87 24 D5 FF FF               ja 0x1409cb3d6
009CDEB2  8B 8C 8A 20 00 9D 00            mov ecx, dword ptr [rdx + rcx*4 + 0x9d0020]
009CDEB9  48 03 CA                        add rcx, rdx
009CDEBC  FF E1                           jmp rcx
009CDEBE  CC                              int3
009CDEBF  CC                              int3
009CDEC0  CC                              int3
009CDEC1  CC                              int3
009CDEC2  41 83 E9 02                     sub r9d, 2
009CDEC6  0F 84 40 01 00 00               je 0x1409ce00c
009CDECC  41 83 E9 01                     sub r9d, 1
009CDED0  0F 84 1D 01 00 00               je 0x1409cdff3
009CDED6  41 83 E9 01                     sub r9d, 1
009CDEDA  0F 84 FA 00 00 00               je 0x1409cdfda
009CDEE0  41 83 E9 01                     sub r9d, 1
009CDEE4  0F 84 D7 00 00 00               je 0x1409cdfc1
009CDEEA  41 83 F9 01                     cmp r9d, 1
009CDEEE  0F 85 E2 D4 FF FF               jne 0x1409cb3d6
009CDEF4  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDEFC  0F B6 08                        movzx ecx, byte ptr [rax]
009CDEFF  8B C6                           mov eax, esi
009CDF01  49 39 0C 24                     cmp qword ptr [r12], rcx
009CDF05  0F 9E C0                        setle al
009CDF08  E9 8B D4 FF FF                  jmp 0x1409cb398
009CDF0D  41 83 E9 02                     sub r9d, 2
009CDF11  0F 84 90 00 00 00               je 0x1409cdfa7
009CDF17  41 83 E9 01                     sub r9d, 1
009CDF1B  74 70                           je 0x1409cdf8d
009CDF1D  41 83 E9 01                     sub r9d, 1
009CDF21  74 50                           je 0x1409cdf73
009CDF23  41 83 E9 01                     sub r9d, 1
009CDF27  74 30                           je 0x1409cdf59
009CDF29  41 83 F9 01                     cmp r9d, 1
009CDF2D  0F 85 A3 D4 FF FF               jne 0x1409cb3d6
009CDF33  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDF3B  48 0F BE 08                     movsx rcx, byte ptr [rax]
009CDF3F  EB 0A                           jmp 0x1409cdf4b
009CDF41  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDF49  8B 08                           mov ecx, dword ptr [rax]
009CDF4B  8B C6                           mov eax, esi
009CDF4D  49 39 0C 24                     cmp qword ptr [r12], rcx
009CDF51  0F 9E C0                        setle al
009CDF54  E9 3F D4 FF FF                  jmp 0x1409cb398
009CDF59  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDF61  48 0F BE 08                     movsx rcx, byte ptr [rax]
009CDF65  8B C6                           mov eax, esi
009CDF67  49 39 0C 24                     cmp qword ptr [r12], rcx
009CDF6B  0F 9D C0                        setge al
009CDF6E  E9 25 D4 FF FF                  jmp 0x1409cb398
009CDF73  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDF7B  48 0F BE 08                     movsx rcx, byte ptr [rax]
009CDF7F  8B C6                           mov eax, esi
009CDF81  49 39 0C 24                     cmp qword ptr [r12], rcx
009CDF85  0F 9C C0                        setl al
009CDF88  E9 0B D4 FF FF                  jmp 0x1409cb398
009CDF8D  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDF95  48 0F BE 08                     movsx rcx, byte ptr [rax]
009CDF99  8B C6                           mov eax, esi
009CDF9B  49 39 0C 24                     cmp qword ptr [r12], rcx
009CDF9F  0F 9F C0                        setg al
009CDFA2  E9 F1 D3 FF FF                  jmp 0x1409cb398
009CDFA7  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDFAF  48 0F BE 08                     movsx rcx, byte ptr [rax]
009CDFB3  8B C6                           mov eax, esi
009CDFB5  49 39 0C 24                     cmp qword ptr [r12], rcx
009CDFB9  0F 94 C0                        sete al
009CDFBC  E9 D7 D3 FF FF                  jmp 0x1409cb398
009CDFC1  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDFC9  0F B6 08                        movzx ecx, byte ptr [rax]
009CDFCC  8B C6                           mov eax, esi
009CDFCE  49 39 0C 24                     cmp qword ptr [r12], rcx
009CDFD2  0F 9D C0                        setge al
009CDFD5  E9 BE D3 FF FF                  jmp 0x1409cb398
009CDFDA  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDFE2  0F B6 08                        movzx ecx, byte ptr [rax]
009CDFE5  8B C6                           mov eax, esi
009CDFE7  49 39 0C 24                     cmp qword ptr [r12], rcx
009CDFEB  0F 9C C0                        setl al
009CDFEE  E9 A5 D3 FF FF                  jmp 0x1409cb398
009CDFF3  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CDFFB  0F B6 08                        movzx ecx, byte ptr [rax]
009CDFFE  8B C6                           mov eax, esi
009CE000  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE004  0F 9F C0                        setg al
009CE007  E9 8C D3 FF FF                  jmp 0x1409cb398
009CE00C  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE014  0F B6 08                        movzx ecx, byte ptr [rax]
009CE017  8B C6                           mov eax, esi
009CE019  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE01D  0F 94 C0                        sete al
009CE020  E9 73 D3 FF FF                  jmp 0x1409cb398
009CE025  41 83 E9 02                     sub r9d, 2
009CE029  0F 84 84 00 00 00               je 0x1409ce0b3
009CE02F  41 83 E9 01                     sub r9d, 1
009CE033  74 64                           je 0x1409ce099
009CE035  41 83 E9 01                     sub r9d, 1
009CE039  74 44                           je 0x1409ce07f
009CE03B  41 83 E9 01                     sub r9d, 1
009CE03F  74 24                           je 0x1409ce065
009CE041  41 83 F9 01                     cmp r9d, 1
009CE045  0F 85 8B D3 FF FF               jne 0x1409cb3d6
009CE04B  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE053  48 0F BF 08                     movsx rcx, word ptr [rax]
009CE057  8B C6                           mov eax, esi
009CE059  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE05D  0F 9E C0                        setle al
009CE060  E9 33 D3 FF FF                  jmp 0x1409cb398
009CE065  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE06D  48 0F BF 08                     movsx rcx, word ptr [rax]
009CE071  8B C6                           mov eax, esi
009CE073  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE077  0F 9D C0                        setge al
009CE07A  E9 19 D3 FF FF                  jmp 0x1409cb398
009CE07F  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE087  48 0F BF 08                     movsx rcx, word ptr [rax]
009CE08B  8B C6                           mov eax, esi
009CE08D  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE091  0F 9C C0                        setl al
009CE094  E9 FF D2 FF FF                  jmp 0x1409cb398
009CE099  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE0A1  48 0F BF 08                     movsx rcx, word ptr [rax]
009CE0A5  8B C6                           mov eax, esi
009CE0A7  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE0AB  0F 9F C0                        setg al
009CE0AE  E9 E5 D2 FF FF                  jmp 0x1409cb398
009CE0B3  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE0BB  48 0F BF 08                     movsx rcx, word ptr [rax]
009CE0BF  8B C6                           mov eax, esi
009CE0C1  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE0C5  0F 94 C0                        sete al
009CE0C8  E9 CB D2 FF FF                  jmp 0x1409cb398
009CE0CD  41 83 E9 02                     sub r9d, 2
009CE0D1  0F 84 80 00 00 00               je 0x1409ce157
009CE0D7  41 83 E9 01                     sub r9d, 1
009CE0DB  74 61                           je 0x1409ce13e
009CE0DD  41 83 E9 01                     sub r9d, 1
009CE0E1  74 42                           je 0x1409ce125
009CE0E3  41 83 E9 01                     sub r9d, 1
009CE0E7  74 23                           je 0x1409ce10c
009CE0E9  41 83 F9 01                     cmp r9d, 1
009CE0ED  0F 85 E3 D2 FF FF               jne 0x1409cb3d6
009CE0F3  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE0FB  0F B7 08                        movzx ecx, word ptr [rax]
009CE0FE  8B C6                           mov eax, esi
009CE100  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE104  0F 9E C0                        setle al
009CE107  E9 8C D2 FF FF                  jmp 0x1409cb398
009CE10C  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE114  0F B7 08                        movzx ecx, word ptr [rax]
009CE117  8B C6                           mov eax, esi
009CE119  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE11D  0F 9D C0                        setge al
009CE120  E9 73 D2 FF FF                  jmp 0x1409cb398
009CE125  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE12D  0F B7 08                        movzx ecx, word ptr [rax]
009CE130  8B C6                           mov eax, esi
009CE132  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE136  0F 9C C0                        setl al
009CE139  E9 5A D2 FF FF                  jmp 0x1409cb398
009CE13E  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE146  0F B7 08                        movzx ecx, word ptr [rax]
009CE149  8B C6                           mov eax, esi
009CE14B  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE14F  0F 9F C0                        setg al
009CE152  E9 41 D2 FF FF                  jmp 0x1409cb398
009CE157  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE15F  0F B7 08                        movzx ecx, word ptr [rax]
009CE162  8B C6                           mov eax, esi
009CE164  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE168  0F 94 C0                        sete al
009CE16B  E9 28 D2 FF FF                  jmp 0x1409cb398
009CE170  41 83 E9 02                     sub r9d, 2
009CE174  0F 84 80 00 00 00               je 0x1409ce1fa
009CE17A  41 83 E9 01                     sub r9d, 1
009CE17E  74 61                           je 0x1409ce1e1
009CE180  41 83 E9 01                     sub r9d, 1
009CE184  74 42                           je 0x1409ce1c8
009CE186  41 83 E9 01                     sub r9d, 1
009CE18A  74 23                           je 0x1409ce1af
009CE18C  41 83 F9 01                     cmp r9d, 1
009CE190  0F 85 40 D2 FF FF               jne 0x1409cb3d6
009CE196  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE19E  48 63 08                        movsxd rcx, dword ptr [rax]
009CE1A1  8B C6                           mov eax, esi
009CE1A3  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE1A7  0F 9E C0                        setle al
009CE1AA  E9 E9 D1 FF FF                  jmp 0x1409cb398
009CE1AF  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE1B7  48 63 08                        movsxd rcx, dword ptr [rax]
009CE1BA  8B C6                           mov eax, esi
009CE1BC  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE1C0  0F 9D C0                        setge al
009CE1C3  E9 D0 D1 FF FF                  jmp 0x1409cb398
009CE1C8  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE1D0  48 63 08                        movsxd rcx, dword ptr [rax]
009CE1D3  8B C6                           mov eax, esi
009CE1D5  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE1D9  0F 9C C0                        setl al
009CE1DC  E9 B7 D1 FF FF                  jmp 0x1409cb398
009CE1E1  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE1E9  48 63 08                        movsxd rcx, dword ptr [rax]
009CE1EC  8B C6                           mov eax, esi
009CE1EE  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE1F2  0F 9F C0                        setg al
009CE1F5  E9 9E D1 FF FF                  jmp 0x1409cb398
009CE1FA  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE202  48 63 08                        movsxd rcx, dword ptr [rax]
009CE205  8B C6                           mov eax, esi
009CE207  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE20B  0F 94 C0                        sete al
009CE20E  E9 85 D1 FF FF                  jmp 0x1409cb398
009CE213  41 83 E9 02                     sub r9d, 2
009CE217  74 7C                           je 0x1409ce295
009CE219  41 83 E9 01                     sub r9d, 1
009CE21D  74 5E                           je 0x1409ce27d
009CE21F  41 83 E9 01                     sub r9d, 1
009CE223  74 40                           je 0x1409ce265
009CE225  41 83 E9 01                     sub r9d, 1
009CE229  74 22                           je 0x1409ce24d
009CE22B  41 83 F9 01                     cmp r9d, 1
009CE22F  0F 85 A1 D1 FF FF               jne 0x1409cb3d6
009CE235  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE23D  8B 08                           mov ecx, dword ptr [rax]
009CE23F  8B C6                           mov eax, esi
009CE241  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE245  0F 9E C0                        setle al
009CE248  E9 4B D1 FF FF                  jmp 0x1409cb398
009CE24D  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE255  8B 08                           mov ecx, dword ptr [rax]
009CE257  8B C6                           mov eax, esi
009CE259  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE25D  0F 9D C0                        setge al
009CE260  E9 33 D1 FF FF                  jmp 0x1409cb398
009CE265  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE26D  8B 08                           mov ecx, dword ptr [rax]
009CE26F  8B C6                           mov eax, esi
009CE271  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE275  0F 9C C0                        setl al
009CE278  E9 1B D1 FF FF                  jmp 0x1409cb398
009CE27D  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE285  8B 08                           mov ecx, dword ptr [rax]
009CE287  8B C6                           mov eax, esi
009CE289  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE28D  0F 9F C0                        setg al
009CE290  E9 03 D1 FF FF                  jmp 0x1409cb398
009CE295  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE29D  8B 08                           mov ecx, dword ptr [rax]
009CE29F  8B C6                           mov eax, esi
009CE2A1  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE2A5  0F 94 C0                        sete al
009CE2A8  E9 EB D0 FF FF                  jmp 0x1409cb398
009CE2AD  41 83 E9 02                     sub r9d, 2
009CE2B1  0F 84 8C 00 00 00               je 0x1409ce343
009CE2B7  41 83 E9 01                     sub r9d, 1
009CE2BB  74 6A                           je 0x1409ce327
009CE2BD  41 83 E9 01                     sub r9d, 1
009CE2C1  74 48                           je 0x1409ce30b
009CE2C3  41 83 E9 01                     sub r9d, 1
009CE2C7  74 26                           je 0x1409ce2ef
009CE2C9  41 83 F9 01                     cmp r9d, 1
009CE2CD  0F 85 03 D1 FF FF               jne 0x1409cb3d6
009CE2D3  8B D6                           mov edx, esi
009CE2D5  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE2DD  48 8B 08                        mov rcx, qword ptr [rax]
009CE2E0  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE2E4  0F 9E C2                        setle dl
009CE2E7  41 89 17                        mov dword ptr [r15], edx
009CE2EA  E9 AC D0 FF FF                  jmp 0x1409cb39b
009CE2EF  8B D6                           mov edx, esi
009CE2F1  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE2F9  48 8B 08                        mov rcx, qword ptr [rax]
009CE2FC  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE300  0F 9D C2                        setge dl
009CE303  41 89 17                        mov dword ptr [r15], edx
009CE306  E9 90 D0 FF FF                  jmp 0x1409cb39b
009CE30B  8B D6                           mov edx, esi
009CE30D  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE315  48 8B 08                        mov rcx, qword ptr [rax]
009CE318  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE31C  0F 9C C2                        setl dl
009CE31F  41 89 17                        mov dword ptr [r15], edx
009CE322  E9 74 D0 FF FF                  jmp 0x1409cb39b
009CE327  8B D6                           mov edx, esi
009CE329  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE331  48 8B 08                        mov rcx, qword ptr [rax]
009CE334  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE338  0F 9F C2                        setg dl
009CE33B  41 89 17                        mov dword ptr [r15], edx
009CE33E  E9 58 D0 FF FF                  jmp 0x1409cb39b
009CE343  8B D6                           mov edx, esi
009CE345  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE34D  48 8B 08                        mov rcx, qword ptr [rax]
009CE350  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE354  0F 94 C2                        sete dl
009CE357  41 89 17                        mov dword ptr [r15], edx
009CE35A  E9 3C D0 FF FF                  jmp 0x1409cb39b
009CE35F  41 83 E9 02                     sub r9d, 2
009CE363  74 DE                           je 0x1409ce343
009CE365  41 83 E9 01                     sub r9d, 1
009CE369  74 6A                           je 0x1409ce3d5
009CE36B  41 83 E9 01                     sub r9d, 1
009CE36F  74 48                           je 0x1409ce3b9
009CE371  41 83 E9 01                     sub r9d, 1
009CE375  74 26                           je 0x1409ce39d
009CE377  41 83 F9 01                     cmp r9d, 1
009CE37B  0F 85 55 D0 FF FF               jne 0x1409cb3d6
009CE381  8B D6                           mov edx, esi
009CE383  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE38B  48 8B 08                        mov rcx, qword ptr [rax]
009CE38E  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE392  0F 96 C2                        setbe dl
009CE395  41 89 17                        mov dword ptr [r15], edx
009CE398  E9 FE CF FF FF                  jmp 0x1409cb39b
009CE39D  8B D6                           mov edx, esi
009CE39F  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE3A7  48 8B 08                        mov rcx, qword ptr [rax]
009CE3AA  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE3AE  0F 93 C2                        setae dl
009CE3B1  41 89 17                        mov dword ptr [r15], edx
009CE3B4  E9 E2 CF FF FF                  jmp 0x1409cb39b
009CE3B9  8B D6                           mov edx, esi
009CE3BB  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE3C3  48 8B 08                        mov rcx, qword ptr [rax]
009CE3C6  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE3CA  0F 92 C2                        setb dl
009CE3CD  41 89 17                        mov dword ptr [r15], edx
009CE3D0  E9 C6 CF FF FF                  jmp 0x1409cb39b
009CE3D5  8B D6                           mov edx, esi
009CE3D7  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE3DF  48 8B 08                        mov rcx, qword ptr [rax]
009CE3E2  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE3E6  0F 97 C2                        seta dl
009CE3E9  41 89 17                        mov dword ptr [r15], edx
009CE3EC  E9 AA CF FF FF                  jmp 0x1409cb39b
009CE3F1  41 83 E9 02                     sub r9d, 2
009CE3F5  74 54                           je 0x1409ce44b
009CE3F7  41 83 E9 01                     sub r9d, 1
009CE3FB  74 40                           je 0x1409ce43d
009CE3FD  41 83 E9 01                     sub r9d, 1
009CE401  74 2C                           je 0x1409ce42f
009CE403  41 83 E9 01                     sub r9d, 1
009CE407  74 18                           je 0x1409ce421
009CE409  41 83 F9 01                     cmp r9d, 1
009CE40D  0F 85 C3 CF FF FF               jne 0x1409cb3d6
009CE413  0F 57 C9                        xorps xmm1, xmm1
009CE416  F3 49 0F 2A 0C 24               cvtsi2ss xmm1, qword ptr [r12]
009CE41C  E9 49 E0 FF FF                  jmp 0x1409cc46a
009CE421  0F 57 C0                        xorps xmm0, xmm0
009CE424  F3 49 0F 2A 04 24               cvtsi2ss xmm0, qword ptr [r12]
009CE42A  E9 98 D6 FF FF                  jmp 0x1409cbac7
009CE42F  0F 57 C9                        xorps xmm1, xmm1
009CE432  F3 49 0F 2A 0C 24               cvtsi2ss xmm1, qword ptr [r12]
009CE438  E9 24 D3 FF FF                  jmp 0x1409cb761
009CE43D  0F 57 C0                        xorps xmm0, xmm0
009CE440  F3 49 0F 2A 04 24               cvtsi2ss xmm0, qword ptr [r12]
009CE446  E9 C8 E0 FF FF                  jmp 0x1409cc513
009CE44B  0F 57 C0                        xorps xmm0, xmm0
009CE44E  F3 49 0F 2A 04 24               cvtsi2ss xmm0, qword ptr [r12]
009CE454  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE45C  0F 2E 00                        ucomiss xmm0, dword ptr [rax]
009CE45F  E9 8D E0 FF FF                  jmp 0x1409cc4f1
009CE464  41 83 E9 02                     sub r9d, 2
009CE468  74 54                           je 0x1409ce4be
009CE46A  41 83 E9 01                     sub r9d, 1
009CE46E  74 40                           je 0x1409ce4b0
009CE470  41 83 E9 01                     sub r9d, 1
009CE474  74 2C                           je 0x1409ce4a2
009CE476  41 83 E9 01                     sub r9d, 1
009CE47A  74 18                           je 0x1409ce494
009CE47C  41 83 F9 01                     cmp r9d, 1
009CE480  0F 85 50 CF FF FF               jne 0x1409cb3d6
009CE486  0F 57 C9                        xorps xmm1, xmm1
009CE489  F2 49 0F 2A 0C 24               cvtsi2sd xmm1, qword ptr [r12]
009CE48F  E9 99 D1 FF FF                  jmp 0x1409cb62d
009CE494  0F 57 C0                        xorps xmm0, xmm0
009CE497  F2 49 0F 2A 04 24               cvtsi2sd xmm0, qword ptr [r12]
009CE49D  E9 17 D1 FF FF                  jmp 0x1409cb5b9
009CE4A2  0F 57 C9                        xorps xmm1, xmm1
009CE4A5  F2 49 0F 2A 0C 24               cvtsi2sd xmm1, qword ptr [r12]
009CE4AB  E9 AF E0 FF FF                  jmp 0x1409cc55f
009CE4B0  0F 57 C0                        xorps xmm0, xmm0
009CE4B3  F2 49 0F 2A 04 24               cvtsi2sd xmm0, qword ptr [r12]
009CE4B9  E9 CB E0 FF FF                  jmp 0x1409cc589
009CE4BE  0F 57 C0                        xorps xmm0, xmm0
009CE4C1  F2 49 0F 2A 04 24               cvtsi2sd xmm0, qword ptr [r12]
009CE4C7  E9 64 E0 FF FF                  jmp 0x1409cc530
009CE4CC  41 83 E9 02                     sub r9d, 2
009CE4D0  0F 84 D1 FA FF FF               je 0x1409cdfa7
009CE4D6  41 83 E9 01                     sub r9d, 1
009CE4DA  74 64                           je 0x1409ce540
009CE4DC  41 83 E9 01                     sub r9d, 1
009CE4E0  74 44                           je 0x1409ce526
009CE4E2  41 83 E9 01                     sub r9d, 1
009CE4E6  74 24                           je 0x1409ce50c
009CE4E8  41 83 F9 01                     cmp r9d, 1
009CE4EC  0F 85 E4 CE FF FF               jne 0x1409cb3d6
009CE4F2  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE4FA  48 0F BE 08                     movsx rcx, byte ptr [rax]
009CE4FE  8B C6                           mov eax, esi
009CE500  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE504  0F 96 C0                        setbe al
009CE507  E9 8C CE FF FF                  jmp 0x1409cb398
009CE50C  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE514  48 0F BE 08                     movsx rcx, byte ptr [rax]
009CE518  8B C6                           mov eax, esi
009CE51A  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE51E  0F 93 C0                        setae al
009CE521  E9 72 CE FF FF                  jmp 0x1409cb398
009CE526  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE52E  48 0F BE 08                     movsx rcx, byte ptr [rax]
009CE532  8B C6                           mov eax, esi
009CE534  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE538  0F 92 C0                        setb al
009CE53B  E9 58 CE FF FF                  jmp 0x1409cb398
009CE540  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE548  48 0F BE 08                     movsx rcx, byte ptr [rax]
009CE54C  8B C6                           mov eax, esi
009CE54E  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE552  0F 97 C0                        seta al
009CE555  E9 3E CE FF FF                  jmp 0x1409cb398
009CE55A  41 83 E9 02                     sub r9d, 2
009CE55E  0F 84 A8 FA FF FF               je 0x1409ce00c
009CE564  41 83 E9 01                     sub r9d, 1
009CE568  74 61                           je 0x1409ce5cb
009CE56A  41 83 E9 01                     sub r9d, 1
009CE56E  74 42                           je 0x1409ce5b2
009CE570  41 83 E9 01                     sub r9d, 1
009CE574  74 23                           je 0x1409ce599
009CE576  41 83 F9 01                     cmp r9d, 1
009CE57A  0F 85 56 CE FF FF               jne 0x1409cb3d6
009CE580  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE588  0F B6 08                        movzx ecx, byte ptr [rax]
009CE58B  8B C6                           mov eax, esi
009CE58D  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE591  0F 96 C0                        setbe al
009CE594  E9 FF CD FF FF                  jmp 0x1409cb398
009CE599  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE5A1  0F B6 08                        movzx ecx, byte ptr [rax]
009CE5A4  8B C6                           mov eax, esi
009CE5A6  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE5AA  0F 93 C0                        setae al
009CE5AD  E9 E6 CD FF FF                  jmp 0x1409cb398
009CE5B2  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE5BA  0F B6 08                        movzx ecx, byte ptr [rax]
009CE5BD  8B C6                           mov eax, esi
009CE5BF  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE5C3  0F 92 C0                        setb al
009CE5C6  E9 CD CD FF FF                  jmp 0x1409cb398
009CE5CB  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE5D3  0F B6 08                        movzx ecx, byte ptr [rax]
009CE5D6  8B C6                           mov eax, esi
009CE5D8  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE5DC  0F 97 C0                        seta al
009CE5DF  E9 B4 CD FF FF                  jmp 0x1409cb398
009CE5E4  41 83 E9 02                     sub r9d, 2
009CE5E8  0F 84 C5 FA FF FF               je 0x1409ce0b3
009CE5EE  41 83 E9 01                     sub r9d, 1
009CE5F2  74 64                           je 0x1409ce658
009CE5F4  41 83 E9 01                     sub r9d, 1
009CE5F8  74 44                           je 0x1409ce63e
009CE5FA  41 83 E9 01                     sub r9d, 1
009CE5FE  74 24                           je 0x1409ce624
009CE600  41 83 F9 01                     cmp r9d, 1
009CE604  0F 85 CC CD FF FF               jne 0x1409cb3d6
009CE60A  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE612  48 0F BF 08                     movsx rcx, word ptr [rax]
009CE616  8B C6                           mov eax, esi
009CE618  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE61C  0F 96 C0                        setbe al
009CE61F  E9 74 CD FF FF                  jmp 0x1409cb398
009CE624  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE62C  48 0F BF 08                     movsx rcx, word ptr [rax]
009CE630  8B C6                           mov eax, esi
009CE632  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE636  0F 93 C0                        setae al
009CE639  E9 5A CD FF FF                  jmp 0x1409cb398
009CE63E  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE646  48 0F BF 08                     movsx rcx, word ptr [rax]
009CE64A  8B C6                           mov eax, esi
009CE64C  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE650  0F 92 C0                        setb al
009CE653  E9 40 CD FF FF                  jmp 0x1409cb398
009CE658  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE660  48 0F BF 08                     movsx rcx, word ptr [rax]
009CE664  8B C6                           mov eax, esi
009CE666  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE66A  0F 97 C0                        seta al
009CE66D  E9 26 CD FF FF                  jmp 0x1409cb398
009CE672  41 83 E9 02                     sub r9d, 2
009CE676  0F 84 DB FA FF FF               je 0x1409ce157
009CE67C  41 83 E9 01                     sub r9d, 1
009CE680  74 61                           je 0x1409ce6e3
009CE682  41 83 E9 01                     sub r9d, 1
009CE686  74 42                           je 0x1409ce6ca
009CE688  41 83 E9 01                     sub r9d, 1
009CE68C  74 23                           je 0x1409ce6b1
009CE68E  41 83 F9 01                     cmp r9d, 1
009CE692  0F 85 3E CD FF FF               jne 0x1409cb3d6
009CE698  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE6A0  0F B7 08                        movzx ecx, word ptr [rax]
009CE6A3  8B C6                           mov eax, esi
009CE6A5  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE6A9  0F 96 C0                        setbe al
009CE6AC  E9 E7 CC FF FF                  jmp 0x1409cb398
009CE6B1  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE6B9  0F B7 08                        movzx ecx, word ptr [rax]
009CE6BC  8B C6                           mov eax, esi
009CE6BE  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE6C2  0F 93 C0                        setae al
009CE6C5  E9 CE CC FF FF                  jmp 0x1409cb398
009CE6CA  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE6D2  0F B7 08                        movzx ecx, word ptr [rax]
009CE6D5  8B C6                           mov eax, esi
009CE6D7  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE6DB  0F 92 C0                        setb al
009CE6DE  E9 B5 CC FF FF                  jmp 0x1409cb398
009CE6E3  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE6EB  0F B7 08                        movzx ecx, word ptr [rax]
009CE6EE  8B C6                           mov eax, esi
009CE6F0  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE6F4  0F 97 C0                        seta al
009CE6F7  E9 9C CC FF FF                  jmp 0x1409cb398
009CE6FC  41 83 E9 02                     sub r9d, 2
009CE700  0F 84 F4 FA FF FF               je 0x1409ce1fa
009CE706  41 83 E9 01                     sub r9d, 1
009CE70A  74 61                           je 0x1409ce76d
009CE70C  41 83 E9 01                     sub r9d, 1
009CE710  74 42                           je 0x1409ce754
009CE712  41 83 E9 01                     sub r9d, 1
009CE716  74 23                           je 0x1409ce73b
009CE718  41 83 F9 01                     cmp r9d, 1
009CE71C  0F 85 B4 CC FF FF               jne 0x1409cb3d6
009CE722  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE72A  48 63 08                        movsxd rcx, dword ptr [rax]
009CE72D  8B C6                           mov eax, esi
009CE72F  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE733  0F 96 C0                        setbe al
009CE736  E9 5D CC FF FF                  jmp 0x1409cb398
009CE73B  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE743  48 63 08                        movsxd rcx, dword ptr [rax]
009CE746  8B C6                           mov eax, esi
009CE748  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE74C  0F 93 C0                        setae al
009CE74F  E9 44 CC FF FF                  jmp 0x1409cb398
009CE754  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE75C  48 63 08                        movsxd rcx, dword ptr [rax]
009CE75F  8B C6                           mov eax, esi
009CE761  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE765  0F 92 C0                        setb al
009CE768  E9 2B CC FF FF                  jmp 0x1409cb398
009CE76D  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE775  48 63 08                        movsxd rcx, dword ptr [rax]
009CE778  8B C6                           mov eax, esi
009CE77A  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE77E  0F 97 C0                        seta al
009CE781  E9 12 CC FF FF                  jmp 0x1409cb398
009CE786  41 83 E9 02                     sub r9d, 2
009CE78A  0F 84 05 FB FF FF               je 0x1409ce295
009CE790  41 83 E9 01                     sub r9d, 1
009CE794  74 5E                           je 0x1409ce7f4
009CE796  41 83 E9 01                     sub r9d, 1
009CE79A  74 40                           je 0x1409ce7dc
009CE79C  41 83 E9 01                     sub r9d, 1
009CE7A0  74 22                           je 0x1409ce7c4
009CE7A2  41 83 F9 01                     cmp r9d, 1
009CE7A6  0F 85 2A CC FF FF               jne 0x1409cb3d6
009CE7AC  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE7B4  8B 08                           mov ecx, dword ptr [rax]
009CE7B6  8B C6                           mov eax, esi
009CE7B8  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE7BC  0F 96 C0                        setbe al
009CE7BF  E9 D4 CB FF FF                  jmp 0x1409cb398
009CE7C4  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE7CC  8B 08                           mov ecx, dword ptr [rax]
009CE7CE  8B C6                           mov eax, esi
009CE7D0  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE7D4  0F 93 C0                        setae al
009CE7D7  E9 BC CB FF FF                  jmp 0x1409cb398
009CE7DC  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE7E4  8B 08                           mov ecx, dword ptr [rax]
009CE7E6  8B C6                           mov eax, esi
009CE7E8  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE7EC  0F 92 C0                        setb al
009CE7EF  E9 A4 CB FF FF                  jmp 0x1409cb398
009CE7F4  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE7FC  8B 08                           mov ecx, dword ptr [rax]
009CE7FE  8B C6                           mov eax, esi
009CE800  49 39 0C 24                     cmp qword ptr [r12], rcx
009CE804  0F 97 C0                        seta al
009CE807  E9 8C CB FF FF                  jmp 0x1409cb398
009CE80C  41 83 E9 02                     sub r9d, 2
009CE810  0F 84 E0 00 00 00               je 0x1409ce8f6
009CE816  41 83 E9 01                     sub r9d, 1
009CE81A  0F 84 A6 00 00 00               je 0x1409ce8c6
009CE820  41 83 E9 01                     sub r9d, 1
009CE824  74 70                           je 0x1409ce896
009CE826  41 83 E9 01                     sub r9d, 1
009CE82A  74 3A                           je 0x1409ce866
009CE82C  41 83 F9 01                     cmp r9d, 1
009CE830  0F 85 A0 CB FF FF               jne 0x1409cb3d6
009CE836  49 8B 0C 24                     mov rcx, qword ptr [r12]
009CE83A  0F 57 C9                        xorps xmm1, xmm1
009CE83D  48 85 C9                        test rcx, rcx
009CE840  78 0A                           js 0x1409ce84c
009CE842  F3 48 0F 2A C9                  cvtsi2ss xmm1, rcx
009CE847  E9 1E DC FF FF                  jmp 0x1409cc46a
009CE84C  48 8B C1                        mov rax, rcx
009CE84F  48 D1 E8                        shr rax, 1
009CE852  83 E1 01                        and ecx, 1
009CE855  48 0B C1                        or rax, rcx
009CE858  F3 48 0F 2A C8                  cvtsi2ss xmm1, rax
009CE85D  F3 0F 58 C9                     addss xmm1, xmm1
009CE861  E9 04 DC FF FF                  jmp 0x1409cc46a
009CE866  49 8B 0C 24                     mov rcx, qword ptr [r12]
009CE86A  0F 57 C0                        xorps xmm0, xmm0
009CE86D  48 85 C9                        test rcx, rcx
009CE870  78 0A                           js 0x1409ce87c
009CE872  F3 48 0F 2A C1                  cvtsi2ss xmm0, rcx
009CE877  E9 4B D2 FF FF                  jmp 0x1409cbac7
009CE87C  48 8B C1                        mov rax, rcx
009CE87F  48 D1 E8                        shr rax, 1
009CE882  83 E1 01                        and ecx, 1
009CE885  48 0B C1                        or rax, rcx
009CE888  F3 48 0F 2A C0                  cvtsi2ss xmm0, rax
009CE88D  F3 0F 58 C0                     addss xmm0, xmm0
009CE891  E9 31 D2 FF FF                  jmp 0x1409cbac7
009CE896  49 8B 0C 24                     mov rcx, qword ptr [r12]
009CE89A  0F 57 C9                        xorps xmm1, xmm1
009CE89D  48 85 C9                        test rcx, rcx
009CE8A0  78 0A                           js 0x1409ce8ac
009CE8A2  F3 48 0F 2A C9                  cvtsi2ss xmm1, rcx
009CE8A7  E9 B5 CE FF FF                  jmp 0x1409cb761
009CE8AC  48 8B C1                        mov rax, rcx
009CE8AF  48 D1 E8                        shr rax, 1
009CE8B2  83 E1 01                        and ecx, 1
009CE8B5  48 0B C1                        or rax, rcx
009CE8B8  F3 48 0F 2A C8                  cvtsi2ss xmm1, rax
009CE8BD  F3 0F 58 C9                     addss xmm1, xmm1
009CE8C1  E9 9B CE FF FF                  jmp 0x1409cb761
009CE8C6  49 8B 0C 24                     mov rcx, qword ptr [r12]
009CE8CA  0F 57 C0                        xorps xmm0, xmm0
009CE8CD  48 85 C9                        test rcx, rcx
009CE8D0  78 0A                           js 0x1409ce8dc
009CE8D2  F3 48 0F 2A C1                  cvtsi2ss xmm0, rcx
009CE8D7  E9 37 DC FF FF                  jmp 0x1409cc513
009CE8DC  48 8B C1                        mov rax, rcx
009CE8DF  48 D1 E8                        shr rax, 1
009CE8E2  83 E1 01                        and ecx, 1
009CE8E5  48 0B C1                        or rax, rcx
009CE8E8  F3 48 0F 2A C0                  cvtsi2ss xmm0, rax
009CE8ED  F3 0F 58 C0                     addss xmm0, xmm0
009CE8F1  E9 1D DC FF FF                  jmp 0x1409cc513
009CE8F6  49 8B 0C 24                     mov rcx, qword ptr [r12]
009CE8FA  0F 57 C0                        xorps xmm0, xmm0
009CE8FD  48 85 C9                        test rcx, rcx
009CE900  78 07                           js 0x1409ce909
009CE902  F3 48 0F 2A C1                  cvtsi2ss xmm0, rcx
009CE907  EB 15                           jmp 0x1409ce91e
009CE909  48 8B C1                        mov rax, rcx
009CE90C  48 D1 E8                        shr rax, 1
009CE90F  83 E1 01                        and ecx, 1
009CE912  48 0B C1                        or rax, rcx
009CE915  F3 48 0F 2A C0                  cvtsi2ss xmm0, rax
009CE91A  F3 0F 58 C0                     addss xmm0, xmm0
009CE91E  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CE926  0F 2E 00                        ucomiss xmm0, dword ptr [rax]
009CE929  E9 C3 DB FF FF                  jmp 0x1409cc4f1
009CE92E  41 83 E9 02                     sub r9d, 2
009CE932  0F 84 E0 00 00 00               je 0x1409cea18
009CE938  41 83 E9 01                     sub r9d, 1
009CE93C  0F 84 A6 00 00 00               je 0x1409ce9e8
009CE942  41 83 E9 01                     sub r9d, 1
009CE946  74 70                           je 0x1409ce9b8
009CE948  41 83 E9 01                     sub r9d, 1
009CE94C  74 3A                           je 0x1409ce988
009CE94E  41 83 F9 01                     cmp r9d, 1
009CE952  0F 85 7E CA FF FF               jne 0x1409cb3d6
009CE958  49 8B 0C 24                     mov rcx, qword ptr [r12]
009CE95C  0F 57 C9                        xorps xmm1, xmm1
009CE95F  48 85 C9                        test rcx, rcx
009CE962  78 0A                           js 0x1409ce96e
009CE964  F2 48 0F 2A C9                  cvtsi2sd xmm1, rcx
009CE969  E9 BF CC FF FF                  jmp 0x1409cb62d
009CE96E  48 8B C1                        mov rax, rcx
009CE971  48 D1 E8                        shr rax, 1
009CE974  83 E1 01                        and ecx, 1
009CE977  48 0B C1                        or rax, rcx
009CE97A  F2 48 0F 2A C8                  cvtsi2sd xmm1, rax
009CE97F  F2 0F 58 C9                     addsd xmm1, xmm1
009CE983  E9 A5 CC FF FF                  jmp 0x1409cb62d
009CE988  49 8B 0C 24                     mov rcx, qword ptr [r12]
009CE98C  0F 57 C0                        xorps xmm0, xmm0
009CE98F  48 85 C9                        test rcx, rcx
009CE992  78 0A                           js 0x1409ce99e
009CE994  F2 48 0F 2A C1                  cvtsi2sd xmm0, rcx
009CE999  E9 1B CC FF FF                  jmp 0x1409cb5b9
009CE99E  48 8B C1                        mov rax, rcx
009CE9A1  48 D1 E8                        shr rax, 1
009CE9A4  83 E1 01                        and ecx, 1
009CE9A7  48 0B C1                        or rax, rcx
009CE9AA  F2 48 0F 2A C0                  cvtsi2sd xmm0, rax
009CE9AF  F2 0F 58 C0                     addsd xmm0, xmm0
009CE9B3  E9 01 CC FF FF                  jmp 0x1409cb5b9
009CE9B8  49 8B 0C 24                     mov rcx, qword ptr [r12]
009CE9BC  0F 57 C9                        xorps xmm1, xmm1
009CE9BF  48 85 C9                        test rcx, rcx
009CE9C2  78 0A                           js 0x1409ce9ce
009CE9C4  F2 48 0F 2A C9                  cvtsi2sd xmm1, rcx
009CE9C9  E9 91 DB FF FF                  jmp 0x1409cc55f
009CE9CE  48 8B C1                        mov rax, rcx
009CE9D1  48 D1 E8                        shr rax, 1
009CE9D4  83 E1 01                        and ecx, 1
009CE9D7  48 0B C1                        or rax, rcx
009CE9DA  F2 48 0F 2A C8                  cvtsi2sd xmm1, rax
009CE9DF  F2 0F 58 C9                     addsd xmm1, xmm1
009CE9E3  E9 77 DB FF FF                  jmp 0x1409cc55f
009CE9E8  49 8B 0C 24                     mov rcx, qword ptr [r12]
009CE9EC  0F 57 C0                        xorps xmm0, xmm0
009CE9EF  48 85 C9                        test rcx, rcx
009CE9F2  78 0A                           js 0x1409ce9fe
009CE9F4  F2 48 0F 2A C1                  cvtsi2sd xmm0, rcx
009CE9F9  E9 8B DB FF FF                  jmp 0x1409cc589
009CE9FE  48 8B C1                        mov rax, rcx
009CEA01  48 D1 E8                        shr rax, 1
009CEA04  83 E1 01                        and ecx, 1
009CEA07  48 0B C1                        or rax, rcx
009CEA0A  F2 48 0F 2A C0                  cvtsi2sd xmm0, rax
009CEA0F  F2 0F 58 C0                     addsd xmm0, xmm0
009CEA13  E9 71 DB FF FF                  jmp 0x1409cc589
009CEA18  49 8B 0C 24                     mov rcx, qword ptr [r12]
009CEA1C  0F 57 C0                        xorps xmm0, xmm0
009CEA1F  48 85 C9                        test rcx, rcx
009CEA22  78 0A                           js 0x1409cea2e
009CEA24  F2 48 0F 2A C1                  cvtsi2sd xmm0, rcx
009CEA29  E9 02 DB FF FF                  jmp 0x1409cc530
009CEA2E  48 8B C1                        mov rax, rcx
009CEA31  48 D1 E8                        shr rax, 1
009CEA34  83 E1 01                        and ecx, 1
009CEA37  48 0B C1                        or rax, rcx
009CEA3A  F2 48 0F 2A C0                  cvtsi2sd xmm0, rax
009CEA3F  F2 0F 58 C0                     addsd xmm0, xmm0
009CEA43  E9 E8 DA FF FF                  jmp 0x1409cc530
009CEA48  83 C1 FE                        add ecx, -2
009CEA4B  83 F9 0D                        cmp ecx, 0xd
009CEA4E  0F 87 82 C9 FF FF               ja 0x1409cb3d6
009CEA54  8B 8C 8A 58 00 9D 00            mov ecx, dword ptr [rdx + rcx*4 + 0x9d0058]
009CEA5B  48 03 CA                        add rcx, rdx
009CEA5E  FF E1                           jmp rcx
009CEA60  CC                              int3
009CEA61  CC                              int3
009CEA62  CC                              int3
009CEA63  CC                              int3
009CEA64  41 83 E9 02                     sub r9d, 2
009CEA68  0F 84 4C 01 00 00               je 0x1409cebba
009CEA6E  41 83 E9 01                     sub r9d, 1
009CEA72  0F 84 CF 00 00 00               je 0x1409ceb47
009CEA78  41 83 E9 01                     sub r9d, 1
009CEA7C  0F 84 A4 00 00 00               je 0x1409ceb26
009CEA82  41 83 E9 01                     sub r9d, 1
009CEA86  74 2B                           je 0x1409ceab3
009CEA88  41 83 F9 01                     cmp r9d, 1
009CEA8C  0F 85 44 C9 FF FF               jne 0x1409cb3d6
009CEA92  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CEA9A  0F BE 08                        movsx ecx, byte ptr [rax]
009CEA9D  66 0F 6E C1                     movd xmm0, ecx
009CEAA1  0F 5B C0                        cvtdq2ps xmm0, xmm0
009CEAA4  8B C6                           mov eax, esi
009CEAA6  41 0F 2F 04 24                  comiss xmm0, dword ptr [r12]
009CEAAB  0F 93 C0                        setae al
009CEAAE  E9 E5 C8 FF FF                  jmp 0x1409cb398
009CEAB3  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CEABB  0F BE 08                        movsx ecx, byte ptr [rax]
009CEABE  EB 0B                           jmp 0x1409ceacb
009CEAC0  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CEAC8  0F B7 08                        movzx ecx, word ptr [rax]
009CEACB  66 0F 6E C9                     movd xmm1, ecx
009CEACF  EB 0C                           jmp 0x1409ceadd
009CEAD1  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CEAD9  66 0F 6E 08                     movd xmm1, dword ptr [rax]
009CEADD  0F 5B C9                        cvtdq2ps xmm1, xmm1
009CEAE0  EB 15                           jmp 0x1409ceaf7
009CEAE2  48 8B C1                        mov rax, rcx
009CEAE5  48 D1 E8                        shr rax, 1
009CEAE8  83 E1 01                        and ecx, 1
009CEAEB  48 0B C1                        or rax, rcx
009CEAEE  F3 48 0F 2A C8                  cvtsi2ss xmm1, rax
009CEAF3  F3 0F 58 C9                     addss xmm1, xmm1
009CEAF7  F3 41 0F 10 04 24               movss xmm0, dword ptr [r12]
009CEAFD  0F 2F C1                        comiss xmm0, xmm1
009CEB00  EB 1A                           jmp 0x1409ceb1c
009CEB02  48 8B C1                        mov rax, rcx
009CEB05  48 D1 E8                        shr rax, 1
009CEB08  83 E1 01                        and ecx, 1
009CEB0B  48 0B C1                        or rax, rcx
009CEB0E  F3 48 0F 2A C0                  cvtsi2ss xmm0, rax
009CEB13  F3 0F 58 C0                     addss xmm0, xmm0
009CEB17  41 0F 2F 04 24                  comiss xmm0, dword ptr [r12]
009CEB1C  8B C6                           mov eax, esi
009CEB1E  0F 93 C0                        setae al
009CEB21  E9 72 C8 FF FF                  jmp 0x1409cb398
009CEB26  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CEB2E  0F BE 08                        movsx ecx, byte ptr [rax]
009CEB31  66 0F 6E C1                     movd xmm0, ecx
009CEB35  0F 5B C0                        cvtdq2ps xmm0, xmm0
009CEB38  8B C6                           mov eax, esi
009CEB3A  41 0F 2F 04 24                  comiss xmm0, dword ptr [r12]
009CEB3F  0F 97 C0                        seta al
009CEB42  E9 51 C8 FF FF                  jmp 0x1409cb398
009CEB47  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CEB4F  0F BE 08                        movsx ecx, byte ptr [rax]
009CEB52  EB 0B                           jmp 0x1409ceb5f
009CEB54  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CEB5C  0F B7 08                        movzx ecx, word ptr [rax]
009CEB5F  66 0F 6E C9                     movd xmm1, ecx
009CEB63  EB 0C                           jmp 0x1409ceb71
009CEB65  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CEB6D  66 0F 6E 08                     movd xmm1, dword ptr [rax]
009CEB71  0F 5B C9                        cvtdq2ps xmm1, xmm1
009CEB74  EB 15                           jmp 0x1409ceb8b
009CEB76  48 8B C1                        mov rax, rcx
009CEB79  48 D1 E8                        shr rax, 1
009CEB7C  83 E1 01                        and ecx, 1
009CEB7F  48 0B C1                        or rax, rcx
009CEB82  F3 48 0F 2A C8                  cvtsi2ss xmm1, rax
009CEB87  F3 0F 58 C9                     addss xmm1, xmm1
009CEB8B  F3 41 0F 10 04 24               movss xmm0, dword ptr [r12]
009CEB91  0F 2F C1                        comiss xmm0, xmm1
009CEB94  EB 1A                           jmp 0x1409cebb0
009CEB96  48 8B C1                        mov rax, rcx
009CEB99  48 D1 E8                        shr rax, 1
009CEB9C  83 E1 01                        and ecx, 1
009CEB9F  48 0B C1                        or rax, rcx
009CEBA2  F3 48 0F 2A C0                  cvtsi2ss xmm0, rax
009CEBA7  F3 0F 58 C0                     addss xmm0, xmm0
009CEBAB  41 0F 2F 04 24                  comiss xmm0, dword ptr [r12]
009CEBB0  8B C6                           mov eax, esi
009CEBB2  0F 97 C0                        seta al
009CEBB5  E9 DE C7 FF FF                  jmp 0x1409cb398
009CEBBA  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CEBC2  0F BE 08                        movsx ecx, byte ptr [rax]
009CEBC5  66 0F 6E C9                     movd xmm1, ecx
009CEBC9  0F 5B C9                        cvtdq2ps xmm1, xmm1
009CEBCC  E9 10 ED FF FF                  jmp 0x1409cd8e1
009CEBD1  41 83 E9 02                     sub r9d, 2
009CEBD5  74 74                           je 0x1409cec4b
009CEBD7  41 83 E9 01                     sub r9d, 1
009CEBDB  74 5E                           je 0x1409cec3b
009CEBDD  41 83 E9 01                     sub r9d, 1
009CEBE1  74 3C                           je 0x1409cec1f
009CEBE3  41 83 E9 01                     sub r9d, 1
009CEBE7  74 26                           je 0x1409cec0f
009CEBE9  41 83 F9 01                     cmp r9d, 1
009CEBED  0F 85 E3 C7 FF FF               jne 0x1409cb3d6
009CEBF3  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CEBFB  0F B6 08                        movzx ecx, byte ptr [rax]
009CEBFE  66 0F 6E C1                     movd xmm0, ecx
009CEC02  0F 5B C0                        cvtdq2ps xmm0, xmm0
009CEC05  41 0F 2F 04 24                  comiss xmm0, dword ptr [r12]
009CEC0A  E9 0D FF FF FF                  jmp 0x1409ceb1c
009CEC0F  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CEC17  0F B6 08                        movzx ecx, byte ptr [rax]
009CEC1A  E9 AC FE FF FF                  jmp 0x1409ceacb
009CEC1F  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CEC27  0F B6 08                        movzx ecx, byte ptr [rax]
009CEC2A  66 0F 6E C1                     movd xmm0, ecx
009CEC2E  0F 5B C0                        cvtdq2ps xmm0, xmm0
009CEC31  41 0F 2F 04 24                  comiss xmm0, dword ptr [r12]
009CEC36  E9 75 FF FF FF                  jmp 0x1409cebb0
009CEC3B  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CEC43  0F B6 08                        movzx ecx, byte ptr [rax]
009CEC46  E9 14 FF FF FF                  jmp 0x1409ceb5f
009CEC4B  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CEC53  0F B6 08                        movzx ecx, byte ptr [rax]
009CEC56  66 0F 6E C9                     movd xmm1, ecx
009CEC5A  0F 5B C9                        cvtdq2ps xmm1, xmm1
009CEC5D  E9 7F EC FF FF                  jmp 0x1409cd8e1
009CEC62  41 83 E9 02                     sub r9d, 2
009CEC66  74 74                           je 0x1409cecdc
009CEC68  41 83 E9 01                     sub r9d, 1
009CEC6C  74 5E                           je 0x1409ceccc
009CEC6E  41 83 E9 01                     sub r9d, 1
009CEC72  74 3C                           je 0x1409cecb0
009CEC74  41 83 E9 01                     sub r9d, 1
009CEC78  74 26                           je 0x1409ceca0
009CEC7A  41 83 F9 01                     cmp r9d, 1
009CEC7E  0F 85 52 C7 FF FF               jne 0x1409cb3d6
009CEC84  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CEC8C  0F BF 08                        movsx ecx, word ptr [rax]
009CEC8F  66 0F 6E C1                     movd xmm0, ecx
009CEC93  0F 5B C0                        cvtdq2ps xmm0, xmm0
009CEC96  41 0F 2F 04 24                  comiss xmm0, dword ptr [r12]
009CEC9B  E9 7C FE FF FF                  jmp 0x1409ceb1c
009CECA0  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CECA8  0F BF 08                        movsx ecx, word ptr [rax]
009CECAB  E9 1B FE FF FF                  jmp 0x1409ceacb
009CECB0  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CECB8  0F BF 08                        movsx ecx, word ptr [rax]
009CECBB  66 0F 6E C1                     movd xmm0, ecx
009CECBF  0F 5B C0                        cvtdq2ps xmm0, xmm0
009CECC2  41 0F 2F 04 24                  comiss xmm0, dword ptr [r12]
009CECC7  E9 E4 FE FF FF                  jmp 0x1409cebb0
009CECCC  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CECD4  0F BF 08                        movsx ecx, word ptr [rax]
009CECD7  E9 83 FE FF FF                  jmp 0x1409ceb5f
009CECDC  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CECE4  0F BF 08                        movsx ecx, word ptr [rax]
009CECE7  66 0F 6E C9                     movd xmm1, ecx
009CECEB  0F 5B C9                        cvtdq2ps xmm1, xmm1
009CECEE  E9 EE EB FF FF                  jmp 0x1409cd8e1
009CECF3  41 83 E9 02                     sub r9d, 2
009CECF7  74 5C                           je 0x1409ced55
009CECF9  41 83 E9 01                     sub r9d, 1
009CECFD  0F 84 51 FE FF FF               je 0x1409ceb54
009CED03  41 83 E9 01                     sub r9d, 1
009CED07  74 30                           je 0x1409ced39
009CED09  41 83 E9 01                     sub r9d, 1
009CED0D  0F 84 AD FD FF FF               je 0x1409ceac0
009CED13  41 83 F9 01                     cmp r9d, 1
009CED17  0F 85 B9 C6 FF FF               jne 0x1409cb3d6
009CED1D  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CED25  0F B7 08                        movzx ecx, word ptr [rax]
009CED28  66 0F 6E C1                     movd xmm0, ecx
009CED2C  0F 5B C0                        cvtdq2ps xmm0, xmm0
009CED2F  41 0F 2F 04 24                  comiss xmm0, dword ptr [r12]
009CED34  E9 E3 FD FF FF                  jmp 0x1409ceb1c
009CED39  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CED41  0F B7 08                        movzx ecx, word ptr [rax]
009CED44  66 0F 6E C1                     movd xmm0, ecx
009CED48  0F 5B C0                        cvtdq2ps xmm0, xmm0
009CED4B  41 0F 2F 04 24                  comiss xmm0, dword ptr [r12]
009CED50  E9 5B FE FF FF                  jmp 0x1409cebb0
009CED55  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CED5D  0F B7 08                        movzx ecx, word ptr [rax]
009CED60  66 0F 6E C9                     movd xmm1, ecx
009CED64  0F 5B C9                        cvtdq2ps xmm1, xmm1
009CED67  E9 75 EB FF FF                  jmp 0x1409cd8e1
009CED6C  41 83 E9 02                     sub r9d, 2
009CED70  74 56                           je 0x1409cedc8
009CED72  41 83 E9 01                     sub r9d, 1
009CED76  0F 84 E9 FD FF FF               je 0x1409ceb65
009CED7C  41 83 E9 01                     sub r9d, 1
009CED80  74 2D                           je 0x1409cedaf
009CED82  41 83 E9 01                     sub r9d, 1
009CED86  0F 84 45 FD FF FF               je 0x1409cead1
009CED8C  41 83 F9 01                     cmp r9d, 1
009CED90  0F 85 40 C6 FF FF               jne 0x1409cb3d6
009CED96  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CED9E  66 0F 6E 00                     movd xmm0, dword ptr [rax]
009CEDA2  0F 5B C0                        cvtdq2ps xmm0, xmm0
009CEDA5  41 0F 2F 04 24                  comiss xmm0, dword ptr [r12]
009CEDAA  E9 6D FD FF FF                  jmp 0x1409ceb1c
009CEDAF  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CEDB7  66 0F 6E 00                     movd xmm0, dword ptr [rax]
009CEDBB  0F 5B C0                        cvtdq2ps xmm0, xmm0
009CEDBE  41 0F 2F 04 24                  comiss xmm0, dword ptr [r12]
009CEDC3  E9 E8 FD FF FF                  jmp 0x1409cebb0
009CEDC8  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CEDD0  66 0F 6E 08                     movd xmm1, dword ptr [rax]
009CEDD4  0F 5B C9                        cvtdq2ps xmm1, xmm1
009CEDD7  E9 05 EB FF FF                  jmp 0x1409cd8e1
009CEDDC  41 83 E9 02                     sub r9d, 2
009CEDE0  74 7A                           je 0x1409cee5c
009CEDE2  41 83 E9 01                     sub r9d, 1
009CEDE6  74 5F                           je 0x1409cee47
009CEDE8  41 83 E9 01                     sub r9d, 1
009CEDEC  74 3F                           je 0x1409cee2d
009CEDEE  41 83 E9 01                     sub r9d, 1
009CEDF2  74 24                           je 0x1409cee18
009CEDF4  41 83 F9 01                     cmp r9d, 1
009CEDF8  0F 85 D8 C5 FF FF               jne 0x1409cb3d6
009CEDFE  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CEE06  0F 57 C0                        xorps xmm0, xmm0
009CEE09  F3 48 0F 2A 00                  cvtsi2ss xmm0, qword ptr [rax]
009CEE0E  41 0F 2F 04 24                  comiss xmm0, dword ptr [r12]
009CEE13  E9 04 FD FF FF                  jmp 0x1409ceb1c
009CEE18  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CEE20  0F 57 C9                        xorps xmm1, xmm1
009CEE23  F3 48 0F 2A 08                  cvtsi2ss xmm1, qword ptr [rax]
009CEE28  E9 CA FC FF FF                  jmp 0x1409ceaf7
009CEE2D  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CEE35  0F 57 C0                        xorps xmm0, xmm0
009CEE38  F3 48 0F 2A 00                  cvtsi2ss xmm0, qword ptr [rax]
009CEE3D  41 0F 2F 04 24                  comiss xmm0, dword ptr [r12]
009CEE42  E9 69 FD FF FF                  jmp 0x1409cebb0
009CEE47  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CEE4F  0F 57 C9                        xorps xmm1, xmm1
009CEE52  F3 48 0F 2A 08                  cvtsi2ss xmm1, qword ptr [rax]
009CEE57  E9 2F FD FF FF                  jmp 0x1409ceb8b
009CEE5C  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CEE64  0F 57 C9                        xorps xmm1, xmm1
009CEE67  F3 48 0F 2A 08                  cvtsi2ss xmm1, qword ptr [rax]
009CEE6C  E9 70 EA FF FF                  jmp 0x1409cd8e1
009CEE71  41 83 E9 02                     sub r9d, 2
009CEE75  0F 84 A0 00 00 00               je 0x1409cef1b
009CEE7B  41 83 E9 01                     sub r9d, 1
009CEE7F  74 79                           je 0x1409ceefa
009CEE81  41 83 E9 01                     sub r9d, 1
009CEE85  74 52                           je 0x1409ceed9
009CEE87  41 83 E9 01                     sub r9d, 1
009CEE8B  74 2B                           je 0x1409ceeb8
009CEE8D  41 83 F9 01                     cmp r9d, 1
009CEE91  0F 85 3F C5 FF FF               jne 0x1409cb3d6
009CEE97  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CEE9F  48 8B 08                        mov rcx, qword ptr [rax]
009CEEA2  0F 57 C0                        xorps xmm0, xmm0
009CEEA5  48 85 C9                        test rcx, rcx
009CEEA8  0F 88 54 FC FF FF               js 0x1409ceb02
009CEEAE  F3 48 0F 2A C1                  cvtsi2ss xmm0, rcx
009CEEB3  E9 5F FC FF FF                  jmp 0x1409ceb17
009CEEB8  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CEEC0  48 8B 08                        mov rcx, qword ptr [rax]
009CEEC3  0F 57 C9                        xorps xmm1, xmm1
009CEEC6  48 85 C9                        test rcx, rcx
009CEEC9  0F 88 13 FC FF FF               js 0x1409ceae2
009CEECF  F3 48 0F 2A C9                  cvtsi2ss xmm1, rcx
009CEED4  E9 1E FC FF FF                  jmp 0x1409ceaf7
009CEED9  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CEEE1  48 8B 08                        mov rcx, qword ptr [rax]
009CEEE4  0F 57 C0                        xorps xmm0, xmm0
009CEEE7  48 85 C9                        test rcx, rcx
009CEEEA  0F 88 A6 FC FF FF               js 0x1409ceb96
009CEEF0  F3 48 0F 2A C1                  cvtsi2ss xmm0, rcx
009CEEF5  E9 B1 FC FF FF                  jmp 0x1409cebab
009CEEFA  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CEF02  48 8B 08                        mov rcx, qword ptr [rax]
009CEF05  0F 57 C9                        xorps xmm1, xmm1
009CEF08  48 85 C9                        test rcx, rcx
009CEF0B  0F 88 65 FC FF FF               js 0x1409ceb76
009CEF11  F3 48 0F 2A C9                  cvtsi2ss xmm1, rcx
009CEF16  E9 70 FC FF FF                  jmp 0x1409ceb8b
009CEF1B  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CEF23  48 8B 08                        mov rcx, qword ptr [rax]
009CEF26  0F 57 C9                        xorps xmm1, xmm1
009CEF29  48 85 C9                        test rcx, rcx
009CEF2C  0F 89 AA E9 FF FF               jns 0x1409cd8dc
009CEF32  48 8B C1                        mov rax, rcx
009CEF35  48 D1 E8                        shr rax, 1
009CEF38  83 E1 01                        and ecx, 1
009CEF3B  48 0B C1                        or rax, rcx
009CEF3E  F3 48 0F 2A C8                  cvtsi2ss xmm1, rax
009CEF43  F3 0F 58 C9                     addss xmm1, xmm1
009CEF47  E9 95 E9 FF FF                  jmp 0x1409cd8e1
009CEF4C  41 83 E9 02                     sub r9d, 2
009CEF50  74 5E                           je 0x1409cefb0
009CEF52  41 83 E9 01                     sub r9d, 1
009CEF56  74 4D                           je 0x1409cefa5
009CEF58  41 83 E9 01                     sub r9d, 1
009CEF5C  74 31                           je 0x1409cef8f
009CEF5E  41 83 E9 01                     sub r9d, 1
009CEF62  74 20                           je 0x1409cef84
009CEF64  41 83 F9 01                     cmp r9d, 1
009CEF68  0F 85 68 C4 FF FF               jne 0x1409cb3d6
009CEF6E  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CEF76  F3 0F 10 00                     movss xmm0, dword ptr [rax]
009CEF7A  41 0F 2F 04 24                  comiss xmm0, dword ptr [r12]
009CEF7F  E9 B9 C6 FF FF                  jmp 0x1409cb63d
009CEF84  F3 41 0F 10 04 24               movss xmm0, dword ptr [r12]
009CEF8A  E9 38 CB FF FF                  jmp 0x1409cbac7
009CEF8F  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CEF97  F3 0F 10 00                     movss xmm0, dword ptr [rax]
009CEF9B  41 0F 2F 04 24                  comiss xmm0, dword ptr [r12]
009CEFA0  E9 CB C7 FF FF                  jmp 0x1409cb770
009CEFA5  F3 41 0F 10 04 24               movss xmm0, dword ptr [r12]
009CEFAB  E9 63 D5 FF FF                  jmp 0x1409cc513
009CEFB0  F3 41 0F 10 04 24               movss xmm0, dword ptr [r12]
009CEFB6  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CEFBE  0F 2E 00                        ucomiss xmm0, dword ptr [rax]
009CEFC1  E9 2B D5 FF FF                  jmp 0x1409cc4f1
009CEFC6  41 83 E9 02                     sub r9d, 2
009CEFCA  74 54                           je 0x1409cf020
009CEFCC  41 83 E9 01                     sub r9d, 1
009CEFD0  74 40                           je 0x1409cf012
009CEFD2  41 83 E9 01                     sub r9d, 1
009CEFD6  74 2C                           je 0x1409cf004
009CEFD8  41 83 E9 01                     sub r9d, 1
009CEFDC  74 18                           je 0x1409ceff6
009CEFDE  41 83 F9 01                     cmp r9d, 1
009CEFE2  0F 85 EE C3 FF FF               jne 0x1409cb3d6
009CEFE8  F3 41 0F 10 0C 24               movss xmm1, dword ptr [r12]
009CEFEE  0F 5A C9                        cvtps2pd xmm1, xmm1
009CEFF1  E9 37 C6 FF FF                  jmp 0x1409cb62d
009CEFF6  F3 41 0F 10 04 24               movss xmm0, dword ptr [r12]
009CEFFC  0F 5A C0                        cvtps2pd xmm0, xmm0
009CEFFF  E9 B5 C5 FF FF                  jmp 0x1409cb5b9
009CF004  F3 41 0F 10 0C 24               movss xmm1, dword ptr [r12]
009CF00A  0F 5A C9                        cvtps2pd xmm1, xmm1
009CF00D  E9 4D D5 FF FF                  jmp 0x1409cc55f
009CF012  F3 41 0F 10 04 24               movss xmm0, dword ptr [r12]
009CF018  0F 5A C0                        cvtps2pd xmm0, xmm0
009CF01B  E9 69 D5 FF FF                  jmp 0x1409cc589
009CF020  F3 41 0F 10 04 24               movss xmm0, dword ptr [r12]
009CF026  0F 5A C0                        cvtps2pd xmm0, xmm0
009CF029  E9 02 D5 FF FF                  jmp 0x1409cc530
009CF02E  41 83 E9 03                     sub r9d, 3
009CF032  74 7D                           je 0x1409cf0b1
009CF034  41 83 E9 01                     sub r9d, 1
009CF038  74 56                           je 0x1409cf090
009CF03A  41 83 E9 01                     sub r9d, 1
009CF03E  74 2B                           je 0x1409cf06b
009CF040  41 83 F9 01                     cmp r9d, 1
009CF044  0F 85 8C C3 FF FF               jne 0x1409cb3d6
009CF04A  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF052  8B 08                           mov ecx, dword ptr [rax]
009CF054  0F 57 C0                        xorps xmm0, xmm0
009CF057  F3 48 0F 2A C1                  cvtsi2ss xmm0, rcx
009CF05C  8B C6                           mov eax, esi
009CF05E  41 0F 2F 04 24                  comiss xmm0, dword ptr [r12]
009CF063  0F 93 C0                        setae al
009CF066  E9 2D C3 FF FF                  jmp 0x1409cb398
009CF06B  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF073  8B 08                           mov ecx, dword ptr [rax]
009CF075  0F 57 C9                        xorps xmm1, xmm1
009CF078  F3 48 0F 2A C9                  cvtsi2ss xmm1, rcx
009CF07D  8B C6                           mov eax, esi
009CF07F  F3 41 0F 10 04 24               movss xmm0, dword ptr [r12]
009CF085  0F 2F C1                        comiss xmm0, xmm1
009CF088  0F 93 C0                        setae al
009CF08B  E9 08 C3 FF FF                  jmp 0x1409cb398
009CF090  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF098  8B 08                           mov ecx, dword ptr [rax]
009CF09A  0F 57 C0                        xorps xmm0, xmm0
009CF09D  F3 48 0F 2A C1                  cvtsi2ss xmm0, rcx
009CF0A2  8B C6                           mov eax, esi
009CF0A4  41 0F 2F 04 24                  comiss xmm0, dword ptr [r12]
009CF0A9  0F 97 C0                        seta al
009CF0AC  E9 E7 C2 FF FF                  jmp 0x1409cb398
009CF0B1  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF0B9  8B 08                           mov ecx, dword ptr [rax]
009CF0BB  0F 57 C9                        xorps xmm1, xmm1
009CF0BE  F3 48 0F 2A C9                  cvtsi2ss xmm1, rcx
009CF0C3  8B C6                           mov eax, esi
009CF0C5  F3 41 0F 10 04 24               movss xmm0, dword ptr [r12]
009CF0CB  0F 2F C1                        comiss xmm0, xmm1
009CF0CE  0F 97 C0                        seta al
009CF0D1  E9 C2 C2 FF FF                  jmp 0x1409cb398
009CF0D6  83 C1 FE                        add ecx, -2
009CF0D9  83 F9 0D                        cmp ecx, 0xd
009CF0DC  0F 87 F4 C2 FF FF               ja 0x1409cb3d6
009CF0E2  8B 8C 8A 90 00 9D 00            mov ecx, dword ptr [rdx + rcx*4 + 0x9d0090]
009CF0E9  48 03 CA                        add rcx, rdx
009CF0EC  FF E1                           jmp rcx
009CF0EE  CC                              int3
009CF0EF  CC                              int3
009CF0F0  CC                              int3
009CF0F1  CC                              int3
009CF0F2  41 83 E9 02                     sub r9d, 2
009CF0F6  0F 84 28 01 00 00               je 0x1409cf224
009CF0FC  41 83 E9 01                     sub r9d, 1
009CF100  0F 84 D0 00 00 00               je 0x1409cf1d6
009CF106  41 83 E9 01                     sub r9d, 1
009CF10A  0F 84 A8 00 00 00               je 0x1409cf1b8
009CF110  41 83 E9 01                     sub r9d, 1
009CF114  74 54                           je 0x1409cf16a
009CF116  41 83 F9 01                     cmp r9d, 1
009CF11A  0F 85 B6 C2 FF FF               jne 0x1409cb3d6
009CF120  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF128  0F BE 08                        movsx ecx, byte ptr [rax]
009CF12B  EB 0B                           jmp 0x1409cf138
009CF12D  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF135  0F B7 08                        movzx ecx, word ptr [rax]
009CF138  66 0F 6E C1                     movd xmm0, ecx
009CF13C  EB 0C                           jmp 0x1409cf14a
009CF13E  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF146  66 0F 6E 00                     movd xmm0, dword ptr [rax]
009CF14A  F3 0F E6 C0                     cvtdq2pd xmm0, xmm0
009CF14E  EB 0F                           jmp 0x1409cf15f
009CF150  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF158  F3 0F 10 00                     movss xmm0, dword ptr [rax]
009CF15C  0F 5A C0                        cvtps2pd xmm0, xmm0
009CF15F  66 41 0F 2F 04 24               comisd xmm0, xmmword ptr [r12]
009CF165  E9 B2 F9 FF FF                  jmp 0x1409ceb1c
009CF16A  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF172  0F BE 08                        movsx ecx, byte ptr [rax]
009CF175  EB 0B                           jmp 0x1409cf182
009CF177  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF17F  0F B7 08                        movzx ecx, word ptr [rax]
009CF182  66 0F 6E C9                     movd xmm1, ecx
009CF186  EB 0C                           jmp 0x1409cf194
009CF188  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF190  66 0F 6E 08                     movd xmm1, dword ptr [rax]
009CF194  F3 0F E6 C9                     cvtdq2pd xmm1, xmm1
009CF198  EB 0F                           jmp 0x1409cf1a9
009CF19A  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF1A2  F3 0F 10 08                     movss xmm1, dword ptr [rax]
009CF1A6  0F 5A C9                        cvtps2pd xmm1, xmm1
009CF1A9  F2 41 0F 10 04 24               movsd xmm0, qword ptr [r12]
009CF1AF  66 0F 2F C1                     comisd xmm0, xmm1
009CF1B3  E9 64 F9 FF FF                  jmp 0x1409ceb1c
009CF1B8  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF1C0  0F BE 08                        movsx ecx, byte ptr [rax]
009CF1C3  66 0F 6E C1                     movd xmm0, ecx
009CF1C7  F3 0F E6 C0                     cvtdq2pd xmm0, xmm0
009CF1CB  66 41 0F 2F 04 24               comisd xmm0, xmmword ptr [r12]
009CF1D1  E9 DA F9 FF FF                  jmp 0x1409cebb0
009CF1D6  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF1DE  0F BE 08                        movsx ecx, byte ptr [rax]
009CF1E1  EB 0B                           jmp 0x1409cf1ee
009CF1E3  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF1EB  0F B7 08                        movzx ecx, word ptr [rax]
009CF1EE  66 0F 6E C9                     movd xmm1, ecx
009CF1F2  EB 0C                           jmp 0x1409cf200
009CF1F4  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF1FC  66 0F 6E 08                     movd xmm1, dword ptr [rax]
009CF200  F3 0F E6 C9                     cvtdq2pd xmm1, xmm1
009CF204  EB 0F                           jmp 0x1409cf215
009CF206  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF20E  F3 0F 10 08                     movss xmm1, dword ptr [rax]
009CF212  0F 5A C9                        cvtps2pd xmm1, xmm1
009CF215  F2 41 0F 10 04 24               movsd xmm0, qword ptr [r12]
009CF21B  66 0F 2F C1                     comisd xmm0, xmm1
009CF21F  E9 8C F9 FF FF                  jmp 0x1409cebb0
009CF224  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF22C  0F BE 08                        movsx ecx, byte ptr [rax]
009CF22F  EB 0B                           jmp 0x1409cf23c
009CF231  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF239  0F B7 08                        movzx ecx, word ptr [rax]
009CF23C  66 0F 6E C9                     movd xmm1, ecx
009CF240  EB 0C                           jmp 0x1409cf24e
009CF242  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF24A  66 0F 6E 08                     movd xmm1, dword ptr [rax]
009CF24E  F3 0F E6 C9                     cvtdq2pd xmm1, xmm1
009CF252  EB 0F                           jmp 0x1409cf263
009CF254  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF25C  F3 0F 10 08                     movss xmm1, dword ptr [rax]
009CF260  0F 5A C9                        cvtps2pd xmm1, xmm1
009CF263  F2 41 0F 10 04 24               movsd xmm0, qword ptr [r12]
009CF269  66 0F 2E C1                     ucomisd xmm0, xmm1
009CF26D  E9 7F D2 FF FF                  jmp 0x1409cc4f1
009CF272  41 83 E9 02                     sub r9d, 2
009CF276  74 78                           je 0x1409cf2f0
009CF278  41 83 E9 01                     sub r9d, 1
009CF27C  74 62                           je 0x1409cf2e0
009CF27E  41 83 E9 01                     sub r9d, 1
009CF282  74 3E                           je 0x1409cf2c2
009CF284  41 83 E9 01                     sub r9d, 1
009CF288  74 28                           je 0x1409cf2b2
009CF28A  41 83 F9 01                     cmp r9d, 1
009CF28E  0F 85 42 C1 FF FF               jne 0x1409cb3d6
009CF294  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF29C  0F B6 08                        movzx ecx, byte ptr [rax]
009CF29F  66 0F 6E C1                     movd xmm0, ecx
009CF2A3  F3 0F E6 C0                     cvtdq2pd xmm0, xmm0
009CF2A7  66 41 0F 2F 04 24               comisd xmm0, xmmword ptr [r12]
009CF2AD  E9 6A F8 FF FF                  jmp 0x1409ceb1c
009CF2B2  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF2BA  0F B6 08                        movzx ecx, byte ptr [rax]
009CF2BD  E9 C0 FE FF FF                  jmp 0x1409cf182
009CF2C2  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF2CA  0F B6 08                        movzx ecx, byte ptr [rax]
009CF2CD  66 0F 6E C1                     movd xmm0, ecx
009CF2D1  F3 0F E6 C0                     cvtdq2pd xmm0, xmm0
009CF2D5  66 41 0F 2F 04 24               comisd xmm0, xmmword ptr [r12]
009CF2DB  E9 D0 F8 FF FF                  jmp 0x1409cebb0
009CF2E0  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF2E8  0F B6 08                        movzx ecx, byte ptr [rax]
009CF2EB  E9 FE FE FF FF                  jmp 0x1409cf1ee
009CF2F0  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF2F8  0F B6 08                        movzx ecx, byte ptr [rax]
009CF2FB  E9 3C FF FF FF                  jmp 0x1409cf23c
009CF300  41 83 E9 02                     sub r9d, 2
009CF304  74 78                           je 0x1409cf37e
009CF306  41 83 E9 01                     sub r9d, 1
009CF30A  74 62                           je 0x1409cf36e
009CF30C  41 83 E9 01                     sub r9d, 1
009CF310  74 3E                           je 0x1409cf350
009CF312  41 83 E9 01                     sub r9d, 1
009CF316  74 28                           je 0x1409cf340
009CF318  41 83 F9 01                     cmp r9d, 1
009CF31C  0F 85 B4 C0 FF FF               jne 0x1409cb3d6
009CF322  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF32A  0F BF 08                        movsx ecx, word ptr [rax]
009CF32D  66 0F 6E C1                     movd xmm0, ecx
009CF331  F3 0F E6 C0                     cvtdq2pd xmm0, xmm0
009CF335  66 41 0F 2F 04 24               comisd xmm0, xmmword ptr [r12]
009CF33B  E9 DC F7 FF FF                  jmp 0x1409ceb1c
009CF340  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF348  0F BF 08                        movsx ecx, word ptr [rax]
009CF34B  E9 32 FE FF FF                  jmp 0x1409cf182
009CF350  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF358  0F BF 08                        movsx ecx, word ptr [rax]
009CF35B  66 0F 6E C1                     movd xmm0, ecx
009CF35F  F3 0F E6 C0                     cvtdq2pd xmm0, xmm0
009CF363  66 41 0F 2F 04 24               comisd xmm0, xmmword ptr [r12]
009CF369  E9 42 F8 FF FF                  jmp 0x1409cebb0
009CF36E  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF376  0F BF 08                        movsx ecx, word ptr [rax]
009CF379  E9 70 FE FF FF                  jmp 0x1409cf1ee
009CF37E  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF386  0F BF 08                        movsx ecx, word ptr [rax]
009CF389  E9 AE FE FF FF                  jmp 0x1409cf23c
009CF38E  41 83 E9 02                     sub r9d, 2
009CF392  0F 84 99 FE FF FF               je 0x1409cf231
009CF398  41 83 E9 01                     sub r9d, 1
009CF39C  0F 84 41 FE FF FF               je 0x1409cf1e3
009CF3A2  41 83 E9 01                     sub r9d, 1
009CF3A6  74 32                           je 0x1409cf3da
009CF3A8  41 83 E9 01                     sub r9d, 1
009CF3AC  0F 84 C5 FD FF FF               je 0x1409cf177
009CF3B2  41 83 F9 01                     cmp r9d, 1
009CF3B6  0F 85 1A C0 FF FF               jne 0x1409cb3d6
009CF3BC  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF3C4  0F B7 08                        movzx ecx, word ptr [rax]
009CF3C7  66 0F 6E C1                     movd xmm0, ecx
009CF3CB  F3 0F E6 C0                     cvtdq2pd xmm0, xmm0
009CF3CF  66 41 0F 2F 04 24               comisd xmm0, xmmword ptr [r12]
009CF3D5  E9 42 F7 FF FF                  jmp 0x1409ceb1c
009CF3DA  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF3E2  0F B7 08                        movzx ecx, word ptr [rax]
009CF3E5  66 0F 6E C1                     movd xmm0, ecx
009CF3E9  F3 0F E6 C0                     cvtdq2pd xmm0, xmm0
009CF3ED  66 41 0F 2F 04 24               comisd xmm0, xmmword ptr [r12]
009CF3F3  E9 B8 F7 FF FF                  jmp 0x1409cebb0
009CF3F8  41 83 E9 02                     sub r9d, 2
009CF3FC  0F 84 40 FE FF FF               je 0x1409cf242
009CF402  41 83 E9 01                     sub r9d, 1
009CF406  0F 84 E8 FD FF FF               je 0x1409cf1f4
009CF40C  41 83 E9 01                     sub r9d, 1
009CF410  74 2F                           je 0x1409cf441
009CF412  41 83 E9 01                     sub r9d, 1
009CF416  0F 84 6C FD FF FF               je 0x1409cf188
009CF41C  41 83 F9 01                     cmp r9d, 1
009CF420  0F 85 B0 BF FF FF               jne 0x1409cb3d6
009CF426  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF42E  66 0F 6E 00                     movd xmm0, dword ptr [rax]
009CF432  F3 0F E6 C0                     cvtdq2pd xmm0, xmm0
009CF436  66 41 0F 2F 04 24               comisd xmm0, xmmword ptr [r12]
009CF43C  E9 DB F6 FF FF                  jmp 0x1409ceb1c
009CF441  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF449  66 0F 6E 00                     movd xmm0, dword ptr [rax]
009CF44D  F3 0F E6 C0                     cvtdq2pd xmm0, xmm0
009CF451  66 41 0F 2F 04 24               comisd xmm0, xmmword ptr [r12]
009CF457  E9 54 F7 FF FF                  jmp 0x1409cebb0
009CF45C  41 83 E9 02                     sub r9d, 2
009CF460  0F 84 84 00 00 00               je 0x1409cf4ea
009CF466  41 83 E9 01                     sub r9d, 1
009CF46A  74 67                           je 0x1409cf4d3
009CF46C  41 83 E9 01                     sub r9d, 1
009CF470  74 44                           je 0x1409cf4b6
009CF472  41 83 E9 01                     sub r9d, 1
009CF476  74 27                           je 0x1409cf49f
009CF478  41 83 F9 01                     cmp r9d, 1
009CF47C  0F 85 54 BF FF FF               jne 0x1409cb3d6
009CF482  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF48A  8B 08                           mov ecx, dword ptr [rax]
009CF48C  0F 57 C0                        xorps xmm0, xmm0
009CF48F  F2 48 0F 2A C1                  cvtsi2sd xmm0, rcx
009CF494  66 41 0F 2F 04 24               comisd xmm0, xmmword ptr [r12]
009CF49A  E9 7D F6 FF FF                  jmp 0x1409ceb1c
009CF49F  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF4A7  8B 08                           mov ecx, dword ptr [rax]
009CF4A9  0F 57 C9                        xorps xmm1, xmm1
009CF4AC  F2 48 0F 2A C9                  cvtsi2sd xmm1, rcx
009CF4B1  E9 F3 FC FF FF                  jmp 0x1409cf1a9
009CF4B6  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF4BE  8B 08                           mov ecx, dword ptr [rax]
009CF4C0  0F 57 C0                        xorps xmm0, xmm0
009CF4C3  F2 48 0F 2A C1                  cvtsi2sd xmm0, rcx
009CF4C8  66 41 0F 2F 04 24               comisd xmm0, xmmword ptr [r12]
009CF4CE  E9 DD F6 FF FF                  jmp 0x1409cebb0
009CF4D3  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF4DB  8B 08                           mov ecx, dword ptr [rax]
009CF4DD  0F 57 C9                        xorps xmm1, xmm1
009CF4E0  F2 48 0F 2A C9                  cvtsi2sd xmm1, rcx
009CF4E5  E9 2B FD FF FF                  jmp 0x1409cf215
009CF4EA  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF4F2  8B 08                           mov ecx, dword ptr [rax]
009CF4F4  0F 57 C9                        xorps xmm1, xmm1
009CF4F7  F2 48 0F 2A C9                  cvtsi2sd xmm1, rcx
009CF4FC  E9 62 FD FF FF                  jmp 0x1409cf263
009CF501  41 83 E9 02                     sub r9d, 2
009CF505  74 7C                           je 0x1409cf583
009CF507  41 83 E9 01                     sub r9d, 1
009CF50B  74 61                           je 0x1409cf56e
009CF50D  41 83 E9 01                     sub r9d, 1
009CF511  74 40                           je 0x1409cf553
009CF513  41 83 E9 01                     sub r9d, 1
009CF517  74 25                           je 0x1409cf53e
009CF519  41 83 F9 01                     cmp r9d, 1
009CF51D  0F 85 B3 BE FF FF               jne 0x1409cb3d6
009CF523  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF52B  0F 57 C0                        xorps xmm0, xmm0
009CF52E  F2 48 0F 2A 00                  cvtsi2sd xmm0, qword ptr [rax]
009CF533  66 41 0F 2F 04 24               comisd xmm0, xmmword ptr [r12]
009CF539  E9 DE F5 FF FF                  jmp 0x1409ceb1c
009CF53E  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF546  0F 57 C9                        xorps xmm1, xmm1
009CF549  F2 48 0F 2A 08                  cvtsi2sd xmm1, qword ptr [rax]
009CF54E  E9 56 FC FF FF                  jmp 0x1409cf1a9
009CF553  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF55B  0F 57 C0                        xorps xmm0, xmm0
009CF55E  F2 48 0F 2A 00                  cvtsi2sd xmm0, qword ptr [rax]
009CF563  66 41 0F 2F 04 24               comisd xmm0, xmmword ptr [r12]
009CF569  E9 42 F6 FF FF                  jmp 0x1409cebb0
009CF56E  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF576  0F 57 C9                        xorps xmm1, xmm1
009CF579  F2 48 0F 2A 08                  cvtsi2sd xmm1, qword ptr [rax]
009CF57E  E9 92 FC FF FF                  jmp 0x1409cf215
009CF583  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF58B  0F 57 C9                        xorps xmm1, xmm1
009CF58E  F2 48 0F 2A 08                  cvtsi2sd xmm1, qword ptr [rax]
009CF593  E9 CB FC FF FF                  jmp 0x1409cf263
009CF598  41 83 E9 02                     sub r9d, 2
009CF59C  0F 84 06 01 00 00               je 0x1409cf6a8
009CF5A2  41 83 E9 01                     sub r9d, 1
009CF5A6  0F 84 C5 00 00 00               je 0x1409cf671
009CF5AC  41 83 E9 01                     sub r9d, 1
009CF5B0  0F 84 81 00 00 00               je 0x1409cf637
009CF5B6  41 83 E9 01                     sub r9d, 1
009CF5BA  74 44                           je 0x1409cf600
009CF5BC  41 83 F9 01                     cmp r9d, 1
009CF5C0  0F 85 10 BE FF FF               jne 0x1409cb3d6
009CF5C6  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF5CE  48 8B 08                        mov rcx, qword ptr [rax]
009CF5D1  0F 57 C0                        xorps xmm0, xmm0
009CF5D4  48 85 C9                        test rcx, rcx
009CF5D7  78 07                           js 0x1409cf5e0
009CF5D9  F2 48 0F 2A C1                  cvtsi2sd xmm0, rcx
009CF5DE  EB 15                           jmp 0x1409cf5f5
009CF5E0  48 8B C1                        mov rax, rcx
009CF5E3  48 D1 E8                        shr rax, 1
009CF5E6  83 E1 01                        and ecx, 1
009CF5E9  48 0B C1                        or rax, rcx
009CF5EC  F2 48 0F 2A C0                  cvtsi2sd xmm0, rax
009CF5F1  F2 0F 58 C0                     addsd xmm0, xmm0
009CF5F5  66 41 0F 2F 04 24               comisd xmm0, xmmword ptr [r12]
009CF5FB  E9 1C F5 FF FF                  jmp 0x1409ceb1c
009CF600  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF608  48 8B 08                        mov rcx, qword ptr [rax]
009CF60B  0F 57 C9                        xorps xmm1, xmm1
009CF60E  48 85 C9                        test rcx, rcx
009CF611  78 0A                           js 0x1409cf61d
009CF613  F2 48 0F 2A C9                  cvtsi2sd xmm1, rcx
009CF618  E9 8C FB FF FF                  jmp 0x1409cf1a9
009CF61D  48 8B C1                        mov rax, rcx
009CF620  48 D1 E8                        shr rax, 1
009CF623  83 E1 01                        and ecx, 1
009CF626  48 0B C1                        or rax, rcx
009CF629  F2 48 0F 2A C8                  cvtsi2sd xmm1, rax
009CF62E  F2 0F 58 C9                     addsd xmm1, xmm1
009CF632  E9 72 FB FF FF                  jmp 0x1409cf1a9
009CF637  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF63F  48 8B 08                        mov rcx, qword ptr [rax]
009CF642  0F 57 C0                        xorps xmm0, xmm0
009CF645  48 85 C9                        test rcx, rcx
009CF648  78 07                           js 0x1409cf651
009CF64A  F2 48 0F 2A C1                  cvtsi2sd xmm0, rcx
009CF64F  EB 15                           jmp 0x1409cf666
009CF651  48 8B C1                        mov rax, rcx
009CF654  48 D1 E8                        shr rax, 1
009CF657  83 E1 01                        and ecx, 1
009CF65A  48 0B C1                        or rax, rcx
009CF65D  F2 48 0F 2A C0                  cvtsi2sd xmm0, rax
009CF662  F2 0F 58 C0                     addsd xmm0, xmm0
009CF666  66 41 0F 2F 04 24               comisd xmm0, xmmword ptr [r12]
009CF66C  E9 3F F5 FF FF                  jmp 0x1409cebb0
009CF671  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF679  48 8B 08                        mov rcx, qword ptr [rax]
009CF67C  0F 57 C9                        xorps xmm1, xmm1
009CF67F  48 85 C9                        test rcx, rcx
009CF682  78 0A                           js 0x1409cf68e
009CF684  F2 48 0F 2A C9                  cvtsi2sd xmm1, rcx
009CF689  E9 87 FB FF FF                  jmp 0x1409cf215
009CF68E  48 8B C1                        mov rax, rcx
009CF691  48 D1 E8                        shr rax, 1
009CF694  83 E1 01                        and ecx, 1
009CF697  48 0B C1                        or rax, rcx
009CF69A  F2 48 0F 2A C8                  cvtsi2sd xmm1, rax
009CF69F  F2 0F 58 C9                     addsd xmm1, xmm1
009CF6A3  E9 6D FB FF FF                  jmp 0x1409cf215
009CF6A8  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF6B0  48 8B 08                        mov rcx, qword ptr [rax]
009CF6B3  0F 57 C9                        xorps xmm1, xmm1
009CF6B6  48 85 C9                        test rcx, rcx
009CF6B9  78 0A                           js 0x1409cf6c5
009CF6BB  F2 48 0F 2A C9                  cvtsi2sd xmm1, rcx
009CF6C0  E9 9E FB FF FF                  jmp 0x1409cf263
009CF6C5  48 8B C1                        mov rax, rcx
009CF6C8  48 D1 E8                        shr rax, 1
009CF6CB  83 E1 01                        and ecx, 1
009CF6CE  48 0B C1                        or rax, rcx
009CF6D1  F2 48 0F 2A C8                  cvtsi2sd xmm1, rax
009CF6D6  F2 0F 58 C9                     addsd xmm1, xmm1
009CF6DA  E9 84 FB FF FF                  jmp 0x1409cf263
009CF6DF  41 83 E9 02                     sub r9d, 2
009CF6E3  0F 84 6B FB FF FF               je 0x1409cf254
009CF6E9  41 83 E9 01                     sub r9d, 1
009CF6ED  0F 84 13 FB FF FF               je 0x1409cf206
009CF6F3  41 83 E9 01                     sub r9d, 1
009CF6F7  74 2E                           je 0x1409cf727
009CF6F9  41 83 E9 01                     sub r9d, 1
009CF6FD  0F 84 97 FA FF FF               je 0x1409cf19a
009CF703  41 83 F9 01                     cmp r9d, 1
009CF707  0F 85 C9 BC FF FF               jne 0x1409cb3d6
009CF70D  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF715  F3 0F 10 00                     movss xmm0, dword ptr [rax]
009CF719  0F 5A C0                        cvtps2pd xmm0, xmm0
009CF71C  66 41 0F 2F 04 24               comisd xmm0, xmmword ptr [r12]
009CF722  E9 F5 F3 FF FF                  jmp 0x1409ceb1c
009CF727  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF72F  F3 0F 10 00                     movss xmm0, dword ptr [rax]
009CF733  0F 5A C0                        cvtps2pd xmm0, xmm0
009CF736  66 41 0F 2F 04 24               comisd xmm0, xmmword ptr [r12]
009CF73C  E9 6F F4 FF FF                  jmp 0x1409cebb0
009CF741  41 83 E9 02                     sub r9d, 2
009CF745  74 60                           je 0x1409cf7a7
009CF747  41 83 E9 01                     sub r9d, 1
009CF74B  74 4F                           je 0x1409cf79c
009CF74D  41 83 E9 01                     sub r9d, 1
009CF751  74 32                           je 0x1409cf785
009CF753  41 83 E9 01                     sub r9d, 1
009CF757  74 21                           je 0x1409cf77a
009CF759  41 83 F9 01                     cmp r9d, 1
009CF75D  0F 85 73 BC FF FF               jne 0x1409cb3d6
009CF763  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF76B  F2 0F 10 00                     movsd xmm0, qword ptr [rax]
009CF76F  66 41 0F 2F 04 24               comisd xmm0, xmmword ptr [r12]
009CF775  E9 C3 BE FF FF                  jmp 0x1409cb63d
009CF77A  F2 41 0F 10 04 24               movsd xmm0, qword ptr [r12]
009CF780  E9 34 BE FF FF                  jmp 0x1409cb5b9
009CF785  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF78D  F2 0F 10 00                     movsd xmm0, qword ptr [rax]
009CF791  66 41 0F 2F 04 24               comisd xmm0, xmmword ptr [r12]
009CF797  E9 D4 BF FF FF                  jmp 0x1409cb770
009CF79C  F2 41 0F 10 04 24               movsd xmm0, qword ptr [r12]
009CF7A2  E9 E2 CD FF FF                  jmp 0x1409cc589
009CF7A7  F2 41 0F 10 04 24               movsd xmm0, qword ptr [r12]
009CF7AD  E9 7E CD FF FF                  jmp 0x1409cc530
009CF7B2  83 C1 FE                        add ecx, -2
009CF7B5  83 F9 0D                        cmp ecx, 0xd
009CF7B8  0F 87 18 BC FF FF               ja 0x1409cb3d6
009CF7BE  8B 8C 8A C8 00 9D 00            mov ecx, dword ptr [rdx + rcx*4 + 0x9d00c8]
009CF7C5  48 03 CA                        add rcx, rdx
009CF7C8  FF E1                           jmp rcx
009CF7CA  CC                              int3
009CF7CB  CC                              int3
009CF7CC  CC                              int3
009CF7CD  CC                              int3
009CF7CE  41 83 E9 02                     sub r9d, 2
009CF7D2  0F 84 34 E8 FF FF               je 0x1409ce00c
009CF7D8  41 83 E9 01                     sub r9d, 1
009CF7DC  0F 84 11 E8 FF FF               je 0x1409cdff3
009CF7E2  41 83 E9 01                     sub r9d, 1
009CF7E6  0F 84 EE E7 FF FF               je 0x1409cdfda
009CF7EC  41 83 E9 01                     sub r9d, 1
009CF7F0  0F 84 CB E7 FF FF               je 0x1409cdfc1
009CF7F6  41 83 F9 01                     cmp r9d, 1
009CF7FA  0F 85 D6 BB FF FF               jne 0x1409cb3d6
009CF800  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF808  0F B6 08                        movzx ecx, byte ptr [rax]
009CF80B  E9 3B E7 FF FF                  jmp 0x1409cdf4b
009CF810  41 83 E9 02                     sub r9d, 2
009CF814  0F 84 99 E8 FF FF               je 0x1409ce0b3
009CF81A  41 83 E9 01                     sub r9d, 1
009CF81E  0F 84 75 E8 FF FF               je 0x1409ce099
009CF824  41 83 E9 01                     sub r9d, 1
009CF828  0F 84 51 E8 FF FF               je 0x1409ce07f
009CF82E  41 83 E9 01                     sub r9d, 1
009CF832  0F 84 2D E8 FF FF               je 0x1409ce065
009CF838  41 83 F9 01                     cmp r9d, 1
009CF83C  0F 85 94 BB FF FF               jne 0x1409cb3d6
009CF842  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF84A  48 0F BF 08                     movsx rcx, word ptr [rax]
009CF84E  E9 F8 E6 FF FF                  jmp 0x1409cdf4b
009CF853  41 83 E9 02                     sub r9d, 2
009CF857  0F 84 FA E8 FF FF               je 0x1409ce157
009CF85D  41 83 E9 01                     sub r9d, 1
009CF861  0F 84 D7 E8 FF FF               je 0x1409ce13e
009CF867  41 83 E9 01                     sub r9d, 1
009CF86B  0F 84 B4 E8 FF FF               je 0x1409ce125
009CF871  41 83 E9 01                     sub r9d, 1
009CF875  0F 84 91 E8 FF FF               je 0x1409ce10c
009CF87B  41 83 F9 01                     cmp r9d, 1
009CF87F  0F 85 51 BB FF FF               jne 0x1409cb3d6
009CF885  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF88D  0F B7 08                        movzx ecx, word ptr [rax]
009CF890  E9 B6 E6 FF FF                  jmp 0x1409cdf4b
009CF895  41 83 E9 02                     sub r9d, 2
009CF899  0F 84 5B E9 FF FF               je 0x1409ce1fa
009CF89F  41 83 E9 01                     sub r9d, 1
009CF8A3  0F 84 38 E9 FF FF               je 0x1409ce1e1
009CF8A9  41 83 E9 01                     sub r9d, 1
009CF8AD  0F 84 15 E9 FF FF               je 0x1409ce1c8
009CF8B3  41 83 E9 01                     sub r9d, 1
009CF8B7  0F 84 F2 E8 FF FF               je 0x1409ce1af
009CF8BD  41 83 F9 01                     cmp r9d, 1
009CF8C1  0F 85 0F BB FF FF               jne 0x1409cb3d6
009CF8C7  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF8CF  48 63 08                        movsxd rcx, dword ptr [rax]
009CF8D2  E9 74 E6 FF FF                  jmp 0x1409cdf4b
009CF8D7  41 83 E9 02                     sub r9d, 2
009CF8DB  0F 84 B4 E9 FF FF               je 0x1409ce295
009CF8E1  41 83 E9 01                     sub r9d, 1
009CF8E5  0F 84 92 E9 FF FF               je 0x1409ce27d
009CF8EB  41 83 E9 01                     sub r9d, 1
009CF8EF  0F 84 70 E9 FF FF               je 0x1409ce265
009CF8F5  41 83 E9 01                     sub r9d, 1
009CF8F9  0F 84 4E E9 FF FF               je 0x1409ce24d
009CF8FF  41 83 F9 01                     cmp r9d, 1
009CF903  0F 85 CD BA FF FF               jne 0x1409cb3d6
009CF909  E9 33 E6 FF FF                  jmp 0x1409cdf41
009CF90E  41 83 E9 02                     sub r9d, 2
009CF912  0F 84 A6 EB FF FF               je 0x1409ce4be
009CF918  41 83 E9 01                     sub r9d, 1
009CF91C  0F 84 8E EB FF FF               je 0x1409ce4b0
009CF922  41 83 E9 01                     sub r9d, 1
009CF926  0F 84 76 EB FF FF               je 0x1409ce4a2
009CF92C  41 83 E9 01                     sub r9d, 1
009CF930  0F 84 5E EB FF FF               je 0x1409ce494
009CF936  E9 41 EB FF FF                  jmp 0x1409ce47c
009CF93B  83 C1 FE                        add ecx, -2
009CF93E  83 F9 0D                        cmp ecx, 0xd
009CF941  0F 87 8F BA FF FF               ja 0x1409cb3d6
009CF947  8B 8C 8A 00 01 9D 00            mov ecx, dword ptr [rdx + rcx*4 + 0x9d0100]
009CF94E  48 03 CA                        add rcx, rdx
009CF951  FF E1                           jmp rcx
009CF953  CC                              int3
009CF954  CC                              int3
009CF955  CC                              int3
009CF956  CC                              int3
009CF957  41 83 E9 02                     sub r9d, 2
009CF95B  0F 84 C3 F8 FF FF               je 0x1409cf224
009CF961  41 83 E9 01                     sub r9d, 1
009CF965  0F 84 6B F8 FF FF               je 0x1409cf1d6
009CF96B  41 83 E9 01                     sub r9d, 1
009CF96F  0F 84 43 F8 FF FF               je 0x1409cf1b8
009CF975  41 83 E9 01                     sub r9d, 1
009CF979  0F 84 EB F7 FF FF               je 0x1409cf16a
009CF97F  E9 92 F7 FF FF                  jmp 0x1409cf116
009CF984  41 83 E9 02                     sub r9d, 2
009CF988  0F 84 62 F9 FF FF               je 0x1409cf2f0
009CF98E  41 83 E9 01                     sub r9d, 1
009CF992  0F 84 48 F9 FF FF               je 0x1409cf2e0
009CF998  41 83 E9 01                     sub r9d, 1
009CF99C  0F 84 20 F9 FF FF               je 0x1409cf2c2
009CF9A2  41 83 E9 01                     sub r9d, 1
009CF9A6  0F 84 06 F9 FF FF               je 0x1409cf2b2
009CF9AC  41 83 F9 01                     cmp r9d, 1
009CF9B0  0F 85 20 BA FF FF               jne 0x1409cb3d6
009CF9B6  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CF9BE  0F B6 08                        movzx ecx, byte ptr [rax]
009CF9C1  E9 72 F7 FF FF                  jmp 0x1409cf138
009CF9C6  41 83 E9 02                     sub r9d, 2
009CF9CA  0F 84 AE F9 FF FF               je 0x1409cf37e
009CF9D0  41 83 E9 01                     sub r9d, 1
009CF9D4  0F 84 94 F9 FF FF               je 0x1409cf36e
009CF9DA  41 83 E9 01                     sub r9d, 1
009CF9DE  0F 84 6C F9 FF FF               je 0x1409cf350
009CF9E4  41 83 E9 01                     sub r9d, 1
009CF9E8  0F 84 52 F9 FF FF               je 0x1409cf340
009CF9EE  41 83 F9 01                     cmp r9d, 1
009CF9F2  0F 85 DE B9 FF FF               jne 0x1409cb3d6
009CF9F8  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CFA00  0F BF 08                        movsx ecx, word ptr [rax]
009CFA03  E9 30 F7 FF FF                  jmp 0x1409cf138
009CFA08  41 83 E9 02                     sub r9d, 2
009CFA0C  0F 84 1F F8 FF FF               je 0x1409cf231
009CFA12  41 83 E9 01                     sub r9d, 1
009CFA16  0F 84 C7 F7 FF FF               je 0x1409cf1e3
009CFA1C  41 83 E9 01                     sub r9d, 1
009CFA20  0F 84 B4 F9 FF FF               je 0x1409cf3da
009CFA26  41 83 E9 01                     sub r9d, 1
009CFA2A  0F 84 47 F7 FF FF               je 0x1409cf177
009CFA30  41 83 F9 01                     cmp r9d, 1
009CFA34  0F 85 9C B9 FF FF               jne 0x1409cb3d6
009CFA3A  E9 EE F6 FF FF                  jmp 0x1409cf12d
009CFA3F  41 83 E9 02                     sub r9d, 2
009CFA43  0F 84 F9 F7 FF FF               je 0x1409cf242
009CFA49  41 83 E9 01                     sub r9d, 1
009CFA4D  0F 84 A1 F7 FF FF               je 0x1409cf1f4
009CFA53  41 83 E9 01                     sub r9d, 1
009CFA57  0F 84 E4 F9 FF FF               je 0x1409cf441
009CFA5D  41 83 E9 01                     sub r9d, 1
009CFA61  0F 84 21 F7 FF FF               je 0x1409cf188
009CFA67  41 83 F9 01                     cmp r9d, 1
009CFA6B  0F 85 65 B9 FF FF               jne 0x1409cb3d6
009CFA71  E9 C8 F6 FF FF                  jmp 0x1409cf13e
009CFA76  41 83 E9 02                     sub r9d, 2
009CFA7A  0F 84 6A FA FF FF               je 0x1409cf4ea
009CFA80  41 83 E9 01                     sub r9d, 1
009CFA84  0F 84 49 FA FF FF               je 0x1409cf4d3
009CFA8A  41 83 E9 01                     sub r9d, 1
009CFA8E  0F 84 22 FA FF FF               je 0x1409cf4b6
009CFA94  41 83 E9 01                     sub r9d, 1
009CFA98  0F 84 01 FA FF FF               je 0x1409cf49f
009CFA9E  41 83 F9 01                     cmp r9d, 1
009CFAA2  0F 85 2E B9 FF FF               jne 0x1409cb3d6
009CFAA8  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CFAB0  8B 08                           mov ecx, dword ptr [rax]
009CFAB2  0F 57 C0                        xorps xmm0, xmm0
009CFAB5  F2 48 0F 2A C1                  cvtsi2sd xmm0, rcx
009CFABA  E9 A0 F6 FF FF                  jmp 0x1409cf15f
009CFABF  41 83 E9 02                     sub r9d, 2
009CFAC3  0F 84 BA FA FF FF               je 0x1409cf583
009CFAC9  41 83 E9 01                     sub r9d, 1
009CFACD  0F 84 9B FA FF FF               je 0x1409cf56e
009CFAD3  41 83 E9 01                     sub r9d, 1
009CFAD7  0F 84 76 FA FF FF               je 0x1409cf553
009CFADD  41 83 E9 01                     sub r9d, 1
009CFAE1  0F 84 57 FA FF FF               je 0x1409cf53e
009CFAE7  41 83 F9 01                     cmp r9d, 1
009CFAEB  0F 85 E5 B8 FF FF               jne 0x1409cb3d6
009CFAF1  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CFAF9  0F 57 C0                        xorps xmm0, xmm0
009CFAFC  F2 48 0F 2A 00                  cvtsi2sd xmm0, qword ptr [rax]
009CFB01  E9 59 F6 FF FF                  jmp 0x1409cf15f
009CFB06  41 83 E9 02                     sub r9d, 2
009CFB0A  0F 84 98 FB FF FF               je 0x1409cf6a8
009CFB10  41 83 E9 01                     sub r9d, 1
009CFB14  0F 84 57 FB FF FF               je 0x1409cf671
009CFB1A  41 83 E9 01                     sub r9d, 1
009CFB1E  0F 84 13 FB FF FF               je 0x1409cf637
009CFB24  41 83 E9 01                     sub r9d, 1
009CFB28  0F 84 D2 FA FF FF               je 0x1409cf600
009CFB2E  41 83 F9 01                     cmp r9d, 1
009CFB32  0F 85 9E B8 FF FF               jne 0x1409cb3d6
009CFB38  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CFB40  48 8B 08                        mov rcx, qword ptr [rax]
009CFB43  0F 57 C0                        xorps xmm0, xmm0
009CFB46  48 85 C9                        test rcx, rcx
009CFB49  78 0A                           js 0x1409cfb55
009CFB4B  F2 48 0F 2A C1                  cvtsi2sd xmm0, rcx
009CFB50  E9 0A F6 FF FF                  jmp 0x1409cf15f
009CFB55  48 8B C1                        mov rax, rcx
009CFB58  48 D1 E8                        shr rax, 1
009CFB5B  83 E1 01                        and ecx, 1
009CFB5E  48 0B C1                        or rax, rcx
009CFB61  F2 48 0F 2A C0                  cvtsi2sd xmm0, rax
009CFB66  F2 0F 58 C0                     addsd xmm0, xmm0
009CFB6A  E9 F0 F5 FF FF                  jmp 0x1409cf15f
009CFB6F  41 83 E9 02                     sub r9d, 2
009CFB73  0F 84 DB F6 FF FF               je 0x1409cf254
009CFB79  41 83 E9 01                     sub r9d, 1
009CFB7D  0F 84 83 F6 FF FF               je 0x1409cf206
009CFB83  41 83 E9 01                     sub r9d, 1
009CFB87  0F 84 9A FB FF FF               je 0x1409cf727
009CFB8D  41 83 E9 01                     sub r9d, 1
009CFB91  0F 84 03 F6 FF FF               je 0x1409cf19a
009CFB97  41 83 F9 01                     cmp r9d, 1
009CFB9B  0F 85 35 B8 FF FF               jne 0x1409cb3d6
009CFBA1  E9 AA F5 FF FF                  jmp 0x1409cf150
009CFBA6  83 F9 10                        cmp ecx, 0x10
009CFBA9  0F 85 27 B8 FF FF               jne 0x1409cb3d6
009CFBAF  41 83 E9 02                     sub r9d, 2
009CFBB3  0F 84 D8 00 00 00               je 0x1409cfc91
009CFBB9  41 83 E9 01                     sub r9d, 1
009CFBBD  0F 84 B1 00 00 00               je 0x1409cfc74
009CFBC3  41 83 E9 01                     sub r9d, 1
009CFBC7  0F 84 8A 00 00 00               je 0x1409cfc57
009CFBCD  41 83 E9 01                     sub r9d, 1
009CFBD1  74 47                           je 0x1409cfc1a
009CFBD3  41 83 F9 01                     cmp r9d, 1
009CFBD7  0F 85 F9 B7 FF FF               jne 0x1409cb3d6
009CFBDD  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
009CFBE5  49 8B CC                        mov rcx, r12
009CFBE8  E8 7F 60 E6 FF                  call 0x140835c6c
009CFBED  83 F8 FF                        cmp eax, -1
009CFBF0  0F 84 49 DD FF FF               je 0x1409cd93f
009CFBF6  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
009CFBFE  49 8B CC                        mov rcx, r12
009CFC01  E8 66 60 E6 FF                  call 0x140835c6c
009CFC06  85 C0                           test eax, eax
009CFC08  8B C6                           mov eax, esi
009CFC0A  0F 85 88 B7 FF FF               jne 0x1409cb398
009CFC10  B8 01 00 00 00                  mov eax, 1
009CFC15  E9 7E B7 FF FF                  jmp 0x1409cb398
009CFC1A  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
009CFC22  49 8B CC                        mov rcx, r12
009CFC25  E8 42 60 E6 FF                  call 0x140835c6c
009CFC2A  83 F8 01                        cmp eax, 1
009CFC2D  0F 84 0C DD FF FF               je 0x1409cd93f
009CFC33  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
009CFC3B  49 8B CC                        mov rcx, r12
009CFC3E  E8 29 60 E6 FF                  call 0x140835c6c
009CFC43  85 C0                           test eax, eax
009CFC45  8B C6                           mov eax, esi
009CFC47  0F 85 4B B7 FF FF               jne 0x1409cb398
009CFC4D  B8 01 00 00 00                  mov eax, 1
009CFC52  E9 41 B7 FF FF                  jmp 0x1409cb398
009CFC57  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
009CFC5F  49 8B CC                        mov rcx, r12
009CFC62  E8 05 60 E6 FF                  call 0x140835c6c
009CFC67  8B CE                           mov ecx, esi
009CFC69  83 F8 FF                        cmp eax, -1
009CFC6C  0F 94 C1                        sete cl
009CFC6F  E9 01 BB FF FF                  jmp 0x1409cb775
009CFC74  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
009CFC7C  49 8B CC                        mov rcx, r12
009CFC7F  E8 E8 5F E6 FF                  call 0x140835c6c
009CFC84  8B CE                           mov ecx, esi
009CFC86  83 F8 01                        cmp eax, 1
009CFC89  0F 94 C1                        sete cl
009CFC8C  E9 E4 BA FF FF                  jmp 0x1409cb775
009CFC91  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
009CFC99  49 8B CC                        mov rcx, r12
009CFC9C  E8 CB 5F E6 FF                  call 0x140835c6c
009CFCA1  8B CE                           mov ecx, esi
009CFCA3  85 C0                           test eax, eax
009CFCA5  0F 94 C1                        sete cl
009CFCA8  E9 C8 BA FF FF                  jmp 0x1409cb775
009CFCAD  83 F9 15                        cmp ecx, 0x15
009CFCB0  0F 85 20 B7 FF FF               jne 0x1409cb3d6
009CFCB6  41 83 F9 02                     cmp r9d, 2
009CFCBA  0F 85 16 B7 FF FF               jne 0x1409cb3d6
009CFCC0  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
009CFCC8  8B 42 10                        mov eax, dword ptr [rdx + 0x10]
009CFCCB  41 39 44 24 10                  cmp dword ptr [r12 + 0x10], eax
009CFCD0  0F 85 C0 B6 FF FF               jne 0x1409cb396
009CFCD6  49 8B 0C 24                     mov rcx, qword ptr [r12]
009CFCDA  48 2B 0A                        sub rcx, qword ptr [rdx]
009CFCDD  75 09                           jne 0x1409cfce8
009CFCDF  49 8B 4C 24 08                  mov rcx, qword ptr [r12 + 8]
009CFCE4  48 2B 4A 08                     sub rcx, qword ptr [rdx + 8]
009CFCE8  48 85 C9                        test rcx, rcx
009CFCEB  E9 52 C8 FF FF                  jmp 0x1409cc542
009CFCF0  83 F9 16                        cmp ecx, 0x16
009CFCF3  EB 03                           jmp 0x1409cfcf8
009CFCF5  83 F9 18                        cmp ecx, 0x18
009CFCF8  0F 85 D8 B6 FF FF               jne 0x1409cb3d6
009CFCFE  41 83 F9 02                     cmp r9d, 2
009CFD02  0F 85 CE B6 FF FF               jne 0x1409cb3d6
009CFD08  8B D6                           mov edx, esi
009CFD0A  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009CFD12  8B 08                           mov ecx, dword ptr [rax]
009CFD14  41 39 0C 24                     cmp dword ptr [r12], ecx
009CFD18  0F 94 C2                        sete dl
009CFD1B  41 89 17                        mov dword ptr [r15], edx
009CFD1E  E9 78 B6 FF FF                  jmp 0x1409cb39b
009CFD23  83 F9 19                        cmp ecx, 0x19
009CFD26  74 09                           je 0x1409cfd31
009CFD28  83 F9 12                        cmp ecx, 0x12
009CFD2B  0F 85 A5 B6 FF FF               jne 0x1409cb3d6
009CFD31  41 83 F9 02                     cmp r9d, 2
009CFD35  0F 85 9B B6 FF FF               jne 0x1409cb3d6
009CFD3B  45 85 C0                        test r8d, r8d
009CFD3E  0F 84 CD DB FF FF               je 0x1409cd911
009CFD44  45 85 DB                        test r11d, r11d
009CFD47  0F 84 4E B6 FF FF               je 0x1409cb39b
009CFD4D  44 3B 9C 24 90 00 00 00         cmp r11d, dword ptr [rsp + 0x90]
009CFD55  0F 85 40 B6 FF FF               jne 0x1409cb39b
009CFD5B  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
009CFD63  49 8B CC                        mov rcx, r12
009CFD66  E8 15 03 B3 FF                  call 0x140500080
009CFD6B  8B CE                           mov ecx, esi
009CFD6D  85 C0                           test eax, eax
009CFD6F  0F 94 C1                        sete cl
009CFD72  41 89 0F                        mov dword ptr [r15], ecx
009CFD75  E9 21 B6 FF FF                  jmp 0x1409cb39b
009CFD7A  41 81 F9 00 20 00 00            cmp r9d, 0x2000
009CFD81  74 16                           je 0x1409cfd99
009CFD83  41 81 F9 00 30 00 00            cmp r9d, 0x3000
009CFD8A  74 0D                           je 0x1409cfd99
009CFD8C  41 81 F9 00 40 00 00            cmp r9d, 0x4000
009CFD93  0F 85 3D B6 FF FF               jne 0x1409cb3d6
009CFD99  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
009CFD9E  45 8B C8                        mov r9d, r8d
009CFDA1  4C 8B 84 24 88 00 00 00         mov r8, qword ptr [rsp + 0x88]
009CFDA9  8B D1                           mov edx, ecx
009CFDAB  49 8B CC                        mov rcx, r12
009CFDAE  E8 F5 5F E6 FF                  call 0x140835da8
009CFDB3  E9 E0 B5 FF FF                  jmp 0x1409cb398
009CFDB8  8D 41 F3                        lea eax, [rcx - 0xd]
009CFDBB  A9 FF EF FF FF                  test eax, 0xffffefff
009CFDC0  0F 85 10 B6 FF FF               jne 0x1409cb3d6
009CFDC6  41 83 F9 02                     cmp r9d, 2
009CFDCA  0F 84 41 DB FF FF               je 0x1409cd911
009CFDD0  41 81 F9 00 00 00 10            cmp r9d, 0x10000000
009CFDD7  0F 85 F9 B5 FF FF               jne 0x1409cb3d6
009CFDDD  48 C7 44 24 20 10 00 00 00      mov qword ptr [rsp + 0x20], 0x10
009CFDE6  44 8B 8C 24 90 00 00 00         mov r9d, dword ptr [rsp + 0x90]
009CFDEE  4C 8B 84 24 88 00 00 00         mov r8, qword ptr [rsp + 0x88]
009CFDF6  41 8B D3                        mov edx, r11d
009CFDF9  49 8B CC                        mov rcx, r12
009CFDFC  E8 5B 32 CD FF                  call 0x1406a305c
009CFE01  E9 92 B5 FF FF                  jmp 0x1409cb398
009CFE06  EB 12                           jmp 0x1409cfe1a
009CFE08  33 F6                           xor esi, esi
009CFE0A  4C 8B BC 24 98 00 00 00         mov r15, qword ptr [rsp + 0x98]
009CFE12  8B 7C 24 30                     mov edi, dword ptr [rsp + 0x30]
009CFE16  8B 5C 24 78                     mov ebx, dword ptr [rsp + 0x78]
009CFE1A  85 DB                           test ebx, ebx
009CFE1C  75 17                           jne 0x1409cfe35
009CFE1E  8B C7                           mov eax, edi
009CFE20  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
009CFE25  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
009CFE2A  48 83 C4 40                     add rsp, 0x40
009CFE2E  41 5F                           pop r15
009CFE30  41 5C                           pop r12
009CFE32  5F                              pop rdi
009CFE33  C3                              ret
009CFE34  CC                              int3
009CFE35  41 83 3F 00                     cmp dword ptr [r15], 0
009CFE39  40 0F 94 C6                     sete sil
009CFE3D  41 89 37                        mov dword ptr [r15], esi
009CFE40  EB DC                           jmp 0x1409cfe1e
009CFE42  66 90                           nop
009CFE44  D6                              .byte 0xd6
009CFE45  B3 9C                           mov bl, 0x9c
009CFE47  00 A2 C5 9C 00 59               add byte ptr [rdx + 0x59009cc5], ah
009CFE4D  B4 9C                           mov ah, 0x9c
009CFE4F  00 FE                           add dh, bh
009CFE51  B4 9C                           mov ah, 0x9c
009CFE53  00 D2                           add dl, dl
009CFE55  B5 9C                           mov ch, 0x9c
009CFE57  00 68 B5                        add byte ptr [rax - 0x4b], ch
009CFE5A  9C                              pushfq
009CFE5B  00 7F B6                        add byte ptr [rdi - 0x4a], bh
009CFE5E  9C                              pushfq
009CFE5F  00 D8                           add al, bl
009CFE61  B6 9C                           mov dh, 0x9c
009CFE63  00 A6 DE 9C 00 E0               add byte ptr [rsi - 0x1fff6322], ah
009CFE69  D9 9C 00 BC D8 9C 00            fstp dword ptr [rax + rax + 0x9cd8bc]
009CFE70  D6                              .byte 0xd6
009CFE71  F0                              .byte 0xf0
009CFE72  9C                              pushfq
009CFE73  00 EF                           add bh, ch
009CFE75  D8 9C 00 D6 B3 9C 00            fcomp dword ptr [rax + rax + 0x9cb3d6]
009CFE7C  B2 F7                           mov dl, 0xf7
009CFE7E  9C                              pushfq
009CFE7F  00 3B                           add byte ptr [rbx], bh
009CFE81  F9                              stc
009CFE82  9C                              pushfq
009CFE83  00 A6 FB 9C 00 CF               add byte ptr [rsi - 0x30ff6305], ah
009CFE89  B4 9C                           mov ah, 0x9c
009CFE8B  00 CD                           add ch, cl
009CFE8D  B3 9C                           mov bl, 0x9c
009CFE8F  00 D6                           add dh, dl
009CFE91  B3 9C                           mov bl, 0x9c
009CFE93  00 D6                           add dh, dl
009CFE95  B3 9C                           mov bl, 0x9c
009CFE97  00 AD FC 9C 00 F0               add byte ptr [rbp - 0xfff6304], ch
009CFE9D  FC                              cld
009CFE9E  9C                              pushfq
009CFE9F  00 49 D9                        add byte ptr [rcx - 0x27], cl
009CFEA2  9C                              pushfq
009CFEA3  00 F5                           add ch, dh
009CFEA5  FC                              cld
009CFEA6  9C                              pushfq
009CFEA7  00 23                           add byte ptr [rbx], ah
009CFEA9  FD                              std
009CFEAA  9C                              pushfq
009CFEAB  00 36                           add byte ptr [rsi], dh
009CFEAD  BC 9C 00 22 B8                  mov esp, 0xb822009c
009CFEB2  9C                              pushfq
009CFEB3  00 70 B8                        add byte ptr [rax - 0x48], dh
009CFEB6  9C                              pushfq
009CFEB7  00 7D B7                        add byte ptr [rbp - 0x49], bh
009CFEBA  9C                              pushfq
009CFEBB  00 BE BC 9C 00 02               add byte ptr [rsi + 0x2009cbc], bh
009CFEC1  BD 9C 00 46 BD                  mov ebp, 0xbd46009c
009CFEC6  9C                              pushfq
009CFEC7  00 8B BD 9C 00 75               add byte ptr [rbx + 0x75009cbd], cl
009CFECD  B4 9C                           mov ah, 0x9c
009CFECF  00 B5 B8 9C 00 D6               add byte ptr [rbp - 0x29ff6348], dh
009CFED5  B3 9C                           mov bl, 0x9c
009CFED7  00 D6                           add dh, dl
009CFED9  B3 9C                           mov bl, 0x9c
009CFEDB  00 46 BD                        add byte ptr [rsi - 0x43], al
009CFEDE  9C                              pushfq
009CFEDF  00 B5 B8 9C 00 1A               add byte ptr [rbp + 0x1a009cb8], dh
009CFEE5  B5 9C                           mov ch, 0x9c
009CFEE7  00 7A BC                        add byte ptr [rdx - 0x44], bh
009CFEEA  9C                              pushfq
009CFEEB  00 03                           add byte ptr [rbx], al
009CFEED  B9 9C 00 48 B9                  mov ecx, 0xb948009c
009CFEF2  9C                              pushfq
009CFEF3  00 D0                           add al, dl
009CFEF5  BD 9C 00 14 BE                  mov ebp, 0xbe14009c
009CFEFA  9C                              pushfq
009CFEFB  00 58 BE                        add byte ptr [rax - 0x42], bl
009CFEFE  9C                              pushfq
009CFEFF  00 9D BE 9C 00 8D               add byte ptr [rbp - 0x72ff6342], bl
009CFF05  B9 9C 00 BF B9                  mov ecx, 0xb9bf009c
009CFF0A  9C                              pushfq
009CFF0B  00 D6                           add dh, dl
009CFF0D  B3 9C                           mov bl, 0x9c
009CFF0F  00 D6                           add dh, dl
009CFF11  B3 9C                           mov bl, 0x9c
009CFF13  00 58 BE                        add byte ptr [rax - 0x42], bl
009CFF16  9C                              pushfq
009CFF17  00 BF B9 9C 00 D7               add byte ptr [rdi - 0x28ff6347], bh
009CFF1D  BA 9C 00 37 C0                  mov edx, 0xc037009c
009CFF22  9C                              pushfq
009CFF23  00 1B                           add byte ptr [rbx], bl
009CFF25  BB 9C 00 A3 BB                  mov ebx, 0xbba3009c
009CFF2A  9C                              pushfq
009CFF2B  00 79 C0                        add byte ptr [rcx - 0x40], bh
009CFF2E  9C                              pushfq
009CFF2F  00 BD C0 9C 00 01               add byte ptr [rbp + 0x1009cc0], bh
009CFF35  C1 9C 00 46 C1 9C 00 5F         rcr dword ptr [rax + rax + 0x9cc146], 0x5f
009CFF3D  BB 9C 00 84 B5                  mov ebx, 0xb584009c
009CFF42  9C                              pushfq
009CFF43  00 D6                           add dh, dl
009CFF45  B3 9C                           mov bl, 0x9c
009CFF47  00 D6                           add dh, dl
009CFF49  B3 9C                           mov bl, 0x9c
009CFF4B  00 01                           add byte ptr [rcx], al
009CFF4D  C1 9C 00 84 B5 9C 00 0D         rcr dword ptr [rax + rax + 0x9cb584], 0xd
009CFF55  BA 9C 00 E2 BE                  mov edx, 0xbee2009c
009CFF5A  9C                              pushfq
009CFF5B  00 24 BF                        add byte ptr [rdi + rdi*4], ah
009CFF5E  9C                              pushfq
009CFF5F  00 4F BA                        add byte ptr [rdi - 0x46], cl
009CFF62  9C                              pushfq
009CFF63  00 F2                           add dl, dh
009CFF65  BB 9C 00 69 BF                  mov ebx, 0xbf69009c
009CFF6A  9C                              pushfq
009CFF6B  00 AD BF 9C 00 F2               add byte ptr [rbp - 0xdff6341], ch
009CFF71  BF 9C 00 93 BA                  mov edi, 0xba93009c
009CFF76  9C                              pushfq
009CFF77  00 EE                           add dh, ch
009CFF79  B5 9C                           mov ch, 0x9c
009CFF7B  00 D6                           add dh, dl
009CFF7D  B3 9C                           mov bl, 0x9c
009CFF7F  00 D6                           add dh, dl
009CFF81  B3 9C                           mov bl, 0x9c
009CFF83  00 AD BF 9C 00 EE               add byte ptr [rbp - 0x11ff6341], ch
009CFF89  B5 9C                           mov ch, 0x9c
009CFF8B  00 8B C1 9C 00 CC               add byte ptr [rbx - 0x33ff633f], cl
009CFF91  C1 9C 00 0D C2 9C 00 4E         rcr dword ptr [rax + rax + 0x9cc20d], 0x4e
009CFF99  C2 9C 00                        ret 0x9c
009CFF9C  8F C2                           pop rdx
009CFF9E  9C                              pushfq
009CFF9F  00 FC                           add ah, bh
009CFFA1  D9 9C 00 D2 C2 9C 00            fstp dword ptr [rax + rax + 0x9cc2d2]
009CFFA8  16                              .byte 0x16
009CFFA9  C3                              ret
009CFFAA  9C                              pushfq
009CFFAB  00 CB                           add bl, cl
009CFFAD  B7 9C                           mov bh, 0x9c
009CFFAF  00 9B B6 9C 00 D6               add byte ptr [rbx - 0x29ff634a], bl
009CFFB5  B3 9C                           mov bl, 0x9c
009CFFB7  00 D6                           add dh, dl
009CFFB9  B3 9C                           mov bl, 0x9c
009CFFBB  00 D2                           add dl, dl
009CFFBD  C2 9C 00                        ret 0x9c
009CFFC0  9B                              wait
009CFFC1  B6 9C                           mov dh, 0x9c
009CFFC3  00 64 DC 9C                     add byte ptr [rsp + rbx*8 - 0x64], ah
009CFFC7  00 EE                           add dh, ch
009CFFC9  DC 9C 00 78 DD 9C 00            fcomp qword ptr [rax + rax + 0x9cdd78]
009CFFD0  FC                              cld
009CFFD1  D9 9C 00 FC D9 9C 00            fstp dword ptr [rax + rax + 0x9cd9fc]
009CFFD8  5A                              pop rdx
009CFFD9  C3                              ret
009CFFDA  9C                              pushfq
009CFFDB  00 D6                           add dh, dl
009CFFDD  B3 9C                           mov bl, 0x9c
009CFFDF  00 25 B7 9C 00 23               add byte ptr [rip + 0x23009cb7], ah
009CFFE5  C4                              .byte 0xc4
009CFFE6  9C                              pushfq
009CFFE7  00 CC                           add ah, cl
009CFFE9  E4 9C                           in al, 0x9c
009CFFEB  00 5A E5                        add byte ptr [rdx - 0x1b], bl
009CFFEE  9C                              pushfq
009CFFEF  00 E4                           add ah, ah
009CFFF1  E5 9C                           in eax, 0x9c
009CFFF3  00 72 E6                        add byte ptr [rdx - 0x1a], dh
009CFFF6  9C                              pushfq
009CFFF7  00 FC                           add ah, bh
009CFFF9  E6 9C                           out 0x9c, al
009CFFFB  00 86 E7 9C 00 5F               add byte ptr [rsi + 0x5f009ce7], al
009D0001  E3 9C                           jrcxz 0x1409cff9f
009D0003  00 5F E3                        add byte ptr [rdi - 0x1d], bl
009D0006  9C                              pushfq
009D0007  00 0C E8                        add byte ptr [rax + rbp*8], cl
009D000A  9C                              pushfq
009D000B  00 2E                           add byte ptr [rsi], ch
009D000D  E9 9C 00 D6 B3                  jmp 0xf47300ae
009D0012  9C                              pushfq
009D0013  00 D6                           add dh, dl
009D0015  B3 9C                           mov bl, 0x9c
009D0017  00 5F E3                        add byte ptr [rdi - 0x1d], bl
009D001A  9C                              pushfq
009D001B  00 2E                           add byte ptr [rsi], ch
009D001D  E9 9C 00 0D DF                  jmp 0x11faa00be
009D0022  9C                              pushfq
009D0023  00 C2                           add dl, al
009D0025  DE 9C 00 25 E0 9C 00            ficomp word ptr [rax + rax + 0x9ce025]
009D002C  CD E0                           int 0xe0
009D002E  9C                              pushfq
009D002F  00 70 E1                        add byte ptr [rax - 0x1f], dh
009D0032  9C                              pushfq
009D0033  00 13                           add byte ptr [rbx], dl
009D0035  E2 9C                           loop 0x1409cffd3
009D0037  00 AD E2 9C 00 5F               add byte ptr [rbp + 0x5f009ce2], ch
009D003D  E3 9C                           jrcxz 0x1409cffdb
009D003F  00 F1                           add cl, dh
009D0041  E3 9C                           jrcxz 0x1409cffdf
009D0043  00 64 E4 9C                     add byte ptr [rsp + riz*8 - 0x64], ah
009D0047  00 D6                           add dh, dl
009D0049  B3 9C                           mov bl, 0x9c
009D004B  00 D6                           add dh, dl
009D004D  B3 9C                           mov bl, 0x9c
009D004F  00 AD E2 9C 00 64               add byte ptr [rbp + 0x64009ce2], ch
009D0055  E4 9C                           in al, 0x9c
009D0057  00 64 EA 9C                     add byte ptr [rdx + rbp*8 - 0x64], ah
009D005B  00 D1                           add cl, dl
009D005D  EB 9C                           jmp 0x1409cfffb
009D005F  00 62 EC                        add byte ptr [rdx - 0x14], ah
009D0062  9C                              pushfq
009D0063  00 F3                           add bl, dh
009D0065  EC                              in al, dx
009D0066  9C                              pushfq
009D0067  00 6C ED 9C                     add byte ptr [rbp + rbp*8 - 0x64], ch
009D006B  00 D6                           add dh, dl
009D006D  B3 9C                           mov bl, 0x9c
009D006F  00 DC                           add ah, bl
009D0071  ED                              in eax, dx
009D0072  9C                              pushfq
009D0073  00 71 EE                        add byte ptr [rcx - 0x12], dh
009D0076  9C                              pushfq
009D0077  00 4C EF 9C                     add byte ptr [rdi + rbp*8 - 0x64], cl
009D007B  00 C6                           add dh, al
009D007D  EF                              out dx, eax
009D007E  9C                              pushfq
009D007F  00 D6                           add dh, dl
009D0081  B3 9C                           mov bl, 0x9c
009D0083  00 D6                           add dh, dl
009D0085  B3 9C                           mov bl, 0x9c
009D0087  00 DC                           add ah, bl
009D0089  ED                              in eax, dx
009D008A  9C                              pushfq
009D008B  00 C6                           add dh, al
009D008D  EF                              out dx, eax
009D008E  9C                              pushfq
009D008F  00 F2                           add dl, dh
009D0091  F0                              .byte 0xf0
009D0092  9C                              pushfq
009D0093  00 72 F2                        add byte ptr [rdx - 0xe], dh
009D0096  9C                              pushfq
009D0097  00 00                           add byte ptr [rax], al
009D0099  F3 9C                           pushfq
009D009B  00 8E F3 9C 00 F8               add byte ptr [rsi - 0x7ff630d], cl
009D00A1  F3 9C                           pushfq
009D00A3  00 5C F4 9C                     add byte ptr [rsp + rsi*8 - 0x64], bl
009D00A7  00 01                           add byte ptr [rcx], al
009D00A9  F5                              cmc
009D00AA  9C                              pushfq
009D00AB  00 98 F5 9C 00 DF               add byte ptr [rax - 0x20ff630b], bl
009D00B1  F6 9C 00 41 F7 9C 00            neg byte ptr [rax + rax + 0x9cf741]
009D00B8  D6                              .byte 0xd6
009D00B9  B3 9C                           mov bl, 0x9c
009D00BB  00 D6                           add dh, dl
009D00BD  B3 9C                           mov bl, 0x9c
009D00BF  00 01                           add byte ptr [rcx], al
009D00C1  F5                              cmc
009D00C2  9C                              pushfq
009D00C3  00 41 F7                        add byte ptr [rcx - 9], al
009D00C6  9C                              pushfq
009D00C7  00 0D DF 9C 00 CE               add byte ptr [rip - 0x31ff6321], cl
009D00CD  F7 9C 00 10 F8 9C 00            neg dword ptr [rax + rax + 0x9cf810]
009D00D4  53                              push rbx
009D00D5  F8                              clc
009D00D6  9C                              pushfq
009D00D7  00 95 F8 9C 00 D7               add byte ptr [rbp - 0x28ff6308], dl
009D00DD  F8                              clc
009D00DE  9C                              pushfq
009D00DF  00 AD E2 9C 00 5F               add byte ptr [rbp + 0x5f009ce2], ch
009D00E5  E3 9C                           jrcxz 0x1409d0083
009D00E7  00 F1                           add cl, dh
009D00E9  E3 9C                           jrcxz 0x1409d0087
009D00EB  00 0E                           add byte ptr [rsi], cl
009D00ED  F9                              stc
009D00EE  9C                              pushfq
009D00EF  00 D6                           add dh, dl
009D00F1  B3 9C                           mov bl, 0x9c
009D00F3  00 D6                           add dh, dl
009D00F5  B3 9C                           mov bl, 0x9c
009D00F7  00 AD E2 9C 00 0E               add byte ptr [rbp + 0xe009ce2], ch
009D00FD  F9                              stc
009D00FE  9C                              pushfq
009D00FF  00 57 F9                        add byte ptr [rdi - 7], dl
009D0102  9C                              pushfq
009D0103  00 84 F9 9C 00 C6 F9            add byte ptr [rcx + rdi*8 - 0x639ff64], al
009D010A  9C                              pushfq
009D010B  00 08                           add byte ptr [rax], cl
009D010D  FA                              cli
009D010E  9C                              pushfq
009D010F  00 3F                           add byte ptr [rdi], bh
009D0111  FA                              cli
009D0112  9C                              pushfq
009D0113  00 76 FA                        add byte ptr [rsi - 6], dh
009D0116  9C                              pushfq
009D0117  00 BF FA 9C 00 06               add byte ptr [rdi + 0x6009cfa], bh
009D011D  FB                              sti
009D011E  9C                              pushfq
009D011F  00 6F FB                        add byte ptr [rdi - 5], ch
009D0122  9C                              pushfq
009D0123  00 41 F7                        add byte ptr [rcx - 9], al
009D0126  9C                              pushfq
009D0127  00 D6                           add dh, dl
009D0129  B3 9C                           mov bl, 0x9c
009D012B  00 D6                           add dh, dl
009D012D  B3 9C                           mov bl, 0x9c
009D012F  00 BF FA 9C 00 41               add byte ptr [rdi + 0x41009cfa], bh
009D0135  F7                              .byte 0xf7
009D0136  9C                              pushfq
009D0137  00                              .byte 0x00
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PropertyEval(int a1, __int64 a2, int a3, int a4, unsigned int a5, __int64 a6, unsigned int a7, __int64 a8)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m28;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (64);
    v_rsi = 0;
    v_stack_m28 = 0;
    v_rbx = (unsigned int)(((unsigned int)(a4)) & (0x10000ULL));
    v_stack_p20 = (unsigned int)(v_rbx);
    a3 = (unsigned int)(((unsigned int)(a4)) & (0x20000ULL));
    a4 = (unsigned int)((a4) & (0xF000FFFFULL));
    *(unsigned int *)(a8) = 0;
    if (a3 != 0) goto loc_009CDA49;
loc_009CB356:
    if (a4 == 1) goto loc_009CB3E1;
    if (a1 == 0) goto loc_009CFE06;
    if ((unsigned int)((unsigned int)(a5)) == 0) goto loc_009CFE06;
    if (((unsigned int)((unsigned int)(a1))) != 13) goto loc_009CB3A0;
    if (((unsigned int)((unsigned int)(a5))) != ((unsigned int)((unsigned int)(a1)))) goto loc_009CB3D6;
    if (a4 != 2) goto loc_009CB3D6;
    if ((*(unsigned int *)(a2)) == ((unsigned int)((unsigned int)(*(unsigned int *)(a6))))) goto loc_009CB3F0;
loc_009CB396:
loc_009CB398:
    *(unsigned int *)(a8) = 0;
loc_009CB39B:
    goto loc_009CFE1A;
loc_009CB3A0:
    if (((unsigned int)((unsigned int)(a1))) > 0x1003ULL) goto loc_009CB40F;
    if (((unsigned int)((unsigned int)(a1))) == 0x1003ULL) goto loc_009CD8F8;
    if (((unsigned int)((unsigned int)(a1))) > 25) goto loc_009CB3D6;
    result = ((unsigned int)(*(unsigned int *)(v_rip - 10269628 + (unsigned int)(a1) * 4 + 10288708))) + (v_rip - 10269628);
loc_009CB3D6:
    v_stack_m28 = (unsigned int)((unsigned int)(0xC00000BBULL));
    goto loc_009CB39B;
loc_009CB3E1:
    result = ((unsigned int)(a6) != 0) ? 1 : 0;
    *(unsigned int *)(a8) = (unsigned int)(result);
    goto loc_009CFE1A;
loc_009CB3F0:
    if ((*(unsigned int *)(v_rip - 10269628 + 4)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a6 + 4))))) goto loc_009CB396;
    if ((*(unsigned int *)(v_rip - 10269628 + 8)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a6 + 8))))) goto loc_009CB396;
    if ((*(unsigned int *)(v_rip - 10269628 + 12)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a6 + 12))))) goto loc_009CB396;
    goto loc_009CB398;
loc_009CB40F:
    if (((unsigned int)((unsigned int)(a1))) == 0x100DULL) goto loc_009CFDB8;
    if (((unsigned int)((unsigned int)(a1))) != 0x2012ULL) goto loc_009CB3D6;
    if ((((unsigned int)(a6 - 18)) & (0xFFFFDFFFULL)) != 0) goto loc_009CB3D6;
    if (a4 != 0x1000ULL) goto loc_009CD8FE;
    result = StringListContains(a2, (unsigned int)((unsigned int)(a6)), a6, (unsigned int)(a3));
    *(unsigned int *)(a8) = (unsigned int)(result);
    goto loc_009CB39B;
loc_009CD8F8:
    goto loc_009CD90B;
loc_009CD8FE:
    if (((unsigned int)((unsigned int)(a3))) != 2) goto loc_009CFD7A;
loc_009CD90B:
    if ((unsigned int)(a6) != 0) goto loc_009CB3D6;
loc_009CD911:
    if (((unsigned int)((unsigned int)(a3))) != a7) goto loc_009CB396;
    if ((unsigned int)((unsigned int)(a3)) == 0) goto loc_009CD93F;
    result = memcmp(a2, a6, (unsigned int)(a3), (unsigned int)(a3));
    if ((unsigned int)(result) != 0) goto loc_009CB396;
loc_009CD93F:
    goto loc_009CB398;
loc_009CDA49:
    if (((unsigned int)((unsigned int)(a1))) == 0x2012ULL) goto loc_009CB356;
    if (((unsigned int)((unsigned int)(a1))) == 18) goto loc_009CB356;
    if (((unsigned int)((unsigned int)(a1))) == 25) goto loc_009CB356;
    v_stack_m28 = (unsigned int)((unsigned int)(0xC00000BBULL));
    goto loc_009CFE1A;
loc_009CFD7A:
    if (((unsigned int)((unsigned int)(a3))) == 0x2000ULL) goto loc_009CFD99;
    if (((unsigned int)((unsigned int)(a3))) == 0x3000ULL) goto loc_009CFD99;
    if (((unsigned int)((unsigned int)(a3))) != 0x4000ULL) goto loc_009CB3D6;
loc_009CFD99:
    v_stack_m38 = (unsigned int)((unsigned int)(a3));
    result = StringListElementSubstringMatch(a2, (unsigned int)((unsigned int)(a2)), a6, (unsigned int)((unsigned int)((unsigned int)(a3))));
    goto loc_009CB398;
loc_009CFDB8:
    if ((((unsigned int)(a2 - 13)) & (0xFFFFEFFFULL)) != 0) goto loc_009CB3D6;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a3))))) == 2) goto loc_009CD911;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a3))))) != 0x10000000ULL) goto loc_009CB3D6;
    v_stack_m38 = 16;
    result = ArrayContains(a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a6, (unsigned int)(a7));
    goto loc_009CB398;
loc_009CFE06:
    goto loc_009CFE1A;
loc_009CFE1A:
    if ((unsigned int)(v_rbx) != 0) goto loc_009CFE35;
loc_009CFE1E:
    v_rsp = (v_rsp) + (64);
    return (unsigned int)((unsigned int)((unsigned int)(0xC00000BBULL)));
loc_009CFE35:
    v_rsi = ((*(unsigned int *)(a8)) == 0) ? 1 : 0;
    *(unsigned int *)(a8) = (unsigned int)(v_rsi);
    goto loc_009CFE1E;
}
```

## 5. (Beta) C Style

```c
int64_t PropertyEval(int32_t Arg1, void *Arg2, int32_t Arg3, int32_t Arg4, uint32_t Arg5, void *Arg6, uint32_t Arg7, void *Arg8)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg6 = (uint8_t *)Arg6;
    uint8_t *arg8 = (uint8_t *)Arg8;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m28;
    uint32_t v_stack_m38;
    uint64_t v_stack_p10;
    uint32_t v_stack_p20;
    uint64_t v_stack_p30;
    uint32_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (64);
    local_rsi = 0;
    v_stack_m28 = 0;
    local_rbx = (uint32_t)(((uint32_t)(Arg4)) & (0x10000ULL));
    v_stack_p20 = (uint32_t)(local_rbx);
    Arg3 = (uint32_t)(((uint32_t)(Arg4)) & (0x20000ULL));
    Arg4 = (uint32_t)((Arg4) & (0xF000FFFFULL));
    *(uint32_t *)(arg8) = 0;
    if (Arg3 != 0) goto loc_009CDA49;
loc_009CB356:
    if (Arg4 == 1) goto loc_009CB3E1;
    if (Arg1 == 0) goto loc_009CFE06;
    if ((uint32_t)((uint32_t)(Arg5)) == 0) goto loc_009CFE06;
    if (((uint32_t)((uint32_t)(Arg1))) != 13) goto loc_009CB3A0;
    if (((uint32_t)((uint32_t)(Arg5))) != ((uint32_t)((uint32_t)(Arg1)))) goto loc_009CB3D6;
    if (Arg4 != 2) goto loc_009CB3D6;
    if ((*(uint32_t *)(arg2)) == ((uint32_t)((uint32_t)(*(uint32_t *)(arg6))))) goto loc_009CB3F0;
loc_009CB396:
loc_009CB398:
    *(uint32_t *)(arg8) = 0;
loc_009CB39B:
    goto loc_009CFE1A;
loc_009CB3A0:
    if (((uint32_t)((uint32_t)(Arg1))) > 0x1003ULL) goto loc_009CB40F;
    if (((uint32_t)((uint32_t)(Arg1))) == 0x1003ULL) goto loc_009CD8F8;
    if (((uint32_t)((uint32_t)(Arg1))) > 25) goto loc_009CB3D6;
    result = ((uint32_t)(*(uint32_t *)(v_rip - 0x9CB3BC + (uint32_t)(Arg1) * 4 + 0x9CFE44))) + (v_rip - 10269628);
loc_009CB3D6:
    v_stack_m28 = (uint32_t)((uint32_t)(0xC00000BBULL));
    goto loc_009CB39B;
loc_009CB3E1:
    result = ((uint32_t)(Arg6) != 0) ? 1 : 0;
    *(uint32_t *)(arg8) = (uint32_t)(result);
    goto loc_009CFE1A;
loc_009CB3F0:
    if ((*(uint32_t *)(v_rip - 0x9CB3BC + 0x4)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg6 + 0x4))))) goto loc_009CB396;
    if ((*(uint32_t *)(v_rip - 0x9CB3BC + 0x8)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg6 + 0x8))))) goto loc_009CB396;
    if ((*(uint32_t *)(v_rip - 0x9CB3BC + 0xC)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg6 + 0xC))))) goto loc_009CB396;
    goto loc_009CB398;
loc_009CB40F:
    if (((uint32_t)((uint32_t)(Arg1))) == 0x100DULL) goto loc_009CFDB8;
    if (((uint32_t)((uint32_t)(Arg1))) != 0x2012ULL) goto loc_009CB3D6;
    if ((((uint32_t)(Arg6 - 18)) & (0xFFFFDFFFULL)) != 0) goto loc_009CB3D6;
    if (Arg4 != 0x1000ULL) goto loc_009CD8FE;
    result = StringListContains(Arg2, (uint32_t)((uint32_t)(Arg6)), Arg6, (uint32_t)(Arg3));
    *(uint32_t *)(arg8) = (uint32_t)(result);
    goto loc_009CB39B;
loc_009CD8F8:
    goto loc_009CD90B;
loc_009CD8FE:
    if (((uint32_t)((uint32_t)(Arg3))) != 2) goto loc_009CFD7A;
loc_009CD90B:
    if ((uint32_t)(Arg6) != 0) goto loc_009CB3D6;
loc_009CD911:
    if (((uint32_t)((uint32_t)(Arg3))) != Arg7) goto loc_009CB396;
    if ((uint32_t)((uint32_t)(Arg3)) == 0) goto loc_009CD93F;
    result = memcmp(Arg2, Arg6, (uint32_t)(Arg3), (uint32_t)(Arg3));
    if ((uint32_t)(result) != 0) goto loc_009CB396;
loc_009CD93F:
    goto loc_009CB398;
loc_009CDA49:
    if (((uint32_t)((uint32_t)(Arg1))) == 0x2012ULL) goto loc_009CB356;
    if (((uint32_t)((uint32_t)(Arg1))) == 18) goto loc_009CB356;
    if (((uint32_t)((uint32_t)(Arg1))) == 25) goto loc_009CB356;
    v_stack_m28 = (uint32_t)((uint32_t)(0xC00000BBULL));
    goto loc_009CFE1A;
loc_009CFD7A:
    if (((uint32_t)((uint32_t)(Arg3))) == 0x2000ULL) goto loc_009CFD99;
    if (((uint32_t)((uint32_t)(Arg3))) == 0x3000ULL) goto loc_009CFD99;
    if (((uint32_t)((uint32_t)(Arg3))) != 0x4000ULL) goto loc_009CB3D6;
loc_009CFD99:
    v_stack_m38 = (uint32_t)((uint32_t)(Arg3));
    result = StringListElementSubstringMatch(Arg2, (uint32_t)((uint32_t)(Arg2)), Arg6, (uint32_t)((uint32_t)((uint32_t)(Arg3))));
    goto loc_009CB398;
loc_009CFDB8:
    if ((((uint32_t)(Arg2 - 13)) & (0xFFFFEFFFULL)) != 0) goto loc_009CB3D6;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg3))))) == 2) goto loc_009CD911;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg3))))) != 0x10000000ULL) goto loc_009CB3D6;
    v_stack_m38 = 16;
    result = ArrayContains(Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg6, (uint32_t)(Arg7));
    goto loc_009CB398;
loc_009CFE06:
    goto loc_009CFE1A;
loc_009CFE1A:
    if ((uint32_t)(local_rbx) != 0) goto loc_009CFE35;
loc_009CFE1E:
    local_rsp = (local_rsp) + (64);
    return (uint32_t)((uint32_t)((uint32_t)(0xC00000BBULL)));
loc_009CFE35:
    local_rsi = ((*(uint32_t *)(arg8)) == 0) ? 1 : 0;
    *(uint32_t *)(arg8) = (uint32_t)(local_rsi);
    goto loc_009CFE1E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x4` | `32` | `R` |
| `Arg2` | `+ 0x8` | `32` | `R` |
| `Arg2` | `+ 0xC` | `32` | `R` |
| `Arg6` | `+ 0x0` | `32` | `R` |
| `Arg6` | `+ 0x4` | `32` | `R` |
| `Arg6` | `+ 0x8` | `32` | `R` |
| `Arg6` | `+ 0xC` | `32` | `R` |
| `Arg8` | `+ 0x0` | `32` | `R` |
| `Arg8` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009CB300&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
