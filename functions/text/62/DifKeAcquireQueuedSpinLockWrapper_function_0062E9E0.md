# DifKeAcquireQueuedSpinLockWrapper

- RVA: `0x0062E9E0`–`0x0062EB3F` (길이 `351` bytes)
- VA: `0x000000014062E9E0`
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
- `0x0062EA0F` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062EA37` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062EA65` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062EA8C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062EAA5` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062EAAD` → [KeAcquireQueuedSpinLock](../27/KeAcquireQueuedSpinLock_function_00273D80.md) (function, `0x00273D80`)
- `0x0062EADA` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062EB01` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062EB1A` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062EA49` → RVA `0x00F048B8` (`.data`; read)
- `0x0062EA52` → RVA `0x00F04980` (`.data`; read)
- `0x0062EA5E` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062E9E0  4C 8B DC                        mov r11, rsp
0062E9E3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
0062E9E7  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0062E9EB  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0062E9EF  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
0062E9F3  41 56                           push r14
0062E9F5  48 83 EC 40                     sub rsp, 0x40
0062E9F9  33 C0                           xor eax, eax
0062E9FB  0F 57 C0                        xorps xmm0, xmm0
0062E9FE  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
0062EA03  48 8B E9                        mov rbp, rcx
0062EA06  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0062EA0A  B9 26 01 00 00                  mov ecx, 0x126
0062EA0F  E8 20 70 E6 FF                  call 0x140495a34
0062EA14  48 8B F0                        mov rsi, rax
0062EA17  48 85 C0                        test rax, rax
0062EA1A  0F 84 8A 00 00 00               je 0x14062eaaa
0062EA20  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062EA23  A8 18                           test al, 0x18
0062EA25  74 0C                           je 0x14062ea33
0062EA27  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0062EA2C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0062EA31  EB 0E                           jmp 0x14062ea41
0062EA33  A8 04                           test al, 4
0062EA35  74 0A                           je 0x14062ea41
0062EA37  E8 CC 51 EA FF                  call 0x1404d3c08
0062EA3C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0062EA41  40 32 FF                        xor dil, dil
0062EA44  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
0062EA49  40 38 3D 68 5E 8D 00            cmp byte ptr [rip + 0x8d5e68], dil
0062EA50  75 0C                           jne 0x14062ea5e
0062EA52  F7 05 24 5F 8D 00 00 08 00 00   test dword ptr [rip + 0x8d5f24], 0x800
0062EA5C  74 13                           je 0x14062ea71
0062EA5E  48 8D 0D 1B 54 8D 00            lea rcx, [rip + 0x8d541b]
0062EA65  E8 B6 7B BE FF                  call 0x140216620
0062EA6A  40 8A F8                        mov dil, al
0062EA6D  84 C0                           test al, al
0062EA6F  74 39                           je 0x14062eaaa
0062EA71  4C 8D 76 20                     lea r14, [rsi + 0x20]
0062EA75  49 8B 1E                        mov rbx, qword ptr [r14]
0062EA78  EB 1A                           jmp 0x14062ea94
0062EA7A  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062EA7E  48 85 C0                        test rax, rax
0062EA81  74 0E                           je 0x14062ea91
0062EA83  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062EA87  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062EA8C  E8 3F C0 08 00                  call 0x1406baad0
0062EA91  48 8B 1B                        mov rbx, qword ptr [rbx]
0062EA94  49 3B DE                        cmp rbx, r14
0062EA97  75 E1                           jne 0x14062ea7a
0062EA99  40 84 FF                        test dil, dil
0062EA9C  74 0C                           je 0x14062eaaa
0062EA9E  48 8D 0D DB 53 8D 00            lea rcx, [rip + 0x8d53db]
0062EAA5  E8 D6 B3 D1 FF                  call 0x140349e80
0062EAAA  48 8B CD                        mov rcx, rbp
0062EAAD  E8 CE 52 C4 FF                  call 0x140273d80
0062EAB2  88 44 24 30                     mov byte ptr [rsp + 0x30], al
0062EAB6  48 85 F6                        test rsi, rsi
0062EAB9  74 64                           je 0x14062eb1f
0062EABB  40 32 FF                        xor dil, dil
0062EABE  40 38 3D F3 5D 8D 00            cmp byte ptr [rip + 0x8d5df3], dil
0062EAC5  75 0C                           jne 0x14062ead3
0062EAC7  F7 05 AF 5E 8D 00 00 08 00 00   test dword ptr [rip + 0x8d5eaf], 0x800
0062EAD1  74 13                           je 0x14062eae6
0062EAD3  48 8D 0D A6 53 8D 00            lea rcx, [rip + 0x8d53a6]
0062EADA  E8 41 7B BE FF                  call 0x140216620
0062EADF  40 8A F8                        mov dil, al
0062EAE2  84 C0                           test al, al
0062EAE4  74 39                           je 0x14062eb1f
0062EAE6  48 83 C6 30                     add rsi, 0x30
0062EAEA  48 8B 1E                        mov rbx, qword ptr [rsi]
0062EAED  EB 1A                           jmp 0x14062eb09
0062EAEF  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062EAF3  48 85 C0                        test rax, rax
0062EAF6  74 0E                           je 0x14062eb06
0062EAF8  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062EAFC  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062EB01  E8 CA BF 08 00                  call 0x1406baad0
0062EB06  48 8B 1B                        mov rbx, qword ptr [rbx]
0062EB09  48 3B DE                        cmp rbx, rsi
0062EB0C  75 E1                           jne 0x14062eaef
0062EB0E  40 84 FF                        test dil, dil
0062EB11  74 0C                           je 0x14062eb1f
0062EB13  48 8D 0D 66 53 8D 00            lea rcx, [rip + 0x8d5366]
0062EB1A  E8 61 B3 D1 FF                  call 0x140349e80
0062EB1F  8A 44 24 30                     mov al, byte ptr [rsp + 0x30]
0062EB23  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0062EB28  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0062EB2D  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
0062EB32  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0062EB37  48 83 C4 40                     add rsp, 0x40
0062EB3B  41 5E                           pop r14
0062EB3D  C3                              ret
0062EB3E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifKeAcquireQueuedSpinLockWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int8 v_stack_m18;
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
    result = DifGetAPIThunkContextById(294, a2, a3, a4);
    if (result == 0) goto loc_0062EAAA;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062EA33;
    v_stack_m28 = v_stack_p0;
    goto loc_0062EA41;
loc_0062EA33:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9264744)) != 0) goto loc_0062EA5E;
    if (((*(unsigned int *)(v_rip + 9264932)) & (0x800ULL)) == 0) goto loc_0062EA71;
loc_0062EA5E:
    result = ExAcquireRundownProtection(v_rip + 9262107, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062EAAA;
loc_0062EA71:
    goto loc_0062EA94;
loc_0062EA7A:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062EA94:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062EA7A;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9262043;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = KeAcquireQueuedSpinLock(a1, a2, a3, a4);
    v_stack_m18 = (unsigned __int8)(result);
    if (result == 0) goto loc_0062EB1F;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9264627)) != 0) goto loc_0062EAD3;
    if (((*(unsigned int *)(v_rip + 9264815)) & (0x800ULL)) == 0) goto loc_0062EAE6;
loc_0062EAD3:
    result = ExAcquireRundownProtection(v_rip + 9261990, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062EB1F;
loc_0062EAE6:
    v_rsi = (result) + (48);
    goto loc_0062EB09;
loc_0062EAEF:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062EB09:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0062EAEF;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9261926;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m18;
}
```

## 5. (Beta) C Style

```c
int64_t DifKeAcquireQueuedSpinLockWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint8_t v_stack_m18;
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
    result = DifGetAPIThunkContextById(294, a2, a3, a4);
    if (result == 0) goto loc_0062EAAA;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062EA33;
    v_stack_m28 = v_stack_p0;
    goto loc_0062EA41;
loc_0062EA33:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8D5E68)) != 0) goto loc_0062EA5E;
    if (((*(uint32_t *)(v_rip + 0x8D5F24)) & (0x800ULL)) == 0) goto loc_0062EA71;
loc_0062EA5E:
    result = ExAcquireRundownProtection(v_rip + 9262107, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062EAAA;
loc_0062EA71:
    goto loc_0062EA94;
loc_0062EA7A:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0062EA94:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062EA7A;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9262043;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = KeAcquireQueuedSpinLock(Arg1, a2, a3, a4);
    v_stack_m18 = (uint8_t)(result);
    if (result == 0) goto loc_0062EB1F;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D5DF3)) != 0) goto loc_0062EAD3;
    if (((*(uint32_t *)(v_rip + 0x8D5EAF)) & (0x800ULL)) == 0) goto loc_0062EAE6;
loc_0062EAD3:
    result = ExAcquireRundownProtection(v_rip + 9261990, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062EB1F;
loc_0062EAE6:
    local_rsi = (result) + (48);
    goto loc_0062EB09;
loc_0062EAEF:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0062EB09:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0062EAEF;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9261926;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m18;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062E9E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062E9E0[BB_0062E9E0]
  bb_0062EA20[BB_0062EA20]
  bb_0062EA27[BB_0062EA27]
  bb_0062EA33[BB_0062EA33]
  bb_0062EA37[BB_0062EA37]
  bb_0062EA41[BB_0062EA41]
  bb_0062EA52[BB_0062EA52]
  bb_0062EA5E[BB_0062EA5E]
  bb_0062EA71[BB_0062EA71]
  bb_0062EA7A[BB_0062EA7A]
  bb_0062EA83[BB_0062EA83]
  bb_0062EA91[BB_0062EA91]
  bb_0062EA94[BB_0062EA94]
  bb_0062EA99[BB_0062EA99]
  bb_0062EA9E[BB_0062EA9E]
  bb_0062EAAA[BB_0062EAAA]
  bb_0062EABB[BB_0062EABB]
  bb_0062EAC7[BB_0062EAC7]
  bb_0062EAD3[BB_0062EAD3]
  bb_0062EAE6[BB_0062EAE6]
  bb_0062EAEF[BB_0062EAEF]
  bb_0062EAF8[BB_0062EAF8]
  bb_0062EB06[BB_0062EB06]
  bb_0062EB09[BB_0062EB09]
  bb_0062EB0E[BB_0062EB0E]
  bb_0062EB13[BB_0062EB13]
  bb_0062EB1F[BB_0062EB1F]
  bb_0062EB3E[BB_0062EB3E]
  bb_0062E9E0 -->|branch| bb_0062EAAA
  bb_0062E9E0 -->|fallthrough| bb_0062EA20
  bb_0062EA20 -->|branch| bb_0062EA33
  bb_0062EA20 -->|fallthrough| bb_0062EA27
  bb_0062EA27 -->|branch| bb_0062EA41
  bb_0062EA33 -->|branch| bb_0062EA41
  bb_0062EA33 -->|fallthrough| bb_0062EA37
  bb_0062EA37 -->|flow| bb_0062EA41
  bb_0062EA41 -->|branch| bb_0062EA5E
  bb_0062EA41 -->|fallthrough| bb_0062EA52
  bb_0062EA52 -->|branch| bb_0062EA71
  bb_0062EA52 -->|fallthrough| bb_0062EA5E
  bb_0062EA5E -->|branch| bb_0062EAAA
  bb_0062EA5E -->|fallthrough| bb_0062EA71
  bb_0062EA71 -->|branch| bb_0062EA94
  bb_0062EA7A -->|branch| bb_0062EA91
  bb_0062EA7A -->|fallthrough| bb_0062EA83
  bb_0062EA83 -->|flow| bb_0062EA91
  bb_0062EA91 -->|flow| bb_0062EA94
  bb_0062EA94 -->|branch| bb_0062EA7A
  bb_0062EA94 -->|fallthrough| bb_0062EA99
  bb_0062EA99 -->|branch| bb_0062EAAA
  bb_0062EA99 -->|fallthrough| bb_0062EA9E
  bb_0062EA9E -->|flow| bb_0062EAAA
  bb_0062EAAA -->|branch| bb_0062EB1F
  bb_0062EAAA -->|fallthrough| bb_0062EABB
  bb_0062EABB -->|branch| bb_0062EAD3
  bb_0062EABB -->|fallthrough| bb_0062EAC7
  bb_0062EAC7 -->|branch| bb_0062EAE6
  bb_0062EAC7 -->|fallthrough| bb_0062EAD3
  bb_0062EAD3 -->|branch| bb_0062EB1F
  bb_0062EAD3 -->|fallthrough| bb_0062EAE6
  bb_0062EAE6 -->|branch| bb_0062EB09
  bb_0062EAEF -->|branch| bb_0062EB06
  bb_0062EAEF -->|fallthrough| bb_0062EAF8
  bb_0062EAF8 -->|flow| bb_0062EB06
  bb_0062EB06 -->|flow| bb_0062EB09
  bb_0062EB09 -->|branch| bb_0062EAEF
  bb_0062EB09 -->|fallthrough| bb_0062EB0E
  bb_0062EB0E -->|branch| bb_0062EB1F
  bb_0062EB0E -->|fallthrough| bb_0062EB13
  bb_0062EB13 -->|flow| bb_0062EB1F
```
