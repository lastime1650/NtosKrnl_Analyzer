# DifExfReleasePushLockWrapper

- RVA: `0x00623D90`–`0x00623EE0` (길이 `336` bytes)
- VA: `0x0000000140623D90`
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
- `0x00623DB8` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00623DE0` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00623E0E` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00623E35` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00623E4E` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00623E56` → [ExfReleasePushLock](../26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x00623E7F` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00623EA6` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00623EBF` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00623DF2` → RVA `0x00F048B8` (`.data`; read)
- `0x00623DFB` → RVA `0x00F04980` (`.data`; read)
- `0x00623E07` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00623D90  48 8B C4                        mov rax, rsp
00623D93  48 89 58 08                     mov qword ptr [rax + 8], rbx
00623D97  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
00623D9B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00623D9F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00623DA3  41 56                           push r14
00623DA5  48 83 EC 30                     sub rsp, 0x30
00623DA9  48 8B E9                        mov rbp, rcx
00623DAC  0F 57 C0                        xorps xmm0, xmm0
00623DAF  B9 7A 01 00 00                  mov ecx, 0x17a
00623DB4  0F 11 40 E8                     movups xmmword ptr [rax - 0x18], xmm0
00623DB8  E8 77 1C E7 FF                  call 0x140495a34
00623DBD  48 8B F8                        mov rdi, rax
00623DC0  48 85 C0                        test rax, rax
00623DC3  0F 84 8A 00 00 00               je 0x140623e53
00623DC9  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00623DCC  A8 18                           test al, 0x18
00623DCE  74 0C                           je 0x140623ddc
00623DD0  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00623DD5  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00623DDA  EB 0E                           jmp 0x140623dea
00623DDC  A8 04                           test al, 4
00623DDE  74 0A                           je 0x140623dea
00623DE0  E8 23 FE EA FF                  call 0x1404d3c08
00623DE5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00623DEA  40 32 F6                        xor sil, sil
00623DED  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00623DF2  40 38 35 BF 0A 8E 00            cmp byte ptr [rip + 0x8e0abf], sil
00623DF9  75 0C                           jne 0x140623e07
00623DFB  F7 05 7B 0B 8E 00 00 08 00 00   test dword ptr [rip + 0x8e0b7b], 0x800
00623E05  74 13                           je 0x140623e1a
00623E07  48 8D 0D 72 00 8E 00            lea rcx, [rip + 0x8e0072]
00623E0E  E8 0D 28 BF FF                  call 0x140216620
00623E13  40 8A F0                        mov sil, al
00623E16  84 C0                           test al, al
00623E18  74 39                           je 0x140623e53
00623E1A  4C 8D 77 20                     lea r14, [rdi + 0x20]
00623E1E  49 8B 1E                        mov rbx, qword ptr [r14]
00623E21  EB 1A                           jmp 0x140623e3d
00623E23  48 8D 43 F0                     lea rax, [rbx - 0x10]
00623E27  48 85 C0                        test rax, rax
00623E2A  74 0E                           je 0x140623e3a
00623E2C  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00623E30  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00623E35  E8 96 6C 09 00                  call 0x1406baad0
00623E3A  48 8B 1B                        mov rbx, qword ptr [rbx]
00623E3D  49 3B DE                        cmp rbx, r14
00623E40  75 E1                           jne 0x140623e23
00623E42  40 84 F6                        test sil, sil
00623E45  74 0C                           je 0x140623e53
00623E47  48 8D 0D 32 00 8E 00            lea rcx, [rip + 0x8e0032]
00623E4E  E8 2D 60 D2 FF                  call 0x140349e80
00623E53  48 8B CD                        mov rcx, rbp
00623E56  E8 75 FA C3 FF                  call 0x1402638d0
00623E5B  48 85 FF                        test rdi, rdi
00623E5E  74 64                           je 0x140623ec4
00623E60  40 32 F6                        xor sil, sil
00623E63  40 38 35 4E 0A 8E 00            cmp byte ptr [rip + 0x8e0a4e], sil
00623E6A  75 0C                           jne 0x140623e78
00623E6C  F7 05 0A 0B 8E 00 00 08 00 00   test dword ptr [rip + 0x8e0b0a], 0x800
00623E76  74 13                           je 0x140623e8b
00623E78  48 8D 0D 01 00 8E 00            lea rcx, [rip + 0x8e0001]
00623E7F  E8 9C 27 BF FF                  call 0x140216620
00623E84  40 8A F0                        mov sil, al
00623E87  84 C0                           test al, al
00623E89  74 39                           je 0x140623ec4
00623E8B  48 83 C7 30                     add rdi, 0x30
00623E8F  48 8B 1F                        mov rbx, qword ptr [rdi]
00623E92  EB 1A                           jmp 0x140623eae
00623E94  48 8D 43 F0                     lea rax, [rbx - 0x10]
00623E98  48 85 C0                        test rax, rax
00623E9B  74 0E                           je 0x140623eab
00623E9D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00623EA1  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00623EA6  E8 25 6C 09 00                  call 0x1406baad0
00623EAB  48 8B 1B                        mov rbx, qword ptr [rbx]
00623EAE  48 3B DF                        cmp rbx, rdi
00623EB1  75 E1                           jne 0x140623e94
00623EB3  40 84 F6                        test sil, sil
00623EB6  74 0C                           je 0x140623ec4
00623EB8  48 8D 0D C1 FF 8D 00            lea rcx, [rip + 0x8dffc1]
00623EBF  E8 BC 5F D2 FF                  call 0x140349e80
00623EC4  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00623EC9  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
00623ECE  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00623ED3  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00623ED8  48 83 C4 30                     add rsp, 0x30
00623EDC  41 5E                           pop r14
00623EDE  C3                              ret
00623EDF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExfReleasePushLockWrapper(__int64 a1)
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
    result = DifGetAPIThunkContextById(378, a2, a3, a4);
    if (result == 0) goto loc_00623E53;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00623DDC;
    v_stack_m18 = v_stack_p0;
    goto loc_00623DEA;
loc_00623DDC:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    v_rsi = 0;
    v_stack_m10 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9308863)) != 0) goto loc_00623E07;
    if (((*(unsigned int *)(v_rip + 9309051)) & (0x800ULL)) == 0) goto loc_00623E1A;
loc_00623E07:
    result = ExAcquireRundownProtection(v_rip + 9306226, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00623E53;
loc_00623E1A:
    goto loc_00623E3D;
loc_00623E23:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00623E3D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00623E23;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9306162;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExfReleasePushLock(a1, a2, a3, a4);
    if (result == 0) goto loc_00623EC4;
    v_rsi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9308750)) != 0) goto loc_00623E78;
    if (((*(unsigned int *)(v_rip + 9308938)) & (0x800ULL)) == 0) goto loc_00623E8B;
loc_00623E78:
    result = ExAcquireRundownProtection(v_rip + 9306113, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00623EC4;
loc_00623E8B:
    v_rdi = (result) + (48);
    goto loc_00623EAE;
loc_00623E94:
    result = *(unsigned __int64 *)(v_rdi) - 16;
    if (*(unsigned __int64 *)(v_rdi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00623EAE:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi))) != v_rdi) goto loc_00623E94;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9306049;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifExfReleasePushLockWrapper(int64_t Arg1)
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
    result = DifGetAPIThunkContextById(378, a2, a3, a4);
    if (result == 0) goto loc_00623E53;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00623DDC;
    v_stack_m18 = v_stack_p0;
    goto loc_00623DEA;
loc_00623DDC:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    local_rsi = 0;
    v_stack_m10 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8E0ABF)) != 0) goto loc_00623E07;
    if (((*(uint32_t *)(v_rip + 0x8E0B7B)) & (0x800ULL)) == 0) goto loc_00623E1A;
loc_00623E07:
    result = ExAcquireRundownProtection(v_rip + 9306226, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00623E53;
loc_00623E1A:
    goto loc_00623E3D;
loc_00623E23:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00623E3D:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00623E23;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9306162;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ExfReleasePushLock(Arg1, a2, a3, a4);
    if (result == 0) goto loc_00623EC4;
    local_rsi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E0A4E)) != 0) goto loc_00623E78;
    if (((*(uint32_t *)(v_rip + 0x8E0B0A)) & (0x800ULL)) == 0) goto loc_00623E8B;
loc_00623E78:
    result = ExAcquireRundownProtection(v_rip + 9306113, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00623EC4;
loc_00623E8B:
    local_rdi = (result) + (48);
    goto loc_00623EAE;
loc_00623E94:
    result = *(uint64_t *)(local_rdi) - 16;
    if (*(uint64_t *)(local_rdi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rdi) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00623EAE:
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi))) != local_rdi) goto loc_00623E94;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9306049;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00623D90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00623D90[BB_00623D90]
  bb_00623DC9[BB_00623DC9]
  bb_00623DD0[BB_00623DD0]
  bb_00623DDC[BB_00623DDC]
  bb_00623DE0[BB_00623DE0]
  bb_00623DEA[BB_00623DEA]
  bb_00623DFB[BB_00623DFB]
  bb_00623E07[BB_00623E07]
  bb_00623E1A[BB_00623E1A]
  bb_00623E23[BB_00623E23]
  bb_00623E2C[BB_00623E2C]
  bb_00623E3A[BB_00623E3A]
  bb_00623E3D[BB_00623E3D]
  bb_00623E42[BB_00623E42]
  bb_00623E47[BB_00623E47]
  bb_00623E53[BB_00623E53]
  bb_00623E60[BB_00623E60]
  bb_00623E6C[BB_00623E6C]
  bb_00623E78[BB_00623E78]
  bb_00623E8B[BB_00623E8B]
  bb_00623E94[BB_00623E94]
  bb_00623E9D[BB_00623E9D]
  bb_00623EAB[BB_00623EAB]
  bb_00623EAE[BB_00623EAE]
  bb_00623EB3[BB_00623EB3]
  bb_00623EB8[BB_00623EB8]
  bb_00623EC4[BB_00623EC4]
  bb_00623EDF[BB_00623EDF]
  bb_00623D90 -->|branch| bb_00623E53
  bb_00623D90 -->|fallthrough| bb_00623DC9
  bb_00623DC9 -->|branch| bb_00623DDC
  bb_00623DC9 -->|fallthrough| bb_00623DD0
  bb_00623DD0 -->|branch| bb_00623DEA
  bb_00623DDC -->|branch| bb_00623DEA
  bb_00623DDC -->|fallthrough| bb_00623DE0
  bb_00623DE0 -->|flow| bb_00623DEA
  bb_00623DEA -->|branch| bb_00623E07
  bb_00623DEA -->|fallthrough| bb_00623DFB
  bb_00623DFB -->|branch| bb_00623E1A
  bb_00623DFB -->|fallthrough| bb_00623E07
  bb_00623E07 -->|branch| bb_00623E53
  bb_00623E07 -->|fallthrough| bb_00623E1A
  bb_00623E1A -->|branch| bb_00623E3D
  bb_00623E23 -->|branch| bb_00623E3A
  bb_00623E23 -->|fallthrough| bb_00623E2C
  bb_00623E2C -->|flow| bb_00623E3A
  bb_00623E3A -->|flow| bb_00623E3D
  bb_00623E3D -->|branch| bb_00623E23
  bb_00623E3D -->|fallthrough| bb_00623E42
  bb_00623E42 -->|branch| bb_00623E53
  bb_00623E42 -->|fallthrough| bb_00623E47
  bb_00623E47 -->|flow| bb_00623E53
  bb_00623E53 -->|branch| bb_00623EC4
  bb_00623E53 -->|fallthrough| bb_00623E60
  bb_00623E60 -->|branch| bb_00623E78
  bb_00623E60 -->|fallthrough| bb_00623E6C
  bb_00623E6C -->|branch| bb_00623E8B
  bb_00623E6C -->|fallthrough| bb_00623E78
  bb_00623E78 -->|branch| bb_00623EC4
  bb_00623E78 -->|fallthrough| bb_00623E8B
  bb_00623E8B -->|branch| bb_00623EAE
  bb_00623E94 -->|branch| bb_00623EAB
  bb_00623E94 -->|fallthrough| bb_00623E9D
  bb_00623E9D -->|flow| bb_00623EAB
  bb_00623EAB -->|flow| bb_00623EAE
  bb_00623EAE -->|branch| bb_00623E94
  bb_00623EAE -->|fallthrough| bb_00623EB3
  bb_00623EB3 -->|branch| bb_00623EC4
  bb_00623EB3 -->|fallthrough| bb_00623EB8
  bb_00623EB8 -->|flow| bb_00623EC4
```
