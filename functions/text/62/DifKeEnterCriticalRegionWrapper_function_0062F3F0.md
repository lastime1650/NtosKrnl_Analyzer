# DifKeEnterCriticalRegionWrapper

- RVA: `0x0062F3F0`–`0x0062F536` (길이 `326` bytes)
- VA: `0x000000014062F3F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A85B0`
- 디코드: `86`개 명령, `326/326` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062F40F` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062F437` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062F460` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062F487` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062F4A0` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062F4DA` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062F501` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062F51A` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062F444` → RVA `0x00F048B8` (`.data`; read)
- `0x0062F44D` → RVA `0x00F04980` (`.data`; read)
- `0x0062F459` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062F3F0  48 8B C4                        mov rax, rsp
0062F3F3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0062F3F7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0062F3FB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0062F3FF  41 56                           push r14
0062F401  48 83 EC 20                     sub rsp, 0x20
0062F405  48 83 60 08 00                  and qword ptr [rax + 8], 0
0062F40A  B9 1E 01 00 00                  mov ecx, 0x11e
0062F40F  E8 20 66 E6 FF                  call 0x140495a34
0062F414  48 8B F8                        mov rdi, rax
0062F417  48 85 C0                        test rax, rax
0062F41A  0F 84 85 00 00 00               je 0x14062f4a5
0062F420  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062F423  A8 18                           test al, 0x18
0062F425  74 0C                           je 0x14062f433
0062F427  48 8B 4C 24 28                  mov rcx, qword ptr [rsp + 0x28]
0062F42C  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
0062F431  EB 0E                           jmp 0x14062f441
0062F433  A8 04                           test al, 4
0062F435  74 0A                           je 0x14062f441
0062F437  E8 CC 47 EA FF                  call 0x1404d3c08
0062F43C  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0062F441  40 32 F6                        xor sil, sil
0062F444  40 38 35 6D 54 8D 00            cmp byte ptr [rip + 0x8d546d], sil
0062F44B  75 0C                           jne 0x14062f459
0062F44D  F7 05 29 55 8D 00 00 08 00 00   test dword ptr [rip + 0x8d5529], 0x800
0062F457  74 13                           je 0x14062f46c
0062F459  48 8D 0D 20 4A 8D 00            lea rcx, [rip + 0x8d4a20]
0062F460  E8 BB 71 BE FF                  call 0x140216620
0062F465  40 8A F0                        mov sil, al
0062F468  84 C0                           test al, al
0062F46A  74 39                           je 0x14062f4a5
0062F46C  4C 8D 77 20                     lea r14, [rdi + 0x20]
0062F470  49 8B 1E                        mov rbx, qword ptr [r14]
0062F473  EB 1A                           jmp 0x14062f48f
0062F475  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062F479  48 85 C0                        test rax, rax
0062F47C  74 0E                           je 0x14062f48c
0062F47E  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062F482  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
0062F487  E8 44 B6 08 00                  call 0x1406baad0
0062F48C  48 8B 1B                        mov rbx, qword ptr [rbx]
0062F48F  49 3B DE                        cmp rbx, r14
0062F492  75 E1                           jne 0x14062f475
0062F494  40 84 F6                        test sil, sil
0062F497  74 0C                           je 0x14062f4a5
0062F499  48 8D 0D E0 49 8D 00            lea rcx, [rip + 0x8d49e0]
0062F4A0  E8 DB A9 D1 FF                  call 0x140349e80
0062F4A5  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0062F4AE  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0062F4B5  90                              nop
0062F4B6  48 85 FF                        test rdi, rdi
0062F4B9  74 64                           je 0x14062f51f
0062F4BB  40 32 F6                        xor sil, sil
0062F4BE  40 38 35 F3 53 8D 00            cmp byte ptr [rip + 0x8d53f3], sil
0062F4C5  75 0C                           jne 0x14062f4d3
0062F4C7  F7 05 AF 54 8D 00 00 08 00 00   test dword ptr [rip + 0x8d54af], 0x800
0062F4D1  74 13                           je 0x14062f4e6
0062F4D3  48 8D 0D A6 49 8D 00            lea rcx, [rip + 0x8d49a6]
0062F4DA  E8 41 71 BE FF                  call 0x140216620
0062F4DF  40 8A F0                        mov sil, al
0062F4E2  84 C0                           test al, al
0062F4E4  74 39                           je 0x14062f51f
0062F4E6  48 83 C7 30                     add rdi, 0x30
0062F4EA  48 8B 1F                        mov rbx, qword ptr [rdi]
0062F4ED  EB 1A                           jmp 0x14062f509
0062F4EF  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062F4F3  48 85 C0                        test rax, rax
0062F4F6  74 0E                           je 0x14062f506
0062F4F8  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062F4FC  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
0062F501  E8 CA B5 08 00                  call 0x1406baad0
0062F506  48 8B 1B                        mov rbx, qword ptr [rbx]
0062F509  48 3B DF                        cmp rbx, rdi
0062F50C  75 E1                           jne 0x14062f4ef
0062F50E  40 84 F6                        test sil, sil
0062F511  74 0C                           je 0x14062f51f
0062F513  48 8D 0D 66 49 8D 00            lea rcx, [rip + 0x8d4966]
0062F51A  E8 61 A9 D1 FF                  call 0x140349e80
0062F51F  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
0062F524  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
0062F529  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
0062F52E  48 83 C4 20                     add rsp, 0x20
0062F532  41 5E                           pop r14
0062F534  C3                              ret
0062F535  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifKeEnterCriticalRegionWrapper(void)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (32);
    result = DifGetAPIThunkContextById(286, a2, a3, a4);
    if (result == 0) goto loc_0062F4A5;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062F433;
    v_stack_p8 = v_stack_p0;
    goto loc_0062F441;
loc_0062F433:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_p8 = result;
    }
    v_rsi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9262189)) != 0) goto loc_0062F459;
    if (((*(unsigned int *)(v_rip + 9262377)) & (0x800ULL)) == 0) goto loc_0062F46C;
loc_0062F459:
    result = ExAcquireRundownProtection(v_rip + 9259552, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062F4A5;
loc_0062F46C:
    goto loc_0062F48F;
loc_0062F475:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_p8;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062F48F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062F475;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9259488;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    if (result == 0) goto loc_0062F51F;
    v_rsi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9262067)) != 0) goto loc_0062F4D3;
    if (((*(unsigned int *)(v_rip + 9262255)) & (0x800ULL)) == 0) goto loc_0062F4E6;
loc_0062F4D3:
    result = ExAcquireRundownProtection(v_rip + 9259430, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062F51F;
loc_0062F4E6:
    v_rdi = (result) + (48);
    goto loc_0062F509;
loc_0062F4EF:
    result = *(unsigned __int64 *)(v_rdi) - 16;
    if (*(unsigned __int64 *)(v_rdi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) - 16 + 8);
        a1 = v_stack_p8;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062F509:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi))) != v_rdi) goto loc_0062F4EF;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9259366;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
void DifKeEnterCriticalRegionWrapper(void)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (32);
    result = DifGetAPIThunkContextById(286, a2, a3, a4);
    if (result == 0) goto loc_0062F4A5;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062F433;
    v_stack_p8 = v_stack_p0;
    goto loc_0062F441;
loc_0062F433:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_p8 = result;
    }
    local_rsi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D546D)) != 0) goto loc_0062F459;
    if (((*(uint32_t *)(v_rip + 0x8D5529)) & (0x800ULL)) == 0) goto loc_0062F46C;
loc_0062F459:
    result = ExAcquireRundownProtection(v_rip + 9259552, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062F4A5;
loc_0062F46C:
    goto loc_0062F48F;
loc_0062F475:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        a1 = v_stack_p8;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062F48F:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062F475;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        a1 = v_rip + 9259488;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    if (result == 0) goto loc_0062F51F;
    local_rsi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D53F3)) != 0) goto loc_0062F4D3;
    if (((*(uint32_t *)(v_rip + 0x8D54AF)) & (0x800ULL)) == 0) goto loc_0062F4E6;
loc_0062F4D3:
    result = ExAcquireRundownProtection(v_rip + 9259430, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062F51F;
loc_0062F4E6:
    local_rdi = (result) + (48);
    goto loc_0062F509;
loc_0062F4EF:
    result = *(uint64_t *)(local_rdi) - 16;
    if (*(uint64_t *)(local_rdi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rdi) - 0x10 + 0x8);
        a1 = v_stack_p8;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062F509:
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi))) != local_rdi) goto loc_0062F4EF;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        a1 = v_rip + 9259366;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062F3F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062F3F0[BB_0062F3F0]
  bb_0062F420[BB_0062F420]
  bb_0062F427[BB_0062F427]
  bb_0062F433[BB_0062F433]
  bb_0062F437[BB_0062F437]
  bb_0062F441[BB_0062F441]
  bb_0062F44D[BB_0062F44D]
  bb_0062F459[BB_0062F459]
  bb_0062F46C[BB_0062F46C]
  bb_0062F475[BB_0062F475]
  bb_0062F47E[BB_0062F47E]
  bb_0062F48C[BB_0062F48C]
  bb_0062F48F[BB_0062F48F]
  bb_0062F494[BB_0062F494]
  bb_0062F499[BB_0062F499]
  bb_0062F4A5[BB_0062F4A5]
  bb_0062F4BB[BB_0062F4BB]
  bb_0062F4C7[BB_0062F4C7]
  bb_0062F4D3[BB_0062F4D3]
  bb_0062F4E6[BB_0062F4E6]
  bb_0062F4EF[BB_0062F4EF]
  bb_0062F4F8[BB_0062F4F8]
  bb_0062F506[BB_0062F506]
  bb_0062F509[BB_0062F509]
  bb_0062F50E[BB_0062F50E]
  bb_0062F513[BB_0062F513]
  bb_0062F51F[BB_0062F51F]
  bb_0062F535[BB_0062F535]
  bb_0062F3F0 -->|branch| bb_0062F4A5
  bb_0062F3F0 -->|fallthrough| bb_0062F420
  bb_0062F420 -->|branch| bb_0062F433
  bb_0062F420 -->|fallthrough| bb_0062F427
  bb_0062F427 -->|branch| bb_0062F441
  bb_0062F433 -->|branch| bb_0062F441
  bb_0062F433 -->|fallthrough| bb_0062F437
  bb_0062F437 -->|flow| bb_0062F441
  bb_0062F441 -->|branch| bb_0062F459
  bb_0062F441 -->|fallthrough| bb_0062F44D
  bb_0062F44D -->|branch| bb_0062F46C
  bb_0062F44D -->|fallthrough| bb_0062F459
  bb_0062F459 -->|branch| bb_0062F4A5
  bb_0062F459 -->|fallthrough| bb_0062F46C
  bb_0062F46C -->|branch| bb_0062F48F
  bb_0062F475 -->|branch| bb_0062F48C
  bb_0062F475 -->|fallthrough| bb_0062F47E
  bb_0062F47E -->|flow| bb_0062F48C
  bb_0062F48C -->|flow| bb_0062F48F
  bb_0062F48F -->|branch| bb_0062F475
  bb_0062F48F -->|fallthrough| bb_0062F494
  bb_0062F494 -->|branch| bb_0062F4A5
  bb_0062F494 -->|fallthrough| bb_0062F499
  bb_0062F499 -->|flow| bb_0062F4A5
  bb_0062F4A5 -->|branch| bb_0062F51F
  bb_0062F4A5 -->|fallthrough| bb_0062F4BB
  bb_0062F4BB -->|branch| bb_0062F4D3
  bb_0062F4BB -->|fallthrough| bb_0062F4C7
  bb_0062F4C7 -->|branch| bb_0062F4E6
  bb_0062F4C7 -->|fallthrough| bb_0062F4D3
  bb_0062F4D3 -->|branch| bb_0062F51F
  bb_0062F4D3 -->|fallthrough| bb_0062F4E6
  bb_0062F4E6 -->|branch| bb_0062F509
  bb_0062F4EF -->|branch| bb_0062F506
  bb_0062F4EF -->|fallthrough| bb_0062F4F8
  bb_0062F4F8 -->|flow| bb_0062F506
  bb_0062F506 -->|flow| bb_0062F509
  bb_0062F509 -->|branch| bb_0062F4EF
  bb_0062F509 -->|fallthrough| bb_0062F50E
  bb_0062F50E -->|branch| bb_0062F51F
  bb_0062F50E -->|fallthrough| bb_0062F513
  bb_0062F513 -->|flow| bb_0062F51F
```
