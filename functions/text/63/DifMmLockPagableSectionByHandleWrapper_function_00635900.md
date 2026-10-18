# DifMmLockPagableSectionByHandleWrapper

- RVA: `0x00635900`–`0x00635A50` (길이 `336` bytes)
- VA: `0x0000000140635900`
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
- `0x00635928` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00635950` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063597E` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006359A5` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006359BE` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006359C6` → [MmLockPagableSectionByHandle](../../page/A4/MmLockPagableSectionByHandle_function_00A4D1E0.md) (function, `0x00A4D1E0`)
- `0x006359EF` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00635A16` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00635A2F` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00635962` → RVA `0x00F048B8` (`.data`; read)
- `0x0063596B` → RVA `0x00F04980` (`.data`; read)
- `0x00635977` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x006359C6` → [MmLockPagableSectionByHandle](../../page/A4/MmLockPagableSectionByHandle_function_00A4D1E0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00635900  48 8B C4                        mov rax, rsp
00635903  48 89 58 08                     mov qword ptr [rax + 8], rbx
00635907  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0063590B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0063590F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00635913  41 56                           push r14
00635915  48 83 EC 30                     sub rsp, 0x30
00635919  48 8B E9                        mov rbp, rcx
0063591C  0F 57 C0                        xorps xmm0, xmm0
0063591F  B9 DE 00 00 00                  mov ecx, 0xde
00635924  0F 11 40 E8                     movups xmmword ptr [rax - 0x18], xmm0
00635928  E8 07 01 E6 FF                  call 0x140495a34
0063592D  48 8B F8                        mov rdi, rax
00635930  48 85 C0                        test rax, rax
00635933  0F 84 8A 00 00 00               je 0x1406359c3
00635939  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0063593C  A8 18                           test al, 0x18
0063593E  74 0C                           je 0x14063594c
00635940  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00635945  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0063594A  EB 0E                           jmp 0x14063595a
0063594C  A8 04                           test al, 4
0063594E  74 0A                           je 0x14063595a
00635950  E8 B3 E2 E9 FF                  call 0x1404d3c08
00635955  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0063595A  40 32 F6                        xor sil, sil
0063595D  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00635962  40 38 35 4F EF 8C 00            cmp byte ptr [rip + 0x8cef4f], sil
00635969  75 0C                           jne 0x140635977
0063596B  F7 05 0B F0 8C 00 00 08 00 00   test dword ptr [rip + 0x8cf00b], 0x800
00635975  74 13                           je 0x14063598a
00635977  48 8D 0D 02 E5 8C 00            lea rcx, [rip + 0x8ce502]
0063597E  E8 9D 0C BE FF                  call 0x140216620
00635983  40 8A F0                        mov sil, al
00635986  84 C0                           test al, al
00635988  74 39                           je 0x1406359c3
0063598A  4C 8D 77 20                     lea r14, [rdi + 0x20]
0063598E  49 8B 1E                        mov rbx, qword ptr [r14]
00635991  EB 1A                           jmp 0x1406359ad
00635993  48 8D 43 F0                     lea rax, [rbx - 0x10]
00635997  48 85 C0                        test rax, rax
0063599A  74 0E                           je 0x1406359aa
0063599C  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006359A0  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006359A5  E8 26 51 08 00                  call 0x1406baad0
006359AA  48 8B 1B                        mov rbx, qword ptr [rbx]
006359AD  49 3B DE                        cmp rbx, r14
006359B0  75 E1                           jne 0x140635993
006359B2  40 84 F6                        test sil, sil
006359B5  74 0C                           je 0x1406359c3
006359B7  48 8D 0D C2 E4 8C 00            lea rcx, [rip + 0x8ce4c2]
006359BE  E8 BD 44 D1 FF                  call 0x140349e80
006359C3  48 8B CD                        mov rcx, rbp
006359C6  E8 15 78 41 00                  call 0x140a4d1e0
006359CB  48 85 FF                        test rdi, rdi
006359CE  74 64                           je 0x140635a34
006359D0  40 32 F6                        xor sil, sil
006359D3  40 38 35 DE EE 8C 00            cmp byte ptr [rip + 0x8ceede], sil
006359DA  75 0C                           jne 0x1406359e8
006359DC  F7 05 9A EF 8C 00 00 08 00 00   test dword ptr [rip + 0x8cef9a], 0x800
006359E6  74 13                           je 0x1406359fb
006359E8  48 8D 0D 91 E4 8C 00            lea rcx, [rip + 0x8ce491]
006359EF  E8 2C 0C BE FF                  call 0x140216620
006359F4  40 8A F0                        mov sil, al
006359F7  84 C0                           test al, al
006359F9  74 39                           je 0x140635a34
006359FB  48 83 C7 30                     add rdi, 0x30
006359FF  48 8B 1F                        mov rbx, qword ptr [rdi]
00635A02  EB 1A                           jmp 0x140635a1e
00635A04  48 8D 43 F0                     lea rax, [rbx - 0x10]
00635A08  48 85 C0                        test rax, rax
00635A0B  74 0E                           je 0x140635a1b
00635A0D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00635A11  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00635A16  E8 B5 50 08 00                  call 0x1406baad0
00635A1B  48 8B 1B                        mov rbx, qword ptr [rbx]
00635A1E  48 3B DF                        cmp rbx, rdi
00635A21  75 E1                           jne 0x140635a04
00635A23  40 84 F6                        test sil, sil
00635A26  74 0C                           je 0x140635a34
00635A28  48 8D 0D 51 E4 8C 00            lea rcx, [rip + 0x8ce451]
00635A2F  E8 4C 44 D1 FF                  call 0x140349e80
00635A34  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00635A39  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
00635A3E  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00635A43  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00635A48  48 83 C4 30                     add rsp, 0x30
00635A4C  41 5E                           pop r14
00635A4E  C3                              ret
00635A4F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifMmLockPagableSectionByHandleWrapper(__int64 a1)
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
    result = DifGetAPIThunkContextById(222, a2, a3, a4);
    if (result == 0) goto loc_006359C3;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063594C;
    v_stack_m18 = v_stack_p0;
    goto loc_0063595A;
loc_0063594C:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    v_rsi = 0;
    v_stack_m10 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9236303)) != 0) goto loc_00635977;
    if (((*(unsigned int *)(v_rip + 9236491)) & (0x800ULL)) == 0) goto loc_0063598A;
loc_00635977:
    result = ExAcquireRundownProtection(v_rip + 9233666, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006359C3;
loc_0063598A:
    goto loc_006359AD;
loc_00635993:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006359AD:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00635993;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9233602;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = MmLockPagableSectionByHandle(a1, a2, a3, a4);
    if (result == 0) goto loc_00635A34;
    v_rsi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9236190)) != 0) goto loc_006359E8;
    if (((*(unsigned int *)(v_rip + 9236378)) & (0x800ULL)) == 0) goto loc_006359FB;
loc_006359E8:
    result = ExAcquireRundownProtection(v_rip + 9233553, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00635A34;
loc_006359FB:
    v_rdi = (result) + (48);
    goto loc_00635A1E;
loc_00635A04:
    result = *(unsigned __int64 *)(v_rdi) - 16;
    if (*(unsigned __int64 *)(v_rdi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00635A1E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi))) != v_rdi) goto loc_00635A04;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9233489;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifMmLockPagableSectionByHandleWrapper(int64_t Arg1)
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
    result = DifGetAPIThunkContextById(222, a2, a3, a4);
    if (result == 0) goto loc_006359C3;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063594C;
    v_stack_m18 = v_stack_p0;
    goto loc_0063595A;
loc_0063594C:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    local_rsi = 0;
    v_stack_m10 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8CEF4F)) != 0) goto loc_00635977;
    if (((*(uint32_t *)(v_rip + 0x8CF00B)) & (0x800ULL)) == 0) goto loc_0063598A;
loc_00635977:
    result = ExAcquireRundownProtection(v_rip + 9233666, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006359C3;
loc_0063598A:
    goto loc_006359AD;
loc_00635993:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_006359AD:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00635993;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9233602;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = MmLockPagableSectionByHandle(Arg1, a2, a3, a4);
    if (result == 0) goto loc_00635A34;
    local_rsi = 0;
    if ((*(uint8_t *)(v_rip + 0x8CEEDE)) != 0) goto loc_006359E8;
    if (((*(uint32_t *)(v_rip + 0x8CEF9A)) & (0x800ULL)) == 0) goto loc_006359FB;
loc_006359E8:
    result = ExAcquireRundownProtection(v_rip + 9233553, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00635A34;
loc_006359FB:
    local_rdi = (result) + (48);
    goto loc_00635A1E;
loc_00635A04:
    result = *(uint64_t *)(local_rdi) - 16;
    if (*(uint64_t *)(local_rdi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rdi) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00635A1E:
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi))) != local_rdi) goto loc_00635A04;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9233489;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00635900&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00635900[BB_00635900]
  bb_00635939[BB_00635939]
  bb_00635940[BB_00635940]
  bb_0063594C[BB_0063594C]
  bb_00635950[BB_00635950]
  bb_0063595A[BB_0063595A]
  bb_0063596B[BB_0063596B]
  bb_00635977[BB_00635977]
  bb_0063598A[BB_0063598A]
  bb_00635993[BB_00635993]
  bb_0063599C[BB_0063599C]
  bb_006359AA[BB_006359AA]
  bb_006359AD[BB_006359AD]
  bb_006359B2[BB_006359B2]
  bb_006359B7[BB_006359B7]
  bb_006359C3[BB_006359C3]
  bb_006359D0[BB_006359D0]
  bb_006359DC[BB_006359DC]
  bb_006359E8[BB_006359E8]
  bb_006359FB[BB_006359FB]
  bb_00635A04[BB_00635A04]
  bb_00635A0D[BB_00635A0D]
  bb_00635A1B[BB_00635A1B]
  bb_00635A1E[BB_00635A1E]
  bb_00635A23[BB_00635A23]
  bb_00635A28[BB_00635A28]
  bb_00635A34[BB_00635A34]
  bb_00635A4F[BB_00635A4F]
  bb_00635900 -->|branch| bb_006359C3
  bb_00635900 -->|fallthrough| bb_00635939
  bb_00635939 -->|branch| bb_0063594C
  bb_00635939 -->|fallthrough| bb_00635940
  bb_00635940 -->|branch| bb_0063595A
  bb_0063594C -->|branch| bb_0063595A
  bb_0063594C -->|fallthrough| bb_00635950
  bb_00635950 -->|flow| bb_0063595A
  bb_0063595A -->|branch| bb_00635977
  bb_0063595A -->|fallthrough| bb_0063596B
  bb_0063596B -->|branch| bb_0063598A
  bb_0063596B -->|fallthrough| bb_00635977
  bb_00635977 -->|branch| bb_006359C3
  bb_00635977 -->|fallthrough| bb_0063598A
  bb_0063598A -->|branch| bb_006359AD
  bb_00635993 -->|branch| bb_006359AA
  bb_00635993 -->|fallthrough| bb_0063599C
  bb_0063599C -->|flow| bb_006359AA
  bb_006359AA -->|flow| bb_006359AD
  bb_006359AD -->|branch| bb_00635993
  bb_006359AD -->|fallthrough| bb_006359B2
  bb_006359B2 -->|branch| bb_006359C3
  bb_006359B2 -->|fallthrough| bb_006359B7
  bb_006359B7 -->|flow| bb_006359C3
  bb_006359C3 -->|branch| bb_00635A34
  bb_006359C3 -->|fallthrough| bb_006359D0
  bb_006359D0 -->|branch| bb_006359E8
  bb_006359D0 -->|fallthrough| bb_006359DC
  bb_006359DC -->|branch| bb_006359FB
  bb_006359DC -->|fallthrough| bb_006359E8
  bb_006359E8 -->|branch| bb_00635A34
  bb_006359E8 -->|fallthrough| bb_006359FB
  bb_006359FB -->|branch| bb_00635A1E
  bb_00635A04 -->|branch| bb_00635A1B
  bb_00635A04 -->|fallthrough| bb_00635A0D
  bb_00635A0D -->|flow| bb_00635A1B
  bb_00635A1B -->|flow| bb_00635A1E
  bb_00635A1E -->|branch| bb_00635A04
  bb_00635A1E -->|fallthrough| bb_00635A23
  bb_00635A23 -->|branch| bb_00635A34
  bb_00635A23 -->|fallthrough| bb_00635A28
  bb_00635A28 -->|flow| bb_00635A34
```
