# DifKeReleaseMutexWrapper

- RVA: `0x00631960`–`0x00631ACB` (길이 `363` bytes)
- VA: `0x0000000140631960`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00093E28`
- 디코드: `100`개 명령, `363/363` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0063198E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006319B6` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x006319E9` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00631A10` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00631A29` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00631A3B` → [KeReleaseMutant](../39/KeReleaseMutant_function_003967D0.md) (function, `0x003967D0`)
- `0x00631A68` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00631A8F` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00631AA8` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006319C8` → RVA `0x00F048B8` (`.data`; read)
- `0x006319D6` → RVA `0x00F04980` (`.data`; read)
- `0x006319E2` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00631960  48 8B C4                        mov rax, rsp
00631963  48 89 58 08                     mov qword ptr [rax + 8], rbx
00631967  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0063196B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0063196F  57                              push rdi
00631970  41 56                           push r14
00631972  41 57                           push r15
00631974  48 83 EC 40                     sub rsp, 0x40
00631978  0F 57 C0                        xorps xmm0, xmm0
0063197B  4C 8B F9                        mov r15, rcx
0063197E  B9 04 01 00 00                  mov ecx, 0x104
00631983  44 8A F2                        mov r14b, dl
00631986  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
0063198A  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
0063198E  E8 A1 40 E6 FF                  call 0x140495a34
00631993  48 8B F0                        mov rsi, rax
00631996  48 85 C0                        test rax, rax
00631999  0F 84 8F 00 00 00               je 0x140631a2e
0063199F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
006319A2  A8 18                           test al, 0x18
006319A4  74 0C                           je 0x1406319b2
006319A6  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
006319AB  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
006319B0  EB 0E                           jmp 0x1406319c0
006319B2  A8 04                           test al, 4
006319B4  74 0A                           je 0x1406319c0
006319B6  E8 4D 22 EA FF                  call 0x1404d3c08
006319BB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006319C0  40 32 ED                        xor bpl, bpl
006319C3  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
006319C8  40 38 2D E9 2E 8D 00            cmp byte ptr [rip + 0x8d2ee9], bpl
006319CF  44 88 74 24 28                  mov byte ptr [rsp + 0x28], r14b
006319D4  75 0C                           jne 0x1406319e2
006319D6  F7 05 A0 2F 8D 00 00 08 00 00   test dword ptr [rip + 0x8d2fa0], 0x800
006319E0  74 13                           je 0x1406319f5
006319E2  48 8D 0D 97 24 8D 00            lea rcx, [rip + 0x8d2497]
006319E9  E8 32 4C BE FF                  call 0x140216620
006319EE  40 8A E8                        mov bpl, al
006319F1  84 C0                           test al, al
006319F3  74 39                           je 0x140631a2e
006319F5  48 8D 7E 20                     lea rdi, [rsi + 0x20]
006319F9  48 8B 1F                        mov rbx, qword ptr [rdi]
006319FC  EB 1A                           jmp 0x140631a18
006319FE  48 8D 43 F0                     lea rax, [rbx - 0x10]
00631A02  48 85 C0                        test rax, rax
00631A05  74 0E                           je 0x140631a15
00631A07  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00631A0B  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00631A10  E8 BB 90 08 00                  call 0x1406baad0
00631A15  48 8B 1B                        mov rbx, qword ptr [rbx]
00631A18  48 3B DF                        cmp rbx, rdi
00631A1B  75 E1                           jne 0x1406319fe
00631A1D  40 84 ED                        test bpl, bpl
00631A20  74 0C                           je 0x140631a2e
00631A22  48 8D 0D 57 24 8D 00            lea rcx, [rip + 0x8d2457]
00631A29  E8 52 84 D1 FF                  call 0x140349e80
00631A2E  45 33 C0                        xor r8d, r8d
00631A31  45 8A CE                        mov r9b, r14b
00631A34  49 8B CF                        mov rcx, r15
00631A37  41 8D 50 01                     lea edx, [r8 + 1]
00631A3B  E8 90 4D D6 FF                  call 0x1403967d0
00631A40  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00631A44  48 85 F6                        test rsi, rsi
00631A47  74 64                           je 0x140631aad
00631A49  40 32 FF                        xor dil, dil
00631A4C  40 38 3D 65 2E 8D 00            cmp byte ptr [rip + 0x8d2e65], dil
00631A53  75 0C                           jne 0x140631a61
00631A55  F7 05 21 2F 8D 00 00 08 00 00   test dword ptr [rip + 0x8d2f21], 0x800
00631A5F  74 13                           je 0x140631a74
00631A61  48 8D 0D 18 24 8D 00            lea rcx, [rip + 0x8d2418]
00631A68  E8 B3 4B BE FF                  call 0x140216620
00631A6D  40 8A F8                        mov dil, al
00631A70  84 C0                           test al, al
00631A72  74 39                           je 0x140631aad
00631A74  48 83 C6 30                     add rsi, 0x30
00631A78  48 8B 1E                        mov rbx, qword ptr [rsi]
00631A7B  EB 1A                           jmp 0x140631a97
00631A7D  48 8D 43 F0                     lea rax, [rbx - 0x10]
00631A81  48 85 C0                        test rax, rax
00631A84  74 0E                           je 0x140631a94
00631A86  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00631A8A  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00631A8F  E8 3C 90 08 00                  call 0x1406baad0
00631A94  48 8B 1B                        mov rbx, qword ptr [rbx]
00631A97  48 3B DE                        cmp rbx, rsi
00631A9A  75 E1                           jne 0x140631a7d
00631A9C  40 84 FF                        test dil, dil
00631A9F  74 0C                           je 0x140631aad
00631AA1  48 8D 0D D8 23 8D 00            lea rcx, [rip + 0x8d23d8]
00631AA8  E8 D3 83 D1 FF                  call 0x140349e80
00631AAD  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
00631AB1  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00631AB6  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
00631ABB  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00631AC0  48 83 C4 40                     add rsp, 0x40
00631AC4  41 5F                           pop r15
00631AC6  41 5E                           pop r14
00631AC8  5F                              pop rdi
00631AC9  C3                              ret
00631ACA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifKeReleaseMutexWrapper(__int64 a1, unsigned __int8 a2, int a3)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int8 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(v_rsp - 56) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 40) = v_xmm0;
    result = DifGetAPIThunkContextById(260, a2, a3, a4);
    if (result == 0) goto loc_00631A2E;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006319B2;
    v_stack_m38 = v_stack_p0;
    goto loc_006319C0;
loc_006319B2:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = a2;
    if ((*(unsigned __int8 *)(v_rip + 9252585)) != 0) goto loc_006319E2;
    if (((*(unsigned int *)(v_rip + 9252768)) & (0x800ULL)) == 0) goto loc_006319F5;
loc_006319E2:
    result = ExAcquireRundownProtection(v_rip + 9249943, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00631A2E;
loc_006319F5:
    goto loc_00631A18;
loc_006319FE:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00631A18:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006319FE;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9249879;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    a3 = 0;
    result = KeReleaseMutant(a1, a3 + 1, a3, a2);
    v_stack_m20 = (unsigned int)(result);
    if (result == 0) goto loc_00631AAD;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9252453)) != 0) goto loc_00631A61;
    if (((*(unsigned int *)(v_rip + 9252641)) & (0x800ULL)) == 0) goto loc_00631A74;
loc_00631A61:
    result = ExAcquireRundownProtection(v_rip + 9249816, a3 + 1, a3, a2);
    if ((unsigned __int8)(result) == 0) goto loc_00631AAD;
loc_00631A74:
    v_rsi = (result) + (48);
    goto loc_00631A97;
loc_00631A7D:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a3 + 1, a3, a2);
    }
loc_00631A97:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00631A7D;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9249752;
        result = ExReleaseRundownProtection(a1, a3 + 1, a3, a2);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m20);
}
```

## 5. (Beta) C Style

```c
int64_t DifKeReleaseMutexWrapper(int64_t Arg1, uint8_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint8_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (64);
    *(uint64_t *)(local_rsp - 0x38) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x28) = v_xmm0;
    result = DifGetAPIThunkContextById(260, Arg2, Arg3, a4);
    if (result == 0) goto loc_00631A2E;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006319B2;
    v_stack_m38 = v_stack_p0;
    goto loc_006319C0;
loc_006319B2:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = Arg2;
    if ((*(uint8_t *)(v_rip + 0x8D2EE9)) != 0) goto loc_006319E2;
    if (((*(uint32_t *)(v_rip + 0x8D2FA0)) & (0x800ULL)) == 0) goto loc_006319F5;
loc_006319E2:
    result = ExAcquireRundownProtection(v_rip + 9249943, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_00631A2E;
loc_006319F5:
    goto loc_00631A18;
loc_006319FE:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_00631A18:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006319FE;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9249879;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    Arg3 = 0;
    result = KeReleaseMutant(Arg1, Arg3 + 1, Arg3, Arg2);
    v_stack_m20 = (uint32_t)(result);
    if (result == 0) goto loc_00631AAD;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D2E65)) != 0) goto loc_00631A61;
    if (((*(uint32_t *)(v_rip + 0x8D2F21)) & (0x800ULL)) == 0) goto loc_00631A74;
loc_00631A61:
    result = ExAcquireRundownProtection(v_rip + 9249816, Arg3 + 1, Arg3, Arg2);
    if ((uint8_t)(result) == 0) goto loc_00631AAD;
loc_00631A74:
    local_rsi = (result) + (48);
    goto loc_00631A97;
loc_00631A7D:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg3 + 1, Arg3, Arg2);
    }
loc_00631A97:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00631A7D;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9249752;
        result = ExReleaseRundownProtection(Arg1, Arg3 + 1, Arg3, Arg2);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m20);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00631960&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00631960[BB_00631960]
  bb_0063199F[BB_0063199F]
  bb_006319A6[BB_006319A6]
  bb_006319B2[BB_006319B2]
  bb_006319B6[BB_006319B6]
  bb_006319C0[BB_006319C0]
  bb_006319D6[BB_006319D6]
  bb_006319E2[BB_006319E2]
  bb_006319F5[BB_006319F5]
  bb_006319FE[BB_006319FE]
  bb_00631A07[BB_00631A07]
  bb_00631A15[BB_00631A15]
  bb_00631A18[BB_00631A18]
  bb_00631A1D[BB_00631A1D]
  bb_00631A22[BB_00631A22]
  bb_00631A2E[BB_00631A2E]
  bb_00631A49[BB_00631A49]
  bb_00631A55[BB_00631A55]
  bb_00631A61[BB_00631A61]
  bb_00631A74[BB_00631A74]
  bb_00631A7D[BB_00631A7D]
  bb_00631A86[BB_00631A86]
  bb_00631A94[BB_00631A94]
  bb_00631A97[BB_00631A97]
  bb_00631A9C[BB_00631A9C]
  bb_00631AA1[BB_00631AA1]
  bb_00631AAD[BB_00631AAD]
  bb_00631ACA[BB_00631ACA]
  bb_00631960 -->|branch| bb_00631A2E
  bb_00631960 -->|fallthrough| bb_0063199F
  bb_0063199F -->|branch| bb_006319B2
  bb_0063199F -->|fallthrough| bb_006319A6
  bb_006319A6 -->|branch| bb_006319C0
  bb_006319B2 -->|branch| bb_006319C0
  bb_006319B2 -->|fallthrough| bb_006319B6
  bb_006319B6 -->|flow| bb_006319C0
  bb_006319C0 -->|branch| bb_006319E2
  bb_006319C0 -->|fallthrough| bb_006319D6
  bb_006319D6 -->|branch| bb_006319F5
  bb_006319D6 -->|fallthrough| bb_006319E2
  bb_006319E2 -->|branch| bb_00631A2E
  bb_006319E2 -->|fallthrough| bb_006319F5
  bb_006319F5 -->|branch| bb_00631A18
  bb_006319FE -->|branch| bb_00631A15
  bb_006319FE -->|fallthrough| bb_00631A07
  bb_00631A07 -->|flow| bb_00631A15
  bb_00631A15 -->|flow| bb_00631A18
  bb_00631A18 -->|branch| bb_006319FE
  bb_00631A18 -->|fallthrough| bb_00631A1D
  bb_00631A1D -->|branch| bb_00631A2E
  bb_00631A1D -->|fallthrough| bb_00631A22
  bb_00631A22 -->|flow| bb_00631A2E
  bb_00631A2E -->|branch| bb_00631AAD
  bb_00631A2E -->|fallthrough| bb_00631A49
  bb_00631A49 -->|branch| bb_00631A61
  bb_00631A49 -->|fallthrough| bb_00631A55
  bb_00631A55 -->|branch| bb_00631A74
  bb_00631A55 -->|fallthrough| bb_00631A61
  bb_00631A61 -->|branch| bb_00631AAD
  bb_00631A61 -->|fallthrough| bb_00631A74
  bb_00631A74 -->|branch| bb_00631A97
  bb_00631A7D -->|branch| bb_00631A94
  bb_00631A7D -->|fallthrough| bb_00631A86
  bb_00631A86 -->|flow| bb_00631A94
  bb_00631A94 -->|flow| bb_00631A97
  bb_00631A97 -->|branch| bb_00631A7D
  bb_00631A97 -->|fallthrough| bb_00631A9C
  bb_00631A9C -->|branch| bb_00631AAD
  bb_00631A9C -->|fallthrough| bb_00631AA1
  bb_00631AA1 -->|flow| bb_00631AAD
```
