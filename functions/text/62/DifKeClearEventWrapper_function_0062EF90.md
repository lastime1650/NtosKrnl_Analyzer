# DifKeClearEventWrapper

- RVA: `0x0062EF90`–`0x0062F0E0` (길이 `336` bytes)
- VA: `0x000000014062EF90`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D7BC`
- 디코드: `90`개 명령, `336/336` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062EFB8` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062EFE0` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062F00E` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062F035` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062F04E` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062F056` → [KeResetEvent](../24/KeResetEvent_function_00248350.md) (function, `0x00248350`)
- `0x0062F07F` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062F0A6` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062F0BF` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062EFF2` → RVA `0x00F048B8` (`.data`; read)
- `0x0062EFFB` → RVA `0x00F04980` (`.data`; read)
- `0x0062F007` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062EF90  48 8B C4                        mov rax, rsp
0062EF93  48 89 58 08                     mov qword ptr [rax + 8], rbx
0062EF97  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0062EF9B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0062EF9F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0062EFA3  41 56                           push r14
0062EFA5  48 83 EC 30                     sub rsp, 0x30
0062EFA9  48 8B E9                        mov rbp, rcx
0062EFAC  0F 57 C0                        xorps xmm0, xmm0
0062EFAF  B9 21 01 00 00                  mov ecx, 0x121
0062EFB4  0F 11 40 E8                     movups xmmword ptr [rax - 0x18], xmm0
0062EFB8  E8 77 6A E6 FF                  call 0x140495a34
0062EFBD  48 8B F8                        mov rdi, rax
0062EFC0  48 85 C0                        test rax, rax
0062EFC3  0F 84 8A 00 00 00               je 0x14062f053
0062EFC9  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062EFCC  A8 18                           test al, 0x18
0062EFCE  74 0C                           je 0x14062efdc
0062EFD0  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0062EFD5  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0062EFDA  EB 0E                           jmp 0x14062efea
0062EFDC  A8 04                           test al, 4
0062EFDE  74 0A                           je 0x14062efea
0062EFE0  E8 23 4C EA FF                  call 0x1404d3c08
0062EFE5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0062EFEA  40 32 F6                        xor sil, sil
0062EFED  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
0062EFF2  40 38 35 BF 58 8D 00            cmp byte ptr [rip + 0x8d58bf], sil
0062EFF9  75 0C                           jne 0x14062f007
0062EFFB  F7 05 7B 59 8D 00 00 08 00 00   test dword ptr [rip + 0x8d597b], 0x800
0062F005  74 13                           je 0x14062f01a
0062F007  48 8D 0D 72 4E 8D 00            lea rcx, [rip + 0x8d4e72]
0062F00E  E8 0D 76 BE FF                  call 0x140216620
0062F013  40 8A F0                        mov sil, al
0062F016  84 C0                           test al, al
0062F018  74 39                           je 0x14062f053
0062F01A  4C 8D 77 20                     lea r14, [rdi + 0x20]
0062F01E  49 8B 1E                        mov rbx, qword ptr [r14]
0062F021  EB 1A                           jmp 0x14062f03d
0062F023  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062F027  48 85 C0                        test rax, rax
0062F02A  74 0E                           je 0x14062f03a
0062F02C  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062F030  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062F035  E8 96 BA 08 00                  call 0x1406baad0
0062F03A  48 8B 1B                        mov rbx, qword ptr [rbx]
0062F03D  49 3B DE                        cmp rbx, r14
0062F040  75 E1                           jne 0x14062f023
0062F042  40 84 F6                        test sil, sil
0062F045  74 0C                           je 0x14062f053
0062F047  48 8D 0D 32 4E 8D 00            lea rcx, [rip + 0x8d4e32]
0062F04E  E8 2D AE D1 FF                  call 0x140349e80
0062F053  48 8B CD                        mov rcx, rbp
0062F056  E8 F5 92 C1 FF                  call 0x140248350
0062F05B  48 85 FF                        test rdi, rdi
0062F05E  74 64                           je 0x14062f0c4
0062F060  40 32 F6                        xor sil, sil
0062F063  40 38 35 4E 58 8D 00            cmp byte ptr [rip + 0x8d584e], sil
0062F06A  75 0C                           jne 0x14062f078
0062F06C  F7 05 0A 59 8D 00 00 08 00 00   test dword ptr [rip + 0x8d590a], 0x800
0062F076  74 13                           je 0x14062f08b
0062F078  48 8D 0D 01 4E 8D 00            lea rcx, [rip + 0x8d4e01]
0062F07F  E8 9C 75 BE FF                  call 0x140216620
0062F084  40 8A F0                        mov sil, al
0062F087  84 C0                           test al, al
0062F089  74 39                           je 0x14062f0c4
0062F08B  48 83 C7 30                     add rdi, 0x30
0062F08F  48 8B 1F                        mov rbx, qword ptr [rdi]
0062F092  EB 1A                           jmp 0x14062f0ae
0062F094  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062F098  48 85 C0                        test rax, rax
0062F09B  74 0E                           je 0x14062f0ab
0062F09D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062F0A1  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062F0A6  E8 25 BA 08 00                  call 0x1406baad0
0062F0AB  48 8B 1B                        mov rbx, qword ptr [rbx]
0062F0AE  48 3B DF                        cmp rbx, rdi
0062F0B1  75 E1                           jne 0x14062f094
0062F0B3  40 84 F6                        test sil, sil
0062F0B6  74 0C                           je 0x14062f0c4
0062F0B8  48 8D 0D C1 4D 8D 00            lea rcx, [rip + 0x8d4dc1]
0062F0BF  E8 BC AD D1 FF                  call 0x140349e80
0062F0C4  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
0062F0C9  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
0062F0CE  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
0062F0D3  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
0062F0D8  48 83 C4 30                     add rsp, 0x30
0062F0DC  41 5E                           pop r14
0062F0DE  C3                              ret
0062F0DF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifKeClearEventWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (48);
    *(unsigned __int64 *)(v_rsp - 24) = v_xmm0;
    result = DifGetAPIThunkContextById(289, a2, a3, a4);
    if (result == 0) goto loc_0062F053;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062EFDC;
    v_stack_m18 = v_stack_p0;
    goto loc_0062EFEA;
loc_0062EFDC:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    v_rsi = 0;
    v_stack_m10 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9263295)) != 0) goto loc_0062F007;
    if (((*(unsigned int *)(v_rip + 9263483)) & (0x800ULL)) == 0) goto loc_0062F01A;
loc_0062F007:
    result = ExAcquireRundownProtection(v_rip + 9260658, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062F053;
loc_0062F01A:
    goto loc_0062F03D;
loc_0062F023:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062F03D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062F023;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9260594;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = KeResetEvent(a1, a2, a3, a4);
    if (result == 0) goto loc_0062F0C4;
    v_rsi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9263182)) != 0) goto loc_0062F078;
    if (((*(unsigned int *)(v_rip + 9263370)) & (0x800ULL)) == 0) goto loc_0062F08B;
loc_0062F078:
    result = ExAcquireRundownProtection(v_rip + 9260545, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062F0C4;
loc_0062F08B:
    v_rdi = (result) + (48);
    goto loc_0062F0AE;
loc_0062F094:
    result = *(unsigned __int64 *)(v_rdi) - 16;
    if (*(unsigned __int64 *)(v_rdi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062F0AE:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi))) != v_rdi) goto loc_0062F094;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9260481;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifKeClearEventWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (48);
    *(uint64_t *)(local_rsp - 0x18) = v_xmm0;
    result = DifGetAPIThunkContextById(289, a2, a3, a4);
    if (result == 0) goto loc_0062F053;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062EFDC;
    v_stack_m18 = v_stack_p0;
    goto loc_0062EFEA;
loc_0062EFDC:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    local_rsi = 0;
    v_stack_m10 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8D58BF)) != 0) goto loc_0062F007;
    if (((*(uint32_t *)(v_rip + 0x8D597B)) & (0x800ULL)) == 0) goto loc_0062F01A;
loc_0062F007:
    result = ExAcquireRundownProtection(v_rip + 9260658, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062F053;
loc_0062F01A:
    goto loc_0062F03D;
loc_0062F023:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0062F03D:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062F023;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9260594;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = KeResetEvent(Arg1, a2, a3, a4);
    if (result == 0) goto loc_0062F0C4;
    local_rsi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D584E)) != 0) goto loc_0062F078;
    if (((*(uint32_t *)(v_rip + 0x8D590A)) & (0x800ULL)) == 0) goto loc_0062F08B;
loc_0062F078:
    result = ExAcquireRundownProtection(v_rip + 9260545, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062F0C4;
loc_0062F08B:
    local_rdi = (result) + (48);
    goto loc_0062F0AE;
loc_0062F094:
    result = *(uint64_t *)(local_rdi) - 16;
    if (*(uint64_t *)(local_rdi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rdi) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0062F0AE:
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi))) != local_rdi) goto loc_0062F094;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9260481;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062EF90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062EF90[BB_0062EF90]
  bb_0062EFC9[BB_0062EFC9]
  bb_0062EFD0[BB_0062EFD0]
  bb_0062EFDC[BB_0062EFDC]
  bb_0062EFE0[BB_0062EFE0]
  bb_0062EFEA[BB_0062EFEA]
  bb_0062EFFB[BB_0062EFFB]
  bb_0062F007[BB_0062F007]
  bb_0062F01A[BB_0062F01A]
  bb_0062F023[BB_0062F023]
  bb_0062F02C[BB_0062F02C]
  bb_0062F03A[BB_0062F03A]
  bb_0062F03D[BB_0062F03D]
  bb_0062F042[BB_0062F042]
  bb_0062F047[BB_0062F047]
  bb_0062F053[BB_0062F053]
  bb_0062F060[BB_0062F060]
  bb_0062F06C[BB_0062F06C]
  bb_0062F078[BB_0062F078]
  bb_0062F08B[BB_0062F08B]
  bb_0062F094[BB_0062F094]
  bb_0062F09D[BB_0062F09D]
  bb_0062F0AB[BB_0062F0AB]
  bb_0062F0AE[BB_0062F0AE]
  bb_0062F0B3[BB_0062F0B3]
  bb_0062F0B8[BB_0062F0B8]
  bb_0062F0C4[BB_0062F0C4]
  bb_0062F0DF[BB_0062F0DF]
  bb_0062EF90 -->|branch| bb_0062F053
  bb_0062EF90 -->|fallthrough| bb_0062EFC9
  bb_0062EFC9 -->|branch| bb_0062EFDC
  bb_0062EFC9 -->|fallthrough| bb_0062EFD0
  bb_0062EFD0 -->|branch| bb_0062EFEA
  bb_0062EFDC -->|branch| bb_0062EFEA
  bb_0062EFDC -->|fallthrough| bb_0062EFE0
  bb_0062EFE0 -->|flow| bb_0062EFEA
  bb_0062EFEA -->|branch| bb_0062F007
  bb_0062EFEA -->|fallthrough| bb_0062EFFB
  bb_0062EFFB -->|branch| bb_0062F01A
  bb_0062EFFB -->|fallthrough| bb_0062F007
  bb_0062F007 -->|branch| bb_0062F053
  bb_0062F007 -->|fallthrough| bb_0062F01A
  bb_0062F01A -->|branch| bb_0062F03D
  bb_0062F023 -->|branch| bb_0062F03A
  bb_0062F023 -->|fallthrough| bb_0062F02C
  bb_0062F02C -->|flow| bb_0062F03A
  bb_0062F03A -->|flow| bb_0062F03D
  bb_0062F03D -->|branch| bb_0062F023
  bb_0062F03D -->|fallthrough| bb_0062F042
  bb_0062F042 -->|branch| bb_0062F053
  bb_0062F042 -->|fallthrough| bb_0062F047
  bb_0062F047 -->|flow| bb_0062F053
  bb_0062F053 -->|branch| bb_0062F0C4
  bb_0062F053 -->|fallthrough| bb_0062F060
  bb_0062F060 -->|branch| bb_0062F078
  bb_0062F060 -->|fallthrough| bb_0062F06C
  bb_0062F06C -->|branch| bb_0062F08B
  bb_0062F06C -->|fallthrough| bb_0062F078
  bb_0062F078 -->|branch| bb_0062F0C4
  bb_0062F078 -->|fallthrough| bb_0062F08B
  bb_0062F08B -->|branch| bb_0062F0AE
  bb_0062F094 -->|branch| bb_0062F0AB
  bb_0062F094 -->|fallthrough| bb_0062F09D
  bb_0062F09D -->|flow| bb_0062F0AB
  bb_0062F0AB -->|flow| bb_0062F0AE
  bb_0062F0AE -->|branch| bb_0062F094
  bb_0062F0AE -->|fallthrough| bb_0062F0B3
  bb_0062F0B3 -->|branch| bb_0062F0C4
  bb_0062F0B3 -->|fallthrough| bb_0062F0B8
  bb_0062F0B8 -->|flow| bb_0062F0C4
```
