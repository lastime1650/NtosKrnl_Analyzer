# DifPsSetLoadImageNotifyRoutineWrapper

- RVA: `0x0063AF30`–`0x0063B08F` (길이 `351` bytes)
- VA: `0x000000014063AF30`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `94`개 명령, `351/351` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0063AF5F` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0063AF87` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063AFB5` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063AFDC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063AFF5` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063AFFD` → [PsSetLoadImageNotifyRoutine](../../page/78/PsSetLoadImageNotifyRoutine_function_00787850.md) (function, `0x00787850`)
- `0x0063B02A` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063B051` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063B06A` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0063AF99` → RVA `0x00F048B8` (`.data`; read)
- `0x0063AFA2` → RVA `0x00F04980` (`.data`; read)
- `0x0063AFAE` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0063AFFD` → [PsSetLoadImageNotifyRoutine](../../page/78/PsSetLoadImageNotifyRoutine_function_00787850.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0063AF30  4C 8B DC                        mov r11, rsp
0063AF33  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
0063AF37  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0063AF3B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0063AF3F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
0063AF43  41 56                           push r14
0063AF45  48 83 EC 40                     sub rsp, 0x40
0063AF49  33 C0                           xor eax, eax
0063AF4B  0F 57 C0                        xorps xmm0, xmm0
0063AF4E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
0063AF53  48 8B E9                        mov rbp, rcx
0063AF56  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0063AF5A  B9 AB 00 00 00                  mov ecx, 0xab
0063AF5F  E8 D0 AA E5 FF                  call 0x140495a34
0063AF64  48 8B F0                        mov rsi, rax
0063AF67  48 85 C0                        test rax, rax
0063AF6A  0F 84 8A 00 00 00               je 0x14063affa
0063AF70  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0063AF73  A8 18                           test al, 0x18
0063AF75  74 0C                           je 0x14063af83
0063AF77  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0063AF7C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0063AF81  EB 0E                           jmp 0x14063af91
0063AF83  A8 04                           test al, 4
0063AF85  74 0A                           je 0x14063af91
0063AF87  E8 7C 8C E9 FF                  call 0x1404d3c08
0063AF8C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0063AF91  40 32 FF                        xor dil, dil
0063AF94  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
0063AF99  40 38 3D 18 99 8C 00            cmp byte ptr [rip + 0x8c9918], dil
0063AFA0  75 0C                           jne 0x14063afae
0063AFA2  F7 05 D4 99 8C 00 00 08 00 00   test dword ptr [rip + 0x8c99d4], 0x800
0063AFAC  74 13                           je 0x14063afc1
0063AFAE  48 8D 0D CB 8E 8C 00            lea rcx, [rip + 0x8c8ecb]
0063AFB5  E8 66 B6 BD FF                  call 0x140216620
0063AFBA  40 8A F8                        mov dil, al
0063AFBD  84 C0                           test al, al
0063AFBF  74 39                           je 0x14063affa
0063AFC1  4C 8D 76 20                     lea r14, [rsi + 0x20]
0063AFC5  49 8B 1E                        mov rbx, qword ptr [r14]
0063AFC8  EB 1A                           jmp 0x14063afe4
0063AFCA  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063AFCE  48 85 C0                        test rax, rax
0063AFD1  74 0E                           je 0x14063afe1
0063AFD3  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063AFD7  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0063AFDC  E8 EF FA 07 00                  call 0x1406baad0
0063AFE1  48 8B 1B                        mov rbx, qword ptr [rbx]
0063AFE4  49 3B DE                        cmp rbx, r14
0063AFE7  75 E1                           jne 0x14063afca
0063AFE9  40 84 FF                        test dil, dil
0063AFEC  74 0C                           je 0x14063affa
0063AFEE  48 8D 0D 8B 8E 8C 00            lea rcx, [rip + 0x8c8e8b]
0063AFF5  E8 86 EE D0 FF                  call 0x140349e80
0063AFFA  48 8B CD                        mov rcx, rbp
0063AFFD  E8 4E C8 14 00                  call 0x140787850
0063B002  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0063B006  48 85 F6                        test rsi, rsi
0063B009  74 64                           je 0x14063b06f
0063B00B  40 32 FF                        xor dil, dil
0063B00E  40 38 3D A3 98 8C 00            cmp byte ptr [rip + 0x8c98a3], dil
0063B015  75 0C                           jne 0x14063b023
0063B017  F7 05 5F 99 8C 00 00 08 00 00   test dword ptr [rip + 0x8c995f], 0x800
0063B021  74 13                           je 0x14063b036
0063B023  48 8D 0D 56 8E 8C 00            lea rcx, [rip + 0x8c8e56]
0063B02A  E8 F1 B5 BD FF                  call 0x140216620
0063B02F  40 8A F8                        mov dil, al
0063B032  84 C0                           test al, al
0063B034  74 39                           je 0x14063b06f
0063B036  48 83 C6 30                     add rsi, 0x30
0063B03A  48 8B 1E                        mov rbx, qword ptr [rsi]
0063B03D  EB 1A                           jmp 0x14063b059
0063B03F  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063B043  48 85 C0                        test rax, rax
0063B046  74 0E                           je 0x14063b056
0063B048  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063B04C  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0063B051  E8 7A FA 07 00                  call 0x1406baad0
0063B056  48 8B 1B                        mov rbx, qword ptr [rbx]
0063B059  48 3B DE                        cmp rbx, rsi
0063B05C  75 E1                           jne 0x14063b03f
0063B05E  40 84 FF                        test dil, dil
0063B061  74 0C                           je 0x14063b06f
0063B063  48 8D 0D 16 8E 8C 00            lea rcx, [rip + 0x8c8e16]
0063B06A  E8 11 EE D0 FF                  call 0x140349e80
0063B06F  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
0063B073  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0063B078  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0063B07D  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
0063B082  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0063B087  48 83 C4 40                     add rsp, 0x40
0063B08B  41 5E                           pop r14
0063B08D  C3                              ret
0063B08E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifPsSetLoadImageNotifyRoutineWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (64);
    result = 0;
    v_stack_m28 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 24) = 0;
    result = DifGetAPIThunkContextById(171, a2, a3, a4);
    if (result == 0) goto loc_0063AFFA;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063AF83;
    v_stack_m28 = v_stack_p0;
    goto loc_0063AF91;
loc_0063AF83:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9214232)) != 0) goto loc_0063AFAE;
    if (((*(unsigned int *)(v_rip + 9214420)) & (0x800ULL)) == 0) goto loc_0063AFC1;
loc_0063AFAE:
    result = ExAcquireRundownProtection(v_rip + 9211595, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063AFFA;
loc_0063AFC1:
    goto loc_0063AFE4;
loc_0063AFCA:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063AFE4:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063AFCA;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9211531;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = PsSetLoadImageNotifyRoutine(a1, a2, a3, a4);
    v_stack_m18 = (unsigned int)(result);
    if (result == 0) goto loc_0063B06F;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9214115)) != 0) goto loc_0063B023;
    if (((*(unsigned int *)(v_rip + 9214303)) & (0x800ULL)) == 0) goto loc_0063B036;
loc_0063B023:
    result = ExAcquireRundownProtection(v_rip + 9211478, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063B06F;
loc_0063B036:
    v_rsi = (result) + (48);
    goto loc_0063B059;
loc_0063B03F:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063B059:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0063B03F;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9211414;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m18);
}
```

## 5. (Beta) C Style

```c
int64_t DifPsSetLoadImageNotifyRoutineWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (64);
    result = 0;
    v_stack_m28 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x18) = 0;
    result = DifGetAPIThunkContextById(171, a2, a3, a4);
    if (result == 0) goto loc_0063AFFA;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063AF83;
    v_stack_m28 = v_stack_p0;
    goto loc_0063AF91;
loc_0063AF83:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8C9918)) != 0) goto loc_0063AFAE;
    if (((*(uint32_t *)(v_rip + 0x8C99D4)) & (0x800ULL)) == 0) goto loc_0063AFC1;
loc_0063AFAE:
    result = ExAcquireRundownProtection(v_rip + 9211595, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063AFFA;
loc_0063AFC1:
    goto loc_0063AFE4;
loc_0063AFCA:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0063AFE4:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063AFCA;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9211531;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = PsSetLoadImageNotifyRoutine(Arg1, a2, a3, a4);
    v_stack_m18 = (uint32_t)(result);
    if (result == 0) goto loc_0063B06F;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C98A3)) != 0) goto loc_0063B023;
    if (((*(uint32_t *)(v_rip + 0x8C995F)) & (0x800ULL)) == 0) goto loc_0063B036;
loc_0063B023:
    result = ExAcquireRundownProtection(v_rip + 9211478, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063B06F;
loc_0063B036:
    local_rsi = (result) + (48);
    goto loc_0063B059;
loc_0063B03F:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0063B059:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0063B03F;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9211414;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m18);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0063AF30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0063AF30[BB_0063AF30]
  bb_0063AF70[BB_0063AF70]
  bb_0063AF77[BB_0063AF77]
  bb_0063AF83[BB_0063AF83]
  bb_0063AF87[BB_0063AF87]
  bb_0063AF91[BB_0063AF91]
  bb_0063AFA2[BB_0063AFA2]
  bb_0063AFAE[BB_0063AFAE]
  bb_0063AFC1[BB_0063AFC1]
  bb_0063AFCA[BB_0063AFCA]
  bb_0063AFD3[BB_0063AFD3]
  bb_0063AFE1[BB_0063AFE1]
  bb_0063AFE4[BB_0063AFE4]
  bb_0063AFE9[BB_0063AFE9]
  bb_0063AFEE[BB_0063AFEE]
  bb_0063AFFA[BB_0063AFFA]
  bb_0063B00B[BB_0063B00B]
  bb_0063B017[BB_0063B017]
  bb_0063B023[BB_0063B023]
  bb_0063B036[BB_0063B036]
  bb_0063B03F[BB_0063B03F]
  bb_0063B048[BB_0063B048]
  bb_0063B056[BB_0063B056]
  bb_0063B059[BB_0063B059]
  bb_0063B05E[BB_0063B05E]
  bb_0063B063[BB_0063B063]
  bb_0063B06F[BB_0063B06F]
  bb_0063B08E[BB_0063B08E]
  bb_0063AF30 -->|branch| bb_0063AFFA
  bb_0063AF30 -->|fallthrough| bb_0063AF70
  bb_0063AF70 -->|branch| bb_0063AF83
  bb_0063AF70 -->|fallthrough| bb_0063AF77
  bb_0063AF77 -->|branch| bb_0063AF91
  bb_0063AF83 -->|branch| bb_0063AF91
  bb_0063AF83 -->|fallthrough| bb_0063AF87
  bb_0063AF87 -->|flow| bb_0063AF91
  bb_0063AF91 -->|branch| bb_0063AFAE
  bb_0063AF91 -->|fallthrough| bb_0063AFA2
  bb_0063AFA2 -->|branch| bb_0063AFC1
  bb_0063AFA2 -->|fallthrough| bb_0063AFAE
  bb_0063AFAE -->|branch| bb_0063AFFA
  bb_0063AFAE -->|fallthrough| bb_0063AFC1
  bb_0063AFC1 -->|branch| bb_0063AFE4
  bb_0063AFCA -->|branch| bb_0063AFE1
  bb_0063AFCA -->|fallthrough| bb_0063AFD3
  bb_0063AFD3 -->|flow| bb_0063AFE1
  bb_0063AFE1 -->|flow| bb_0063AFE4
  bb_0063AFE4 -->|branch| bb_0063AFCA
  bb_0063AFE4 -->|fallthrough| bb_0063AFE9
  bb_0063AFE9 -->|branch| bb_0063AFFA
  bb_0063AFE9 -->|fallthrough| bb_0063AFEE
  bb_0063AFEE -->|flow| bb_0063AFFA
  bb_0063AFFA -->|branch| bb_0063B06F
  bb_0063AFFA -->|fallthrough| bb_0063B00B
  bb_0063B00B -->|branch| bb_0063B023
  bb_0063B00B -->|fallthrough| bb_0063B017
  bb_0063B017 -->|branch| bb_0063B036
  bb_0063B017 -->|fallthrough| bb_0063B023
  bb_0063B023 -->|branch| bb_0063B06F
  bb_0063B023 -->|fallthrough| bb_0063B036
  bb_0063B036 -->|branch| bb_0063B059
  bb_0063B03F -->|branch| bb_0063B056
  bb_0063B03F -->|fallthrough| bb_0063B048
  bb_0063B048 -->|flow| bb_0063B056
  bb_0063B056 -->|flow| bb_0063B059
  bb_0063B059 -->|branch| bb_0063B03F
  bb_0063B059 -->|fallthrough| bb_0063B05E
  bb_0063B05E -->|branch| bb_0063B06F
  bb_0063B05E -->|fallthrough| bb_0063B063
  bb_0063B063 -->|flow| bb_0063B06F
```
