# DifExfTryAcquirePushLockSharedWrapper

- RVA: `0x00623EF0`–`0x00624051` (길이 `353` bytes)
- VA: `0x0000000140623EF0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `95`개 명령, `353/353` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00623F1F` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00623F47` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00623F75` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00623F9C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00623FB5` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00623FBF` → [ExfTryAcquirePushLockSharedEx](../3F/ExfTryAcquirePushLockSharedEx_function_003FC210.md) (function, `0x003FC210`)
- `0x00623FEC` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00624013` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062402C` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00623F59` → RVA `0x00F048B8` (`.data`; read)
- `0x00623F62` → RVA `0x00F04980` (`.data`; read)
- `0x00623F6E` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00623EF0  4C 8B DC                        mov r11, rsp
00623EF3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00623EF7  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
00623EFB  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
00623EFF  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
00623F03  41 56                           push r14
00623F05  48 83 EC 40                     sub rsp, 0x40
00623F09  33 C0                           xor eax, eax
00623F0B  0F 57 C0                        xorps xmm0, xmm0
00623F0E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00623F13  48 8B E9                        mov rbp, rcx
00623F16  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
00623F1A  B9 78 01 00 00                  mov ecx, 0x178
00623F1F  E8 10 1B E7 FF                  call 0x140495a34
00623F24  48 8B F0                        mov rsi, rax
00623F27  48 85 C0                        test rax, rax
00623F2A  0F 84 8A 00 00 00               je 0x140623fba
00623F30  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00623F33  A8 18                           test al, 0x18
00623F35  74 0C                           je 0x140623f43
00623F37  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00623F3C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00623F41  EB 0E                           jmp 0x140623f51
00623F43  A8 04                           test al, 4
00623F45  74 0A                           je 0x140623f51
00623F47  E8 BC FC EA FF                  call 0x1404d3c08
00623F4C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00623F51  40 32 FF                        xor dil, dil
00623F54  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00623F59  40 38 3D 58 09 8E 00            cmp byte ptr [rip + 0x8e0958], dil
00623F60  75 0C                           jne 0x140623f6e
00623F62  F7 05 14 0A 8E 00 00 08 00 00   test dword ptr [rip + 0x8e0a14], 0x800
00623F6C  74 13                           je 0x140623f81
00623F6E  48 8D 0D 0B FF 8D 00            lea rcx, [rip + 0x8dff0b]
00623F75  E8 A6 26 BF FF                  call 0x140216620
00623F7A  40 8A F8                        mov dil, al
00623F7D  84 C0                           test al, al
00623F7F  74 39                           je 0x140623fba
00623F81  4C 8D 76 20                     lea r14, [rsi + 0x20]
00623F85  49 8B 1E                        mov rbx, qword ptr [r14]
00623F88  EB 1A                           jmp 0x140623fa4
00623F8A  48 8D 43 F0                     lea rax, [rbx - 0x10]
00623F8E  48 85 C0                        test rax, rax
00623F91  74 0E                           je 0x140623fa1
00623F93  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00623F97  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00623F9C  E8 2F 6B 09 00                  call 0x1406baad0
00623FA1  48 8B 1B                        mov rbx, qword ptr [rbx]
00623FA4  49 3B DE                        cmp rbx, r14
00623FA7  75 E1                           jne 0x140623f8a
00623FA9  40 84 FF                        test dil, dil
00623FAC  74 0C                           je 0x140623fba
00623FAE  48 8D 0D CB FE 8D 00            lea rcx, [rip + 0x8dfecb]
00623FB5  E8 C6 5E D2 FF                  call 0x140349e80
00623FBA  33 D2                           xor edx, edx
00623FBC  48 8B CD                        mov rcx, rbp
00623FBF  E8 4C 82 DD FF                  call 0x1403fc210
00623FC4  88 44 24 30                     mov byte ptr [rsp + 0x30], al
00623FC8  48 85 F6                        test rsi, rsi
00623FCB  74 64                           je 0x140624031
00623FCD  40 32 FF                        xor dil, dil
00623FD0  40 38 3D E1 08 8E 00            cmp byte ptr [rip + 0x8e08e1], dil
00623FD7  75 0C                           jne 0x140623fe5
00623FD9  F7 05 9D 09 8E 00 00 08 00 00   test dword ptr [rip + 0x8e099d], 0x800
00623FE3  74 13                           je 0x140623ff8
00623FE5  48 8D 0D 94 FE 8D 00            lea rcx, [rip + 0x8dfe94]
00623FEC  E8 2F 26 BF FF                  call 0x140216620
00623FF1  40 8A F8                        mov dil, al
00623FF4  84 C0                           test al, al
00623FF6  74 39                           je 0x140624031
00623FF8  48 83 C6 30                     add rsi, 0x30
00623FFC  48 8B 1E                        mov rbx, qword ptr [rsi]
00623FFF  EB 1A                           jmp 0x14062401b
00624001  48 8D 43 F0                     lea rax, [rbx - 0x10]
00624005  48 85 C0                        test rax, rax
00624008  74 0E                           je 0x140624018
0062400A  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062400E  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00624013  E8 B8 6A 09 00                  call 0x1406baad0
00624018  48 8B 1B                        mov rbx, qword ptr [rbx]
0062401B  48 3B DE                        cmp rbx, rsi
0062401E  75 E1                           jne 0x140624001
00624020  40 84 FF                        test dil, dil
00624023  74 0C                           je 0x140624031
00624025  48 8D 0D 54 FE 8D 00            lea rcx, [rip + 0x8dfe54]
0062402C  E8 4F 5E D2 FF                  call 0x140349e80
00624031  8A 44 24 30                     mov al, byte ptr [rsp + 0x30]
00624035  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0062403A  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0062403F  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00624044  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00624049  48 83 C4 40                     add rsp, 0x40
0062404D  41 5E                           pop r14
0062404F  C3                              ret
00624050  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExfTryAcquirePushLockSharedWrapper(__int64 a1, int a2)
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
    result = DifGetAPIThunkContextById(376, a2, a3, a4);
    if (result == 0) goto loc_00623FBA;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00623F43;
    v_stack_m28 = v_stack_p0;
    goto loc_00623F51;
loc_00623F43:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9308504)) != 0) goto loc_00623F6E;
    if (((*(unsigned int *)(v_rip + 9308692)) & (0x800ULL)) == 0) goto loc_00623F81;
loc_00623F6E:
    result = ExAcquireRundownProtection(v_rip + 9305867, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00623FBA;
loc_00623F81:
    goto loc_00623FA4;
loc_00623F8A:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00623FA4:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00623F8A;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9305803;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    a2 = 0;
    result = ExfTryAcquirePushLockSharedEx(a1, a2, a3, a4);
    v_stack_m18 = (unsigned __int8)(result);
    if (result == 0) goto loc_00624031;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9308385)) != 0) goto loc_00623FE5;
    if (((*(unsigned int *)(v_rip + 9308573)) & (0x800ULL)) == 0) goto loc_00623FF8;
loc_00623FE5:
    result = ExAcquireRundownProtection(v_rip + 9305748, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00624031;
loc_00623FF8:
    v_rsi = (result) + (48);
    goto loc_0062401B;
loc_00624001:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062401B:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00624001;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9305684;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m18;
}
```

## 5. (Beta) C Style

```c
int64_t DifExfTryAcquirePushLockSharedWrapper(int64_t Arg1, int32_t Arg2)
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
    result = DifGetAPIThunkContextById(376, Arg2, a3, a4);
    if (result == 0) goto loc_00623FBA;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00623F43;
    v_stack_m28 = v_stack_p0;
    goto loc_00623F51;
loc_00623F43:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8E0958)) != 0) goto loc_00623F6E;
    if (((*(uint32_t *)(v_rip + 0x8E0A14)) & (0x800ULL)) == 0) goto loc_00623F81;
loc_00623F6E:
    result = ExAcquireRundownProtection(v_rip + 9305867, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00623FBA;
loc_00623F81:
    goto loc_00623FA4;
loc_00623F8A:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_00623FA4:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00623F8A;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9305803;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    Arg2 = 0;
    result = ExfTryAcquirePushLockSharedEx(Arg1, Arg2, a3, a4);
    v_stack_m18 = (uint8_t)(result);
    if (result == 0) goto loc_00624031;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E08E1)) != 0) goto loc_00623FE5;
    if (((*(uint32_t *)(v_rip + 0x8E099D)) & (0x800ULL)) == 0) goto loc_00623FF8;
loc_00623FE5:
    result = ExAcquireRundownProtection(v_rip + 9305748, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00624031;
loc_00623FF8:
    local_rsi = (result) + (48);
    goto loc_0062401B;
loc_00624001:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_0062401B:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00624001;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9305684;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m18;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00623EF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00623EF0[BB_00623EF0]
  bb_00623F30[BB_00623F30]
  bb_00623F37[BB_00623F37]
  bb_00623F43[BB_00623F43]
  bb_00623F47[BB_00623F47]
  bb_00623F51[BB_00623F51]
  bb_00623F62[BB_00623F62]
  bb_00623F6E[BB_00623F6E]
  bb_00623F81[BB_00623F81]
  bb_00623F8A[BB_00623F8A]
  bb_00623F93[BB_00623F93]
  bb_00623FA1[BB_00623FA1]
  bb_00623FA4[BB_00623FA4]
  bb_00623FA9[BB_00623FA9]
  bb_00623FAE[BB_00623FAE]
  bb_00623FBA[BB_00623FBA]
  bb_00623FCD[BB_00623FCD]
  bb_00623FD9[BB_00623FD9]
  bb_00623FE5[BB_00623FE5]
  bb_00623FF8[BB_00623FF8]
  bb_00624001[BB_00624001]
  bb_0062400A[BB_0062400A]
  bb_00624018[BB_00624018]
  bb_0062401B[BB_0062401B]
  bb_00624020[BB_00624020]
  bb_00624025[BB_00624025]
  bb_00624031[BB_00624031]
  bb_00624050[BB_00624050]
  bb_00623EF0 -->|branch| bb_00623FBA
  bb_00623EF0 -->|fallthrough| bb_00623F30
  bb_00623F30 -->|branch| bb_00623F43
  bb_00623F30 -->|fallthrough| bb_00623F37
  bb_00623F37 -->|branch| bb_00623F51
  bb_00623F43 -->|branch| bb_00623F51
  bb_00623F43 -->|fallthrough| bb_00623F47
  bb_00623F47 -->|flow| bb_00623F51
  bb_00623F51 -->|branch| bb_00623F6E
  bb_00623F51 -->|fallthrough| bb_00623F62
  bb_00623F62 -->|branch| bb_00623F81
  bb_00623F62 -->|fallthrough| bb_00623F6E
  bb_00623F6E -->|branch| bb_00623FBA
  bb_00623F6E -->|fallthrough| bb_00623F81
  bb_00623F81 -->|branch| bb_00623FA4
  bb_00623F8A -->|branch| bb_00623FA1
  bb_00623F8A -->|fallthrough| bb_00623F93
  bb_00623F93 -->|flow| bb_00623FA1
  bb_00623FA1 -->|flow| bb_00623FA4
  bb_00623FA4 -->|branch| bb_00623F8A
  bb_00623FA4 -->|fallthrough| bb_00623FA9
  bb_00623FA9 -->|branch| bb_00623FBA
  bb_00623FA9 -->|fallthrough| bb_00623FAE
  bb_00623FAE -->|flow| bb_00623FBA
  bb_00623FBA -->|branch| bb_00624031
  bb_00623FBA -->|fallthrough| bb_00623FCD
  bb_00623FCD -->|branch| bb_00623FE5
  bb_00623FCD -->|fallthrough| bb_00623FD9
  bb_00623FD9 -->|branch| bb_00623FF8
  bb_00623FD9 -->|fallthrough| bb_00623FE5
  bb_00623FE5 -->|branch| bb_00624031
  bb_00623FE5 -->|fallthrough| bb_00623FF8
  bb_00623FF8 -->|branch| bb_0062401B
  bb_00624001 -->|branch| bb_00624018
  bb_00624001 -->|fallthrough| bb_0062400A
  bb_0062400A -->|flow| bb_00624018
  bb_00624018 -->|flow| bb_0062401B
  bb_0062401B -->|branch| bb_00624001
  bb_0062401B -->|fallthrough| bb_00624020
  bb_00624020 -->|branch| bb_00624031
  bb_00624020 -->|fallthrough| bb_00624025
  bb_00624025 -->|flow| bb_00624031
```
